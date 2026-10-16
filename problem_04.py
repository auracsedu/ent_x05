"""
문제 4. 괴물 번호표 (클래스 변수)

종류 kind, 체력 hp, 공격력 attack을 받는 클래스 Monster를 작성하세요.
괴물은 만들어질 때마다 1번, 2번, 3번, … 순서로 번호표 id를 받고,
지금까지 만들어진 괴물의 수는 클래스 변수 Monster.count에 들어 있습니다.

    Monster.count              지금까지 만들어진 괴물 수. 처음에는 0. (클래스 변수)
    m.kind, m.hp, m.attack     받은 값 그대로 (인스턴스 변수)
    m.id                       몇 번째로 만들어졌는지. 1부터. (인스턴스 변수)

예시
    Monster.count       -> 0
    a = Monster("슬라임", 20, 3)
    b = Monster("고블린", 35, 6)
    c = Monster("슬라임", 20, 3)
    a.id, b.id, c.id    -> 1, 2, 3
    Monster.count       -> 3
    a.count             -> 3     # 인스턴스를 통해 읽어도 클래스 변수가 보입니다

클래스로 생각하는 법
    인스턴스 변수(self.hp)는 괴물 한 마리마다 따로 있습니다. 반면 "지금까지
    몇 마리 만들어졌는가"는 어느 한 마리의 것이 아니라 Monster라는 종류 전체의
    정보입니다. 이런 값은 클래스 몸통(def 들과 같은 높이)에 count = 0 처럼 바로
    적습니다. 이것이 클래스 변수이고, 모든 인스턴스가 하나를 공유합니다.

    클래스 변수를 바꿀 때는 반드시 Monster.count += 1 처럼 클래스 이름으로
    접근합니다. self.count += 1 이라고 쓰면 공유된 값이 바뀌는 게 아니라, 그
    인스턴스에만 count라는 인스턴스 변수가 새로 생깁니다. (읽을 때는 self.count
    로도 클래스 변수가 보이지만, 대입하는 순간 새 인스턴스 변수가 됩니다.
    서술형 S2에서 직접 확인합니다.)

힌트
    - __init__ 안에서 Monster.count 를 1 올린 다음, 그 값을 self.id 에 넣습니다.
    - 테스트는 매번 Monster.count = 0 으로 되돌린 뒤 시작합니다.
      self.count += 1 로 쓰면 Monster.count 가 0에 머물러 테스트가 실패합니다.
"""


class Monster:
    def __init__(self, kind: str, hp: int, attack: int) -> None:
        raise NotImplementedError
