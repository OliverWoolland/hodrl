from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

from hodrl import asset_queries

app = FastAPI()

@app.get("/assets")
async def get_assets():
    assets = asset_queries.get_all_assets()
    result = JSONResponse(content=assets, status_code=200)
    return result

def main():
    uvicorn.run("hodrl.api:app",
                host="0.0.0.0",
                port=8000,
                workers=4,
                reload=True)

if __name__ == "__main__":
    main()
