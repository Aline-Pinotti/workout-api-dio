from fastapi import FastAPI
from fastapi_pagination import add_pagination
from workout_api.routers import api_router

HOST = '0.0.0.0'
PORT = 8080

app = FastAPI(title='WorkoutAPI')
add_pagination(app)
app.include_router(api_router)

""" if __name__ == 'main':
    import uvicorn
    
    uvicorn.run('main:app', host= HOST, port=PORT, log_level='info', reload = True) """