import db

def add_recipe(title, ingredients, instruction, user_id):
    sql = "INSERT INTO recipes (title, ingredients, instruction, user_id) VALUES (?, ?, ?, ?)"

    db.execute(sql, [title, ingredients, instruction, user_id])

def get_recipes():
    sql = "SELECT id, title FROM recipes ORDER BY id DESC"
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.title,
                    recipes.id,
                    recipes.ingredients,
                    recipes.instruction,
                    users.id user_id,
                    users.username
             FROM recipes, users
             WHERE recipes.user_id = users.id AND
                   recipes.id = ?"""
    return db.query(sql, [recipe_id])[0]

def update_recipe(recipe_id, title, ingredients, instruction):
    sql = """UPDATE recipes SET title = ?,
                    ingredients = ?,
                    instruction = ?
                WHERE id = ?"""
    db.execute(sql, [title, ingredients, instruction, recipe_id])

def remove_recipe(recipe_id):
    sql = "DELETE FROM recipes WHERE id = ?"
    db.execute(sql, [recipe_id])
