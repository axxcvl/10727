import streamlit as st
import random
from datetime import datetime
# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="AeroTune 🌈",
    page_icon="🎧",
    layout="wide"
)

# -----------------------------------
# CSS (Frutiger Aero 스타일)
# -----------------------------------
st.markdown("""
<style>

/* 귀여운 옛날 감성 글씨체 */
@font-face {
    font-family: 'Ownglyph_Nana';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2202@1.0/Ownglyph_Nana-Rg.woff') format('woff');
}

html, body, [class*="css"] {
    font-family: 'Ownglyph_Nana';
}

/* 배경 */
.stApp {
    background:
    linear-gradient(to bottom, rgba(255,255,255,0.6), rgba(255,255,255,0.2)),
    url('https://images.unsplash.com/photo-1519608487953-e999c86e7455?q=80&w=1920&auto=format&fit=crop');
    background-size: cover;
    background-attachment: fixed;
}

/* 상단 타이틀 */
.main-title {
    text-align: center;
    font-size: 75px;
    color: white;
    text-shadow:
        0px 0px 10px #7df9ff,
        0px 0px 20px #7df9ff,
        3px 3px 0px rgba(0,0,0,0.2);
    margin-top: 10px;
}

.sub-title {
    text-align: center;
    color: white;
    font-size: 28px;
    text-shadow: 0px 0px 8px #7df9ff;
    margin-bottom: 30px;
}

/* 유리 카드 */
.glass-card {
    background: rgba(255,255,255,0.35);
    backdrop-filter: blur(12px);
    border-radius: 30px;
    padding: 20px;
    border: 2px solid rgba(255,255,255,0.5);
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}

/* 플레이리스트 카드 */
.song-card {
    background: rgba(255,255,255,0.45);
    backdrop-filter: blur(10px);
    padding: 15px;
    border-radius: 20px;
    margin-bottom: 12px;
    border: 2px solid rgba(255,255,255,0.5);
    color: #004d66;
    font-size: 24px;
}

/* 입력창 */
textarea, input {
    border-radius: 20px !important;
    border: 2px solid #8ffcff !important;
    background: rgba(255,255,255,0.7) !important;
    font-size: 22px !important;
}

/* 버튼 */
.stButton > button {
    background: linear-gradient(to right, #7df9ff, #9effd9);
    color: #005f73;
    border: none;
    border-radius: 20px;
    padding: 12px 20px;
    font-size: 24px;
    font-weight: bold;
    box-shadow: 0px 0px 15px rgba(125,249,255,0.8);
}

.stButton > button:hover {
    background: linear-gradient(to right, #9effff, #b8fff0);
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #dffcff, #c6fff1);
}

/* 상태 */
.status {
    color: #00bcd4;
    font-size: 22px;
    text-align: center;
}

/* 반짝 애니메이션 */
.glow {
    animation: glow-animation 2s infinite alternate;
}

@keyframes glow-animation {
    from {
        text-shadow: 0px 0px 10px #7df9ff;
    }
    to {
        text-shadow: 0px 0px 25px #b2ffff;
    }
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# 세션 상태
# -----------------------------------
if "playlist" not in st.session_state:
    st.session_state.playlist = [
        {
            "user": "민트별",
            "song": "🎵 NewJeans - Ditto"
        },
        {
            "user": "핑크구름",
            "song": "🎵 아이유 - 좋은날"
        }
    ]

# -----------------------------------
# 랜덤 감성 문구
# -----------------------------------
aero_quotes = [
    "음악은 우리의 우주야 🌍",
    "오늘의 감정은 어떤 노래야? 🎧",
    "플레이리스트로 마음을 공유해 💿",
    "반짝이는 추억을 저장중... ✨",
    "지금 듣는 노래가 네 분위기야 🌈"
]

# -----------------------------------
# 사이드바
# -----------------------------------
with st.sidebar:

    st.markdown("# 🌈 AeroTune")

    st.markdown(
        """
        <div class='glass-card'>
        💿 Frutiger Aero Music Community
        </div>
        """,
        unsafe_allow_html=True
    )

    nickname = st.text_input(
        "🌸 닉네임",
        value="하늘소녀"
    )

    mood = st.selectbox(
        "🎧 지금 기분",
        ["몽글몽글", "새벽감성", "짝사랑", "비오는날", "행복", "우주여행"]
    )

    st.markdown("---")

    st.markdown(
        f"""
        <div class='status glow'>
        🟢 {nickname} 접속중
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------
# 상단 헤더
# -----------------------------------
st.markdown(
    """
    <div class='main-title glow'>
    🌈 AeroTune 🎧
    </div>

    <div class='sub-title'>
    프루티거에어로 감성 플레이리스트 공유 공간 💿
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# 상단 카드
# -----------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class='glass-card'>
        <h2>🎧 현재 기분</h2>
        <h1>{mood}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    random_temp = random.randint(18, 28)

    st.markdown(
        f"""
        <div class='glass-card'>
        <h2>☁️ 감성 온도</h2>
        <h1>{random_temp}°</h1>
        몽글몽글한 하루 🌈
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        f"""
        <div class='glass-card'>
        <h2>✨ 오늘의 문장</h2>
        <h3>{random.choice(aero_quotes)}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------
# 메인 레이아웃
# -----------------------------------
left, right = st.columns([2, 1])

# -----------------------------------
# 플레이리스트 공유
# -----------------------------------
with left:

    st.markdown("## 💿 플레이리스트 공유")

    song_input = st.text_input(
        "🎵 좋아하는 노래 공유하기",
        placeholder="예: NewJeans - Ditto"
    )

    if st.button("✨ 플레이리스트 추가"):

        if song_input.strip() != "":

            st.session_state.playlist.insert(0, {
                "user": nickname,
                "song": f"🎵 {song_input}"
            })

    st.markdown("---")

    for item in st.session_state.playlist:

        st.markdown(
            f"""
            <div class='song-card'>
            🌸 {item['user']}<br><br>
            {item['song']}
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------------
# 우측 패널
# -----------------------------------
with right:

    st.markdown("## 🌈 지금 인기 분위기")

    moods = [
        "☁️ 새벽감성",
        "🌸 벚꽃플리",
        "💿 Y2K",
        "🫧 몽환",
        "🌧 비오는날"
    ]

    for m in moods:

        st.markdown(
            f"""
            <div class='glass-card'>
            <h3>{m}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("## 🕒 현재 시간")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    st.markdown(
        f"""
        <div class='glass-card'>
        <h2>{now}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 💬 오늘의 한마디")

    st.markdown(
        f"""
        <div class='glass-card'>
        <h2>{random.choice(aero_quotes)}</h2>
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
    <h2 style='color:white; text-shadow:0px 0px 15px #7df9ff;'>
    🌈 AeroTune Community 🌈
    </h2>

    <p style='font-size:24px; color:white;'>
    프루티거에어로 + Y2K + MSN 메신저 감성 🎧
    </p>
    </center>
    """,
    unsafe_allow_html=True
)
