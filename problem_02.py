"""
문제 2. 피해와 회복 (인스턴스 메서드)

문제 1의 Hero에 메서드 세 개를 추가하세요. __init__은 문제 1과 같습니다.
(문제 1의 코드를 복사해 와서 이어서 쓰면 됩니다.)

(1) is_alive()
    체력이 0보다 크면 True, 아니면 False를 돌려줍니다.

(2) take_damage(amount)
    체력을 amount만큼 깎습니다. 체력은 0 아래로 내려가지 않습니다.
    돌려주는 값은 없습니다.

(3) heal(amount)
    체력을 amount만큼 회복합니다. 체력은 max_hp를 넘지 않습니다.
    이미 쓰러진(체력 0) 영웅은 회복되지 않습니다. 돌려주는 값은 없습니다.

예시
    h = Hero("용사", 100, 12)
    h.take_damage(30)
    h.hp                -> 70
    h.heal(50)
    h.hp                -> 100    # 최대 체력을 넘지 않음
    h.take_damage(999)
    h.hp                -> 0      # 0 아래로 내려가지 않음
    h.is_alive()        -> False
    h.heal(10)
    h.hp                -> 0      # 쓰러진 영웅은 회복되지 않음

클래스로 생각하는 법
    인스턴스 메서드는 "그 영웅이 하는 동작"입니다. def take_damage(self, amount):
    처럼 첫 매개변수로 self를 받고, 몸통에서는 self.hp처럼 그 영웅의 속성을
    읽고 바꿉니다. h.take_damage(30) 이라고 부르면 self 자리에 h가 들어갑니다.
    (h.take_damage(30) 은 Hero.take_damage(h, 30) 과 같은 뜻입니다.)

    보통 함수와 다른 점은 딱 하나, 결과를 돌려주는 대신 "자기 자신의 상태를
    바꾼다"는 것입니다. take_damage와 heal은 return 없이 self.hp만 바꿉니다.

힌트
    - "0 아래로 내려가지 않음"은 max(0, ...) 으로, "max_hp를 넘지 않음"은
      min(self.max_hp, ...) 으로 한 줄에 쓸 수 있습니다.
    - heal은 먼저 self.is_alive() 를 확인합니다. 자기 메서드도 self. 로 부릅니다.
    - 테스트가 is True / is False 로 확인하므로 is_alive는 진짜 bool을 돌려줘야
      합니다. self.hp > 0 은 이미 bool입니다.
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
