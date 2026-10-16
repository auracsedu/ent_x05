import pytest

from problem_extra_02 import Fraction


@pytest.mark.parametrize(
    "num, den, e_num, e_den",
    [(2, 4, 1, 2), (3, -6, -1, 2), (0, 5, 0, 1), (-2, -4, 1, 2), (7, 1, 7, 1), (6, 3, 2, 1), (-3, 9, -1, 3), (5, 7, 5, 7)],
)
def test_만들어질_때_기약분수로_고친다(num, den, e_num, e_den):
    f = Fraction(num, den)
    assert (f.num, f.den) == (e_num, e_den), f"Fraction({num}, {den})이 {f.num}/{f.den}입니다. 기대값 {e_num}/{e_den}"


def test_분모가_0이면_ValueError():
    with pytest.raises(ValueError):
        Fraction(1, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    [((1, 2), (1, 3), (5, 6)), ((1, 2), (1, 2), (1, 1)), ((1, 3), (-1, 3), (0, 1)), ((-1, 4), (1, 2), (1, 4)), ((2, 3), (5, 6), (3, 2))],
)
def test_add(a, b, expected):
    c = Fraction(*a).add(Fraction(*b))
    assert isinstance(c, Fraction)
    assert (c.num, c.den) == expected, f"{a[0]}/{a[1]} + {b[0]}/{b[1]} = {c.num}/{c.den}, 기대값 {expected[0]}/{expected[1]}"


@pytest.mark.parametrize(
    "a, b, expected",
    [((1, 2), (1, 3), (1, 6)), ((2, 3), (3, 2), (1, 1)), ((0, 1), (5, 7), (0, 1)), ((-1, 2), (1, 2), (-1, 4)), ((3, 4), (-4, 3), (-1, 1))],
)
def test_mul(a, b, expected):
    c = Fraction(*a).mul(Fraction(*b))
    assert isinstance(c, Fraction)
    assert (c.num, c.den) == expected, f"{a[0]}/{a[1]} * {b[0]}/{b[1]} = {c.num}/{c.den}, 기대값 {expected[0]}/{expected[1]}"


def test_add와_mul은_새_객체를_돌려주고_원본은_그대로():
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    c = a.add(b)
    d = a.mul(b)
    assert c is not a and c is not b and d is not a, "self나 other를 돌려주지 말고 새 Fraction을 만드세요"
    assert (a.num, a.den) == (1, 2), "add/mul 뒤에 a가 바뀌었습니다. self를 건드리면 안 됩니다"
    assert (b.num, b.den) == (1, 3)


@pytest.mark.parametrize(
    "a, b, expected",
    [((1, 2), (2, 4), True), ((1, 2), (1, 3), False), ((0, 3), (0, 7), True), ((-1, 2), (1, -2), True), ((2, 1), (4, 2), True)],
)
def test_equals(a, b, expected):
    assert Fraction(*a).equals(Fraction(*b)) is expected


@pytest.mark.parametrize("num, den, s", [(5, 6, "5/6"), (2, 2, "1"), (-1, 2, "-1/2"), (0, 5, "0"), (4, 2, "2"), (-6, 3, "-2")])
def test_to_string(num, den, s):
    assert Fraction(num, den).to_string() == s
