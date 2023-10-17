import datetime


class LogBook:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        timestamp = datetime.datetime.now()
        self.entries.append(f"{timestamp}: {entry}")

    def view_entries(self):
        for entry in self.entries:
            print(entry)


def main():
    logbook = LogBook()

    while True:
        print("1. Add log entry")
        print("2. View log entries")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            entry = input("Enter your log entry: ")
            logbook.add_entry(entry)
        elif choice == '2':
            logbook.view_entries()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
