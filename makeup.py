import streamlit as st
from PIL import Image
import random

st.set_page_config(
    page_title="💖 화장법 연구소",
    page_icon="💄",
    layout="wide"
)

# --------------------
# CSS
# --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Gaegu', cursive !important;
}

.stApp{
    background: linear-gradient(to bottom,#ffeaf5,#fff8fb);
}

.main-title{
    text-align:center;
    font-size:55px;
    color:#ff5da2;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    font-size:25px;
    color:#666;
}

.cyworld-box{
    background:white;
    padding:20px;
    border-radius:20px;
    border:4px solid #ffb6d9;
    box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
}

.result-box{
    background:#fff4fa;
    padding:25px;
    border-radius:20px;
    border:3px dashed #ff82bf;
    font-size:22px;
}

.library-card{
    background:white;
    border-radius:20px;
    padding:20px;
    border:3px solid pink;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# --------------------
# 데이터
# --------------------

MAKEUP_LIBRARY = {
    "🌸 청순 메이크업":
    """
    • 핑크 베이스
    • 자연스러운 눈매
    • 코랄 립
    • 투명한 피부 표현
    """,

    "💕 러블리 메이크업":
    """
    • 핑크 블러셔
    • 반짝이 애교살
    • 글로시 립
    • 사랑스러운 분위기
    """,

    "🖤 스모키 메이크업":
    """
    • 스모키 아이
    • 또렷한 쉐딩
    • 매트 립
    • 강렬한 분위기
    """,

    "☀️ 데일리 메이크업":
    """
    • 브라운 음영
    • 자연스러운 피부
    • MLBB 립
    • 직장/학교 추천
    """,

    "👰 웨딩 메이크업":
    """
    • 화사한 피부
    • 은은한 펄
    • 코랄핑크 립
    • 사진발 최고
    """,

    "✨ 파티 메이크업":
    """
    • 글리터 섀도우
    • 하이라이터 강조
    • 선명한 립 컬러
    • 화려한 분위기
    """
}

# --------------------
# 추천 함수
# --------------------

def recommend_makeup(
        skin_tone,
        skin_condition,
        eye_type,
        lip_type,
        face_shape):

    result = []

    if skin_tone == "밝음":
        result.append("🌸 로즈핑크, 코랄 계열 추천")

    elif skin_tone == "중간":
        result.append("☀️ 피치, 살구 계열 추천")

    else:
        result.append("🧡 브론즈, 딥코랄 계열 추천")

    if skin_condition == "건성":
        result.append("💧 글로우 쿠션 사용")

    elif skin_condition == "지성":
        result.append("🧴 세미매트 파운데이션 추천")

    else:
        result.append("✨ 촉촉한 세미글로우 피부 표현")

    if eye_type == "작음":
        result.append("👁️ 애교살 + 트임 메이크업")

    elif eye_type == "큼":
        result.append("🌟 음영 중심 아이메이크업")

    if lip_type == "얇음":
        result.append("💋 글로시 립으로 볼륨 연출")

    else:
        result.append("❤️ 틴트 그라데이션 추천")

    if face_shape == "둥근형":
        result.append("📐 쉐딩 강조")

    elif face_shape == "긴형":
        result.append("🌷 가로 블러셔 추천")

    else:
        result.append("✨ 자연스러운 입체 메이크업")

    return result

# --------------------
# 헤더
# --------------------

st.markdown(
    "<div class='main-title'>💄 화장법 연구소 💖</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>오늘 나에게 어울리는 메이크업 찾기 ✨</div>",
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs([
    "📷 얼굴 인식",
    "💄 얼굴 진단받기",
    "makeup library"
])

# --------------------
# 얼굴 인식
# --------------------

with tab1:

    st.markdown("### 📷 얼굴 인식 카메라")

    photo = st.camera_input("사진 찍기")

    if photo is not None:

        image = Image.open(photo)

        st.image(
            image,
            caption="촬영된 얼굴",
            use_container_width=True
        )

        st.success(
            "얼굴 사진이 등록되었습니다!\n\n"
            "실제 AI 얼굴 분석 대신 안전하고 무료로 사용할 수 있도록 "
            "설문 기반 진단과 함께 활용됩니다."
        )

# --------------------
# 진단
# --------------------

with tab2:

    st.markdown("### 얼굴 진단받기")

    skin_tone = st.selectbox(
        "피부톤",
        ["밝음","중간","어두움"]
    )

    skin_condition = st.selectbox(
        "피부 상태",
        ["건성","지성","복합성"]
    )

    eye_type = st.selectbox(
        "눈 크기",
        ["작음","보통","큼"]
    )

    lip_type = st.selectbox(
        "입술 두께",
        ["얇음","보통","도톰"]
    )

    face_shape = st.selectbox(
        "얼굴형",
        ["둥근형","계란형","긴형"]
    )

    if st.button("✨ 나에게 어울리는 화장법 찾기"):

        result = recommend_makeup(
            skin_tone,
            skin_condition,
            eye_type,
            lip_type,
            face_shape
        )

        mood = random.choice([
            "청순 메이크업",
            "러블리 메이크업",
            "구운 메이크업",
            "데일리 메이크업"
        ])

        st.markdown(
            f"""
            <div class='result-box'>
            <h2> 추천 결과</h2>

            추천 컨셉 :
            <b>{mood}</b>

            <br><br>

            {'<br>'.join(result)}

            </div>
            """,
            unsafe_allow_html=True
        )

# --------------------
# 라이브러리
# --------------------

with tab3:

    st.markdown("## makeup library")

    cols = st.columns(2)

    items = list(MAKEUP_LIBRARY.items())

    for i, (title, desc) in enumerate(items):

        with cols[i % 2]:

            st.markdown(
                f"""
                <div class='library-card'>
                <h3>{title}</h3>
                <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")
