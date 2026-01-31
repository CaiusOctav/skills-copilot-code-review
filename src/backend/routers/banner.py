"""
Banner configuration API endpoints
"""

from fastapi import APIRouter, HTTPException
from ..database import banner_collection

router = APIRouter()


@router.get("/banner")
def get_banner():
    """Get the current banner configuration"""
    banner = banner_collection.find_one({"_id": "announcement_banner"})
    
    if not banner:
        return {
            "enabled": False,
            "message": "",
            "end_date": None
        }
    
    # Remove MongoDB _id field from response
    banner_data = {
        "enabled": banner.get("enabled", False),
        "message": banner.get("message", ""),
        "end_date": banner.get("end_date", None)
    }
    
    return banner_data
