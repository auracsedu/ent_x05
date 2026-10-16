"""
문제 8. 전투 (통합)

영웅 한 명과 괴물 한 마리가 턴제로 싸웁니다. 전투를 진행하는 클래스 Battle을
작성하세요. Hero(문제 3의 답)와 Monster는 완성되어 있습니다. 고치지 마세요.

    Battle(hero, monster)   전투를 만듭니다. hero, monster, turns(지난 턴 수, 처음 0)
                            세 속성을 가집니다.
    is_over()               둘 중 하나라도 쓰러졌으면 True
    turn()                  한 턴을 진행하고 turns를 1 올립니다. 돌려주는 값은 없습니다.
                              1) 영웅이 괴물을 공격합니다. (hero.strike(monster))
                              2) 괴물이 아직 살아 있으면 영웅을 반격합니다.
                                 영웅의 체력이 괴물의 attack만큼 깎입니다.
                            전투가 이미 끝났으면 아무 일도 하지 않습니다.
                            (turns도 오르지 않습니다)
    run()                   전투가 끝날 때까지 turn()을 반복한 뒤 이긴 쪽의 이름을
                            돌려줍니다. 영웅이 이기면 hero.name, 괴물이 이기면
                            monster.kind 입니다.

예시
    h = Hero("용사", 30, 10)
    m = Monster("슬라임", 25, 4)
    bt = Battle(h, m)
    bt.turn()
    m.hp, h.hp, bt.turns     -> 15, 26, 1
    bt.turn()
    m.hp, h.hp, bt.turns     -> 5, 22, 2
    bt.turn()
    m.hp, h.hp, bt.turns     -> 0, 22, 3     # 괴물이 쓰러져 반격이 없음
    bt.is_over()             -> True
    h.level, h.attack        -> 2, 12        # strike가 레벨을 올렸습니다
    bt.turn()
    bt.turns                 -> 3            # 끝난 전투. 아무 일도 없음

    h = Hero("용사", 10, 3)
    m = Monster("드래곤", 100, 7)
    Battle(h, m).run()       -> "드래곤"     # 2턴 만에 영웅 체력 10 -> 3 -> 0

클래스로 생각하는 법
    Battle은 자기 상태(turns)도 갖지만, 주로 다른 두 객체에게 일을 시키는
    "진행자"입니다. 체력을 직접 계산하지 말고 strike와 take_damage를 부르세요.
    문제 1~7에서 만든 메서드들이 그대로 부품이 됩니다.

힌트
    - turn()의 첫 줄은 if self.is_over(): return 입니다.
    - 반격 여부는 공격한 "뒤"의 self.monster.is_alive() 로 판단합니다.
    - run()은 while not self.is_over(): self.turn() 다음에 승자를 고르면 됩니다.
      공격력은 항상 1 이상이라고 보장되므로 전투는 반드시 끝납니다.
    - 테스트에는 20초 제한이 있습니다. 끝나지 않으면 is_over 조건을 확인하세요.
"""


# ---- 아래 Hero와 Monster는 완성된 코드입니다. 고치지 마세요. ----
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

    def strike(self, target) -> bool:
        if not target.is_alive():
            return False
        target.take_damage(self.attack)
        if target.is_alive():
            return False
        self.level += 1
        self.attack += 2
        return True


class Monster:
    def __init__(self, kind: str, hp: int, attack: int) -> None:
        self.kind = kind
        self.hp = hp
        self.attack = attack

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)


# ---- 여기서부터 작성하세요. ----
class Battle:
    def __init__(self, hero: Hero, monster: Monster) -> None:
        raise NotImplementedError

    def is_over(self) -> bool:
        raise NotImplementedError

    def turn(self) -> None:
        raise NotImplementedError

    def run(self) -> str:
        raise NotImplementedError
