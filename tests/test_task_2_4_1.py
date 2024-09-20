import pytest
from src.task_2_4_1 import sum_divisible_by_3_or_5


@pytest.fixture
def nums_1():
    return [i for i in range(10)]


@pytest.fixture
def nums_2():
    return [i for i in range(3)]


@pytest.fixture
def nums_3():
    return [3, 5, 6, 9]


def test_sum_divisible_by_3_or_5_1(nums_1):
    assert sum_divisible_by_3_or_5(nums_1) == 23


def test_sum_divisible_by_3_or_5_2(nums_2):
    assert sum_divisible_by_3_or_5(nums_2) == 0


def test_sum_divisible_by_3_or_5_3(nums_3):
    assert sum_divisible_by_3_or_5(nums_3) == 23

def test_sum_divisible_by_3_or_5_4():
    assert sum_divisible_by_3_or_5([9, 11, 12]) == 21
