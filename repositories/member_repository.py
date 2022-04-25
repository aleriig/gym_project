from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, age, address, phone_number) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.name, member.age, member.address, member.phone_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member
    

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for result in results:
        member = Member(result["name"], result["age"], result["address"], result["phone_number"])
        members.append(member)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result["name"], result["age"], result["address"], result["phone_number"], result["id"])
    return member

def update(member):
    sql = "UPDATE members SET (name, age, addess, phone_number) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.name, member.age, member.address, member.phone_number, member.id]
    run_sql(sql,values)
