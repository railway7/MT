from fastapi import FastAPI
import uvicorn
from main import application



app = FastAPI(
    title='MTAPI by spiritlhl',
    description='个人部署，请修改run.py文件部署',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
)

#prefix后缀地址
app.include_router(application, prefix='/MT', tags=['MT'])#, prefix='/b'



if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8765, reload=True, debug=True, workers=1)
