from flask import Flask, jsonify, request
import secrets
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

limiter = Limiter(
    key_func=lambda: request.headers.get('X-API-KEY', get_remote_address()),
    app=app,
    default_limits=["200 per day"]
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    api_key = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.get_json(force=True)

    if not data or 'username' not in data:
        return jsonify ({'error' : 'usernaem is required.'}), 400
    
    username = data['username']

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error' : 'Username already exsits'}), 400
    
    
    new_api_key = f'api_live_{secrets.token_hex(12)}'

    new_user = User(username=username, api_key=new_api_key)
    db.session.add(new_user)
    db.session.commit()

    return jsonify ({
        "status": "success",
        "message": "Registration successful. Keep your API key safe.",
        "api_key": new_api_key
    }), 201

@app.route('/api/status', methods=['GET'])
@limiter.limit("5 per minute")
def get_status():
    user_api_key = request.headers.get('X-API-KEY')

    if not user_api_key:
        return jsonify({'error' : 'this is not an API!!'}), 401
    
    user = User.query.filter_by(api_key=user_api_key).first()
    if not user:
        return jsonify({'error' : 'invalid API Key'}), 403
    
    return jsonify({
        'status' : 'success',
        'message' : f'welcome {user.username}!'
    })


if __name__ == "__main__":
    app.run(debug=True)