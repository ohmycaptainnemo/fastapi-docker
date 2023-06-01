import uvicorn
import os
from fastapi import FastAPI, Query


PORT = int(os.environ.get("API_PORT", "5555"))

app = FastAPI(
    version="0.0.1",
    title="Test Rest API",
    description="An API for Testing Purposes.",
    docs_url="/",
)

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
fake_items = [
    {
        "item_id": 1,
        "secondary_key": 2,
        "another_one": "hello"
    },
    {
        "item_id": 2,
        "secondary_key": 2,
        "another_one": "bye"
    },
    {
        "item_id": 3,
        "secondary_key": 2,
        "another_one": "bye2"
    },
    {
        "item_id": 4,
        "secondary_key": 3,
        "another_one": "bye33"
    },
    {
        "item_id": 5,
        "secondary_key": 6,
        "another_one": "noice!!"
    },
    {
        "item_id": 6,
        "secondary_key": 7,
        "another_one": "noice!!"
    }
]

@app.get("/items/")
async def read_items(another_one: str = "", sort_by: str = Query("item_id", enum=["item_id", "secondary_key"]), order_by: str = Query("asc", enum=["asc", "desc"])):
    print("heelo")
    if another_one:
        result = [d for d in fake_items if d['another_one'] == another_one]
    else:
        result = fake_items
    if order_by=="desc":
        result = sorted(result, key=lambda x: x[sort_by], reverse=True)
        return result
    result = sorted(result, key=lambda x: x[sort_by])
    return result


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return [d for d in fake_items if d.get("item_id") == item_id]


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=PORT, reload=True)
