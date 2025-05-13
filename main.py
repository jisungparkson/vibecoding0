import streamlit as st

# 웹앱 제목 설정 (이모티콘을 넣어봤어요! ✨)
st.title("💖 MBTI 기반 맞춤 직업 추천 💖")
st.subheader("당신의 MBTI를 선택하고 숨겨진 가능성을 찾아보세요! 🚀")

# MBTI 유형 리스트
mbti_types = [
    "선택하세요!", # 기본 선택지
    "INTJ - 용의주도한 전략가",
    "INTP - 논리적인 사색가",
    "ENTJ - 대담한 통솔자",
    "ENTP - 뜨거운 논쟁을 즐기는 변론가",
    "INFJ - 선의의 옹호자",
    "INFP - 열정적인 중재자",
    "ENFJ - 정의로운 사회운동가",
    "ENFP - 재기발랄한 활동가",
    "ISTJ - 청렴결백한 논리주의자",
    "ISFJ - 용감한 수호자",
    "ESTJ - 엄격한 관리자",
    "ESFJ - 사교적인 외교관",
    "ISTP - 만능 재주꾼",
    "ISFP - 호기심 많은 예술가",
    "ESTP - 모험을 즐기는 사업가",
    "ESFP - 자유로운 영혼의 연예인"
]

# 드롭다운 메뉴로 MBTI 선택
selected_mbti = st.selectbox("👇 당신의 MBTI 유형을 선택해주세요!", mbti_types)

# 선택된 MBTI 출력
if selected_mbti != "선택하세요!":
    st.success(f"당신이 선택한 MBTI는 🎉 {selected_mbti} 🎉 입니다!")
    st.balloons() # 선택하면 풍선 효과! 🎈

st.markdown("---") # 구분선
st.markdown("### 💡 다음 단계는?")
st.markdown("""
- 선택된 MBTI에 따른 직업 정보 보여주기
- 더 많은 이모티콘과 이미지로 페이지 꾸미기! 🎨
- MBTI별 상세 설명 추가하기
""")

# (선택 사항) 사이드바에 간단한 설명 추가
st.sidebar.header("✨ 앱 정보")
st.sidebar.info(
    "이 앱은 여러분의 MBTI 유형에 맞는 직업을 추천해 드립니다. "
    "재미로 즐겨주시고, 진로 선택에 작은 영감이 되길 바랍니다! 😊"
)
st.sidebar.markdown("Made with ❤️ by AI & You")
