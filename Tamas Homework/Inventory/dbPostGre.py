import psycopg2

DB_NAME ="hucodjek"
USER = "hucodjek"
PASSWORD = "postgres://hucodjek:Eryt_3nZU6fPM3tO1Q11735_FJIvBAys@flora.db.elephantsql.com/hucodjek"
HOST = "flora.db.elephantsql.com"

conn = psycopg2(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST)
