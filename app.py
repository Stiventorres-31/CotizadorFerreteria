from fastapi import FastAPI
from routes.personasRoutes import personasApiRouter
from routes.rolesRoutes import rolesApiRouter
app = FastAPI()
app.include_router(personasApiRouter)
app.include_router(rolesApiRouter)
