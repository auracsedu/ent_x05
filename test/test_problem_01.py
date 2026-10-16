from problem_01 import Hero


def test_속성_다섯_개가_받은_값대로_설정된다():
    """Hero(name, hp, attack)은 name, hp, max_hp, attack, level 다섯 속성을 가진다."""
    h = Hero("용사", 100, 12)
    assert h.name == "용사", f"name이 {h.name!r}입니다"
    assert h.hp == 100, f"hp가 {h.hp!r}입니다"
    assert h.max_hp == 100, f"max_hp는 처음 hp와 같아야 합니다: {h.max_hp!r}"
    assert h.attack == 12, f"attack이 {h.attack!r}입니다"
    assert h.level == 1, f"level은 항상 1에서 시작합니다: {h.level!r}"


def test_hp를_바꿔도_max_hp는_그대로():
    h = Hero("용사", 100, 12)
    h.hp = 70
    assert h.max_hp == 100, "hp와 max_hp는 서로 다른 속성이어야 합니다. 둘 다 따로 저장하세요"


def test_인스턴스마다_값이_따로_있다():
    a = Hero("전사", 120, 10)
    b = Hero("궁수", 80, 15)
    assert (a.name, a.hp, a.attack) == ("전사", 120, 10)
    assert (b.name, b.hp, b.attack) == ("궁수", 80, 15)
    a.hp = 0
    assert b.hp == 80, "a의 hp를 바꿨는데 b의 hp가 바뀌었습니다. self.hp 에 넣고 있는지 확인하세요"


def test_속성은_인스턴스에_붙어_있다():
    """다섯 속성 모두 self.속성 = ... 으로 인스턴스에 붙어 있어야 한다."""
    h = Hero("용사", 100, 12)
    for attr in ("name", "hp", "max_hp", "attack", "level"):
        assert attr in vars(h), (
            f"{attr}가 인스턴스 변수가 아닙니다. __init__ 안에서 self.{attr} = ... 로 쓰세요"
        )
