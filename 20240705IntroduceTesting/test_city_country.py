from city_functions import changing_cities

def test_city_country():
    assert changing_cities('santiago', 'chile', 50000) == "Santiago, Chile - population 50000"

def test_city_no_population():
    assert changing_cities("mak", "bela") == "Mak, Bela"