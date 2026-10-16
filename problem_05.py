"""
문제 5. 문자열에서 영웅 만들기 (@classmethod)

파일에서 읽어 온 "이름,체력,공격력" 꼴의 문자열로 영웅을 만들려고 합니다.
아래 Hero에 클래스 메서드 두 개를 추가하세요. __init__은 완성되어 있습니다.

(1) from_string(s)
    "용사,100,12" 같은 문자열을 받아 Hero 인스턴스를 만들어 돌려줍니다.
    - 쉼표(,)로 나눕니다. 조각 앞뒤의 공백은 무시합니다.
    - 체력과 공격력은 정수로 바꿉니다.

(2) from_lines(lines)
    위 꼴의 문자열이 여러 개 담긴 리스트를 받아 Hero 인스턴스의 리스트를
    돌려줍니다. 순서는 그대로입니다. 빈 리스트면 빈 리스트입니다.
    (1)의 from_string을 다시 쓰세요.

예시
    h = Hero.from_string("용사,100,12")
    h.name, h.hp, h.attack     -> "용사", 100, 12
    h.level                    -> 1            # __init__ 을 거쳐 만들어집니다

    Hero.from_string(" 궁수 , 80 , 15 ").name   -> "궁수"

    team = Hero.from_lines(["용사,100,12", "궁수,80,15"])
    len(team)                  -> 2
    team[1].attack             -> 15
    Hero.from_lines([])        -> []

클래스로 생각하는 법
    from_string은 "어떤 영웅"의 동작이 아닙니다. 영웅이 아직 없는데 영웅을 만드는
    일이니까요. 이렇게 인스턴스가 아니라 클래스에 묶인 메서드를 클래스 메서드라
    하고, def 바로 윗줄에 @classmethod 를 붙입니다. 첫 매개변수는 self 대신
    cls(클래스 자신)이고, 몸통에서 cls(name, hp, attack) 이라고 부르면
    Hero(name, hp, attack) 과 같이 새 인스턴스가 만들어집니다.

    교재에서는 이것을 "대안 생성자"라고 부릅니다. 생성자(__init__)는 하나지만,
    "문자열로부터", "여러 줄로부터"처럼 만드는 방법은 여러 개 둘 수 있습니다.

힌트
    - s.split(",") 으로 세 조각을 만들고, 각 조각에 .strip() 을 합니다.
    - int("100") -> 100. int(" 100 ") 도 100이지만, 이름에는 strip이 꼭 필요합니다.
    - from_lines 안에서 from_string을 부를 때는 cls.from_string(line) 입니다.
    - 골격의 def 윗줄에 데코레이터가 비어 있습니다. 알맞은 것을 붙이세요.
"""

from typing import List


class Hero:
    def __init__(self, name: str, hp: int, attack: int) -> None:
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.level = 1

    def from_string(cls, s: str) -> "Hero":
        raise NotImplementedError

    def from_lines(cls, lines: List[str]) -> List["Hero"]:
        raise NotImplementedError
