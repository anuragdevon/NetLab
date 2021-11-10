import psycopg2

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
