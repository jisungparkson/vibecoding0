import streamlit as st

# --- 페이지 설정 ----
st.set_page_config(page_title="MBTI 맞춤 커리어 나침반", page_icon="🧭", layout="centered")

# --- 데이터 ----
MBTI_LIST = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

MBTI_DESCRIPTIONS = {
    "INTJ": "**전략가형 (The Architect)**\n\n상상력이 풍부하며 철두철미한 계획을 세우는 전략가형입니다. 모든 일에 계획을 세우고 상상력을 발휘하여 목표를 달성합니다. 독립적이고 분석적이며, 복잡한 문제를 해결하는 데 능숙합니다.",
    "INTP": "**논리술사형 (The Logician)**\n\n끊임없이 새로운 지식에 목말라 하는 혁신가형입니다. 논리적이고 분석적이며, 독창적인 아이디어를 탐구하는 것을 즐깁니다. 지적 호기심이 강하고, 복잡한 이론을 이해하는 데 뛰어납니다.",
    "ENTJ": "**통솔자형 (The Commander)**\n\n대담하면서도 상상력이 풍부한 강한 의지의 지도자형입니다. 다양한 방법을 모색하거나 여의치 않을 경우 새로운 방안을 창출합니다. 타고난 리더십과 결단력으로 목표를 추진하며, 조직을 이끄는 데 능합니다.",
    "ENTP": "**변론가형 (The Debater)**\n\n지적인 도전을 두려워하지 않는 똑똑한 호기심형입니다. 새로운 아이디어를 탐구하고 논쟁하는 것을 즐깁니다. 재치 있고 창의적이며, 기존의 방식에 의문을 제기하며 혁신을 추구합니다.",
    "INFJ": "**옹호자형 (The Advocate)**\n\n조용하고 신비로우며 샘솟는 영감으로 지칠 줄 모르는 이상주의자입니다. 깊은 통찰력과 공감 능력을 바탕으로 다른 사람을 돕고자 합니다. 강한 신념을 가지고 있으며, 세상을 더 나은 곳으로 만들고자 노력합니다.",
    "INFP": "**중재자형 (The Mediator)**\n\n상냥한 성격의 이타주의자로 건강하고 밝은 사회 건설에 앞장서는 낭만형입니다. 진실함과 연민을 중요시하며, 자신의 가치관에 따라 살아갑니다. 창의적이고 이상적이며, 다른 사람의 감정에 깊이 공감합니다.",
    "ENFJ": "**선도자형 (The Protagonist)**\n\n넘치는 카리스마와 영향력으로 청중을 압도하는 리더형입니다. 사람들에게 영감을 주고 긍정적인 변화를 이끌어내는 데 열정적입니다. 사교적이고 공감 능력이 뛰어나며, 타인의 성장을 돕는 것을 중요하게 생각합니다.",
    "ENFP": "**활동가형 (The Campaigner)**\n\n창의적이며 항상 웃을 거리를 찾아다니는 활발한 성격으로 사람들과 자유롭게 어울리기를 좋아하는 사교형입니다. 열정적이고 상상력이 풍부하며, 새로운 가능성을 탐색하는 것을 즐깁니다. 긍정적이고 에너지가 넘칩니다.",
    "ISTJ": "**현실주의자형 (The Logistician)**\n\n사실에 근거하여 사고하며 이들의 행동이나 결정 사항에 한 치의 의심을 사지 않는 현실주의자형입니다. 책임감이 강하고 조직적이며, 규칙과 절차를 중요시합니다. 신뢰할 수 있고 꼼꼼합니다.",
    "ISFJ": "**수호자형 (The Defender)**\n\n소중한 이들을 방어할 준비가 되어 있는 헌신적이고 따뜻한 수호자형입니다. 타인에 대한 배려심이 깊고 책임감이 강합니다. 안정적이고 실용적이며, 주변 사람들을 돕는 데서 만족을 느낍니다.",
    "ESTJ": "**경영자형 (The Executive)**\n\n사물이나 사람을 관리하는 데 뛰어난 실력을 갖춘 경영자형입니다. 질서와 조직을 중시하며, 효율적으로 일을 처리합니다. 결단력 있고 책임감이 강하며, 전통적인 가치를 존중합니다.",
    "ESFJ": "**집정관형 (The Consul)**\n\n타인을 향한 세심한 관심과 사교적인 성향으로 사람들 내에서 인기가 많으며, 타인을 돕는데 열성적인 세심형입니다. 주변 사람들과의 조화를 중요시하며, 타인의 필요를 채워주는 데 능숙합니다. 친절하고 협조적입니다.",
    "ISTP": "**장인형 (The Virtuoso)**\n\n대담하고 현실적인 성향으로 다양한 도구 사용에 능숙한 탐험형입니다. 손으로 무언가를 만들거나 문제를 해결하는 것을 즐깁니다. 논리적이고 실용적이며, 위기 상황에서 침착하게 대처합니다.",
    "ISFP": "**모험가형 (The Adventurer)**\n\n항상 새로운 것을 찾아 시도하거나 도전할 준비가 되어 있는 융통성 있는 성격의 매력 넘치는 예술가형입니다. 현재를 즐기며, 아름다움과 미적 감각을 중요시합니다. 온화하고 겸손하며, 예술적인 재능을 가진 경우가 많습니다.",
    "ESTP": "**사업가형 (The Entrepreneur)**\n\n명석한 두뇌와 에너지, 그리고 뛰어난 직관력으로 위험을 즐기는 성격의 사업가형입니다. 현실적이고 행동 지향적이며, 새로운 경험과 도전을 즐깁니다. 사교적이고 설득력이 뛰어나며, 문제 해결에 능숙합니다.",
    "ESFP": "**연예인형 (The Entertainer)**\n\n주위에 있으면 인생이 지루할 새가 없을 정도로 즉흥적이며 열정과 에너지가 넘치는 연예인형입니다. 사교적이고 활동적이며, 사람들과 어울리는 것을 좋아합니다. 현재를 즐기고, 다른 사람들에게 즐거움을 선사합니다."
}

JOB_RECOMMENDATIONS = {
    "INTJ": ["데이터 과학자", "전략 컨설턴트", "시스템 엔지니어", "연구 개발 관리자", "투자 분석가", "변리사", "대학교수"],
    "INTP": ["이론 물리학자", "AI 개발자", "UX 디자이너", "소프트웨어 아키텍트", "철학자", "데이터 분석가", "정보 보안 분석가"],
    "ENTJ": ["CEO", "정책 분석가", "경영 컨설턴트", "벤처 캐피탈리스트", "변호사", "기업 임원", "프로덕트 오너"],
    "ENTP": ["창업가", "마케팅 전략가", "프로덕트 매니저", "광고 크리에이터", "정치 컨설턴트", "발명가", "저널리스트"],
    "INFJ": ["상담사", "작가", "사회복지사", "임상 심리사", "특수교육 교사", "UX 리서처", "인사 전문가"],
    "INFP": ["시인", "예술가", "콘텐츠 크리에이터", "그래픽 디자이너", "편집자", "심리 치료사", "사서"],
    "ENFJ": ["교사", "HR 매니저", "심리학자", "기업 코치", "영업 관리자", "비영리 단체 운영자", "커뮤니티 매니저"],
    "ENFP": ["홍보 전문가", "여행작가", "교육 콘텐츠 개발자", "이벤트 기획자", "카피라이터", "아트 디렉터", "상담가"],
    "ISTJ": ["회계사", "공무원", "품질 관리 전문가", "프로젝트 관리자", "법률 사무원", "데이터베이스 관리자", "감리사"],
    "ISFJ": ["간호사", "초등교사", "도서관 사서", "행정 보조원", "영양사", "물리치료사", "수의사 보조"],
    "ESTJ": ["프로젝트 매니저", "행정 공무원", "기업 관리자", "경찰관", "판사", "건설 관리자", "재무 관리자"],
    "ESFJ": ["상담 교사", "사회복지사", "이벤트 플래너", "호텔 지배인", "고객 서비스 매니저", "인사 담당자", "영양사"],
    "ISTP": ["엔지니어", "기계 기술자", "보안 전문가", "파일럿", "소방관", "응급 구조사", "목수"],
    "ISFP": ["플로리스트", "패션 디자이너", "요리사", "사진작가", "음악가", "인테리어 디자이너", "수의사"],
    "ESTP": ["세일즈 전문가", "응급 구조사", "스포츠 코치", "기업가", "부동산 중개인", "경찰 형사", "마케터"],
    "ESFP": ["연예인", "방송인", "뷰티 크리에이터", "행사 MC", "항공 승무원", "피트니스 강사", "파티 플래너"]
}

# --- 스타일 커스터마이징 ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
        body {
            font-family: 'Nanum Gothic', sans-serif;
        }
        .title {
            font-size:42px; /* 살짝 줄임 */
            font-weight:800; /* 굵게 */
            color:#2c3e50;
            text-align:center;
            margin-bottom: 10px; /* 간격 추가 */
            font-family: 'Nanum Gothic', sans-serif;
        }
        .subtitle {
            font-size:18px; /* 살짝 줄임 */
            color:#7f8c8d;
            text-align:center;
            margin-bottom: 30px; /* 간격 추가 */
            font-family: 'Nanum Gothic', sans-serif;
        }
        .mbti-header {
            font-size: 28px;
            font-weight: 700;
            color: #2980b9;
            margin-top: 20px;
            margin-bottom: 10px;
            font-family: 'Nanum Gothic', sans-serif;
        }
        .recommendation-header {
            font-size: 22px;
            font-weight: 700;
            color: #16a085;
            margin-top: 15px;
            margin-bottom: 8px;
            font-family: 'Nanum Gothic', sans-serif;
        }
        .job-item {
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 8px;
            font-size: 16px;
            font-family: 'Nanum Gothic', sans-serif;
        }
        .mbti-description-box {
            background-color: #e8f6f3;
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #1abc9c;
            margin-bottom: 20px;
            font-family: 'Nanum Gothic', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# --- 제목 ---
st.markdown('<div class="title">🧭 MBTI 맞춤 커리어 나침반</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">나의 성향에 딱 맞는 직업을 탐색하고 미래를 설계해 보세요!</div>', unsafe_allow_html=True)
st.markdown("---")

# --- MBTI 선택 ---
selected_mbti = st.selectbox(
    "👇 당신의 MBTI 유형을 선택해 주세요:",
    MBTI_LIST,
    index=None, # 기본 선택 없음
    placeholder="MBTI 유형을 선택하세요..."
)

# --- 결과 출력 ---
if selected_mbti:
    st.markdown(f'<div class="mbti-header">✨ {selected_mbti} 유형 특징 및 추천 직업</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([0.8, 1.2]) # MBTI 설명과 직업 추천 영역 비율 조정

    with col1:
        st.subheader(f"💡 {selected_mbti}는 어떤 유형일까요?")
        mbti_desc = MBTI_DESCRIPTIONS.get(selected_mbti, "해당 MBTI 유형에 대한 설명이 아직 준비되지 않았습니다.")
        st.markdown(f'<div class="mbti-description-box">{mbti_desc}</div>', unsafe_allow_html=True)

    with col2:
        st.subheader("🎯 추천 직업 리스트")
        jobs = JOB_RECOMMENDATIONS.get(selected_mbti, [])
        if jobs:
            for job in jobs:
                st.markdown(f"<div class='job-item'>💼 {job}</div>", unsafe_allow_html=True)
        else:
            st.warning("해당 MBTI 유형에 대한 추천 직업 정보가 아직 없습니다.")

    st.markdown("---")
    st.info("🌟 **팁:** MBTI는 성격 선호도를 나타내는 지표일 뿐, 절대적인 기준은 아니에요. 다양한 가능성을 열어두고 자신에게 맞는 길을 찾아보세요!")
    st.balloons() # 풍선 효과로 변경

else:
    st.info("👆 위에서 MBTI 유형을 선택하면 맞춤 정보를 확인할 수 있습니다.")
    st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80", caption="나에게 맞는 길을 찾아 떠나요!") # 예시 이미지

st.markdown("---")
st.markdown("<div style='text-align: center; color: #888;'>MBTI 정보는 일반적인 성향을 바탕으로 하며, 개인차를 고려하여 참고용으로 활용해 주세요.</div>", unsafe_allow_html=True)
