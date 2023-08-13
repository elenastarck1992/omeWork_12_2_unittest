from utils import arrs


def test_get(test_collection):
    assert arrs.get(test_collection, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(test_collection):
    assert arrs.get(test_collection, 1, 3) == [2, 3]
    assert arrs.get(test_collection, 1) == [2, 3, 4]
    assert arrs.get(test_collection, -2) == [3, 4]
    assert arrs.get(test_collection, -5) == [1, 2, 3, 4]
    assert arrs.get([]) == []
