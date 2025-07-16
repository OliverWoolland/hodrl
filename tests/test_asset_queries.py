from hodrl import asset_queries

import pytest

@pytest.fixture
def all_assets():
    all_assets = [{'asset': {'type': 'uri', 'value': 'http://example.com/asset:9898.movie'}}]
    return all_assets

def test_get_all_assets(all_assets):
    result = asset_queries.get_all_assets()
    print(result)

    # Asset data should not be empty
    assert result is not None

    # Asset data should be a list
    assert isinstance(result, list)

    # Asset data should contain dictionaries
    assert all(isinstance(asset, dict) for asset in result)

    # Asset all_assets should match the expected data
    assert result == all_assets
