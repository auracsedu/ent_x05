import pytest

from problem_extra_01 import Inventory


def test_빈_가방():
    bag = Inventory(10)
    assert bag.total() == 0
    assert bag.names() == []
    assert bag.count("포션") == 0, "없는 물건의 count는 0이어야 합니다. dict.get(item, 0)"
    assert isinstance(bag.items, dict), "items는 딕셔너리여야 합니다"


def test_add_기본값은_1개():
    bag = Inventory(10)
    bag.add("포션")
    assert bag.count("포션") == 1, "n을 생략하면 1개입니다. def add(self, item, n=1)"


def test_여러_번_add하면_누적():
    bag = Inventory(10)
    bag.add("포션", 3)
    bag.add("포션")
    bag.add("열쇠")
    assert bag.count("포션") == 4
    assert bag.total() == 5
    assert bag.items == {"포션": 4, "열쇠": 1}


def test_names는_정렬된_이름():
    bag = Inventory(10)
    bag.add("포션", 3)
    bag.add("열쇠")
    bag.add("활")
    assert bag.names() == ["열쇠", "포션", "활"]


def test_remove하면_줄고_0개가_되면_이름이_사라진다():
    bag = Inventory(10)
    bag.add("포션", 4)
    bag.add("열쇠")
    bag.remove("포션", 3)
    assert bag.count("포션") == 1
    bag.remove("포션")
    assert bag.count("포션") == 0
    assert bag.names() == ["열쇠"], "0개가 된 물건은 items에서 지워야 합니다. del self.items[item]"
    assert "포션" not in bag.items


def test_가진_것보다_많이_빼면_ValueError_그리고_변화_없음():
    bag = Inventory(10)
    bag.add("열쇠")
    with pytest.raises(ValueError):
        bag.remove("열쇠", 2)
    assert bag.count("열쇠") == 1, "실패한 remove는 가방을 바꾸면 안 됩니다. 검사를 먼저 하세요"
    with pytest.raises(ValueError):
        bag.remove("방패")


def test_용량을_넘기면_ValueError_그리고_변화_없음():
    bag = Inventory(10)
    bag.add("열쇠")
    with pytest.raises(ValueError):
        bag.add("화살", 10)
    assert bag.total() == 1 and bag.count("화살") == 0, "실패한 add는 가방을 바꾸면 안 됩니다. 검사를 먼저 하세요"


def test_딱_용량만큼은_넣을_수_있다():
    bag = Inventory(10)
    bag.add("열쇠")
    bag.add("화살", 9)
    assert bag.total() == 10


def test_가방마다_items가_따로_있다():
    a = Inventory(10)
    b = Inventory(10)
    a.add("포션")
    assert b.total() == 0, "다른 가방이 비어 있지 않습니다. self.items = {} 를 __init__ 안에 쓰세요"
