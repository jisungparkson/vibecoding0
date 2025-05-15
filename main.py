import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 심층 분석", page_icon="🔬")

# --- MBTI 유형 데이터 (외부 파일로 분리하는 것이 이상적) ---
# 예시: 각 유형별 상세 정보 (개요, 강점, 약점, 업무 스타일, 스트레스 반응, 개발할 점 등)
mbti_details = {
    "ISTJ": {
        "icon": "꼼꼼한_ISTJ_아이콘.png", # 가상의 이미지 파일
        "catchphrase": "세상의 소금, 책임감 있는 현실주의자",
        "summary": "실제 경험을 중시하며, 한번 시작한 일은 끝까지 해내는 책임감이 강한 유형입니다. 약속을 잘 지키고 질서와 규칙을 중요하게 생각합니다.",
        "strengths": ["책임감 강함", "철저함", "현실적", "조직적", "끈기 있음"],
        "weaknesses": ["융통성 부족 가능성", "새로운 변화에 대한 저항감", "타인의 감정 고려 미흡 가능성"],
        "work_style": "구체적이고 명확한 업무 지시를 선호하며, 체계적인 계획 하에 업무를 수행합니다. 마감 기한을 철저히 준수합니다.",
        "stress_response": "과도한 업무량이나 예측 불가능한 상황에서 스트레스를 받으며, 혼자만의 시간을 통해 회복하려는 경향이 있습니다.",
        "development_points": ["새로운 시도에 대한 개방성 기르기", "타인의 감정에 대한 공감 능력 향상"],
        "recommended_jobs_detailed": {
            "회계사": {
                "reason": "정확성, 꼼꼼함, 규칙 준수를 중시하는 ISTJ의 성향과 잘 맞습니다.",
                "tasks": ["재무 기록 분석", "세무 보고서 작성", "예산 관리"],
                "skills": ["수리 능력", "분석적 사고", "세법 지식"]
            },
            "프로젝트 관리자": {
                "reason": "체계적인 계획 수립 및 실행, 일정 관리에 능한 ISTJ에게 적합합니다.",
                "tasks": ["프로젝트 계획 및 실행", "자원 배분", "위험 관리"],
                "skills": ["리더십", "조직력", "문제 해결 능력"]
            }
            # ... 기타 직업 상세 정보
        }
    },
    # ... 다른 MBTI 유형 상세 정보
}

# --- MBTI 검사 로직 (개선된 방식) ---
def run_mbti_test():
    st.subheader("🔍 MBTI 간이 검사")
    st.caption("각 문항에 대해 자신에게 더 가깝다고 생각되는 쪽을 선택해주세요. 깊이 생각하기보다 떠오르는 대로 응답하는 것이 좋습니다.")

    questions = {
        "E/I": [
            ("나는 여러 사람들과 넓게 교류하는 편이다", "E"),
            ("나는 소수의 사람들과 깊게 교류하는 편이다", "I"),
            ("나는 활동적인 모임에서 에너지를 얻는다", "E"),
            ("나는 조용한 환경에서 혼자 생각할 때 에너지를 얻는다", "I"),
        ],
        "S/N": [
            ("나는 현재의 실제적인 정보에 집중한다", "S"),
            ("나는 미래의 가능성과 아이디어에 집중한다", "N"),
            ("나는 구체적이고 사실적인 설명을 선호한다", "S"),
            ("나는 비유적이고 암시적인 설명을 선호한다", "N"),
        ],
        "T/F": [
            ("나는 객관적인 사실과 논리에 근거해 결정한다", "T"),
            ("나는 사람들과의 관계와 감정을 고려해 결정한다", "F"),
            ("나는 공정성과 원칙을 중요하게 생각한다", "T"),
            ("나는 조화와 공감을 중요하게 생각한다", "F"),
        ],
        "J/P": [
            ("나는 미리 계획을 세우고 체계적으로 일을 처리한다", "J"),
            ("나는 상황에 맞춰 유연하게 일을 처리하는 편이다", "P"),
            ("나는 결정된 사항을 빨리 마무리 짓는 것을 선호한다", "J"),
            ("나는 가능한 많은 선택지를 열어두는 것을 선호한다", "P"),
        ]
    }

    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    for key, q_list in questions.items():
        st.markdown(f"**{key.split('/')[0]} (외향/내향 등) 선호 지표:**") # 실제 지표명으로 변경
        for i, (q_text, q_type) in enumerate(q_list):
            # 좀 더 세분화된 선택지를 제공할 수 있습니다. (예: 5점 척도)
            # 여기서는 단순화를 위해 라디오 버튼 유지
            answer = st.radio(f"{q_text}", ("선택1", "선택2"), key=f"{key}_{i}", horizontal=True, label_visibility="collapsed")
            # 실제로는 선택지에 따라 점수를 다르게 부여해야 합니다.
            # 예시: '선택1'이 E에 가깝다면 scores[q_type] += 1
            # 이 부분은 질문 설계에 따라 정교하게 만들어야 합니다.
            # 임시로 첫번째 선택이 해당 타입이라고 가정
            if answer == "선택1": # 이 부분을 실제 로직에 맞게 수정
                 scores[q_type] +=1


    if st.button("결과 분석하기", type="primary"):
        result_mbti = ""
        result_mbti += "E" if scores["E"] >= scores["I"] else "I"
        result_mbti += "S" if scores["S"] >= scores["N"] else "N"
        result_mbti += "T" if scores["T"] >= scores["F"] else "F"
        result_mbti += "J" if scores["J"] >= scores["P"] else "P"
        st.session_state.mbti_result = result_mbti
        st.session_state.mbti_scores = scores # 점수도 저장하여 활용 가능

        st.success(f"검사가 완료되었습니다! 당신의 예상 MBTI 유형은 **{result_mbti}** 입니다.")
        st.balloons()


# --- 페이지 시작 ---
st.title("🔬 MBTI 심층 분석 및 직업 탐색")

if 'mbti_result' not in st.session_state:
    run_mbti_test()
else:
    user_mbti = st.session_state.mbti_result
    st.header(f"🌟 {user_mbti} 유형 분석 결과")

    if user_mbti in mbti_details:
        details = mbti_details[user_mbti]
        
        # 아이콘 및 캐치프레이즈
        # if details.get("icon"):
        #     st.image(details["icon"], width=100) # 실제 이미지 경로 설정
        st.subheader(f"*{details.get('catchphrase', '')}*")
        st.markdown(f"**개요:** {details.get('summary', '정보 없음')}")

        # 탭으로 상세 정보 제공
        tab1, tab2, tab3, tab4 = st.tabs(["💪 강점과 약점", "👔 업무 스타일", "😥 스트레스와 개발점", "🎯 추천 직업"])

        with tab1:
            st.subheader("👍 강점")
            for strength in details.get("strengths", []):
                st.markdown(f"- {strength}")
            st.subheader("👎 보완할 수 있는 점")
            for weakness in details.get("weaknesses", []):
                st.markdown(f"- {weakness}")
        
        with tab2:
            st.markdown(f"**주요 업무 스타일:** {details.get('work_style', '정보 없음')}")
            # 추가적인 업무 관련 팁이나 정보 제공 가능

        with tab3:
            st.markdown(f"**스트레스 상황 및 대처:** {details.get('stress_response', '정보 없음')}")
            st.markdown(f"**성장을 위한 개발 포인트:**")
            for point in details.get("development_points", []):
                st.markdown(f"- {point}")

        with tab4:
            st.subheader(f"{user_mbti} 유형에게 추천하는 직업군")
            if "recommended_jobs_detailed" in details:
                for job, job_info in details["recommended_jobs_detailed"].items():
                    with st.expander(f"**{job}**"):
                        st.markdown(f"**🤔 이 직업이 왜 잘 맞을까요?**\n {job_info.get('reason', '정보 없음')}")
                        st.markdown(f"**📋 주요 업무:**")
                        for task in job_info.get("tasks", []):
                            st.markdown(f"  - {task}")
                        st.markdown(f"**💡 필요 역량:**")
                        for skill in job_info.get("skills", []):
                            st.markdown(f"  - {skill}")
                        # st.link_button("관련 정보 더 보기", "워크넷_링크_등") # 실제 링크로
            else:
                st.write("추천 직업 정보가 준비 중입니다.")
    else:
        st.warning("해당 MBTI 유형에 대한 상세 정보가 아직 준비되지 않았습니다.")

    if st.button("🔄 다시 검사하기"):
        del st.session_state.mbti_result
        if 'mbti_scores' in st.session_state:
            del st.session_state.mbti_scores
        st.experimental_rerun()

st.markdown("---")
st.caption("본 MBTI 분석 정보는 일반적인 경향성을 바탕으로 하며, 개인의 특성은 다를 수 있습니다. 자기 이해를 위한 참고 자료로 활용하시기 바랍니다.")
