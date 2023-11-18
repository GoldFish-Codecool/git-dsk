import json
import os
from player import Player

FILE = os.path.dirname(os.path.abspath(__file__)) + '/board.json'

class LeadershipBoard:
    def __init__(self):
        self.scores = {}
        self.get_leaderboard()
    
    def add_player(self, name):
        if name not in self.scores.keys():
            self.scores[name] = 0
        self.save_leaderboard()

    def save_score(self, name, add_score):
        if name in self.scores.keys():
            self.scores[name] += add_score
        self.save_leaderboard()

    def get_leaderboard(self):
    # Reading the leadership board from the JSON file
        with open(FILE, 'r') as json_file:
            self.scores = json.load(json_file)

    def save_leaderboard(self):
    # Writing the dictionary to a JSON file
        with open(FILE, 'w') as json_file:
            json.dump(self.scores, json_file)
    
    def display_leaderboard(self):
        # Sort the scores in descending order
        scores_sorted = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)

        # Print the scores
        print('Leadership board:')
        for name, score in scores_sorted:
            print(f'{name}: {score}')