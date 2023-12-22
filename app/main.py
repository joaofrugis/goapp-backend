from fastapi import FastAPI
from app.routes import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'https://www.elevengrandesobras.com.br/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(predict.router)
