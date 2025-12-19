import pytest, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),'..','src'))
from lab_2 import Lab_2

class TestLab:
    def test_fibonacci_negative(self):
        """n < 1 — граничное значение"""
        assert Fibonacci(-5) == []
        assert Fibonacci(0) == []

    def test_fibonacci_boundary(self):
        """Граничные значения"""
        assert Fibonacci(1) == [0]
        assert Fibonacci(2) == [0, 1]

    def test_fibonacci_normal(self):
        """Корректные значения n > 2"""
        assert Fibonacci(5) == [0, 1, 1, 2, 3]
        assert Fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

    def test_fibonacci_invalid_type(self):
        """Некорректный тип данных"""
        with pytest.raises(TypeError):
            Fibonacci("abc")


    def test_bubblesort_empty(self):
        """Пустой список"""
        assert BubbleSort([]) == []

    def test_bubblesort_sorted(self):
        """Уже отсортированный список"""
        assert BubbleSort([1, 2, 3]) == [1, 2, 3]

    def test_bubblesort_unsorted(self):
        """Неотсортированный список"""
        assert BubbleSort([3, 1, 2]) == [1, 2, 3]

    def test_bubblesort_negative_numbers(self):
        """Список с отрицательными числами"""
        assert BubbleSort([0, -1, -5, 2]) == [-5, -1, 0, 2]

    def test_bubblesort_invalid_type(self):
        """Некорректный тип данных"""
        with pytest.raises(TypeError):
            BubbleSort("1230")


    def test_eratosthen_negative(self):
        """n < 2 — граничные значения"""
        assert EratosthenSieve(-10) == []
        assert EratosthenSieve(0) == []
        assert EratosthenSieve(1) == []

    def test_eratosthen_boundary(self):
        """Граничное значение"""
        assert EratosthenSieve(2) == [2]

    def test_eratosthen_normal(self):
        """Корректные входные данные"""
        assert EratosthenSieve(10) == [2, 3, 5, 7]
        assert EratosthenSieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_eratosthen_invalid_type(self):
        """Некорректный тип данных"""
        with pytest.raises(TypeError):
            EratosthenSieve("abc")
