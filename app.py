import streamlit as st
st.title('연애 코칭 웹앱')
st.write('2026')
import streamlit as st
from datetime import datetime
import random
# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="버디러브 💖",
    page_icon="💌",
    layout="wide"
)

# -----------------------------------
# 레트로 감성 CSS
# -----------------------------------
st.markdown("""
<style>
@font-face {
    font-family: 'Ownglyph_Nana';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2202@1.0/Ownglyph_Nana-Rg.woff') format('woff');
}

html, body, [class*="css"] {
    font-family: 'Ownglyph_Nana';
}

.stApp {
    background: linear-gradient(to bottom, #fff0f7, #ffe5f1);
}

/* 상단 타이틀 */
.main-title {
    text-align: center;
    font-size: 70px;
    color: #ff4fa3;
    font-weight: bold;
    text-shadow: 3px 3px #ffffff;
}

.sub-title {
    text-align: center;
    color: #ff7eb8;
    font-size: 24px;
    margin-bottom: 20px;
}

/* 카드 */
.card {
    background: white;
    padding: 20px;
    border-radius: 25px;
    border: 3px solid #ffc7df;
    box-shadow: 0px 4px 10px rgba(255,105,180,0.2);
    margin-bottom: 20px;
}

/* 채팅 */
.user-msg {
    background: #d8fff0;
    padding: 14px;
    border-radius: 18px;
    margin: 10px 0;
    border: 2px solid #9df5d5;
    font-size: 22px;
}

.ai-msg {
    background: #ffe0ef;
    padding: 14px;
    border-radius: 18px;
    margin: 10px 0;
    border: 2px solid #ffb8d5;
    font-size: 22px;
}

/* 버튼 */
.stButton > button {
    background: linear-gradient(to right, #ff7eb8, #ffb6d9);
    color: white;
    border: none;
    border-radius: 15px;
    padding: 12px 20px;
    font-size: 24px;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(to right, #ff5fa2, #ff9ac7);
}

/* 입력창 */
textarea {
    border-radius: 15px !important;
    border: 3px solid #ffc2de !important;
    font-size: 22px !important;
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #ffe8f3, #ffd7ea);
}

/* 상태 */
.status-box {
    background: #fff;
    padding: 12px;
    border-radius: 15px;
    border: 2px dashed #ff99c8;
    text-align: center;
    margin-bottom: 15px;
}

/* 음악 카드 */
.music-card {
    background: #fff8fc;
    padding: 12px;
    border-radius: 15px;
    border: 2px solid #ffc2de;
    margin-bottom: 10px;
}

/* 반짝 */
.blink {
    animation: blink-animation 1.5s infinite;
}

@keyframes blink-animation {
    50% {
        opacity: 0.5;
    }
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# 세션 상태
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# 랜덤 데이터
# -----------------------------------
love_quotes = [
    "사랑은 타이밍이래 💖",
    "오늘은 먼저 연락해보는 건 어때? ✨",
    "두근거림은 시작의 신호 🌸",
    "너의 매력은 생각보다 훨씬 커 😊",
    "썸은 작은 관심에서 시작돼 💌"
]

bgm_list = [
    "🎵 아이유 - 좋은날",
    "🎵 SG워너비 - Timeless",
    "🎵 버즈 - 겁쟁이",
    "🎵 소녀시대 - Kissing You",
    "🎵 NewJeans - Ditto"
]

reply_list = [
    "나도 너랑 얘기하면 기분 좋아 😊",
    "오늘 하루 어땠어? 💖",
    "답장 기다리고 있었어 😳",
    "다음엔 같이 가자 🌸",
    "너랑 있으면 편해 ✨"
]

mbti_love = {
    "INFP": "감성적인 사랑꾼 💖",
    "ENFP": "설렘 가득 직진형 🌸",
    "INTJ": "츤데레 스타일 😎",
    "ESFJ": "다정다감 케어형 🥰"
}

# -----------------------------------
# 사이드바
# -----------------------------------
with st.sidebar:

    st.markdown("# 💖 버디러브")

    st.markdown("""
    <div class='status-box blink'>
    🟢 접속중
    </div>
    """, unsafe_allow_html=True)

    nickname = st.text_input("💌 닉네임", value="핑크토끼")

    mood = st.selectbox(
        "🌈 오늘 기분",
        ["설렘", "짝사랑", "썸", "재회", "연애중", "이별"]
    )

    mbti = st.selectbox(
        "✨ MBTI",
        ["INFP", "ENFP", "INTJ", "ESFJ"]
    )

    st.markdown("---")

    st.markdown("## 💬 상태메시지")

    status_msg = st.text_input(
        "",
        value="너만 보면 심장이 두근💖"
    )

    st.markdown("---")

    st.markdown("## 🎵 오늘의 BGM")

    for _ in range(3):
        st.markdown(
            f"""
            <div class='music-card'>
            {random.choice(bgm_list)}
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------------
# 상단 헤더
# -----------------------------------
st.markdown(
    """
    <div class='main-title'>
    💖 버디러브 💖
    </div>
    <div class='sub-title'>
    버디버디 감성 연애 코칭 공간 🌸
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# 상단 카드
# -----------------------------------
colA, colB, colC = st.columns(3)

with colA:
    st.markdown(
        f"""
        <div class='card'>
        <h2>🌈 오늘 기분</h2>
        <h1>{mood}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with colB:
    love_score = random.randint(70, 99)

    st.markdown(
        f"""
        <div class='card'>
        <h2>💘 연애운</h2>
        <h1>{love_score}점</h1>
        오늘은 연락운 상승✨
        </div>
        """,
        unsafe_allow_html=True
    )

with colC:
    st.markdown(
        f"""
        <div class='card'>
        <h2>✨ MBTI 연애스타일</h2>
        <h3>{mbti_love[mbti]}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------
# 메인 레이아웃
# -----------------------------------
left, right = st.columns([2, 1])

# -----------------------------------
# 채팅
# -----------------------------------
with left:

    st.markdown("## 💬 연애 상담 채팅")

    user_input = st.text_area(
        "고민 입력",
        placeholder="예: 썸남이 답장이 느린데 관심 없는 걸까?"
    )

    if st.button("💌 상담받기"):

        if user_input.strip() != "":

            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            ai_reply = random.choice([
                "상대도 조심스럽게 다가오는 중일 수 있어 💖",
                "답장 속도보다 대화의 분위기가 더 중요해 😊",
                "지금은 자연스럽게 가까워지는 흐름 같아 ✨",
                "너무 불안해하지 않아도 괜찮아 🌸",
                "상대도 너를 신경 쓰고 있는 것 같아 👀"
            ])

            st.session_state.messages.append({
                "role": "assistant",
                "content": ai_reply
            })

    # 채팅 출력
    for msg in st.session_state.messages:

        if msg["role"] == "user":

            st.markdown(
                f"""
                <div class='user-msg'>
                🧑 {nickname}<br><br>
                {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class='ai-msg'>
                💖 연애코치 루나<br><br>
                {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

# -----------------------------------
# 우측 패널
# -----------------------------------
with right:

    st.markdown("## 🌸 오늘의 한마디")

    st.markdown(
        f"""
        <div class='card'>
        <h2>{random.choice(love_quotes)}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 💌 추천 답장")

    st.markdown(
        f"""
        <div class='card'>
        <h2>{random.choice(reply_list)}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🕒 현재 시간")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    st.markdown(
        f"""
        <div class='card'>
        <h2>{now}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🌟 오늘의 인기 고민")

    고민목록 = [
        "썸남 답장 느릴 때",
        "재회 가능성 있을까?",
        "읽씹 후 연락법",
        "고백 타이밍",
        "짝사랑 성공법"
    ]

    for 고민 in 고민목록:
        st.markdown(
            f"""
            <div class='music-card'>
            💭 {고민}
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------------
# 하단
# -----------------------------------
st.markdown("---")

st.markdown(
    """
    <center>
    <h3 style='color:#ff69b4;'>
    💖 BuddyLove Retro Edition 💖
    </h3>
    <p style='font-size:22px; color:#ff8ab8;'>
    버디버디 + 싸이월드 감성 연애 웹앱 🌸
    </p>
    </center>
    """,
    unsafe_allow_html=True
)
