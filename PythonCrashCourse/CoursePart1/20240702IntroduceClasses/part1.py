class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"The restaurant is named {self.name}")
        print(f"The topic is {self.type}")

    def open_restaurant(self):
        print("restaurant is opened!")

# restaurant = Restaurant("zhanchik", "shavermichna")
# restaurant.open_restaurant()
# restaurant.describe_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, name, toppings):
        super().__init__(name, "Icecream")
        self.flavors = toppings

    def print_toppings(self):
        print(self.flavors)

temp = IceCreamStand("kobrin", ['cheese', 'choco', 'vanille'])
temp.print_toppings()

class User:
    def __init__(self, first_name, last_name = '', age = '99'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.number_served = 0

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num

    def print_number_served(self):
        print(f"{self.number_served} people are already served")

    def describe_user(self):
        print(f'The user is named as {self.first_name} {self.last_name}')
        print(f"he said his age is {self.age}")

    def greet_user(self):
        print(f"Hello, my dear {self.first_name}")

class Admin(User):
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.print_priv()

    # def delete_privilege(self, str):
    #     self.privileges.remove(str)

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def print_priv(self):
        print(self.privileges)

joe = Admin("joe", "brook", 13, ['cooks', 'codes', 'sleeps'])
joe.show_privileges()
joe.describe_user()
# joe.delete_privilege('cooks')
# joe.show_privileges()

# user1 = User("John")
# user2 = User("Maria", "Bellick", 23)

# user1.describe_user()
# user2.describe_user()

# user1.greet_user()

# user1.set_number_served(5)
# user1.print_number_served()
# user1.increment_number_served(10)
# user1.print_number_served()