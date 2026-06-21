# API Key Management & Rate Limiting Service

A secure and lightweight RESTful API built with **Flask** that demonstrates API Key authentication, persistent database storage, and traffic management (Rate Limiting).

## Features
- **Dynamic API Key Generation**: Secure, randomly generated tokens using Python's `secrets`.
- **Database Persistence**: User records and keys are stored safely using SQLite and SQLAlchemy ORM.
- **Rate Limiting**: Protects endpoints from abuse by restricting users to 5 requests per minute using Flask-Limiter.

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy (SQLite)
- Flask-Limiter

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```
   ---
    Create and activate a virtual environment:
    
    Bash
    
    ```cmd
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
    
3. Install dependencies:
    
    Bash
    
    ```
    pip install -r requirements.txt
    ```
    
4. Run the application:
    
    Bash
    
    ```
    python main.py
    ```
