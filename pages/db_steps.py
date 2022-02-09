def create_group(db, values):
    query = "INSERT INTO auth_group(name) VALUES (%s)"
    db.execute(query, values)
    return db.connection.commit()


def get_group_name(db):
    query = "SELECT name FROM auth_group"
    db.execute(query)
    return db.fetchall()
