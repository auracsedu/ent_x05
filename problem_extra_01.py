"""
[숙제] 문제 extra 1. 가방 (딕셔너리를 품은 객체)

영웅의 가방을 나타내는 클래스 Inventory를 작성하세요. 가방에는 물건을 종류별로
여러 개 넣을 수 있고, 전체 개수에 상한(capacity)이 있습니다.

    Inventory(capacity)   빈 가방. 물건은 딕셔너리 items 에 {이름: 개수} 로 둡니다.
    add(item, n=1)        item을 n개 넣습니다. 넣은 뒤 전체 개수가 capacity를
                          넘으면 ValueError를 일으키고 가방은 바뀌지 않습니다.
    remove(item, n=1)     item을 n개 뺍니다. 가진 개수보다 많이 빼려 하면
                          ValueError를 일으키고 가방은 바뀌지 않습니다.
                          개수가 0이 되면 items 에서 그 이름을 지웁니다.
    count(item)           item의 개수. 없으면 0.
    total()               전체 개수.
    names()               가진 물건 이름을 정렬한 리스트.

예시
    bag = Inventory(10)
    bag.add("포션", 3)
    bag.add("포션")                # n을 생략하면 1개
    bag.add("열쇠")
    bag.count("포션")       -> 4
    bag.count("방패")       -> 0
    bag.total()             -> 5
    bag.names()             -> ["열쇠", "포션"]
    bag.remove("포션", 4)
    bag.names()             -> ["열쇠"]        # 0개가 되면 이름도 사라집니다
    bag.remove("열쇠", 2)   -> ValueError      # 1개뿐
    bag.add("화살", 10)     -> ValueError      # 1 + 10 > 10
    bag.total()             -> 1               # 실패한 연산은 가방을 바꾸지 않습니다

힌트
    - 매개변수 기본값: def add(self, item, n=1): 로 쓰면 n을 생략할 수 있습니다.
    - "없으면 0"은 self.items.get(item, 0) 입니다. (2주차 word_count와 같습니다)
    - 에러는 바꾸기 "전에" 검사해서 일으킵니다. raise 가 실행되면 그 아래 줄은
      실행되지 않으므로, 검사를 맨 위에 두면 "가방은 바뀌지 않습니다"가 저절로
      지켜집니다.
    - 키 지우기: del self.items[item]
    - sum(self.items.values()), sorted(self.items) 가 유용합니다.
"""

from typing import List


class Inventory:
    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def add(self, item: str, n: int = 1) -> None:
        raise NotImplementedError

    def remove(self, item: str, n: int = 1) -> None:
        raise NotImplementedError

    def count(self, item: str) -> int:
        raise NotImplementedError

    def total(self) -> int:
        raise NotImplementedError

    def names(self) -> List[str]:
        raise NotImplementedError
