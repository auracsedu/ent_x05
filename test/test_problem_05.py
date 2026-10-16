import pytest

from problem_05 import Hero


def test_from_string은_클래스_메서드다():
    assert isinstance(vars(Hero).get("from_string"), classmethod), (
        "from_string이 클래스 메서드가 아닙니다. def 윗줄에 @classmethod 를 붙이세요"
    )


def test_from_lines도_클래스_메서드다():
    assert isinstance(vars(Hero).get("from_lines"), classmethod), (
        "from_lines가 클래스 메서드가 아닙니다. def 윗줄에 @classmethod 를 붙이세요"
    )


@pytest.mark.parametrize(
    "s, name, hp, attack",
    [("용사,100,12", "용사", 100, 12), (" 궁수 , 80 , 15 ", "궁수", 80, 15), ("도적,1,1", "도적", 1, 1)],
)
def test_문자열에서_영웅을_만든다(s, name, hp, attack):
    h = Hero.from_string(s)
    assert isinstance(h, Hero), f"Hero 인스턴스가 아니라 {h!r}를 돌려줬습니다. return cls(...) 를 쓰세요"
    assert h.name == name, f"name이 {h.name!r}입니다. 앞뒤 공백은 strip으로 지우세요"
    assert h.hp == hp and h.attack == attack, f"(hp, attack)이 {(h.hp, h.attack)}입니다"
    assert isinstance(h.hp, int) and isinstance(h.attack, int), "hp와 attack은 int()로 바꿔야 합니다"


def test_init을_거쳐_만들어진다():
    h = Hero.from_string("용사,100,12")
    assert h.level == 1 and h.max_hp == 100, "from_string이 만든 영웅도 level 1, max_hp = hp 여야 합니다"


def test_여러_줄에서_영웅_여러_명():
    team = Hero.from_lines(["용사,100,12", "궁수,80,15", "도적,60,9"])
    assert isinstance(team, list) and len(team) == 3, f"길이 3인 리스트여야 합니다: {team!r}"
    assert all(isinstance(h, Hero) for h in team), "리스트의 원소는 Hero 인스턴스여야 합니다"
    assert [h.name for h in team] == ["용사", "궁수", "도적"], "순서가 바뀌었습니다"
    assert team[1].attack == 15


def test_빈_리스트면_빈_리스트():
    assert Hero.from_lines([]) == []
