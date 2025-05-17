import streamlit as st
import json

# --- 데이터 로드 함수 ---
def load_mbti_data(filepath="mbti_data.json"):
    """MBTI 데이터를 JSON 파일에서 로드합니다."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"{filepath} 파일을 찾을 수 없습니다. MBTI 데이터 파일이 올바른 위치에 있는지 확인해주세요.")
        return {}
    except json.JSONDecodeError:
        st.error(f"{filepath} 파일의 형식이 올바르지 않습니다. JSON 형식을 확인해주세요.")
        return {}

# --- MBTI 유형 데이터 로드 ---
mbti_details_data = load_mbti_data()

# MBTI 지표 설명
dimension_map = {
    "E": "외향형", "I": "내향형",
    "S": "감각형", "N": "직관형",
    "T": "사고형", "F": "감정형",
    "J": "판단형", "P": "인식형"
}

# --- MBTI 검사 로직 ---
def run_mbti_test():
    st.subheader("🔍 MBTI 간이 검사")
    st.caption("각 문항 쌍에서 자신에게 더 가깝다고 생각되는 쪽을 선택해주세요. 깊이 생각하기보다 떠오르는 대로 응답하는 것이 좋습니다.")

    # 각 지표별로 2개의 질문 쌍을 제공 (총 8개 질문 그룹)
    # 각 질문은 두 개의 상반된 선택지를 가지며, 각 선택지는 특정 MBTI 타입에 해당함
    questions = {
        "EI": [ # 에너지 방향 (외향E / 내향I)
            {"id": "EI1", "options": [("여러 사람들과 어울리는 것이 좋다", "E"), ("혼자만의 시간을 즐기는 것이 좋다", "I")]},
            {"id": "EI2", "options": [("활동적인 모임에서 에너지를 얻는다", "E"), ("조용한 환경에서 에너지를 얻는다", "I")]},
        ],
        "SN": [ # 인식 기능 (감각형S / 직관형N)
            {"id": "SN1", "options": [("실제 경험과 현실적인 정보를 중시한다", "S"), ("미래의 가능성과 숨겨진 의미를 찾는다", "N")]},
            {"id": "SN2", "options": [("구체적이고 명확한 설명을 선호한다", "S"), ("비유적이고 암시적인 설명을 선호한다", "N")]},
        ],
        "TF": [ # 판단 기능 (사고형T / 감정형F)
            {"id": "TF1", "options": [("결정할 때 논리와 분석을 우선시한다", "T"), ("결정할 때 관계와 감정을 우선시한다", "F")]},
            {"id": "TF2", "options": [("공정성과 원칙을 중요하게 생각한다", "T"), ("타인의 감정에 공감하고 조화를 추구한다", "F")]},
        ],
        "JP": [ # 생활 양식 (판단형J / 인식형P)
            {"id": "JP1", "options": [("미리 계획을 세우고 체계적으로 일을 처리한다", "J"), ("상황에 맞춰 유연하게 일을 처리하는 편이다", "P")]},
            {"id": "JP2", "options": [("결정된 사항을 빨리 마무리 짓는 것을 선호한다", "J"), ("가능한 많은 선택지를 열어두는 것을 선호한다", "P")]},
        ]
    }

    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    # 각 지표(차원)별 질문 표시
    for dimension_code, q_pairs in questions.items():
        dim_label1 = dimension_code[0] # E, S, T, J
        dim_label2 = dimension_code[1] # I, N, F, P
        st.markdown(f"--- \n**{dimension_map[dim_label1]} ({dim_label1}) vs {dimension_map[dim_label2]} ({dim_label2}) 선호 지표:**")

        for i, q_info in enumerate(q_pairs):
            options_text = [opt[0] for opt in q_info["options"]]
            
            # 각 질문 쌍에 대해 하나의 라디오 버튼 그룹 생성
            chosen_text = st.radio(
                label=f"질문 {i+1}:", # 각 질문마다 고유한 레이블보다는, 선택지 자체가 질문의 역할을 하도록 함
                options=options_text,
                key=q_info["id"], # 고유 키 (필수)
                horizontal=False, # 가로 정렬이 모바일에서 깨질 수 있어 세로로 변경
                label_visibility="collapsed" # "질문 N:" 레이블 숨기기 (선택 사항)
            )
            
            # 선택된 텍스트에 해당하는 MBTI 타입 찾아서 점수 부여
            if chosen_text: # 사용자가 선택을 한 경우 (기본적으로 첫번째가 선택됨)
                chosen_type = ""
                for text, type_val in q_info["options"]:
                    if text == chosen_text:
                        chosen_type = type_val
                        break
                if chosen_type:
                    scores[chosen_type] += 1
            else: # 만약 아무것도 선택되지 않은 상태를 처리해야 한다면 (st.radio는 기본 선택이 있음)
                pass


    if st.button("결과 분석하기", type="primary", use_container_width=True):
        result_mbti = ""
        result_mbti += "E" if scores["E"] >= scores["I"] else "I"
        result_mbti += "S" if scores["S"] >= scores["N"] else "N"
        result_mbti += "T" if scores["T"] >= scores["F"] else "F"
        result_mbti += "J" if scores["J"] >= scores["P"] else "P"
        
        st.session_state.mbti_result = result_mbti
        st.session_state.mbti_scores = scores # 점수도 저장

        st.success(f"검사가 완료되었습니다! 당신의 예상 MBTI 유형은 **{result_mbti}** 입니다.")
        st.balloons()
        st.info("아래에서 상세 분석 결과를 확인하거나, 다시 검사를 진행할 수 있습니다.")

# --- MBTI 결과 표시 함수 ---
def display_mbti_results(user_mbti, scores):
    st.header(f"🌟 {user_mbti} 유형 분석 결과")

    if user_mbti in mbti_details_data:
        details = mbti_details_data[user_mbti]
        
        # 아이콘 및 캐치프레이즈
        # icon_path = details.get("icon")
        # if icon_path:
        #     try:
        #         st.image(icon_path, width=100) # 실제 이미지 경로 설정 필요
        #     except Exception as e:
        #         st.warning(f"아이콘을 불러올 수 없습니다: {icon_path} (오류: {e})")
        # else:
        #     st.info("해당 유형의 아이콘 정보가 없습니다.")
            
        st.subheader(f"*{details.get('catchphrase', '캐치프레이즈 정보 없음')}*")
        st.markdown(f"**개요:** {details.get('summary', '요약 정보 없음')}")

        # 점수 시각화
        st.subheader("📈 간이 검사 점수 (선호도)")
        score_pairs = [
            ("E (외향)", scores.get("E", 0), "I (내향)", scores.get("I", 0)),
            ("S (감각)", scores.get("S", 0), "N (직관)", scores.get("N", 0)),
            ("T (사고)", scores.get("T", 0), "F (감정)", scores.get("F", 0)),
            ("J (판단)", scores.get("J", 0), "P (인식)", scores.get("P", 0)),
        ]
        
        cols = st.columns(len(score_pairs))
        for i, (label1, score1, label2, score2) in enumerate(score_pairs):
            with cols[i]:
                st.metric(label=f"{label1} vs {label2}", value=f"{score1} : {score2}")
                total_score_for_dim = score1 + score2
                if total_score_for_dim > 0:
                    # 각 지표의 선호 강도를 간략히 표시 (예: E가 2점, I가 0점이면 E 선호)
                    if score1 > score2:
                        st.caption(f"{label1.split(' ')[0]} 선호")
                    elif score2 > score1:
                        st.caption(f"{label2.split(' ')[0]} 선호")
                    else:
                        st.caption("균형") # 또는 문항 수가 적어 명확한 구분이 어려울 수 있음
                else:
                    st.caption("점수 없음")


        # 탭으로 상세 정보 제공
        tab_titles = ["💪 강점과 약점", "👔 업무 스타일", "😥 스트레스와 개발점", "🎯 추천 직업"]
        tab1, tab2, tab3, tab4 = st.tabs(tab_titles)

        with tab1:
            st.subheader("👍 강점")
            strengths = details.get("strengths", [])
            if strengths:
                for strength in strengths:
                    st.markdown(f"- {strength}")
            else:
                st.info("강점 정보가 준비 중입니다.")
            
            st.subheader("👎 보완할 수 있는 점")
            weaknesses = details.get("weaknesses", [])
            if weaknesses:
                for weakness in weaknesses:
                    st.markdown(f"- {weakness}")
            else:
                st.info("보완점 정보가 준비 중입니다.")
        
        with tab2:
            st.markdown(f"**주요 업무 스타일:** {details.get('work_style', '정보 없음')}")

        with tab3:
            st.markdown(f"**스트레스 상황 및 대처:** {details.get('stress_response', '정보 없음')}")
            st.markdown(f"**성장을 위한 개발 포인트:**")
            dev_points = details.get("development_points", [])
            if dev_points:
                for point in dev_points:
                    st.markdown(f"- {point}")
            else:
                st.info("개발 포인트 정보가 준비 중입니다.")

        with tab4:
            st.subheader(f"{user_mbti} 유형에게 추천하는 직업군")
            if "recommended_jobs_detailed" in details and details["recommended_jobs_detailed"]:
                for job, job_info in details["recommended_jobs_detailed"].items():
                    with st.expander(f"**{job}**"):
                        st.markdown(f"**🤔 이 직업이 왜 잘 맞을까요?**\n {job_info.get('reason', '정보 없음')}")
                        st.markdown(f"**📋 주요 업무:**")
                        tasks = job_info.get("tasks", [])
                        if tasks:
                            for task in tasks:
                                st.markdown(f"  - {task}")
                        else:
                            st.markdown("  - 정보 없음")
                        
                        st.markdown(f"**💡 필요 역량:**")
                        skills = job_info.get("skills", [])
                        if skills:
                            for skill in skills:
                                st.markdown(f"  - {skill}")
                        else:
                            st.markdown("  - 정보 없음")
                        
                        # 예시 링크 버튼 (실제 유효한 URL로 변경 필요)
                        st.link_button("관련 정보 더 보기 (예: 워크넷)", f"https://www.work.go.kr/seekWanted/summaryWantedList.do?schTxt={job}&paramJson=") 
            else:
                st.write("추천 직업 정보가 준비 중입니다.")
    else:
        st.warning(f"해당 MBTI 유형({user_mbti})에 대한 상세 정보가 아직 mbti_data.json 파일에 준비되지 않았습니다.")

# --- 페이지 설정 및 메인 로직 ---
def main():
    st.set_page_config(page_title="MBTI 심층 분석", page_icon="🔬", layout="wide")
    st.title("🔬 MBTI 심층 분석 및 직업 탐색")
    st.markdown("---")

    if 'mbti_result' not in st.session_state or not mbti_details_data: # 데이터 로드 실패 시 검사 화면으로
        if not mbti_details_data:
             st.error("MBTI 데이터를 불러오는데 실패했습니다. 앱을 정상적으로 실행할 수 없습니다.")
        run_mbti_test()
    else:
        user_mbti = st.session_state.mbti_result
        user_scores = st.session_state.get('mbti_scores', {}) # 점수 가져오기, 없으면 빈 딕셔너리
        
        display_mbti_results(user_mbti, user_scores)

        st.markdown("---")
        if st.button("🔄 MBTI 검사 다시하기", use_container_width=True):
            # 세션 상태 초기화
            keys_to_delete = ['mbti_result', 'mbti_scores']
            for key in keys_to_delete:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun() # st.experimental_rerun() 대신 st.rerun() 사용

    st.markdown("---")
    st.caption("본 MBTI 분석 정보는 일반적인 경향성을 바탕으로 하며, 개인의 특성은 다를 수 있습니다. 자기 이해를 위한 참고 자료로 활용하시기 바랍니다.")

if __name__ == "__main__":
    main()
