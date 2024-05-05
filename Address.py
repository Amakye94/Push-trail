class Address:

    # constructor
    def __init__(self,street, house_number, postal_code, town):
        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.town = town

    def getAddress(self):
        return self.street + " " + str(self.house_number) + " " \
            + str(self.postal_code) +" " + self.town

# getter and setter
def get_postal_code(self):
    return self.postal_code()

def get_house_number(self):
    return self.house_number

def set_street(self, street):
    self.street = street

def set_postal_code(self, postal_code):
    self.postal_code = postal_code