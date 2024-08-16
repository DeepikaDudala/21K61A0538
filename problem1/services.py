import httpx
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

async def fetch_products(
    companyName: str,
    categoryname: str,
    top: int,
    minPrice: int,
    maxPrice: int
) -> List[Dict]:
    
    url = f"{os.getenv("TEST_SERVER_URL")}/companies/{companyName}/categories/{categoryname}/products"
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url, 
            headers={"Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"},
            params={"top": top, "minPrice": minPrice, "maxPrice": maxPrice}
        )
        response.raise_for_status()
        data = response.json()
    
    return data
