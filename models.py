from database import get_connection

def get_user_by_email(email: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM userlogin WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def create_task(name: str, date: str, task_details: str):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO user_task (name, date, task_details) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, date, task_details))
    conn.commit()
    task_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return task_id
