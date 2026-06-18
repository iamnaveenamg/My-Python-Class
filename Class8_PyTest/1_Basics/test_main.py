from main import weather_checker

def test_weather_check():
    assert weather_checker(-5)=="It's Freezing outside"
    assert weather_checker(10)=="It's a bit chilly"
    assert weather_checker(20)=="The Weather is pleasant"
    assert weather_checker(30)=="It's Hot outside"
    print("All the Test Cases are Passed")



if __name__ == "__main__":
    test_weather_check()
