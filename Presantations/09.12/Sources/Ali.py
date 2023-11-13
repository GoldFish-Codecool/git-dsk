attendees = [
    {'name': 'John', 'present': True},
    {'name': 'Mary', 'present': False},
    {'name': 'Bob', 'present': True},
    {'name': 'Sarah', 'present': True},
    {'name': 'Ali', 'present': None},
]

Ali_present = input('Is Ali present today? (Y/N)')

if Ali_present == 'Y':
    attendees[4]['present'] = True
else:
    attendees[4]['present'] = False

present_attendees = []
non_present_attendees = []

for attendee in attendees:
    if attendee['present']:
        present_attendees.append('Hello ' + attendee['name'])
    else:
        non_present_attendees.append('Goodbye ' + attendee['name'])

print("\n".join(present_attendees))
print("\n".join(non_present_attendees))