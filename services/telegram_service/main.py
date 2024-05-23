import uvicorn
from fastapi import FastAPI, Request

from schemas import Answer

app = FastAPI()


@app.post('/')
async def root(request: Request):
    result_dict = await request.json()
    result_obj = Answer(**result_dict)
    print(f'<first_name="{result_obj.message.from_tg.first_name}", message="{result_obj.message.text}">')
    return True


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8001,
        reload=True
    )
