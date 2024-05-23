import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/')
async def root(request: Request):
    print(await request.json())
    return True


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8001,
        reload=True
    )
