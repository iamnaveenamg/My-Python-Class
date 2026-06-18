def my_decorator(fx):
     
    def mainfunc(*args):
        print("Before calling the function")
        response = fx(*args)
        print("After calling the function")
        return response

    return mainfunc

@my_decorator
def fetch_data(url:str, path:str):
    return f"Fetching data from {url} and saving to {path}"


obj=fetch_data("https://api.example.com/data","temp/data.json")
print(obj)

print("Second Response")

obj1=fetch_data("https://example.com/data","temp/data.json")
print(obj1)