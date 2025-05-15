import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(page_title="MBTI 직업 추천 웹", page_icon="🧠", layout="wide")

# --- MBTI 검사 페이지 ---
def mbti_test_page():
    st.title("나의 MBTI 유형 찾기")
    st.write("아래 질문에 솔직하게 답변해주세요.")

    # 예시 질문 (실제 검사 질문으로 대체해야 합니다)
    q1_options = {"외향적 (사람들과 어울리는 것을 즐김)": "E", "내향적 (혼자만의 시간을 즐김)": "I"}
    q1_answer = st.radio("1. 당신은 주로 어떤 활동을 통해 에너지를 얻나요?", list(q1_options.keys()))
    user_e_i = q1_options[q1_answer]

    q2_options = {"감각형 (오감을 통해 현재 정보를 받아들임)": "S", "직관형 (육감이나 영감을 통해 미래 가능성을 봄)": "N"}
    q2_answer = st.radio("2. 정보를 인식할 때 어떤 방식을 더 선호하나요?", list(q2_options.keys()))
    user_s_n = q2_options[q2_answer]

    # ... (나머지 질문 T/F, J/P 추가) ...
    # 이 부분은 실제 MBTI 검사 로직으로 채워야 합니다.
    # 간단화를 위해 임의로 유형을 지정합니다. 실제로는 사용자의 답변을 바탕으로 계산해야 합니다.

    if st.button("결과 보기"):
        # 실제로는 계산된 MBTI 결과를 사용해야 합니다.
        # 예시: calculated_mbti = user_e_i + user_s_n + "TF" + "JP" # 실제 계산 로직 필요
        # 여기서는 임의의 결과를 사용합니다.
        if 'mbti_result' not in st.session_state:
            st.session_state.mbti_result = "ISTJ" # 예시 결과

        st.subheader(f"당신의 예상 MBTI 유형은 {st.session_state.mbti_result} 입니다.")
        st.write("이제 'MBTI별 직업 정보' 페이지에서 더 자세한 내용을 확인해보세요!")
        st.session_state.page = "직업 정보" # 페이지 전환을 위한 상태 저장 (멀티페이지 앱의 경우 다르게 처리)


# --- MBTI 유형별 직업 정보 페이지 ---
def job_recommendation_page():
    st.title("MBTI 유형별 추천 직업")

    # MBTI 유형별 직업 정보 (예시 데이터)
    # 실제로는 CSV, JSON 파일 또는 데이터베이스에서 불러오는 것이 좋습니다.
    job_data = {
        "ISTJ": ["회계사", "감사관", "프로젝트 관리자", "공무원", "법률가"],
        "ISFJ": ["간호사", "교사", "사회복지사", "사서", "상담사"],
        "INFJ": ["상담가", "작가", "디자이너", "심리학자", "인사 전문가"],
        "INTJ": ["전략가", "과학자", "엔지니어", "변호사", "개발자"],
        "ISTP": ["엔지니어", "파일럿", "운동선수", "목수", "요리사"],
        "ISFP": ["예술가", "음악가", "패션 디자이너", "수의사", "플로리스트"],
        "INFP": ["작가", "편집자", "심리상담사", "그래픽 디자이너", "사회운동가"],
        "INTP": ["프로그래머", "분석가", "교수", "철학자", "연구원"],
        "ESTP": ["사업가", "마케터", "영업 담당자", "경찰관", "소방관"],
        "ESFP": ["배우", "가수", "이벤트 플래너", "여행 가이드", "고객 서비스 담당자"],
        "ENFP": ["저널리스트", "광고 기획자", "컨설턴트", "배우", "기업가"],
        "ENTP": ["발명가", "변호사", "컨설턴트", "정치인", "마케팅 디렉터"],
        "ESTJ": ["관리자", "경영자", "감독관", "교장", "판사"],
        "ESFJ": ["교사", "인사 관리자", "행사 기획자", "의료계 종사자", "호텔리어"],
        "ENFJ": ["교사", "상담가", "인사 책임자", "사회복지사", "정치인"],
        "ENTJ": ["CEO", "임원", "변호사", "경영 컨설턴트", "기업가"]
    }

    # 세션 상태에서 MBTI 결과 가져오기
    user_mbti = st.session_state.get('mbti_result', None)

    if user_mbti:
        st.subheader(f"'{user_mbti}' 유형에게 추천하는 직업:")
        if user_mbti in job_data:
            for job in job_data[user_mbti]:
                st.markdown(f"- {job}")
        else:
            st.write("해당 MBTI 유형에 대한 직업 정보가 아직 준비되지 않았습니다.")
    else:
        st.write("먼저 'MBTI 검사'를 진행해주세요.")
        if st.button("MBTI 검사하러 가기"):
            st.session_state.page = "MBTI 검사" # 페이지 전환

# --- 사이드바를 사용한 페이지 네비게이션 (간단한 멀티페이지 구현) ---
# Streamlit 1.10.0 이상에서는 pages/ 폴더를 사용한 멀티페이지 앱이 더 권장됩니다.
# 여기서는 간단한 세션 상태를 이용한 페이지 전환 예시입니다.
if 'page' not in st.session_state:
    st.session_state.page = "MBTI 검사"

if st.session_state.page == "MBTI 검사":
    mbti_test_page()
elif st.session_state.page == "직업 정보":
    job_recommendation_page()

# --- 사이드바 메뉴 (좀 더 나은 방법은 pages/ 폴더 사용) ---
st.sidebar.title("메뉴")
if st.sidebar.button("MBTI 검사"):
    st.session_state.page = "MBTI 검사"
    # st.experimental_rerun() # 페이지 즉시 새로고침 (필요에 따라)
if st.sidebar.button("MBTI별 직업 정보"):
    if 'mbti_result' in st.session_state : # 검사를 먼저 하도록 유도
        st.session_state.page = "직업 정보"
        # st.experimental_rerun()
    else:
        st.sidebar.warning("MBTI 검사를 먼저 진행해주세요.")
