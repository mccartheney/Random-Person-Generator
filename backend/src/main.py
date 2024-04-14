from fastapi import FastAPI
from routes import persons
import uvicorn

api = FastAPI(
    title="Random Person Generator",
    description= "Api to generate persons"
)

routers = [
    persons.router
]

for router in routers :
    api.include_router(router=router)

if __name__ == "__main__" :
    uvicorn.run(
        app=api,
        host="0.0.0.0",
    )