from fastapi import FastAPI
from app.routes import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'https://www.elevengrandesobras.com.br/',
    'https://editor.wix.com/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=['POST', 'OPTIONS'],
    allow_headers=['Content-Type'],
)

app.include_router(predict.router)
