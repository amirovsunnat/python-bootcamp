country = input("Which country did you visit?\n>>> ")  # Add country name
visits = int(input("How many times did you visit to this country?\n>>> "))  # Number of visits
list_of_cities = eval(input("Name the list of cities you have visited\n>>> "))  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, visits_count, cities):
    new_country = {"country": country_visited, "visits": visits_count, "cities": cities}
    travel_log.append(new_country)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
