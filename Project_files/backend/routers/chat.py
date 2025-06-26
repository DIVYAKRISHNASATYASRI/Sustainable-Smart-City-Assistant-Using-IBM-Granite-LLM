from fastapi import APIRouter, Request
from services.ibm_granite_llm import query_llm

router = APIRouter()

@router.post("/")
async def chat_response(request: Request):
    data = await request.json()
    user_query = data.get("query")
    response = query_llm(user_query)
    return {"response": response}