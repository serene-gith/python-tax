# app.py
import streamlit as st

st.set_page_config(page_title="소득세 계산기", layout="centered")

st.title("소득세 계산기 (예시)")
st.caption("간단한 세율 구간 예시 코드 — 데모용")

def compute_tax_and_level(income: int):
    if income <= 12_000_000:
        return income * 0.06, "저소득층"
    elif income <= 46_000_000:
        return income * 0.15, "중간소득층"
    elif income <= 88_000_000:
        return income * 0.24, "고소득층"
    else:
        return income * 0.35, "초고소득층"

income = st.number_input("연 소득(원)", min_value=0, step=1_000_000, value=55_000_000, format="%d")
tax, level = compute_tax_and_level(income)

st.write("### 결과")
st.write(f"- 소득 수준: **{level}**")
st.write(f"- 연 소득: **{income:,}원**")
st.write(f"- 예상 세금: **{tax:,.0f}원**")
