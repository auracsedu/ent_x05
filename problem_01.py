"""
문제 1. 영웅 만들기 (클래스 첫 문제)

이번 주 소재는 텍스트 RPG입니다. 영웅, 괴물, 파티, 전투를 클래스로 만듭니다.

이름 name, 체력 hp, 공격력 attack을 받아 영웅 한 명을 나타내는 클래스 Hero를
작성하세요. 만들어진 영웅은 다음 다섯 속성을 가집니다.

    name      이름 (받은 값 그대로)
    hp        현재 체력 (처음에는 받은 hp)
    max_hp    최대 체력 (처음에는 받은 hp와 같음. 이후 hp가 줄어도 변하지 않음)
    attack    공격력
    level     레벨 (항상 1에서 시작. 매개변수로 받지 않습니다)

예시
    h = Hero("용사", 100, 12)
    h.name       -> "용사"
    h.hp         -> 100
    h.max_hp     -> 100
    h.attack     -> 12
    h.level      -> 1

    h.hp = 70              # 체력이 줄어도
    h.max_hp     -> 100    # 최대 체력은 그대로

    a = Hero("전사", 120, 10)
    b = Hero("궁수", 80, 15)
    a.hp, b.hp   -> 120, 80          # 인스턴스마다 값이 따로 있습니다

클래스로 생각하는 법
    클래스는 "영웅이란 이런 것이다"라는 설계도이고, Hero("용사", 100, 12)처럼
    괄호를 붙여 부르면 설계도대로 인스턴스(실제 영웅 한 명)가 만들어집니다.

    인스턴스가 만들어질 때 __init__ 메서드가 자동으로 불립니다. 첫 번째 매개변수
    self는 "지금 막 만들어진 그 영웅"이고, self.name = name 은 그 영웅에게
    name이라는 속성을 붙이는 문장입니다. 속성은 self. 를 붙여야 인스턴스에
    남습니다. self. 없이 name = name 이라고 쓰면 함수가 끝나는 순간 사라집니다.

힌트
    - __init__(self, name, hp, attack) 안에 self.속성 = 값 을 다섯 줄 씁니다.
    - max_hp와 level은 매개변수가 아니지만 __init__ 안에서 정할 수 있습니다.
    - Hero(...)를 부를 때 self는 쓰지 않습니다. 파이썬이 알아서 넣어 줍니다.
"""


class Hero:
    def __init__(self, name: str, hp: int, attack: int) -> None:
        raise NotImplementedError
