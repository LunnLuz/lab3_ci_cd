import pytest, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),'..','src'))

from lab_2 import Lab_2

lab = Lab_2()


def test_fibonacci_negative():
    assert lab.Fibonacci(-5) == []
    assert lab.Fibonacci(0) == []


def test_fibonacci_boundary():
    assert lab.Fibonacci(1) == [0]
    assert lab.Fibonacci(2) == [0, 1]


def test_fibonacci_normal():
    assert lab.Fibonacci(5) == [0, 1, 1, 2, 3]
    assert lab.Fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_invalid_type():
    with pytest.raises(TypeError):
        lab.Fibonacci("abc")


def test_bubblesort_empty():
    assert lab.BubbleSort([]) == []


def test_bubblesort_sorted():
    assert lab.BubbleSort([1, 2, 3]) == [1, 2, 3]


def test_bubblesort_unsorted():
    assert lab.BubbleSort([3, 1, 2]) == [1, 2, 3]


def test_bubblesort_negative_numbers():
    assert lab.BubbleSort([0, -1, -5, 2]) == [-5, -1, 0, 2]


def test_bubblesort_invalid_type():
    with pytest.raises(TypeError):
        lab.BubbleSort("1230")


def test_eratosthen_negative():
    assert lab.EratosthenSieve(-10) == []
    assert lab.EratosthenSieve(0) == []
    assert lab.EratosthenSieve(1) == []


def test_eratosthen_boundary():
    assert lab.EratosthenSieve(2) == [2]


def test_eratosthen_normal():
    assert lab.EratosthenSieve(10) == [2, 3, 5, 7]
    assert lab.EratosthenSieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_eratosthen_invalid_type():
    with pytest.raises(TypeError):
        lab.EratosthenSieve("abc")
