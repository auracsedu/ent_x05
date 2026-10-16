"""
[도전] 문제 extra 2. 분수 (새 객체를 돌려주는 메서드)

분수를 나타내는 클래스 Fraction을 작성하세요. 분자 num, 분모 den은 정수입니다.

    Fraction(num, den)   만들어질 때 바로 기약분수로 고칩니다.
                         - 분모가 0이면 ValueError
                         - 분모는 항상 양수. 부호는 분자에 둡니다.
                         - 분자가 0이면 분모는 1로 둡니다.
    add(other)           두 분수의 합을 "새" Fraction으로 돌려줍니다.
    mul(other)           두 분수의 곱을 "새" Fraction으로 돌려줍니다.
    equals(other)        두 분수가 같은 수이면 True
    to_string()          "3/4" 꼴의 문자열. 분모가 1이면 "2" 처럼 정수만.

    add, mul은 self와 other를 바꾸지 않습니다.

예시
    Fraction(2, 4).num, Fraction(2, 4).den       -> 1, 2
    Fraction(3, -6).num, Fraction(3, -6).den     -> -1, 2
    Fraction(0, 5).num, Fraction(0, 5).den       -> 0, 1
    Fraction(1, 0)                               -> ValueError

    a = Fraction(1, 2)
    b = Fraction(1, 3)
    c = a.add(b)
    c.to_string()            -> "5/6"
    a.to_string()            -> "1/2"       # a는 그대로
    a.mul(b).to_string()     -> "1/6"
    Fraction(1, 2).add(Fraction(1, 2)).to_string()   -> "1"
    Fraction(-1, 2).to_string()                      -> "-1/2"
    a.equals(Fraction(2, 4))     -> True
    a.equals(b)                  -> False

클래스로 생각하는 법
    지금까지의 메서드는 자기 상태를 바꿨습니다(take_damage). 수를 나타내는 객체는
    다릅니다. 1/2에 1/3을 더했다고 1/2이 5/6으로 변하면 곤란하니까요. 그래서
    add는 self를 건드리지 않고 Fraction(새 분자, 새 분모) 를 만들어 돌려줍니다.
    두 방식 모두 자주 쓰이므로, 문제를 읽을 때 "바꾸는가, 새로 만드는가"를 먼저
    확인하는 습관을 들이세요.

    다음 주 예고: a.add(b) 대신 a + b, a.equals(b) 대신 a == b, print(a) 로
    "1/2"가 나오게 만드는 방법(__add__, __eq__, __str__)을 배웁니다. 이 클래스를
    그대로 들고 가서 고치게 되니 잘 보관해 두세요.

힌트
    - 기약분수: math.gcd(num, den) 으로 나눕니다. (4주차에 썼습니다)
      math.gcd(0, 5) 는 5라서 0/5 -> 0/1 이 저절로 됩니다. 음수가 섞여도 gcd는 양수입니다.
    - 부호: if den < 0: num, den = -num, -den
    - 약분 로직은 __init__에 한 번만 쓰고, add와 mul은 그냥 Fraction(...)을
      만들어 돌려줍니다. 그러면 결과도 저절로 기약분수입니다.
    - a/b + c/d = (ad + bc) / bd,  a/b * c/d = ac / bd
    - equals는 둘 다 기약분수라서 분자와 분모를 각각 비교하면 됩니다.
"""


class Fraction:
    def __init__(self, num: int, den: int) -> None:
        raise NotImplementedError

    def add(self, other: "Fraction") -> "Fraction":
        raise NotImplementedError

    def mul(self, other: "Fraction") -> "Fraction":
        raise NotImplementedError

    def equals(self, other: "Fraction") -> bool:
        raise NotImplementedError

    def to_string(self) -> str:
        raise NotImplementedError
