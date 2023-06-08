import os
import asyncio
from concurrent.futures import ProcessPoolExecutor
from loguru import logger
from datetime import date

from pydantic import BaseModel
from typing import List

import uvicorn
from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv()



app = FastAPI()


class Images(BaseModel):
    images: List[str]


@app.get('/healthcheck')
def healthcheck():
    return {'status': 'ok'}


@app.post('/images_to_json_post')
async def images_to_json_post(images: Images):
    for image in images.images:
        logger.info(image)

    return {"status": "POST method ok"}


@app.get('/images_to_json_get')
async def images_to_json_get(images: Images):
    for image in images.images:
        logger.info(image)
    
    return {"status": "GET method ok"}



# @app.post('/train/pitcher')
# async def train_pitcher(train_player: TrainPlayer):
#     return await train(Pitcher, train_player)


# @app.post('/train/runner')
# async def train_runner(train_player: TrainPlayer):
#     return await train(Runner, train_player)


# @app.post('/train/selector')
# async def train_selector(train_player: TrainPlayer):
#     return await train(Selector, train_player)


# @app.on_event("startup")
# async def on_startup():
#     app.state.executor = ProcessPoolExecutor()


# @app.on_event("shutdown")
# async def cancel_tasks():
#     app.state.executor.shutdown()


# def handle(connection_str, player):
#     if player.position in ('pitcher', 'better'):
#         instructor = InstructorPB(player, connection_str)
#         instructor.train_player(player)
#     elif player.position in ('runner', 'selector'):
#         instructor = InstructorSR(player, connection_str)
#         instructor.train_player(player)


# async def train(player_type: type, train_player: TrainPlayer):
#     player = player_type(
#         train_player.player_id,
#         train_player.team_abbr,
#         train_player.date)

#     fut = asyncio.get_running_loop().run_in_executor(
#         app.state.executor,
#         handle,
#         connection, player)

#     await fut
#     return {'status': 'done'}


if __name__ == '__main__':
    uvicorn.run("server:app", port=int(os.environ['SERVER_PORT']), log_level="info")
