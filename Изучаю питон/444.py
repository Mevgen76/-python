class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("year:", self.year, ' City:', self.city)   

school = Building(2000, "Miami")  
blabla = Building(2000, "Miami")    
qweqwe = Building(2000, "Miami")      
