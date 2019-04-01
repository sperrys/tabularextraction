
from ..validators import number


def test_number_true():

    results = []

    res, val = number("1")
    results.append(res)

    res, val = number("02144")
    results.append(res)

    assert False not in results


def test_number_false():

    results = []

    res, val = number("()")
    results.append(res)

    res, val = number(" ")
    results.append(res)

    assert True not in results


def test_num_digits_true():

    results = []

    res, val = number("1", num_digits=1)
    results.append(res)

    res, val = number("02155", num_digits=5)
    results.append(res)

    assert False not in results


def test_num_digits_false():

    results = []

    res, val = number("1", 0)
    results.append(res)

    res, val = number("02155", num_digits=4)
    results.append(res)

    assert True not in results


def test_max_true():

    results = []

    res, val = number("0", max=0)
    results.append(res)

    res, val = number("10", max=12)
    results.append(res)

    assert False not in results


def test_max_false():

    results = []

    res, val = number("1", max=0)
    results.append(res)

    res, val = number("14", max=12)
    results.append(res)

    assert True not in results


def test_min_true():

    results = []

    res, val = number("12", min=10)
    results.append(res)

    res, val = number("0", min=0)
    results.append(res)

    assert False not in results


def test_min_false():

    results = []

    res, val = number("1", min=10)
    results.append(res)

    res, val = number("2", min=0)
    results.append(res)

    assert False not in results

