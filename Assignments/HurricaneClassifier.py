def get_wind_speed():
    wind_speed = input("What is the wind speed? ")
    try:
        wind_speed = int(wind_speed)
    except:
        print("Invalid speed. Enter a valid wind speed.")
        get_wind_speed()
    return wind_speed

wind_speed = get_wind_speed()
get_wind_speed()

if wind_speed < 74:  
    print("Tropical storm")
elif wind_speed < 96:
    print("Category 1")
elif wind_speed < 111:
    print("Category 2")
elif wind_speed < 130:
    print("Category 3")
elif wind_speed < 157:
    print("Category 4")
else:
    print("Category 5")