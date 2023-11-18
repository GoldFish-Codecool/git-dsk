import psycopg2
#from dbPostGre import *

DB_NAME ="hucodjek"
USER = "hucodjek"
PASSWORD = "Eryt_3nZU6fPM3tO1Q11735_FJIvBAys"
HOST = "flora.db.elephantsql.com"

conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST)
cur = conn.cursor()

def get_winners() :
    cur.execute("SELECT * FROM tictactoe ORDER BY id;")
    tictactoe = cur.fetchall()
    for winner in tictactoe :
        print(winner)

def add_winner(winner, opponent, xoro) :
    cur.execute("INSERT INTO tictactoe (winner, opponent, xoro) VALUES (%s, %s, %s) RETURNING iD;", (winner, opponent, xoro))
    winner_id = cur.fetchone()[0]
    conn.commit()
    print (f"Winner added with id: {winner_id}")

    conn.commit()
    print(f"Winner with id {winner_id} updated successfully")

if __name__ == "__main__":
    
    while True:
        print("\nList of Winners Menu")
        print("1. List winners")
        print("2. Add winner")
        print("X. Exit")

        choice = input("Enter your choice: ")

        if choice == "1": 
            get_winners()
        elif choice == "2" :
            winner = input("Winner name: ")
            opponent = input("Opponent: ")
            xoro= input("xoro: ")
            add_winner(winner, opponent, xoro)
            break
