import datetime
from Consignment import Consignment

if __name__ == "__main__":

  revenue = 0
  Customer_actions = []
  choice = "Y"
  
  while choice == "Y" :
  
    type = input("What do you want to post (Letter or Package)? ")
    address = input("Zip code: ")
    date = datetime.date.today()
    weight = 0
    size = None
    
    if type == "Package":
      size = input("Package size (L or S): ") 
      if size != "S":
          weight = int(input ("Package weight: "))
  
    Customer_actions.append(Consignment(address, date, type, size, weight))
  
    Customer_actions[0].post()
    revenue += Customer_actions[0].price

    print(revenue)
    print(Customer_actions)

    choice = input("Do you want to enter a new customer: (Y/N)")