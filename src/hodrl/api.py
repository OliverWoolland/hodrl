from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

def main():
    uvicorn.run("hodrl.api:app",
                host="0.0.0.0",
                port=8000,
                workers=4,
                reload=True)

if __name__ == "__main__":
    main()
