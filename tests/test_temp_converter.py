
from utils.temp_converter import c_to_f, f_to_c
import math


def test_c_to_f_basic():
    assert c_to_f(0)==32
    assert c_to_f(100)==212



def test_f_to_c_basic():
    assert f_to_c(32) == 0
    assert math.isclose(f_to_c(212), 100.0, rel_tol=1e-9)


def test_invalid_inputs_raise():
    for bad in ["abc",None,object()]:
        try:
            c_to_f(bad)
            assert False, "Expected ValueError"
        except ValueError:
            pass