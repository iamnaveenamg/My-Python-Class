def weather_checker(temp:float)->str:
    if temp<0:
        return "It's Freezing outside"
    elif temp<15:
        return "It's a bit chilly"
    elif temp<25:
        return "The Weather is pleasant"
    else:
        return "It's Hot outside"

print(weather_checker(20))