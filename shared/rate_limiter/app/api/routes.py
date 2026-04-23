from fastapi import APIRouter, HTTPException
from app.services.rate_limiter import RateLimiter

router = APIRouter()
limiter = RateLimiter()

@router.get("/test")
def test(user_id: str):   
    if not limiter.allow_request(user_id):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    return {"message": "Success"}