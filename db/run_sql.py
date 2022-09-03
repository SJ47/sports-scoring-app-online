import os  # heroku requirements
import psycopg2
import psycopg2.extras as ext

# Heroku postgreSQL
# DATABASE_URL = "postgres://xfoowbbpougyio:406b005ea83a5a9e8e7986641a5eafb014e39c12816a83d9f20d367ed786fa43@ec2-52-7-115-250.compute-1.amazonaws.com:5432/dc76jahp7jbrjt"

# ElephantSql.com postgreSQL
DATABASE_URL = "postgres://bvzcotcn:aMi98H-xm8Uy75kbYcrF88bmFtS_nwdB@tyke.db.elephantsql.com/bvzcotcn"

def run_sql(sql, values = None):
    conn = None
    results = []
    # DATABASE_URL = os.environ['DATABASE_URL']

    try:
        # conn = psycopg2.connect("dbname='sports_scoring_app'")   # Normal local run
        conn=psycopg2.connect(DATABASE_URL, sslmode='require')   # Heroku requirement
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
