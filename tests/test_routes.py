from starlette.testclient import TestClient
from search_engine_parser.core.engines import ENGINE_DICT
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_query_fail_without_engine():
    response = client.get("/search/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Specified Engine Does not Exist"}

def test_query_fail_without_engine():
    for engine in ENGINE_DICT.keys():
        response = client.get(f"/search/?engine={engine}&&query=\"Who am I\"")
        assert response.status_code == 200
