city_monuments = {
    "Delhi": "Red Fort",
    "Agra": "Taj Mahal",
    "Jaipur": "Jal Mahal"
}

city = input("Enter the name of the city: ").strip()

if city in city_monuments:
    print(f"The monument of {city} is {city_monuments[city]}.")
else:
    print("Sorry, monument information for this city is not available.")