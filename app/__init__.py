import os
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

    
def create_app():

    app = FastAPI()

    # app.config.from_mapping( SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess',)
    
    from app.routes import index

    app.include_router(index.router)

    app.add_middleware( CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)

    return app

app = create_app()