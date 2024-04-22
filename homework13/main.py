from fastapi import FastAPI
from src.routes.contacts import router as contacts_router
from src.routes.auth import router as auth_router
from src.routes.users import router as users_router
from src.middleware.cors import add_cors_middleware

app = FastAPI()

add_cors_middleware(app)

app.include_router(contacts_router, prefix="/contacts", tags=["contacts"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])
