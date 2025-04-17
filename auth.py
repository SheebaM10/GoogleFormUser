from models import get_user_by_email

def verify_password(input_password: str, stored_password: str) -> bool:
    return input_password == stored_password  

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if user and verify_password(password, user['password']):
        return user
    return None

