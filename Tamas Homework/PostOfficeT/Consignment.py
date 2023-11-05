class Consignment:

  def __init__(self, address, date, tpye, size, weight):

    self.address = address
    self.date = date
    self.type = type
    self.size = size
    self.weight = weight
    self.price = 0

  def post (self) :
    #self.price = 111
    if self.type == "Letter" :
      self.price = 1.99
    
    elif self.type == "Package" and self.size == "S" :
      self.price = 7.99
    
    elif self.type == "Package" and self.size == "L" :
      self.price = 10.29 + self.weight * 0.29

    #print ("run")
    #print (self.type)
    #print (self.price)

    return self.price


