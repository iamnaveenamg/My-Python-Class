class api_fetch:
    def fetch(self):
        print("Fetching data from API...")

class database_fetch:
    def fetch(self):
        print("Fetching data from database...")

class s3_fetch:
    def fetch(self):
        print("Fetching data from s3....")

## Same Action but different implementation

obj=s3_fetch()
print(obj.fetch())