from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers import summarization, feedback, chat, kpi

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarization.router, prefix="/summarize")
app.include_router(feedback.router, prefix="/feedback")
app.include_router(chat.router, prefix="/chat")
app.include_router(kpi.router, prefix="/forecast")