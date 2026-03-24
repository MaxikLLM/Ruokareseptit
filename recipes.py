import db

def add_recipe(title, ingredients, instruction, user_id):
    sql = "INSERT INTO recipes (title, ingredients, instruction, user_id) VALUES (?, ?, ?, ?)"

    db.execute(sql, [title, ingredients, instruction, user_id])
