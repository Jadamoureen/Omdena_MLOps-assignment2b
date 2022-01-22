# import modules 

from calculateArces import acres 
import uvicorn
from fastapi import FastAPI, Request 


# instantiate fastapi
app = FastAPI()

@app.get("/")

async def get_input(request:Request):
    packet = await request.json()
    print(packet)
    length = packet['length']
    width = packet['width']

    acres_ = acres(length, width)

    return {"Acres":acres_}

# driver function 

if __name__ == "__main__":
    uvicorn.run()


     