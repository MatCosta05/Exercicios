import test
import pytest

from Fibo import Fibo

class TesteFibo:
    @pytest.fixture
    def setup(self):
        pass

    def TestFibo(self):
        x = Fibo()
        assert x.Fibo(0) == StopIteration
        assert x.__next__(5) == 8
