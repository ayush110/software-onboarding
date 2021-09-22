import sandbox as sb


def test_add_one():
    val = 10
    assert sb.add_one(val) == 11


def test_add_two():
    val = 1
    assert sb.add_two(val) == 3


def test_fibonnaci_by_index():
    indices = (0, 1, 2, 3, 19, 35, 74, 100)
    values = (0, 1, 1, 2, 4181, 9227465, 1304969544928657, 354224848179261915075)
    for index, val in zip(indices, values):
        assert sb.fibonacci_by_index(index) == val


def test_multiply_by_two():
    val = 1
    assert sb.multiply_by_two(val) == 2


def test_subtract_one():
    val = 1
    assert sb.subtract_one(val) == 0


def test_triple_add_one():
    inputs = (0, 1, 2, -1, 10)
    expecteds = (1, 4, 7, -2, 31)
    for val, exp in zip(inputs, expecteds):
        assert sb.triple_add_one(val) == exp
