from fastapi import FastAPI, HTTPException
from search_engine_parser.core.engines import ENGINE_DICT
from search_engine_parser.core.exceptions import NoResultsOrTrafficError

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/search/")
async def query(query: str, engine: str = "google", page: int = 1, limit: int = 10):
    try:
        _engine = ENGINE_DICT[engine]()
    except KeyError:
        raise HTTPException(status_code=404, detail="Specified Engine Does not Exist")
    results = await _engine.async_search(query, page)
    return results

