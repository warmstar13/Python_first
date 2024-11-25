def greet_user():
    """Display a simple greeting."""
    print("Hello!") 
    """fdsfasdf"""
greet_user()

def display_message():
    print("I am learning about functions in this chapter")

display_message()

def favourite_book(title):
    print(f"Today the winner is {title}")

favourite_book("terminator")
favourite_book("mecha")

def describe_pet(animal_type="dog", pet_name="cat"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster')