import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url:str):
    print("Fetching data from:", url)
    time.sleep(5)
    print("data fetched form:", url)
    return "Data from "+url


urls_list=[
    "https://example.com/api/data1",
    "https://example.com/api/data2",
    "https://example.com/api/data3",
    "https://example.com/api/data4",
    "https://example.com/api/data5"
]

for i in urls_list:
    fetch_data(i)


print("Using ThreadPoolExecutor")
results = []
with ThreadPoolExecutor(max_workers=len(urls_list)) as executor:
    futures=[executor.submit(fetch_data, url) for url in urls_list]
    results.extend(futures)

print(results)
