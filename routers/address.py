from fastapi import APIRouter
router=APIRouter()
@router.get("/address")
def root():
    return {"Message":"Launching Soon!!!!"}