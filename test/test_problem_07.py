from problem_07 import Hero, Party


def make_party():
    a = Hero("용사", 100, 12)
    b = Hero("궁수", 80, 15)
    c = Hero("도적", 60, 15)
    p = Party()
    p.add(a)
    p.add(b)
    p.add(c)
    return p, a, b, c


def test_빈_파티():
    p = Party()
    assert p.size() == 0
    assert p.alive_members() == []
    assert p.total_attack() == 0
    assert p.strongest() is None, "살아 있는 영웅이 없으면 None이어야 합니다"


def test_add하면_size가_는다():
    p = Party()
    p.add(Hero("용사", 100, 12))
    assert p.size() == 1
    p.add(Hero("궁수", 80, 15))
    assert p.size() == 2


def test_members에_넣은_순서대로_들어_있다():
    p, a, b, c = make_party()
    assert p.members == [a, b, c], "members 리스트에 영웅 객체가 넣은 순서대로 있어야 합니다"


def test_파티마다_members가_따로_있다():
    p = Party()
    p.add(Hero("용사", 100, 12))
    q = Party()
    assert q.size() == 0, (
        "새 파티가 비어 있지 않습니다. members = [] 를 클래스 몸통에 쓰면 모든 파티가 리스트 하나를 "
        "같이 씁니다. __init__ 안에서 self.members = [] 로 쓰세요 (서술형 S3)"
    )


def test_alive_members는_살아_있는_영웅만_순서대로():
    p, a, b, c = make_party()
    b.take_damage(999)
    alive = p.alive_members()
    assert len(alive) == 2 and alive[0] is a and alive[1] is c, "쓰러진 궁수를 빼고 [용사, 도적] 순서여야 합니다"


def test_alive_members는_새_리스트다():
    p, a, b, c = make_party()
    assert p.alive_members() is not p.members, "members 자체가 아니라 새 리스트를 돌려주세요"


def test_total_attack은_살아_있는_영웅만_더한다():
    p, a, b, c = make_party()
    assert p.total_attack() == 42
    b.take_damage(999)
    assert p.total_attack() == 27, "쓰러진 영웅의 attack은 더하지 않습니다"


def test_strongest_동점이면_먼저_넣은_영웅():
    p, a, b, c = make_party()
    s = p.strongest()
    assert isinstance(s, Hero), f"영웅 객체를 돌려줘야 합니다: {s!r}"
    assert s is b, f"attack 15로 같을 때는 먼저 넣은 궁수여야 합니다. {s.name}이(가) 나왔습니다"


def test_strongest는_쓰러진_영웅을_뺀다():
    p, a, b, c = make_party()
    b.take_damage(999)
    assert p.strongest() is c


def test_모두_쓰러지면_strongest는_None():
    p, a, b, c = make_party()
    for h in (a, b, c):
        h.take_damage(999)
    assert p.strongest() is None
    assert p.size() == 3, "쓰러져도 파티원 수는 그대로입니다"
