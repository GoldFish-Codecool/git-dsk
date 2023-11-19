import psycopg2

DB_NAME ="hucodjek"
USER = "hucodjek"
PASSWORD = "Eryt_3nZU6fPM3tO1Q11735_FJIvBAys"
HOST = "flora.db.elephantsql.com"

conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST)
cur = conn.cursor()

def get_leaderboard() :
    cur.execute("SELECT winner, count(winner) FROM tictactoe GROUP BY winner ORDER BY count(winner) desc;")
    tictactoe = cur.fetchall()
    for winner in tictactoe :
        print(winner)
