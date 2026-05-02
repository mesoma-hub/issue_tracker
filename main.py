from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware

app = FastAPI()
app.middleware("http")(timing_middleware)
app.include_router(issues_router)


















# Next we start creating routes using the @app.get() decorator. 
# This decorator tells FastAPI that the function that follows is a 
# route handler for GET requests to the specified path.

# items = [
#     {"id": 1, "name": "Item One"},
#     {"id": 2, "name": "Item Two"},
#     {"id": 3, "name": "Item Three"},
# ]
# # The dictionary returned by the function will be automatically converted to JSON and sent as the response.
# @app.get("/health")
# def health_check():
#     return {"status": "ok"}


# @app.get("/items")
# def read_items():
#     return items

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     for item in items:
#         if item["id"] == item_id:
#             return item
#     return {"error": "Item not found"}

# @app.post("/items")
# def create_item(item: dict):
#     new_item = {"id": len(items) + 1, "name": item["name"]}
#     items.append(new_item)
#     return new_item