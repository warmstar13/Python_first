def changing_cities(city_name, country_name, population=''):
    str = f"{city_name}, {country_name}".title()
    if population:
        str += f" - population {population}"
    return str