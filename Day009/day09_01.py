# nested dictionary

travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visit": 12
     },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visit": 5
     }
]


def add_new_country(country_1, cities_visited_1, total_visit_1):
    new_country = dict()
    x = (travel_log[0].keys())

    l_keys = []
    for _ in x:
        l_keys.append(_)

    new_country[l_keys[0]] = country_1
    new_country[l_keys[1]] = cities_visited_1
    new_country[l_keys[2]] = total_visit_1
    travel_log.append(new_country)

    print(travel_log)


add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)


