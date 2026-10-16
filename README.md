# 시작하기

vscode에서 프로젝트를 열고, 아래 명령어를 실행하세요.
(명령어 대신 [VS Code 작업으로 실행하기](#vs-code-작업으로-실행하기)의 `환경 설정` 작업을 써도 됩니다.)

Windows:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup.ps1
```

MacOS:

```bash
chmod +x ./setup.sh
./setup.sh
```

# 테스트 돌리기

터미널에서 다음을 붙여넣으면 테스트가 됩니다.

## 전체 테스트하기

```bash
python -m pytest
```

## 특정 번호만 테스트하기

```bash
python -m pytest -k problem_01
```

# VS Code 작업으로 실행하기

터미널 명령어 대신 VS Code 메뉴 `Terminal > Run Task...` (한국어 UI: `터미널 > 작업 실행...`)에서 아래 작업을 선택해도 됩니다.

| 작업                 | 하는 일                                                                       |
| -------------------- | ----------------------------------------------------------------------------- |
| `환경 설정`          | `setup.ps1` / `setup.sh` 실행 (Windows에서는 실행 정책 설정 없이 바로 됩니다) |
| `전체 테스트`        | `python -m pytest`                                                            |
| `특정 번호만 테스트` | 문제 번호를 입력받아 `python -m pytest -k problem_번호` 실행                  |

# 문제 목록 (5주차: 클래스와 객체)

각 파일 맨 위의 설명을 읽고, `raise NotImplementedError` 를 지우고 그 자리에 코드를 쓰세요.
"완성된 코드입니다"라고 적힌 클래스는 고치지 않습니다. 소재는 **텍스트 RPG**입니다.
서술형(S1~S5)은 `서술형.md`에 있습니다. 코드를 실행하기 **전에** 답을 적고, 적은 뒤에 실행해 확인하세요.

| 파일                  | 주제                    | 새로 배우는 것                                  |
| --------------------- | ----------------------- | ----------------------------------------------- |
| `problem_01.py`       | 영웅 만들기             | **`class`, `__init__`, `self.속성`**            |
| `problem_02.py`       | 피해와 회복             | 인스턴스 메서드 — 상태 읽기·바꾸기              |
| `problem_03.py`       | 공격                    | 다른 객체를 받는 메서드 (`self`와 `target`)     |
| `problem_04.py`       | 괴물 번호표             | **클래스 변수** (`Monster.count`)               |
| `problem_05.py`       | 문자열에서 영웅 만들기  | `@classmethod`, `cls(...)`                      |
| `problem_06.py`       | 이름 검사               | `@staticmethod`, 세 메서드 비교                 |
| `problem_07.py`       | 파티                    | 객체를 담는 객체 (`self.members = []`)          |
| `problem_08.py`       | 전투                    | 통합 — 객체들에게 일 시키기                     |
| `problem_extra_01.py` | [숙제] 가방             | 딕셔너리를 품은 객체, 기본값 매개변수           |
| `problem_extra_02.py` | [도전] 분수             | 새 객체를 돌려주는 메서드 (6주차 예고)          |
| `서술형.md`           | S1~S5: 출력 예측과 이유 | `self` 누락, 클래스 변수 함정, `==`             |

## 다 못 풀어도 괜찮습니다

수업에서는 **1 → S1 → 2 → 3 → 4 → S2 → S3 → 5 → 6 → 7 → 8** 순서로 갑니다.
나머지(extra 1, extra 2, S4, S5)는 숙제입니다. 숙제는 `python -m pytest -k problem_extra_01` 처럼 테스트합니다.
