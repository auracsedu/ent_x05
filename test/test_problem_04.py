import pytest

from problem_04 import Monster


@pytest.fixture(autouse=True)
def count를_0으로_되돌림(monkeypatch):
    assert "count" in vars(Monster), "클래스 변수 count가 없습니다. class Monster: 바로 아래 줄에 count = 0 을 적으세요"
    monkeypatch.setattr(Monster, "count", 0)


def test_처음에는_0마리():
    assert Monster.count == 0


def test_속성_세_개():
    m = Monster("슬라임", 20, 3)
    assert (m.kind, m.hp, m.attack) == ("슬라임", 20, 3)


def test_번호표는_1부터_차례로():
    a = Monster("슬라임", 20, 3)
    b = Monster("고블린", 35, 6)
    c = Monster("슬라임", 20, 3)
    assert (a.id, b.id, c.id) == (1, 2, 3), f"id가 {(a.id, b.id, c.id)}입니다. 1, 2, 3이어야 합니다"


def test_count는_지금까지_만든_수():
    Monster("슬라임", 20, 3)
    Monster("고블린", 35, 6)
    Monster("슬라임", 20, 3)
    assert Monster.count == 3, (
        f"괴물 3마리를 만들었는데 Monster.count가 {Monster.count}입니다. "
        "self.count += 1 은 클래스 변수를 바꾸지 않습니다. Monster.count += 1 로 쓰세요"
    )


def test_count는_클래스_변수여야_한다():
    a = Monster("슬라임", 20, 3)
    assert "count" not in vars(a), (
        "count가 인스턴스 변수로 만들어졌습니다. self.count = ... 또는 self.count += 1 을 쓰면 "
        "그 인스턴스에만 count가 새로 생깁니다. Monster.count 로 접근하세요"
    )


def test_인스턴스를_통해_읽어도_같은_값이_보인다():
    a = Monster("슬라임", 20, 3)
    b = Monster("고블린", 35, 6)
    assert a.count == b.count == Monster.count == 2


def test_count를_되돌리면_번호표도_다시_1부터():
    Monster("슬라임", 20, 3)
    Monster("슬라임", 20, 3)
    Monster.count = 0
    m = Monster("고블린", 35, 6)
    assert m.id == 1, f"Monster.count를 0으로 되돌린 뒤 만든 괴물의 id가 {m.id}입니다. id는 Monster.count 에서 와야 합니다"
