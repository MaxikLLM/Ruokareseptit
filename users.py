from werkzeug.security import generate_password_hash, check_password_hash
import db
def get_user(user_id):
    sql = "SELECT id, username FROM users WHERE id = ?"
    result = db.query(sql, [user_id])
    return result[0] if result else None

def get_recipes(user_id):
    sql = """
    SELECT r.id,
           r.title,
           COALESCE(AVG(c.grade), 0) AS avg_grade
    FROM recipes r
    LEFT JOIN comments c ON c.recipe_id = r.id
    WHERE r.user_id = ?
    GROUP BY r.id
    ORDER BY r.id DESC"""
    return db.query(sql, [user_id])

def get_user_avg_grade(user_id):
    sql = """
    SELECT COALESCE(AVG(c.grade), 0) AS user_avg_grade
    FROM recipes r
    LEFT JOIN comments c ON c.recipe_id = r.id
    WHERE r.user_id = ?"""
    result = db.query(sql, [user_id])
    return result[0][0] if result and result[0][0] is not None else 0

def create_user(username, password1):
    password_hash = generate_password_hash(password1)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])
    if not result:
        return None

    user_id = result[0]["id"]
    password_hash = result[0]["password_hash"]
    if check_password_hash(password_hash, password):
        return user_id
    else:
        return None
