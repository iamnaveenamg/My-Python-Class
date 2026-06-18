#import time

# Normal API Call

#def api_call():
#    time.sleep(3)
#    return "Ordered Data"

#def execute():
#    print("Executing API Call")
#    result=api_call()
#    print("Data Fetched:", result)


#execute()

# Asyncio API Call
import asyncio

async def api_call():
    await asyncio.sleep(3)
    return "Orders Data"


async def execute():
    print("Executing API Call")
    result=await api_call()
    print("Data Fetched: ", result)

asyncio.run(execute())
