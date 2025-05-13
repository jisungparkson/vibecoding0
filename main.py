import streamlit as st

# 웹앱 제목 설정
st.set_page_config(page_title="MBTI 맞춤 직업 추천", layout="wide") # 페이지 타이틀과 넓은 레이아웃 설정

st.title("💖 MBTI 기반 맞춤 직업 추천 💖")
st.subheader("나의 MBTI를 찾고, 숨겨진 가능성을 발견해보세요! 🚀")

# --- MBTI 검사 안내 ---
st.markdown("## 🔍 나의 MBTI 유형 찾기")
mbti_knowledge = st.radio(
    "자신의 MBTI를 이미 알고 계신가요?",
    ('네, 알고 있어요!', '아니요, 검사해보고 싶어요!'),
    horizontal=True, # 라디오 버튼 가로 정렬
    key="mbti_knowledge_radio"
)

if mbti_knowledge == '아니요, 검사해보고 싶어요!':
    st.info(
        """
        MBTI는 자신을 더 깊이 이해하는 데 도움이 되는 유용한 성격 유형 지표 중 하나예요. 🧭
        아래 버튼을 클릭하여 외부 사이트에서 성격 유형 검사를 진행해 보세요. 
        자신의 MBTI 유형을 확인한 후, 이 페이지로 돌아와서 아래에서 해당 유형을 선택해주시면 됩니다! 😊
        """
    )
    # 외부 링크는 새 탭에서 열리도록 markdown을 사용합니다.
    st.markdown(
        '<a href="https://www.16personalities.com/ko" target="_blank" style="display: inline-block; padding: 10px 20px; background-color: #FF4B4B; color: white; text-align: center; text-decoration: none; border-radius: 5px; font-weight: bold;">✨ 16Personalities 무료 검사하러 가기 (새 창) ✨</a>',
        unsafe_allow_html=True
    )
    st.caption("👆 위 버튼을 클릭하면 검사 사이트로 이동합니다. 검사 후 이 페이지로 돌아와서 결과를 선택해주세요.")
    st.markdown("---") # 구분선

# MBTI 유형 리스트 (표시용 이름)
mbti_types_display = [
    "선택하세요!",
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

# --- MBTI별 직업 추천 데이터 ---
career_recommendations = {
    "INTJ - 용의주도한 전략가": {
        "title": "🎯 INTJ (용의주도한 전략가) 맞춤 추천 직업",
        "summary": "INTJ는 독립적이고 분석적이며, 미래지향적인 사고를 하는 유형입니다. 복잡한 문제를 해결하고 시스템을 개선하는 분야에서 뛰어난 역량을 발휘할 수 있습니다. 논리적이고 효율적인 것을 중요하게 생각하며, 높은 기준을 가지고 목표를 달성하려고 합니다.",
        "careers": [
            {"name": "👩‍💻 프로젝트 관리자", "desc": "장기적인 비전을 가지고 복잡한 프로젝트를 계획하고 실행합니다. 전체 시스템을 보고 개선점을 찾아내는 능력이 탁월합니다."},
            {"name": "🔬 데이터 과학자/분석가", "desc": "방대한 데이터를 논리적으로 분석하여 패턴을 찾고, 이를 바탕으로 전략적 의사결정에 기여합니다."},
            {"name": "🛠️ 시스템 엔지니어/아키텍트", "desc": "복잡한 시스템의 구조를 설계하고 최적화하여 효율성을 극대화합니다."},
            {"name": "⚖️ 변호사 (특히 특허, 기업법)", "desc": "논리적이고 분석적인 능력으로 복잡한 법적 문제를 해결하고, 지적 재산권이나 기업 전략을 다룹니다."}
        ],
        "image_url": "https://images.unsplash.com/photo-1521737852567-6949f3f9f2b5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8c3RyYXRlZ3l8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60" # 예시 이미지
    },
    "INFP - 열정적인 중재자": {
        "title": "🎨 INFP (열정적인 중재자) 맞춤 추천 직업",
        "summary": "INFP는 이상적이고 창의적이며, 자신의 가치와 신념에 따라 행동하는 유형입니다. 사람들에게 긍정적인 영향을 주고, 의미 있는 일을 하는 분야에서 만족감을 느낍니다. 공감 능력이 뛰어나고 타인의 가능성을 믿습니다.",
        "careers": [
            {"name": "✍️ 작가/시나리오 작가/편집자", "desc": "자신의 가치관과 이상을 창의적으로 표현하고, 사람들에게 깊은 영감과 감동을 전달합니다."},
            {"name": "🧑‍🏫 상담사/심리치료사", "desc": "타인의 감정에 깊이 공감하며, 그들의 내적 성장과 문제 해결을 돕는 데 보람을 느낍니다."},
            {"name": "🖼️ 그래픽 디자이너/일러스트레이터", "desc": "독창적인 아이디어와 풍부한 미적 감각으로 시각적인 결과물을 창조하여 메시지를 전달합니다."},
            {"name": "🤝 사회복지사/비영리 단체 활동가", "desc": "타인을 돕고 사회에 긍정적인 변화를 만들고자 하는 열정이 강하며, 소외된 이들을 위해 일합니다."}
        ],
        "image_url": "https://images.unsplash.com/photo-1501523460185-2aa5d2a0f981?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGFydGlzdCUyMGljb258ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60" # 예시 이미지
    },
    "ENFP - 재기발랄한 활동가": {
        "title": "✨ ENFP (재기발랄한 활동가) 맞춤 추천 직업",
        "summary": "ENFP는 열정적이고 상상력이 풍부하며, 새로운 가능성을 탐색하는 것을 즐기는 유형입니다. 사람들과의 관계를 중요하게 생각하고, 긍정적인 에너지가 넘칩니다. 창의적이고 다양한 경험을 할 수 있는 일을 선호합니다.",
        "careers": [
            {"name": "📣 마케터/광고 기획자", "desc": "창의적인 아이디어와 뛰어난 소통 능력으로 사람들의 마음을 사로잡는 캠페인을 기획하고 실행합니다."},
            {"name": "🎉 이벤트 기획자", "desc": "새롭고 흥미로운 아이디어를 현실로 만들며, 사람들에게 즐거운 경험을 선사합니다."},
            {"name": "💡 기업가/스타트업 창업가", "desc": "새로운 아이디어를 발굴하고, 열정적으로 사업을 추진하여 세상에 변화를 만듭니다."},
            {"name": "🎤 저널리스트/리포터", "desc": "다양한 사람들을 만나고 새로운 사실을 탐구하며, 이를 대중에게 알리는 역할을 합니다."}
        ],
        "image_url": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGVvcGxlJTIwdGFsa2luZ3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60" # 예시 이미지
    },
    # --- 다른 MBTI 유형들도 여기에 추가해주세요! ---
}

st.markdown("## 💼 나의 MBTI 선택 및 맞춤 직업 보기")
# 드롭다운 메뉴로 MBTI 선택
selected_mbti_display_name = st.selectbox(
    "MBTI 검사를 하셨거나 이미 알고 계신다면, 당신의 유형을 선택해주세요! 👇",
    mbti_types_display,
    index=0 # 기본적으로 "선택하세요!"가 보이도록
)

# 선택된 MBTI에 따라 결과 출력
if selected_mbti_display_name != "선택하세요!":
    st.success(f"선택하신 MBTI는 🎉 **{selected_mbti_display_name}** 🎉 입니다!")
    st.balloons()

    if selected_mbti_display_name in career_recommendations:
        recommendation = career_recommendations[selected_mbti_display_name]
        
        st.markdown("---")
        
        # 컬럼을 사용해 이미지와 설명을 나란히 배치
        col1, col2 = st.columns([1, 2]) # 이미지 컬럼을 조금 더 작게
        
        with col1:
            if "image_url" in recommendation:
                st.image(recommendation["image_url"], caption=recommendation["title"], use_column_width=True)
            else:
                st.image("https://images.unsplash.com/photo-1531297484001-80022131f5a1?auto=format&fit=crop&w=500&q=60", caption="Recommendation", use_column_width=True) # 기본 이미지

        with col2:
            st.subheader(f"{recommendation['title']} 🌟")
            st.info(recommendation['summary'])
        
        st.markdown("#### <br>💼 추천 직업 목록:", unsafe_allow_html=True) # 제목 앞에 약간의 공백 추가
        
        # 각 직업을 카드 형태로 보여주기 (st.container와 st.markdown 활용)
        for career in recommendation['careers']:
            with st.container():
                st.markdown(f"""
                <div style="border: 1px solid #FFC0CB; border-radius: 10px; padding: 15px; margin-bottom: 10px; background-color: #FFF0F5;">
                    <h5 style="color: #FF1493; margin-bottom: 5px;">{career['name']}</h5>
                    <p style="font-size: 0.9em;">{career['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
                # st.markdown(f"##### {career['name']}")
                # st.markdown(career['desc'])
                # st.markdown("---") # 각 직업 설명 후 구분선 (선택 사항)

    else:
        st.warning("앗! 아직 해당 MBTI에 대한 직업 정보가 준비되지 않았어요. 😢 곧 추가될 예정입니다!")
        st.image("https://images.unsplash.com/photo-1594322436404-5a0526db4d13?auto=format&fit=crop&w=500&q=60", caption="Coming Soon!", use_column_width=True)


else:
    st.info("위에서 MBTI를 선택하면 맞춤 직업 정보를 볼 수 있어요! 😊")


st.markdown("---")
st.markdown("### 💡 앱 활용 Tip!")
st.markdown("""
- 이 앱에서 제공하는 직업 추천은 일반적인 성향에 따른 것이며, 절대적인 기준이 아니에요.
- 가장 중요한 것은 **자신의 흥미, 가치관, 강점**을 깊이 탐색하고, 이를 바탕으로 진로를 결정하는 것입니다.
- 추천된 직업 외에도 다양한 가능성을 열어두고 탐색해 보세요!
- '워크넷', '커리어넷' 등의 진로 정보 사이트에서 더 많은 직업 정보를 얻을 수 있습니다.
- 이 앱이 여러분의 진로 탐색 여정에 작은 영감이 되기를 바랍니다! ✨
""")

# 사이드바
st.sidebar.header("✨ 앱 정보")
st.sidebar.image("https://images.unsplash.com/photo-1551803985-f3c9bf3f563e?auto=format&fit=crop&w=200&q=60", use_column_width=True) # 사이드바에 귀여운 이미지
st.sidebar.info(
    "이 앱은 여러분의 MBTI 유형에 맞는 직업을 추천해 드립니다. "
    "재미로 즐겨주시고, 진로 선택에 작은 영감이 되길 바랍니다! 😊"
)
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by AI & You")
st.sidebar.markdown("MBTI 데이터 출처: 일반적인 MBTI 유형별 특징 및 직업 정보 참고")
