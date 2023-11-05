import datetime
from Consignment import Consignment

if __name__ == "__main__":

  revenue = 0
  counter = 0
  Customer_actions = []
  choice = "Y"
  
  while choice == "Y" :
  
    kind = input("What do you want to post (Letter or Package)? ")
    address = input("Zip code: ")
    date = datetime.date.today()
    weight = 0
    size = None
    
    if kind == "Package":
      size = input("Package size (L or S): ") 
      if size != "S":
          weight = int(input ("Package weight: "))
  
    Customer_actions.append(Consignment(address, date, kind, size, weight))
  
    Customer_actions[counter].post()
    revenue += Customer_actions[counter].price

    print(revenue)
    print(Customer_actions)

    choice = input("Do you want to enter a new customer: (Y/N)")
    counter += 1