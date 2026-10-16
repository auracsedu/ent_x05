import pytest

from problem_08 import Battle, Hero, Monster


def test_처음_상태():
    h = Hero("용사", 30, 10)
    m = Monster("슬라임", 25, 4)
    bt = Battle(h, m)
    assert bt.hero is h and bt.monster is m, "hero, monster 속성에 받은 객체를 그대로 넣으세요"
    assert bt.turns == 0
    assert bt.is_over() is False


def test_한_턴():
    h = Hero("용사", 30, 10)
    m = Monster("슬라임", 25, 4)
    bt = Battle(h, m)
    bt.turn()
    assert (m.hp, h.hp, bt.turns) == (15, 26, 1), f"(괴물 hp, 영웅 hp, turns) = {(m.hp, h.hp, bt.turns)}, 기대값 (15, 26, 1)"


def test_괴물이_쓰러지면_반격이_없다():
    h = Hero("용사", 30, 10)
    m = Monster("슬라임", 25, 4)
    bt = Battle(h, m)
    bt.turn()
    bt.turn()
    assert (m.hp, h.hp, bt.turns) == (5, 22, 2)
    bt.turn()
    assert m.hp == 0
    assert h.hp == 22, f"괴물이 쓰러진 턴에는 반격이 없어야 합니다. 영웅 hp가 {h.hp}입니다"
    assert bt.turns == 3
    assert bt.is_over() is True


def test_strike를_써서_영웅이_레벨업한다():
    h = Hero("용사", 30, 10)
    m = Monster("슬라임", 25, 4)
    bt = Battle(h, m)
    for _ in range(3):
        bt.turn()
    assert (h.level, h.attack) == (2, 12), "hero.strike(monster)를 써야 쓰러뜨렸을 때 레벨이 오릅니다"


def test_끝난_전투에서_turn은_아무_일도_하지_않는다():
    h = Hero("용사", 30, 10)
    m = Monster("슬라임", 25, 4)
    bt = Battle(h, m)
    for _ in range(3):
        bt.turn()
    bt.turn()
    bt.turn()
    assert bt.turns == 3, f"끝난 전투에서 turn()을 불렀는데 turns가 {bt.turns}입니다"
    assert (h.hp, h.level) == (22, 2)


def test_run_영웅_승리():
    h = Hero("용사", 30, 10)
    m = Monster("슬라임", 25, 4)
    bt = Battle(h, m)
    assert bt.run() == "용사"
    assert bt.turns == 3


def test_run_괴물_승리():
    h = Hero("용사", 10, 3)
    m = Monster("드래곤", 100, 7)
    bt = Battle(h, m)
    assert bt.run() == "드래곤"
    assert bt.turns == 2
    assert h.hp == 0 and m.hp == 94


def test_run을_다시_불러도_같은_승자():
    h = Hero("용사", 30, 10)
    m = Monster("슬라임", 25, 4)
    bt = Battle(h, m)
    bt.run()
    assert bt.run() == "용사"
    assert bt.turns == 3


def test_처음부터_쓰러진_영웅():
    h = Hero("용사", 0, 10)
    m = Monster("슬라임", 25, 4)
    bt = Battle(h, m)
    assert bt.is_over() is True
    bt.turn()
    assert bt.turns == 0 and m.hp == 25
    assert bt.run() == "슬라임"


@pytest.mark.parametrize(
    "hero_hp, hero_atk, mon_hp, mon_atk, winner, turns, hero_hp_after",
    [
        (30, 10, 25, 4, "용사", 3, 22),
        (10, 3, 100, 7, "괴물", 2, 0),
        (50, 7, 20, 10, "용사", 3, 30),
        (1, 100, 100, 100, "용사", 1, 1),
        (12, 4, 12, 4, "용사", 3, 4),
        (5, 1, 3, 5, "괴물", 1, 0),
    ],
)
def test_여러_전투(hero_hp, hero_atk, mon_hp, mon_atk, winner, turns, hero_hp_after):
    h = Hero("용사", hero_hp, hero_atk)
    m = Monster("괴물", mon_hp, mon_atk)
    bt = Battle(h, m)
    assert bt.run() == winner
    assert bt.turns == turns, f"turns가 {bt.turns}, 기대값 {turns}"
    assert h.hp == hero_hp_after
