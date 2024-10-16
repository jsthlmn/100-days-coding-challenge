travel_log = [
    {
        "country": "france",
        "cities_visited": ["paris", "lile", "dijon"],
        "total_visited": 12
    },
    {
        "country": "german",
        "cities_visited": ["berlin", "hambrug", "stuttgard"],
        "total_visited": 10
    }
]

def add_new_dictionary(counrty_visited, time_visited, cities_visited):
    new_dictionary = {}
    new_dictionary["country"] = counrty_visited
    new_dictionary["cities_visited"] = cities_visited
    new_dictionary["total_visited"] = time_visited

    travel_log.append(new_dictionary)

add_new_dictionary("rusia", "15", ["moscow", "saint-petersburg", "kalingrad"])
print(travel_log)