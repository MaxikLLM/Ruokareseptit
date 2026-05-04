import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_recipe(title, ingredients, instruction, user_id, classes):
    sql = "INSERT INTO recipes (title, ingredients, instruction, user_id) VALUES (?, ?, ?, ?)"

    db.execute(sql, [title, ingredients, instruction, user_id])

    recipe_id = db.last_insert_id()

    sql = "INSERT INTO recipe_classes (recipe_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value])

def add_review(recipe_id, user_id, grade, commentary):
    sql = "INSERT INTO comments (recipe_id, user_id, grade, commentary) VALUES (?, ?, ?, ?)"

    db.execute(sql, [recipe_id, user_id, grade, commentary])

def get_reviews(recipe_id):
    sql = """
        SELECT comments.grade,
               comments.commentary,
               users.id AS user_id,
               users.username
        FROM comments
        LEFT JOIN users ON comments.user_id = users.id
        WHERE comments.recipe_id = ?
        ORDER BY comments.id DESC
    """
    return db.query(sql, [recipe_id])

def get_images(recipe_id):
    sql = "SELECT id FROM images WHERE recipe_id = ?"
    return db.query(sql, [recipe_id])

def add_image(recipe_id, image):
    sql = "INSERT INTO images (recipe_id, image) VALUES (?, ?)"
    db.execute(sql, [recipe_id, image])

def get_image(image_id):
    sql = "SELECT image FROM images WHERE id = ?"
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def remove_image(recipe_id, image_id):
    sql = "DELETE FROM images WHERE id = ? AND recipe_id = ?"
    db.execute(sql, [image_id, recipe_id])

def get_classes(recipe_id):
    sql = "SELECT title, value FROM recipe_classes WHERE recipe_id = ?"
    return db.query(sql, [recipe_id])

def get_recipes():
    sql = """SELECT recipes.id, recipes.title, users.id user_id, users.username,
                COUNT(comments.id) comment_count
             FROM recipes JOIN users ON recipes.user_id = users.id
                          LEFT JOIN comments ON recipes.id = comments.recipe_id
             GROUP BY recipes.id
             ORDER BY recipes.id DESC"""
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
    result = db.query(sql, [recipe_id])
    return result[0] if result else None

def update_recipe(recipe_id, title, ingredients, instruction, classes):
    sql = """UPDATE recipes SET title = ?,
                    ingredients = ?,
                    instruction = ?
                WHERE id = ?"""
    db.execute(sql, [title, ingredients, instruction, recipe_id])

    sql = "DELETE FROM recipe_classes WHERE recipe_id = ?"
    db.execute(sql, [recipe_id])

    sql = "INSERT INTO recipe_classes (recipe_id, title, value) VALUES (?, ?, ?)"
    for title, value in classes:
        db.execute(sql, [recipe_id, title, value])

def remove_recipe(recipe_id):
    sql = "DELETE FROM recipe_classes WHERE recipe_id = ?"
    db.execute(sql, [recipe_id])

    sql = "DELETE FROM recipes WHERE id = ?"
    db.execute(sql, [recipe_id])

def find_recipes(query):
    sql = """SELECT id, title
             FROM recipes
             WHERE title LIKE ? OR ingredients LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])
