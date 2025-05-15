import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 관계 심층 분석", page_icon="💞")

# --- MBTI 유형 목록 ---
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# --- MBTI 궁합 데이터 (외부 파일로 분리하고 더 상세하게 구성) ---
# 예시: (유형1, 유형2) 키에 대해 상세 궁합 정보 딕셔너리 포함
# 각 궁합 정보에는 'title', 'summary', 'strengths_in_relationship', 'challenges', 'tips' 등을 포함
detailed_compatibility_data = {
    ("ENFP", "INFJ"): {
        "title": "✨ 영혼의 단짝, 이상적인 파트너십",
        "icon": "💖", # 또는 이미지 경로
        "summary": "ENFP의 창의성과 열정, INFJ의 통찰력과 공감 능력이 만나 서로에게 깊은 영감을 주는 관계입니다. 함께 성장하며 이상을 실현해나갈 수 있는 최고의 조합 중 하나입니다.",
        "strengths_in_relationship": [
            "서로의 가능성을 믿고 지지함",
            "새로운 아이디어와 가능성을 함께 탐색",
            "정서적으로 깊이 연결되고 서로를 잘 이해함",
            "서로의 성장을 촉진하는 긍정적 시너지"
        ],
        "potential_challenges": [
            "ENFP의 즉흥성과 INFJ의 계획성 사이의 조율 필요",
            "이상과 현실 사이의 괴리감에 대한 대처",
            "외부 자극에 대한 민감도 차이"
        ],
        "tips_for_growth": [
            "정기적인 깊은 대화를 통해 서로의 생각과 감정을 공유하세요.",
            "서로의 다른 에너지 관리 방식을 존중하고 배려하세요.",
            "함께 새로운 경험을 하거나 공동의 목표를 설정하여 관계를 더욱 풍요롭게 만드세요."
        ]
    },
    ("ISTJ", "ENFP"): {
        "title": " opposites_attract.png 반대가 끌리는 매력, 상호 보완적 관계",
        "icon": "🔄",
        "summary": "현실적이고 체계적인 ISTJ와 이상적이고 자유로운 ENFP는 서로에게 없는 부분을 채워줄 수 있는 매력적인 조합입니다. 서로의 다름을 이해하고 존중하는 것이 핵심입니다.",
        "strengths_in_relationship": [
            "ISTJ의 안정감과 ENFP의 활력이 균형을 이룸",
            "서로 다른 관점을 제공하여 문제 해결에 도움",
            "일상에 새로운 자극과 재미를 더할 수 있음"
        ],
        "potential_challenges": [
            "의사소통 방식의 차이 (직설적 vs. 감성적)",
            "변화를 수용하는 속도와 방식의 차이",
            "가치관의 우선순위 충돌 가능성"
        ],
        "tips_for_growth": [
            "서로의 강점을 인정하고 칭찬하는 시간을 가지세요.",
            "갈등 발생 시, 상대방의 입장에서 생각해보려는 노력이 필요합니다.",
            "함께 새로운 규칙이나 타협점을 찾아가는 과정을 즐기세요."
        ]
    },
    # ... 다른 유형 조합에 대한 상세 궁합 정보
}


st.title("💞 MBTI 관계 심층 분석")
st.markdown("나와 상대방의 MBTI 유형을 선택하고, 두 유형 간의 관계 역학을 자세히 알아보세요.")
st.caption("모든 관계는 개인의 노력과 상황에 따라 달라질 수 있습니다. 본 정보는 관계 이해를 돕기 위한 참고 자료입니다.")

col1, col2 = st.columns(2)

with col1:
    my_mbti_default_index = 0
    if 'mbti_result' in st.session_state and st.session_state.mbti_result in mbti_types:
        my_mbti_default_index = mbti_types.index(st.session_state.mbti_result)
    my_mbti = st.selectbox("나의 MBTI 유형:", mbti_types, index=my_mbti_default_index, key="my_mbti_compatibility_detail")

with col2:
    partner_mbti = st.selectbox("상대방 MBTI 유형:", mbti_types, index=1, key="partner_mbti_compatibility_detail")


if st.button("궁합 심층 분석 보기 🔬", type="primary"):
    if my_mbti and partner_mbti:
        if my_mbti == partner_mbti:
            st.info(f"😊 **{my_mbti}** 와 **{my_mbti}** (자기 자신과의 관계)\n\n자기 자신을 이해하고 사랑하는 것은 모든 관계의 시작입니다! 스스로의 강점을 발견하고 발전시켜나가세요.")
        else:
            # 궁합 데이터 조회 (순서 무관하게)
            key1 = (my_mbti, partner_mbti)
            key2 = (partner_mbti, my_mbti)
            
            comp_info = detailed_compatibility_data.get(key1) or detailed_compatibility_data.get(key2)

            if comp_info:
                st.header(f"{comp_info.get('icon', '')} {my_mbti} & {partner_mbti} : {comp_info.get('title', '궁합 정보')}")
                st.markdown(f"**💬 종합 설명:** {comp_info.get('summary', '정보 없음')}")
                
                st.subheader("🤝 관계의 강점")
                for strength in comp_info.get("strengths_in_relationship", []):
                    st.markdown(f"- {strength}")

                st.subheader("🤔 주의할 점 및 갈등 요소")
                for challenge in comp_info.get("potential_challenges", []):
                    st.markdown(f"- {challenge}")

                st.subheader("💡 관계 발전을 위한 조언")
                for tip in comp_info.get("tips_for_growth", []):
                    st.markdown(f"- {tip}")
                
                # 추가적인 시각화나 정보 (예: 두 유형의 핵심 특징 비교표)
                # with st.expander("두 유형 핵심 특징 비교"):
                #     # mbti_details 에서 각 유형 정보 가져와서 비교 표시
                #     st.write(f"**{my_mbti}의 특징:** {mbti_details.get(my_mbti, {}).get('summary', '정보 없음')}")
                #     st.write(f"**{partner_mbti}의 특징:** {mbti_details.get(partner_mbti, {}).get('summary', '정보 없음')}")

            else:
                st.warning(f"'{my_mbti}'와(과) '{partner_mbti}' 조합에 대한 상세 궁합 정보가 아직 준비되지 않았습니다. 😥")
    else:
        st.error("두 MBTI 유형을 모두 선택해주세요.")

st.markdown("---")
st.caption("MBTI는 성격의 선호 경향을 나타내는 지표이며, 궁합은 절대적인 것이 아닙니다. 서로의 다름을 이해하고 존중하는 것이 건강한 관계의 기초입니다.")
