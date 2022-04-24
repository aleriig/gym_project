from db.run_sql import run_sql
from models.sport_class import Sport_class
from models.member import Member
import repositories.member_repository as member_repository

def save(sport_class):
    sql = "INSERT INTO sport_classes (name, date, duration) VALUES (%s, %s, %s) RETURNING id"
    values = [sport_class.name, sport_class.date, sport_class.duration]
    results = run_sql(sql, values)
    id = results[0]['id']
    sport_class.id = id