import streamlit as st

# --- 페이지 설정 (선택 사항, 메인 앱에서 한 번만 해도 됨) ---
# st.set_page_config(page_title="MBTI 궁합 보기", page_icon="💕")

st.title("💖 MBTI 유형별 궁합 보기")
st.write("나와 상대방의 MBTI 유형을 선택하고 궁합을 알아보세요!")
st.caption("MBTI 궁합은 재미로 참고해주세요. 모든 관계는 개인의 노력과 성향에 따라 달라질 수 있습니다.")

# --- MBTI 유형 목록 ---
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# --- MBTI 궁합 데이터 (예시) ---
# 실제 데이터는 더 상세하게 구성하거나 외부 파일(CSV, JSON)에서 불러오는 것이 좋습니다.
# 여기서는 간단한 설명을 위해 직접 정의합니다.
# 키: (유형1, 유형2) 튜플, 값: 궁합 설명 (순서는 상관없도록 처리하거나, 양방향 모두 정의)
compatibility_dict = {
    # 천생연분 예시 (일방향 또는 양방향 모두 정의 필요)
    ("ENFP", "INFJ"): "✨ 천생연분: 서로에게 깊은 영감을 주고 끊임없이 새로운 것을 발견하는, 영혼의 단짝 같은 관계입니다. 함께 있을 때 가장 큰 행복과 성장을 경험할 수 있습니다.",
    ("INFJ", "ENFP"): "✨ 천생연분: 서로에게 깊은 영감을 주고 끊임없이 새로운 것을 발견하는, 영혼의 단짝 같은 관계입니다. 함께 있을 때 가장 큰 행복과 성장을 경험할 수 있습니다.",
    ("ENTP", "INFJ"): "🤝 좋은 궁합: 서로의 지적인 면을 자극하며 끊임없이 대화하고 탐구하는 것을 즐깁니다. 때로는 의견 충돌도 있지만, 이를 통해 더욱 발전하는 관계입니다.",
    ("INFJ", "ENTP"): "🤝 좋은 궁합: 서로의 지적인 면을 자극하며 끊임없이 대화하고 탐구하는 것을 즐깁니다. 때로는 의견 충돌도 있지만, 이를 통해 더욱 발전하는 관계입니다.",
    ("ISFP", "ESFJ"): "😊 좋은 궁합: 서로를 편안하게 해주고 감정적인 지지를 아끼지 않는 따뜻한 관계입니다. 함께 소소한 행복을 나누는 것을 즐깁니다.",
    ("ESFJ", "ISFP"): "😊 좋은 궁합: 서로를 편안하게 해주고 감정적인 지지를 아끼지 않는 따뜻한 관계입니다. 함께 소소한 행복을 나누는 것을 즐깁니다.",

    # 그저 그런 궁합 예시
    ("ISTJ", "INTP"): "😐 보통 궁합: 서로 다른 점이 많지만, 각자의 영역을 존중한다면 무난한 관계를 이어갈 수 있습니다. 공통의 목표를 설정하는 것이 도움이 됩니다.",
    ("INTP", "ISTJ"): "😐 보통 궁합: 서로 다른 점이 많지만, 각자의 영역을 존중한다면 무난한 관계를 이어갈 수 있습니다. 공통의 목표를 설정하는 것이 도움이 됩니다.",

    # 안 좋은 궁합 예시 (표현에 주의)
    ("INFP", "ESTJ"): "⚠️ 노력이 필요한 궁합: 가치관과 문제 해결 방식에서 큰 차이를 보여 많은 이해와 노력이 필요합니다. 서로의 다름을 인정하고 존중하는 것이 중요합니다.",
    ("ESTJ", "INFP"): "⚠️ 노력이 필요한 궁합: 가치관과 문제 해결 방식에서 큰 차이를 보여 많은 이해와 노력이 필요합니다. 서로의 다름을 인정하고 존중하는 것이 중요합니다.",

    # 파국 (매우 안 좋은 관계) 표현보다는 "서로 매우 다른 유형" 등으로 순화하는 것이 좋습니다.
    ("ISFJ", "ENTP"): "🤯 서로 매우 다른 유형: 삶의 방식과 우선순위가 매우 달라 갈등이 잦을 수 있습니다. 열린 마음으로 소통하고 서로를 배우려는 자세가 중요합니다.",
    ("ENTP", "ISFJ"): "🤯 서로 매우 다른 유형: 삶의 방식과 우선순위가 매우 달라 갈등이 잦을 수 있습니다. 열린 마음으로 소통하고 서로를 배우려는 자세가 중요합니다.",
}

# --- 사용자 입력 ---
col1, col2 = st.columns(2)

with col1:
    # 만약 이전 페이지(MBTI 검사)에서 결과를 st.session_state에 저장했다면, 기본값으로 활용 가능
    my_mbti_default_index = 0 # 기본적으로 첫 번째 MBTI를 선택
    if 'mbti_result' in st.session_state and st.session_state.mbti_result in mbti_types:
        my_mbti_default_index = mbti_types.index(st.session_state.mbti_result)
    my_mbti = st.selectbox("나의 MBTI 유형:", mbti_types, index=my_mbti_default_index, key="my_mbti_compatibility")

with col2:
    partner_mbti = st.selectbox("상대방 MBTI 유형:", mbti_types, index=1, key="partner_mbti_compatibility") # 기본적으로 두 번째 MBTI를 선택

# --- 궁합 결과 표시 ---
if st.button("궁합 결과 보기 🔍"):
    if my_mbti and partner_mbti:
        if my_mbti == partner_mbti:
            st.info("😊 자기 자신과의 궁합은 언제나 최고죠! 스스로를 사랑하는 당신은 멋져요!")
        else:
            # 궁합 데이터에서 결과 조회 (순서에 상관없이 조회 가능하도록 처리)
            result_key1 = (my_mbti, partner_mbti)
            result_key2 = (partner_mbti, my_mbti)
            
            compatibility_info = compatibility_dict.get(result_key1)
            if compatibility_info is None:
                compatibility_info = compatibility_dict.get(result_key2)

            if compatibility_info:
                st.subheader(f"'{my_mbti}'와(과) '{partner_mbti}'의 궁합")
                # 궁합 설명에 따라 아이콘이나 색상 변경 가능
                if "천생연분" in compatibility_info:
                    st.success(compatibility_info)
                elif "좋은 궁합" in compatibility_info:
                    st.info(compatibility_info)
                elif "보통 궁합" in compatibility_info or "무난한" in compatibility_info:
                    st.markdown(compatibility_info)
                elif "노력이 필요한" in compatibility_info or "매우 다른" in compatibility_info:
                    st.warning(compatibility_info)
                else:
                    st.markdown(compatibility_info) # 기본
            else:
                st.warning(f"'{my_mbti}'와(과) '{partner_mbti}' 조합에 대한 궁합 정보가 아직 준비되지 않았습니다. 😥")
    else:
        st.error("두 MBTI 유형을 모두 선택해주세요.")

st.markdown("---")
st.caption("본 MBTI 궁합 정보는 일반적인 경향성을 나타내며, 개인차를 고려해야 합니다. 재미로 참고하시고, 모든 관계는 서로의 이해와 노력이 가장 중요합니다.")
