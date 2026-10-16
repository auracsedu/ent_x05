from problem_03 import Hero


def test_공격하면_상대_체력이_공격력만큼_준다():
    a = Hero("용사", 100, 12)
    b = Hero("도적", 20, 5)
    result = a.strike(b)
    assert b.hp == 8, f"attack 12로 hp 20인 상대를 공격했는데 상대 hp가 {b.hp}입니다"
    assert result is False, f"상대가 쓰러지지 않았으므로 False여야 합니다: {result!r}"


def test_공격한_쪽의_체력과_레벨은_그대로():
    a = Hero("용사", 100, 12)
    b = Hero("도적", 20, 5)
    a.strike(b)
    assert a.hp == 100, f"공격한 쪽의 hp가 {a.hp}로 바뀌었습니다. self와 target을 바꿔 쓰지 않았는지 확인하세요"
    assert (a.level, a.attack) == (1, 12), "쓰러뜨리지 못했는데 레벨이나 공격력이 바뀌었습니다"


def test_쓰러뜨리면_True_그리고_레벨과_공격력이_오른다():
    a = Hero("용사", 100, 12)
    b = Hero("도적", 20, 5)
    a.strike(b)
    result = a.strike(b)
    assert b.hp == 0
    assert result is True, f"이번 공격으로 상대가 쓰러졌으므로 True여야 합니다: {result!r}"
    assert a.level == 2, f"쓰러뜨리면 level이 1 올라 2여야 합니다: {a.level}"
    assert a.attack == 14, f"쓰러뜨리면 attack이 2 올라 14여야 합니다: {a.attack}"


def test_정확히_0이_되어도_쓰러진_것이다():
    a = Hero("용사", 100, 20)
    b = Hero("도적", 20, 5)
    assert a.strike(b) is True
    assert b.is_alive() is False


def test_이미_쓰러진_상대는_공격할_수_없다():
    a = Hero("용사", 100, 50)
    b = Hero("도적", 20, 5)
    a.strike(b)  # 쓰러뜨림. level 2, attack 52
    result = a.strike(b)
    assert result is False, "이미 쓰러진 상대를 공격하면 False여야 합니다"
    assert (a.level, a.attack) == (2, 52), "이미 쓰러진 상대를 공격했는데 레벨이나 공격력이 또 올랐습니다"
    assert b.hp == 0


def test_오른_공격력으로_다음_공격을_한다():
    a = Hero("용사", 100, 12)
    b = Hero("도적", 10, 5)
    c = Hero("궁수", 30, 7)
    a.strike(b)  # 쓰러뜨림. attack 14
    a.strike(c)
    assert c.hp == 16, f"attack이 14로 올랐으므로 30 - 14 = 16이어야 합니다: {c.hp}"


def test_두_영웅이_서로_공격한다():
    a = Hero("용사", 30, 10)
    b = Hero("도적", 25, 8)
    a.strike(b)
    b.strike(a)
    assert (a.hp, b.hp) == (22, 15)


def test_문제2의_메서드도_그대로_동작한다():
    h = Hero("용사", 100, 12)
    h.take_damage(999)
    assert h.hp == 0 and h.is_alive() is False
    h.heal(10)
    assert h.hp == 0
