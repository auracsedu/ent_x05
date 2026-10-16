"""
문제 3. 공격 (다른 객체를 받는 메서드)

문제 2의 Hero에 메서드 strike를 추가하세요. 나머지는 문제 2와 같습니다.

strike(target)
    다른 영웅 target을 공격합니다.
    - target의 체력을 자신의 attack만큼 깎습니다. (target.take_damage를 쓰세요)
    - 이 공격으로 target이 쓰러졌으면 자신의 level이 1 오르고 attack이 2 오릅니다.
      그리고 True를 돌려줍니다. 쓰러지지 않았으면 False를 돌려줍니다.
    - 이미 쓰러진 target은 공격할 수 없습니다. 아무 일도 하지 않고 False를
      돌려줍니다. (레벨도 오르지 않습니다)
    - 공격한 쪽의 체력은 변하지 않습니다.

예시
    a = Hero("용사", 100, 12)
    b = Hero("도적", 20, 5)

    a.strike(b)         -> False     # b.hp 20 -> 8
    b.hp                -> 8
    a.hp                -> 100       # 공격한 쪽은 그대로
    a.strike(b)         -> True      # b.hp 8 -> 0, 쓰러짐
    a.level, a.attack   -> 2, 14
    a.strike(b)         -> False     # 이미 쓰러진 상대. 아무 일도 없음
    a.level             -> 2

클래스로 생각하는 법
    이 메서드 안에는 객체가 둘 있습니다. self(공격하는 쪽)와 target(맞는 쪽).
    누구의 attack을 쓰고 누구의 hp가 줄어드는지 한 줄 한 줄 확인하세요.

    "체력을 깎는" 동작은 이미 take_damage로 만들어 두었으니, 직접 target.hp를
    고치지 말고 target.take_damage(...) 를 부릅니다. 메서드는 그 객체가 가진
    도구라서, 다른 객체의 메서드도 점(.)으로 부를 수 있습니다.

힌트
    - 순서가 중요합니다. 공격하기 "전"에 target.is_alive() 를 확인하고,
      공격한 "뒤"에 다시 확인해야 "이번 공격으로 쓰러졌는지"를 알 수 있습니다.
    - 공격한 뒤의 not target.is_alive() 를 그대로 돌려줘도 됩니다.
      어느 쪽이든 bool이어야 합니다. (테스트가 is True / is False 로 확인합니다.)
"""


class Hero:
    def __init__(self, name: str, hp: int, attack: int) -> None:
        raise NotImplementedError

    def is_alive(self) -> bool:
        raise NotImplementedError

    def take_damage(self, amount: int) -> None:
        raise NotImplementedError

    def heal(self, amount: int) -> None:
        raise NotImplementedError

    def strike(self, target: "Hero") -> bool:
        raise NotImplementedError
