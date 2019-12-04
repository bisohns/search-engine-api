from fastapi import FastAPI, HTTPException
from search_engine_parser.core.engines import ENGINE_DICT
from search_engine_parser.core.exceptions import NoResultsOrTrafficError

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/search/")
async def query(query: str, engine: str = "google", page: int = 1):
    try:
        _engine = ENGINE_DICT[engine]()
        results = await _engine.async_search(query, page)
    except KeyError:
        raise HTTPException(status_code=404, detail="Specified Engine Does not Exist")
    except NoResultsOrTrafficError:
        raise HTTPException(status_code=404, detail=f"Cannot contact the {engine.upper()} server, try again")

    return results

