"""
문제 7. 파티 (객체를 담는 객체)

영웅 여러 명을 묶은 파티를 나타내는 클래스 Party를 작성하세요.
Hero는 완성되어 있습니다(문제 3의 답). 고치지 말고 그대로 쓰세요.

    Party()             빈 파티를 만듭니다. 영웅들은 리스트 members 에 들어갑니다.
    add(hero)           영웅을 파티 맨 뒤에 넣습니다. 돌려주는 값은 없습니다.
    size()              파티에 든 영웅 수 (쓰러진 영웅 포함)
    alive_members()     살아 있는 영웅만 담은 새 리스트. 순서는 넣은 순서.
    total_attack()      살아 있는 영웅들의 attack 합계. 아무도 없으면 0.
    strongest()         살아 있는 영웅 중 attack이 가장 큰 영웅. 같으면 먼저 넣은
                        영웅. 살아 있는 영웅이 없으면 None.

예시
    p = Party()
    p.size()                 -> 0
    a = Hero("용사", 100, 12)
    b = Hero("궁수", 80, 15)
    c = Hero("도적", 60, 15)
    p.add(a)
    p.add(b)
    p.add(c)
    p.size()                 -> 3
    p.total_attack()         -> 42
    p.strongest() is b       -> True       # 15로 같지만 b를 먼저 넣음
    b.take_damage(999)                     # 궁수가 쓰러지면
    p.alive_members()        -> [a, c]     # 같은 객체들이 그대로 들어 있습니다
    p.total_attack()         -> 27
    p.strongest() is c       -> True
    p.size()                 -> 3          # 쓰러져도 파티원 수는 그대로

    q = Party()
    q.size()                 -> 0          # 다른 파티는 비어 있어야 합니다

클래스로 생각하는 법
    지금까지 속성에는 숫자와 문자열만 넣었습니다. 속성에는 다른 객체도, 객체가 든
    리스트도 들어갑니다. Party는 Hero들을 담는 상자이고, 상자의 메서드는 안에 든
    영웅들을 하나씩 꺼내 그 영웅의 메서드(is_alive)와 속성(attack)을 씁니다.

    members = [] 를 어디에 쓰는지가 이 문제의 핵심입니다. 클래스 몸통에 쓰면
    클래스 변수가 되어 모든 파티가 리스트 하나를 함께 씁니다(서술형 S3).
    파티마다 따로 가지려면 __init__ 안에서 self.members = [] 라고 써야 합니다.

힌트
    - alive_members는 for 문으로 self.members 를 돌며 h.is_alive() 인 것만 모읍니다.
      다른 메서드들은 alive_members() 를 다시 쓰면 짧아집니다.
    - strongest: 살아 있는 영웅이 없으면 먼저 None을 돌려주고, 아니면 첫 영웅을
      best로 잡고 돌면서 attack이 "더 큰" 경우에만 바꿉니다. (크거나 같은 경우에
      바꾸면 나중 영웅이 뽑혀서 틀립니다.) attack을 돌려주는 함수를 만들어
      max(목록, key=그_함수) 로 써도 됩니다. max도 같은 값이면 앞의 것을 고릅니다.
    - 돌려주는 것은 영웅 객체 자체입니다. 이름이나 attack 값이 아닙니다.
"""

from typing import List, Optional


# ---- 아래 Hero는 완성된 코드입니다. 고치지 마세요. ----
class Hero:
    def __init__(self, name: str, hp: int, attack: int) -> None:
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.level = 1

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

    def heal(self, amount: int) -> None:
        if not self.is_alive():
            return
        self.hp = min(self.max_hp, self.hp + amount)

    def strike(self, target: "Hero") -> bool:
        if not target.is_alive():
            return False
        target.take_damage(self.attack)
        if target.is_alive():
            return False
        self.level += 1
        self.attack += 2
        return True


# ---- 여기서부터 작성하세요. ----
class Party:
    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, hero: Hero) -> None:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError

    def alive_members(self) -> List[Hero]:
        raise NotImplementedError

    def total_attack(self) -> int:
        raise NotImplementedError

    def strongest(self) -> Optional[Hero]:
        raise NotImplementedError
