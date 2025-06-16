# Argon Plasma Global Model Simulator

## 개요
Streamlit 기반 0D 글로벌 모델 시뮬레이터입니다. 아르곤 가스 조건에서 전자밀도, 전자온도 시간변화를 예측합니다.

## 실행 방법
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 입력 변수
- 가스 압력 (mTorr)
- RF 흡수 전력 (W)
- 초기 전자 온도 (eV)
- 초기 전자 밀도 (m⁻³)

## 출력
- 시간에 따른 전자 밀도 (n_e)
- 시간에 따른 전자 온도 (T_e)
- 그래프로 시각화