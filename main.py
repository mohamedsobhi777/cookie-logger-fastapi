from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root(request: Request):
    print("Received cookies:", request.cookies)
    return {"message": "Cookie information logged to console"}