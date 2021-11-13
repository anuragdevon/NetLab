# Imports
import psycopg2
import hashlib
import uuid

def SQL_init():
    """
    Initialize the database connection
    """
    try:
        conn = psycopg2.connect(database="sqli", user="postgres")
        cur = conn.cursor()
        return cur, conn
    except:
        print("Unable to connect to the database")

def SQL_RunQuery(query, commit=False):
    """
    Execute a query on the database
    """
    try:
        cur, conn = SQL_init()
        cur.execute(query)
        if commit:
            conn.commit()
            return None
        else:
            return cur.fetchall()
    except Exception as e:
        print("Unable to execute the query")
        return e

# SQL close
def SQLclose(cur, conn):
    """
    Close the database connection
    """
    try:
        cur.close()
        conn.close()
    except:
        print("Unable to close the connection")

def make_password_hash(password):
    """
    Hash a password
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def uuid_generator():
    """
    Generate a random UUID
    """
    return uuid.uuid4()  

def token_generator(amount):
    salt = "80u340w50n$hgsrngt9834t5h083&hnisf523bqtkrf^658"
    token = hashlib.sha256((amount+salt).encode('utf-8')).hexdigest()
    return token

