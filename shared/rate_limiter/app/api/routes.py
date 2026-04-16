from fastapi import APIRouter, HTTPException
from app.services.rate_limiter import RateLimiter

router = APIRouter()
limiter = RateLimiter()

@router.get("/test")
def test(user id: str):
    if limiter.is_allowed(user_id):
        return {"message": "Request allowed"}
    else:
        raise HTTPException(status_code=429, detail="Too Many Requests")    