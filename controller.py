import mysql.connector
import os
import matplotlib.pyplot as pt

# Configurations
from config import config
from dotenv import load_dotenv

load_dotenv()  # Imports environemnt variables from the '.env' file

# ===================SQL Connectivity=================

# SQL Connection
connection = mysql.connector.connect(
    host=config.get("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=config.get("DB_NAME"),
    port="3306",
    autocommit=config.get("DB_AUTOCOMMIT"),
)

cursor = connection.cursor(buffered=True)

# SQL functions


def checkUser(username, password=None):
    cmd = f"Select count(username) from login where username='{username}' and BINARY password='{password}'"
    cursor.execute(cmd)
    cmd = None
    a = cursor.fetchone()[0] >= 1
    return a


def human_format(num):
    if num < 1000:
        return num

    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000
    return "%.1f%s" % (num, ["", "K", "M", "G", "T", "P"][magnitude])


def updatePassword(username, sec_ans, sec_que, password):
    cmd = f"update login set password='{password}' where username='{username}' and sec_ans='{sec_ans}' and sec_que='{sec_que}' limit 1;"
    cursor.execute(cmd)
    cmd = f"select count(username) from login where username='{username}' and password='{password}' and sec_ans='{sec_ans}' and sec_que='{sec_que}';"
    cursor.execute(cmd)
    return cursor.fetchone()[0] >= 1


def updateUsername(oldusername, password, newusername):
    cmd = f"update login set username='{newusername}' where username='{oldusername}' and password='{password}' limit 1;"
    cursor.execute(cmd)
    cmd = f"select count(username) from login where username='{newusername}' and password='{password}''"
    cursor.execute(cmd)
    return cursor.fetchone()[0] >= 1



def find_p_id(name):
    cmd = f"select p_id from prisoners where name = '{name}'"
    cursor.execute(cmd)
    out = cursor.fetchone()[0]
    return out


def A_llocate(p_id):
    cmd = f"select * from prison_allocate where p_id = '{p_id}';"
    cursor.execute(cmd)
    prison_allocate = cursor.fetchall()
    if prison_allocate != []:
        subcmd = f"update prison_allocate set allocate = curdate() where p_id = '{p_id}' "
        cursor.execute(subcmd)
        return "successful"
    else:
        return "No prison_allocate for the given Prisoners"



def R_eleased(id):
    cmd = f"update prison_allocate set released=current_timestamp where id={id} limit 1;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


# ============Python Functions==========


def acceptable(*args, acceptables):
    """
    If the characters in StringVars passed as arguments are in acceptables return True, else returns False
    """
    for arg in args:
        for char in arg:
            if char.lower() not in acceptables:
                return False
    return True



# Get all prisoners
def get_prisoners():
    cmd = "select id, name, address, sections, other_details, created_at from prisoners;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()


# Add a Prisoners
def add_prisoners(name, address, sections, other_details):
    cmd = f"insert into prisoners(name,address,sections,other_details) values('{name}','{address}','{sections}','{other_details}');"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


# add a Prison Cell
def add_prison_cell(prison_no, charges, prison_type):
    cmd = f"insert into prison_cell(prison_no,charges,prison_type) values('{prison_no}',{charges},'{prison_type}');"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


# Get All prison_cell
def get_prison_cell():
    cmd = "select id, prison_no, prison_type, charges, created_at from prison_cell;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()


# Get all prison_allocate
def get_prison_allocate():
    cmd = "select id, p_id, p_c_a_id, allocate, released, Supplies from prison_allocate;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()


# Add a prison_allocate
def add_prison_allocate(p_id, Supplies, p_c_a_id, allocate="now"):
    cmd = f"insert into prison_allocate(p_id,allocate,p_c_a_id, Supplies) values('{p_id}',{f'{chr(39) + allocate + chr(39)}' if allocate != 'now' else 'current_timestamp'},'{Supplies}','{p_c_a_id}');"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


# Get all Prison Cell count
def get_total_prison_cell():
    cmd = "select count(prison_no) from prison_cell;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchone()[0]


# Check if a Prison Cell is vacant
def allocated():
    cmd = f"select count(p_c.id) from prison_allocate p_a, prison_cell p_c where p_a.p_c_a_id = p_c.id and p_a.released is Null;"
    cursor.execute(cmd)

    return cursor.fetchone()[0]


def vacant():
    return get_total_prison_cell() - allocated()


def allocating():
    cmd = f"select count(p_a.id) from prison_allocate p_a , prison_cell p_c where p_a.p_c_a_id = p_c.id and p_c.prison_type = 'T';"
    cursor.execute(cmd)
    terrorist = cursor.fetchone()[0]

    cmd1 = f"select count(p_a.id) from prison_allocate p_a , prison_cell p_c where p_a.p_c_a_id = p_c.id and p_c.prison_type = 'G';"
    cursor.execute(cmd1)
    general = cursor.fetchone()[0]

    return [terrorist, general]


# Get total hotel fine
def get_total_charges():
    cmd = "select sum(charges) from prison_cell;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    fine = cursor.fetchone()[0]

    return human_format(fine)


def delete_prison_allocate(id):
    cmd = f"delete from prison_allocate where id='{id}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


def delete_prison_cell(id):
    cmd = f"delete from prison_cell where id='{id}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


def delete_prisoners(id):
    cmd = f"delete from prisoners where id='{id}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


def update_prison_cell(id, prison_no, prison_type, charges):
    cmd = f"update prison_cell set prison_type = '{prison_type}',charges= {charges}, prison_no = {prison_no} where id = {id};"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


def update_prisoners(name, address, id, other_details):

    cmd = f"update prisoners set address = '{address}',other_details = '{other_details}' , name = '{name}' where id = {id};"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


def update_prison_allocates(
    p_id, allocate, prison_allocate_id, prison_allocate_date, released, Supplies, type, id
):
    cmd = f"update prison_allocate set allocate = '{allocate}',released = '{released}',p_id = {p_id}, \
        p_a_date = '{prison_allocate_date}',Supplies = {Supplies},p_c_a_type='{type}', p_c_a_id = {prison_allocate_id} where id= {id};"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True


def S_upplies():
    cmd = f"select sum(Supplies) from prison_allocate;"
    cursor.execute(cmd)
    S_upplies = cursor.fetchone()[0]

    return human_format(S_upplies)


def update_prison_allocate(id, p_id, allocate, prison_allocate_id, released, Supplies):
    cmd = f"update prison_allocate set allocate = '{allocate}', released = '{released}', p_id = {p_id}, Supplies = '{Supplies}', p_c_a_id = '{prison_allocate_id}' where id= '{id}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True
