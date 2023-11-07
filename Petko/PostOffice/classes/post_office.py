import csv

from classes.letter import Letter
from classes.box import Box

class PostOffice:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.save_item_to_file(item)

    def calculate_revenue(self):
        revenue_letters = 0
        revenue_small_boxes = 0
        revenue_big_boxes = 0
        for item in self.items:
            if isinstance(item, Letter):
                revenue_letters += item.price
            elif isinstance(item, Box) and item.price == 7.99:
                revenue_small_boxes += item.price
            elif isinstance(item, Box) and item.price > 7.99:
                revenue_big_boxes += item.price

        return revenue_letters, revenue_small_boxes, revenue_big_boxes

    def print_items_on_date(self, date):
        items_on_date = []
        for item in self.items:
            if item.date_posted == date:
                items_on_date.append(item)

        if len(items_on_date) == 0:
            print(f"No items posted on {date}.")
        else:
            print(f"Items posted on {date}:")
            for item in items_on_date:
                if isinstance(item, Letter):
                    print(f"Letter to {item.address}")
                elif isinstance(item, Box):
                    print(f"Box to {item.address} ({item.weight} grams)")

    def print_revenue(self):
        revenue_letters, revenue_small_boxes, revenue_big_boxes = self.calculate_revenue()
        total_revenue = revenue_letters + revenue_small_boxes + revenue_big_boxes

        print(f"Total revenue: {total_revenue} Euros")
        print(f"Revenue from letters: {revenue_letters} Euros")
        print(f"Revenue from small boxes: {revenue_small_boxes} Euros")
        print(f"Revenue from big boxes: {revenue_big_boxes} Euros")

    def save_item_to_file(self, item):
        with open("database/posted_items.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if isinstance(item, Letter):
                writer.writerow(["Letter", item.address, item.date_posted, "", item.price])
            elif isinstance(item, Box):
                writer.writerow(["Box", item.address, item.date_posted, item.weight, item.price])
