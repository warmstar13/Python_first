def city_country(name_city, country):
    return(f"{name_city.title()}, {country.title()}")

print(city_country("minsk", "belarus"))

def make_album(name_author, title, count=None):
    res = dict()
    res['name_author'] = name_author
    res["title"] = title
    res['count'] = count
    return res

print(make_album('Verocika', 'heavy jazz', 5))

list = []
while True:
    print("to quit, write 'q'")
    name = input("write name")
    if name == 'q':
        break
    title = input("write title")
    if title == 'q':
        break
    time = input("write num, '-1' if not given")
    if time == 'q':
        break
    if time == -1:
        list.append(make_album(name, title))
    else:
        list.append(make_album(name, title, time))
print(list)