class Consignment:

  def __init__(self, address, date, kind, size, weight):

    self.address = address
    self.date = date
    self.kind = kind
    self.size = size
    self.weight = weight
    self.price = 0

  def post (self) :

    if self.kind == "Letter" :
      self.price = 1.99
    
    elif self.kind == "Package" and self.size == "S" :
      self.price = 7.99
    
    elif self.kind == "Package" and self.size == "L" :
      self.price = 10.29 + self.weight * 0.29

    print ("run")
    print (self.kind)
    print (self.price)

    return self.price


