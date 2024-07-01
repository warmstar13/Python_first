"""
def temp(x):
    x += 1
    print("flag 1")

num = 5
temp(num)
print(num)  

def temp2(x):
    x.append(12)
    print("flag 2")

list = [10]
temp2(list)
print(list)
""" 

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('albert', 'einstein',
#                             location='princeton',
#                             field='physics')
# print(user_profile) 


def func(*food):
    print(f"You have added {len(food)} toppings")

func('ketchup', 'runt', 'eggs')
func('nothing')