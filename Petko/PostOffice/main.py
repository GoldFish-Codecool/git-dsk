from classes.letter import Letter
from classes.box import Box
from classes.post_office import PostOffice

# Create a PostOffice object.
post_office = PostOffice()

# Add some items to the post office.
post_office.add_item(Letter("Moskovska 19", "2023-11-03"))
post_office.add_item(Box("Stamboliiski 73", "2023-11-03", 1500))
post_office.add_item(Box("Varnenchik 59", "2023-11-03", 500))

# Print the items posted on a given date.
post_office.print_items_on_date("2023-11-03")

# Print the total revenue and breakdown by item type.
post_office.print_revenue()
