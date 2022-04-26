from db.run_sql import run_sql
from models.sport_class import Sport_class
from models.member import Member
import repositories.member_repository as member_repository

def save(sport_class):
    sql = "INSERT INTO sport_classes (name, date, duration, capacity) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [sport_class.name, sport_class.date, sport_class.duration, sport_class.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    sport_class.id = id
    return sport_class

def select_all():
    sport_classes = []
    sql = "SELECT * FROM sport_classes"
    results = run_sql(sql)
    for result in results:
        sport_class = Sport_class(result["name"], result["date"], result["duration"], result["capacity"], result["id"])
        sport_classes.append(sport_class)
    return sport_classes

def select(id):
    sql = "SELECT * FROM sport_classes WHERE id=%s"
    values = [id]
    result = run_sql(sql,values)[0]
    sport_class = Sport_class(result["name"], result["date"], result["duration"], result["capacity"], result["id"])
    return sport_class

def update(sport_class):
    sql = "UPDATE sport_classes SET (name, date, duration, capacity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [sport_class.name, sport_class.date, sport_class.duration, sport_class.capacity, sport_class.id]
    run_sql(sql, values)

# def delete_all():
#     sql = "DELETE FROM sport_classes"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM sport_classes WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)
