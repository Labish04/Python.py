weather = input("What is the weather like today? (sunny/rainy): ")

if weather == "sunny":
    print("The weather is sunny! You could go hiking or have a picnic.")
elif weather == "rainy":
    has_rain_gear = input("Do you have a raincoat or umbrella? (yes/no): ")
    if has_rain_gear == "yes":
        print("You could visit a nearby mall or museum.")
    else:
        print("It's best to stay home and watch some movies.")
else:
    print("Sorry, I don't have suggestions for this weather.")