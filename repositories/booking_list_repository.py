from db.run_sql import run_sql
from models.booking_list import Booking_list
from models.member import Member
import repositories.member_repository as member_repository
from models.sport_class import Sport_class
import repositories.sport_class_repository as sport_class_repository

def save(booking_list):
    sql = "INSERT INTO booking_lists (member_id, sport_class_id) VALUES (%s, %s) RETURNING id"
    values = [booking_list.member.id, booking_list.sport_class.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking_list.id = id

def select_all():
    booking_lists = []
    sql = "SELECT * FROM booking_lists"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        sport_class = sport_class_repository.select(result["sport_class_id"])
        booking_list = Booking_list(member, sport_class, result['id'])
        booking_lists.append(booking_list)
    return booking_lists

def select(id):
    sql = "SELECT * FROM booking_lists WHERE id= %s"
    values = [id]
    result = run_sql(sql,values)[0]
    member = member_repository.select(result["member_id"])
    sport_class = sport_class_repository.select["sport_class_id"]
    booking_list = Booking_list(member, sport_class, result["id"])
    return booking_list

def update(booking_list):
    sql = "UPDATE booking_lists SET (member_id, sport_class_id) = (%s, %s) WHERE id = %s"
    values = [booking_list.member.id, booking_list.sport_class.id, booking_list.id]
    run_sql(sql, values) 


