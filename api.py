import uvicorn
import os
from fastapi import FastAPI


PORT = int(os.environ.get("API_PORT", "5555"))

app = FastAPI(
    version="0.0.1",
    title="Test Rest API",
    description="An API for Testing Purposes.",
    docs_url="/",
)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=PORT, reload=True)
