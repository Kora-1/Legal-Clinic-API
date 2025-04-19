# from fastapi import FastAPI
# from auth.routes import router as auth_router
#
# app = FastAPI()
#
# app.include_router(auth_router, prefix="/auth")
#

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router as auth_router  # Assuming auth.routes contains your router
from history import router as chat_router

app = FastAPI()


# CORS middleware setup
origins = [
    "*"
]

# Add CORSMiddleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific domains to access
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
@app.get("/")
async def root():
    return {"message": "API CREATED BY D (TEAM Techvocates)"}

# Include the router for authentication
app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router, prefix="/chat")
