from fastapi import FastAPI, Query
from services import fetch_products 

app = FastAPI()



@app.get("/company/{companyName}/categories/{categoryname}/products")
async def get_sorted_products(
    companyName: str,
    categoryname: str,
    sort_by: str = Query(),
    top: int = Query(10, le=50),
    page: int = Query(1, ge=1),
    minPrice: int = Query(10, ge=0),
    maxPrice: int = Query(1000000, le=1000000),
    field: str = Query()
):
    products = await fetch_products(companyName, categoryname, top, minPrice, maxPrice)
    
    if field == "rating":
        products.sort(key=lambda p: p["rating"])
    elif field == "price":
        products.sort(key=lambda p: p["price"])
    elif field == "company":
        products.sort(key=lambda p: p["company"])
    elif field == "discount":
        products.sort(key=lambda p: p["discount"])
    else:
        return {"error": "Invalid sort field. Please use 'rating', 'price', 'company', or 'discount'."}
    skip = (page - 1) * 5
    products = products[skip:]
    
    if sort_by == "desc":
        products.reverse()
    
    return products


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
