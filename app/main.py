from fastapi import FastAPI, Response, status

app = FastAPI()

@app.get("/", tags = ["test"], summary = "A test endpoint", description = "A test with get method", response_description ="Return dummy info")
async def root(response:Response):
    response.status_code = status.HTTP_200_OK
    return {"message": "Hello world"}

@app.post("/item/{id}", tags = ["test", "item"], summary = "A test endpoint", description = "A test with post method", response_description ="Return dummy info")
async def add_item(response:Response, id:int):
    response.status_code = status.HTTP_200_OK
    return {"item_id": f"{id}"}