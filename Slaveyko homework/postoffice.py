# Parcel classes
class Parcel:
    def __init__(self, address, date_posted):
        self.address = address
        self.date_posted = date_posted
        self.post_index = None
        self.price = 0

class Letter(Parcel):
    def __init__(self, address, date_posted):
        super().__init__(address, date_posted)
        self.price = 1.99

class Small_Box(Parcel):
    def __init__(self, address, date_posted):
        super().__init__(address, date_posted)
        self.price = 7.99

class Large_Box(Parcel):
    def __init__(self, address, date_posted, weight_grams):
        super().__init__(address, date_posted)
        self.weight = weight_grams
        self.calculate_price()
    
    def calculate_price(self):
        self.price = round(10.29 + 0.29 * self.weight, 2)


# Post Office class
class PostOffice:
    post_index = 0

    def __init__(self):
        self.parcels = []
    
    def add_parcel(self, parcels_to_add):
        for parcel in parcels_to_add:
            PostOffice.post_index += 1
            parcel.post_index = PostOffice.post_index
            self.parcels.append(parcel)
    
    def parcels_bydate(self, date_filter):
        str_parcel = '\n'
        
        for parcel in self.parcels:
            if parcel.date_posted == date_filter:
                str_parcel += f'post_index:{parcel.post_index} address:{parcel.address} price:{parcel.price}\n'
        
        return str_parcel

    def income_bytype(self, parcel_type='all'):  
    # parcel_type l, sb, lb, all
        income = 0
        
        for parcel in self.parcels:
            if isinstance(parcel, Large_Box) and parcel_type == 'lb':
                income += parcel.price
            elif isinstance(parcel, Small_Box) and parcel_type == 'sb':
                income += parcel.price
            elif isinstance(parcel, Letter) and parcel_type == 'l':
                income += parcel.price
            elif parcel_type == 'all':
                income += parcel.price
        
        return income


# Main program
if __name__ == "__main__":

    # Generate samples
    a1 = Large_Box('Sofia, etc', '2023-12-11', 200)
    a2 = Small_Box('Paris, etc', '2023-12-11')
    a3 = Letter('London, etc', '2023-12-12')
    a4 = Large_Box('Sofia, etc', '2023-12-12', 340)
    a5 = Small_Box('Paris, etc', '2023-12-12')
    a6 = Letter('London, etc', '2023-12-12')

    post_office = PostOffice()

    post_office.add_parcel([a1, a2, a3, a4, a5, a6])

    print(post_office.income_bytype('lb'))
    print(post_office.parcels_bydate('2023-12-12'))
