import pytest

#==========================================================================================
@pytest.mark.parametrize("input, expected", [((1, '11',111 ,1 ,1), 5), ((), 0), ((1,), 1)])
def test_tuple_len(input, expected):
    assert len(input) == expected

Tuple01 = (1, 2, (2, (2, 2)), 3, 4, 5, "sleep")
def test_tuple_count():
    assert Tuple01.count(2) == 1

Tuple02 = ("stop", "testing", "make", "love")
def test_tuple_out_of_index():
    try:
        assert Tuple02[7]
    except IndexError:
        pass

#=========================================================================================

def test_dict_keys():
    D = {"Money":None, "Time":None, "Energy":None}
    assert list(D.keys()) == ["Money", "Time", "Energy"]

def test_dict_clear():
    D = {"name":"Vasya", "job":"Bratyunya"}
    D.clear()
    assert list(D.items()) == []

def test_dict_update():
    D = {"name":"Vasya", "job":"Bratyunya"}
    D.update({"salary":"70k"})
    assert D["salary"] == "70k"