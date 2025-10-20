# 소득과 세금 변수 선언
income = 55000000   # 연 소득 (단위: 원)
tax = 0

# if-else 문으로 소득 수준 분류 및 세율 계산
if income <= 12000000:
    tax = income * 0.06
    level = "저소득층"
elif income <= 46000000:
    tax = income * 0.15
    level = "중간소득층"
elif income <= 88000000:
    tax = income * 0.24
    level = "고소득층"
else:
    tax = income * 0.35
    level = "초고소득층"

# 결과 출력
print(f"소득 수준: {level}")
print(f"연 소득: {income:,}원")
print(f"예상 세금: {tax:,.0f}원")
