# 자연어처리 입문 학습 환경

이 폴더는 VS Code에서 `딥 러닝을 이용한 자연어 처리 입문 - RAG, 에이전트, LLM 파인튜닝까지`를 학습하기 위한 Python 환경입니다.

## 참고 및 출처

본 저장소의 노트북은 `딥 러닝을 이용한 자연어 처리 입문 - RAG, 에이전트, LLM 파인튜닝까지`를 학습하며 작성한 실습 코드입니다.

책의 예제 흐름을 참고했으며, 개인 학습을 위해 직접 실행하고 일부 설명을 덧붙였습니다. 원문의 저작권은 해당 도서와 저자에게 있습니다.

## 빠른 시작

1. VS Code에서 이 폴더를 엽니다.
2. 터미널에서 가상환경을 활성화합니다.

```bash
source .venv/bin/activate
```

3. 설치가 완료되어 있는지 확인합니다.

```bash
python scripts/check_environment.py
```

4. 노트북을 사용할 때는 VS Code에서 `.venv` 또는 `Python (.venv 자연어처리_입문)` 커널을 선택합니다.

환경을 다시 만들 때는 아래 순서로 진행하면 됩니다.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python scripts/download_nltk_data.py
python scripts/check_environment.py
```

## 폴더 구조

```text
.
├── .venv/                  # Python 3.11 가상환경
├── .vscode/                # VS Code 프로젝트 설정
├── data/                   # 직접 내려받은 데이터 보관
├── nltk_data/              # NLTK 토크나이저 데이터
├── notebooks/              # 장별 실습 노트북
├── scripts/                # 실행/검증용 Python 스크립트
├── requirements.txt        # 기본 학습 패키지
└── .env.example            # API 키 예시 파일
```

## 선택 설치 메모

- KoNLPy, TensorFlow/Keras, PyTorch, Hugging Face, RAG 실습은 현재 환경에서 바로 진행할 수 있게 구성했습니다.
- NLTK `word_tokenize`에 필요한 `punkt`, `punkt_tab` 데이터는 `nltk_data/`에 준비되어 있습니다.
- API 키가 필요한 장에서는 `.env.example`을 `.env`로 복사한 뒤 값을 채우면 됩니다.
- 현재 PyTorch는 설치와 import가 정상 동작합니다. 이 Mac에서는 `torch.backends.mps.is_built()`는 `True`, `torch.backends.mps.is_available()`은 `False`로 확인되어 기본 실행 장치는 CPU입니다.
