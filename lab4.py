class Park:
    def __init__(self, name, rating=0.0, address="", bike_path_lenght=0, ticket_price=0.0):
        self.name = name
        self.rating = rating
        
        self.__address = address
        self.__bike_paths = bike_path_lenght
        self.__ticket_price = ticket_price

    def __del__(self):
        print(f"Парк '{self.name}' видалено.")

    def get_address(self):
        return self.__address
    
    def get_bike_paths(self):
        return self.__bike_paths
    
    def get_ticket_price(self):
        return self.__ticket_price

    def __str__(self):
        return f"Парк '{self.name}' ({self.rating}★) | {self.__address} | Доріжки: {self.__bike_paths}м | Вхід: {self.__ticket_price}"

    def __repr__(self):
        return f"Park('{self.name}', {self.rating}, '{self.__address}', {self.__bike_paths}, {self.__ticket_price})"



if __name__ == "__main__":
    parks = [
        Park(name="pepe"), 
        Park("Стрийській", 4.8, "вул. Стрийська", 5000, 0.0),
        Park("Культури", 4.5, "вул. Дмитра Вітовського", 12000, 300.0)
    ]

    for p in parks:
        print(f"__str__: {p}")
        print(f"__repr__: {repr(p)}")
        print(f"Геттери: {p.get_address()}, {p.get_bike_paths()}м, {p.get_ticket_price()}грн\n")

        print(parks[0].rating)