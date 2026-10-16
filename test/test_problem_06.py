import pytest

from problem_06 import Hero


def test_is_valid_name은_정적_메서드다():
    assert isinstance(vars(Hero).get("is_valid_name"), staticmethod), (
        "is_valid_name이 정적 메서드가 아닙니다. def 윗줄에 @staticmethod 를 붙이세요"
    )


@pytest.mark.parametrize(
    "name, expected",
    [
        ("용사", True),
        ("ab", True),
        ("abcdefgh", True),
        ("a", False),
        ("abcdefghi", False),
        ("용 사", False),
        ("", False),
        (" ", False),
        ("a b", False),
        ("  ", False),
    ],
)
def test_이름_규칙(name, expected):
    result = Hero.is_valid_name(name)
    assert result is expected, f"Hero.is_valid_name({name!r}) = {result!r}, 기대값 {expected}"


def test_인스턴스를_통해_불러도_된다():
    h = Hero("용사", 100, 12)
    assert h.is_valid_name("용 사") is False
    assert h.is_valid_name("궁수") is True


def test_올바른_이름이면_문제1처럼_만들어진다():
    h = Hero("용사", 100, 12)
    assert (h.name, h.hp, h.max_hp, h.attack, h.level) == ("용사", 100, 100, 12, 1)


@pytest.mark.parametrize("bad", ["a", "용 사", "", "abcdefghi"])
def test_잘못된_이름이면_ValueError(bad):
    with pytest.raises(ValueError):
        Hero(bad, 100, 12)
