import psycopg2

# SQL intilization
def SQLinit():
    """
    Initialize the database connection
    """
    try:
        conn = psycopg2.connect("dbname=SQLi", user="postgres")
        cur = conn.cursor()
        return cur, conn
        print("Hello")
    except:
        print("Unable to connect to the database")

# SQL query
def SQLquery(cur, conn, query, commit=False):
    """
    Execute a query on the database
    """
    try:
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

# Intialize the database connection
# SQLinit()