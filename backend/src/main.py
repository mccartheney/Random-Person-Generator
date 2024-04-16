# import fast api
from fastapi import FastAPI
# import persons route
from routes import persons
# import uvicorn to run app
import uvicorn

# init api app
api = FastAPI(
    title="Random Person Generator",
    description= "Api to generate persons"
)

# create routers array and add router from persons
routers = [
    persons.router
]

# loop through routers
for router in routers :
    # add routers to api app
    api.include_router(router=router)

# init api
if __name__ == "__main__" :
    uvicorn.run(
        app=api,
        host="0.0.0.0",
    )