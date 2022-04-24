from optparse import Values
from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT TO members (name) VALUES =%s RETURNING id"
    values = [member.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
