import pytest

@pytest.fixture
def all_assets():
    all_assets = [
        {'asset': {'type': 'uri', 'value': 'http://example.com/asset:9898.movie'}}
    ]
    return all_assets
