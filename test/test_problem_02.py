import pytest

from problem_02 import Hero


def test_문제1의_속성이_그대로():
    h = Hero("용사", 100, 12)
    assert (h.name, h.hp, h.max_hp, h.attack, h.level) == ("용사", 100, 100, 12, 1)


def test_처음에는_살아_있다():
    assert Hero("용사", 100, 12).is_alive() is True, "is_alive()는 True/False(bool)를 돌려줘야 합니다"


def test_피해를_입으면_체력이_준다():
    h = Hero("용사", 100, 12)
    h.take_damage(30)
    assert h.hp == 70, f"100에서 30을 깎았는데 hp가 {h.hp}입니다"


@pytest.mark.parametrize("damages, expected", [([10, 20, 30], 40), ([60, 60], 0), ([], 100), ([100], 0), ([99, 1], 0)])
def test_여러_번_피해를_입는다(damages, expected):
    h = Hero("용사", 100, 12)
    for d in damages:
        h.take_damage(d)
    assert h.hp == expected, f"take_damage{damages} 뒤 hp가 {h.hp}, 기대값 {expected}"


def test_체력은_0_아래로_내려가지_않는다():
    h = Hero("용사", 100, 12)
    h.take_damage(999)
    assert h.hp == 0, f"hp가 {h.hp}입니다. 0 아래로 내려가면 안 됩니다. max(0, ...)"


def test_체력이_0이면_쓰러진_것이다():
    h = Hero("용사", 100, 12)
    h.take_damage(100)
    assert h.is_alive() is False, "hp가 0이면 is_alive()는 False여야 합니다"


@pytest.mark.parametrize(
    "damage, heal, expected",
    [(30, 10, 80), (30, 50, 100), (30, 30, 100), (0, 10, 100), (100, 10, 0), (99, 1, 2), (99, 99, 100), (999, 999, 0)],
)
def test_회복은_max_hp를_넘지_않고_쓰러진_영웅은_회복되지_않는다(damage, heal, expected):
    h = Hero("용사", 100, 12)
    h.take_damage(damage)
    h.heal(heal)
    assert h.hp == expected, f"take_damage({damage}) 뒤 heal({heal}): hp가 {h.hp}, 기대값 {expected}"


def test_max_hp는_변하지_않는다():
    h = Hero("용사", 100, 12)
    h.take_damage(40)
    h.heal(10)
    assert h.max_hp == 100, f"피해와 회복을 거쳐도 max_hp는 100이어야 합니다: {h.max_hp}"


def test_다른_영웅에게는_영향이_없다():
    a = Hero("전사", 120, 10)
    b = Hero("궁수", 80, 15)
    a.take_damage(50)
    assert (a.hp, b.hp) == (70, 80), "a가 피해를 입었는데 b의 hp가 바뀌었습니다"
