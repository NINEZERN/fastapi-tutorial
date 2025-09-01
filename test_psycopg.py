import psycopg2

try:
    conn = psycopg2.connect(
        "dbname=postgres user=postgres password=gleb030788 host=localhost port=5432"
    )
    print("connected to db")

    cur = conn.cursor()

    cur.execute(
        """
                SELECT * FROM postgres;
                """
    )
    print(cur.fetchall())

    cur.close()
    conn.close()
except Exception as e:
    print("Error", e)
