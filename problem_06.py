"""
문제 6. 이름 검사 (@staticmethod)

영웅 이름에 규칙을 두려고 합니다. 아래 Hero에 정적 메서드 is_valid_name을
추가하고, __init__이 그것을 써서 잘못된 이름을 거부하게 작성하세요.

(1) is_valid_name(name)
    이름이 규칙에 맞으면 True, 아니면 False를 돌려줍니다. 규칙은 두 가지입니다.
    - 길이가 2 이상 8 이하
    - 띄어쓰기(" ")가 들어 있지 않음

(2) __init__(name, hp, attack)
    name이 규칙에 맞지 않으면 ValueError를 일으킵니다.
    맞으면 문제 1과 똑같이 다섯 속성을 설정합니다.

예시
    Hero.is_valid_name("용사")          -> True
    Hero.is_valid_name("a")             -> False    # 너무 짧음
    Hero.is_valid_name("abcdefghi")     -> False    # 9글자, 너무 긺
    Hero.is_valid_name("용 사")         -> False    # 띄어쓰기
    Hero.is_valid_name("")              -> False

    Hero("용사", 100, 12).name          -> "용사"
    Hero("용 사", 100, 12)              -> ValueError

클래스로 생각하는 법
    is_valid_name은 self도 cls도 필요 없습니다. 이름 문자열만 보고 답하니까요.
    그냥 함수로 만들어도 되지만, "영웅 이름의 규칙"은 Hero와 함께 있는 것이
    자연스럽습니다. 이렇게 어떤 상태도 건드리지 않지만 논리적으로 클래스에
    속한 함수에는 def 윗줄에 @staticmethod 를 붙입니다. 첫 매개변수에 self나
    cls를 쓰지 않습니다.

    세 종류 메서드 정리 (교재 1.8)
        인스턴스 메서드   첫 인자 self    그 인스턴스의 상태를 읽고 바꿈     h.heal(10)
        클래스 메서드     첫 인자 cls     클래스 자체를 다룸 (대안 생성자)   Hero.from_string(s)
        정적 메서드       첫 인자 없음    어느 상태도 안 건드림              Hero.is_valid_name(s)

힌트
    - 2 <= len(name) <= 8 처럼 비교를 이어 쓸 수 있습니다.
    - " " in name 은 띄어쓰기가 들어 있으면 True입니다.
    - __init__ 안에서는 Hero.is_valid_name(name) 또는 self.is_valid_name(name)
      둘 다 됩니다. 정적 메서드는 어느 쪽으로 불러도 self가 끼어들지 않습니다.
    - 에러를 일으키는 문장: raise ValueError("이름이 규칙에 맞지 않습니다")
      raise 가 실행되면 그 아래 줄은 실행되지 않습니다.
"""


class Hero:
    def __init__(self, name: str, hp: int, attack: int) -> None:
        raise NotImplementedError

    def is_valid_name(name: str) -> bool:
        raise NotImplementedError
