import streamlit as st
st.title('연애 코칭 웹앱')
st.write('2026')
import streamlit as st
from datetime import datetime
import random
# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="버디러브",
    page_icon="💖",
    layout="wide"
)

# -----------------------------
# CSS 스타일
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #fff5fa;
}

.chat-box {
    background: white;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
    border: 2px solid #ffd6e7;
}

.user-msg {
    background: #d7fff1;
    padding: 10px;
    border-radius: 12px;
    margin: 8px 0;
}

.ai-msg {
    background: #ffe1f0;
    padding: 10px;
    border-radius: 12px;
    margin: 8px 0;
}

.title {
    font-size: 40px;
    color: #ff4fa3;
    font-weight: bold;
}

.status {
    color: #00c48c;
    font-size: 14px;
}

.sidebar .sidebar-content {
    background-color: #ffeef7;
}

.small-text {
    font-size: 13px;
    color: gray;
}

.buddy-card {
    background: white;
    padding: 15px;
    border-radius: 15px;
    border: 2px solid #ffc2dc;
    margin-bottom: 15px;
}

.reply-box {
    background: #fff;
    border: 2px dashed #ff9ec9;
    padding: 10px;
    border-radius: 10px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 세션 상태
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:
    st.markdown("## 💖 버디러브")
    st.markdown("### 🟢 접속중")

    nickname = st.text_input("닉네임", value="핑크토끼")

    mood = st.selectbox(
        "오늘의 기분",
        ["설렘", "짝사랑", "썸", "이별", "재회", "연애 고민"]
    )

    st.markdown("---")

    st.markdown("### 💌 상태메시지")
    status_msg = st.text_input(
        "",
        value="너만 보면 두근두근💖"
    )

    st.markdown("---")

    st.markdown("### 🎵 BGM 추천")
    bgm_list = [
        "아이유 - 좋은날",
        "태연 - 사계",
        "볼빨간사춘기 - 우주를 줄게",
        "NewJeans - Ditto"
    ]

    st.write(random.choice(bgm_list))

# -----------------------------
# 헤더
# -----------------------------
st.markdown(
    f"""
    <div class='title'>💖 버디러브</div>
    <div class='status'>🟢 {nickname}님 접속중</div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# 메인 레이아웃
# -----------------------------
col1, col2 = st.columns([2, 1])

# -----------------------------
# 채팅 영역
# -----------------------------
with col1:

    st.markdown("## 💬 연애 코치 채팅")

    user_input = st.text_area(
        "고민을 입력해보세요",
        placeholder="예: 썸남이 답장이 느린데 관심 없는 걸까?"
    )

    if st.button("💌 상담받기"):

        if user_input.strip() != "":

            # 사용자 메시지 저장
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            # 간단 AI 응답 로직
            ai_replies = [
                "상대가 조심스럽게 다가오는 중일 수도 있어요 💖",
                "답장 속도보다 대화의 질이 더 중요할 수 있어요 😊",
                "너무 불안해하지 말고 여유를 가져보세요 ✨",
                "지금은 밀당보다 자연스러운 대화가 좋아 보여요 🌸",
                "상대도 당신의 반응을 살피는 중일 가능성이 있어요 👀"
            ]

            ai_message = random.choice(ai_replies)

            # AI 메시지 저장
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": ai_message
                }
            )

    # 채팅 출력
    for msg in st.session_state.messages:

        if msg["role"] == "user":
            st.markdown(
                f"""
                <div class='user-msg'>
                🧑 <b>{nickname}</b><br>
                {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                f"""
                <div class='ai-msg'>
                💖 <b>연애코치 </b><br>
                {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

# -----------------------------
# 우측 패널
# -----------------------------
with col2:

    st.markdown("## 🌸 오늘의 연애운")

    love_score = random.randint(60, 99)

    st.markdown(
        f"""
        <div class='buddy-card'>
        💘 연애운 점수<br><br>
        <h1>{love_score}점</h1>
        오늘은 감정 표현이 중요한 날!
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## ✨ 추천 답장")

    recommend_reply = random.choice([
        "나도 너랑 얘기하면 재밌어 😊",
        "오늘 뭐 했어? 궁금하다!",
        "답장 기다렸잖아 😳",
        "다음엔 같이 가자 💖",
        "너랑 있으면 편해 ✨"
    ])

    st.markdown(
        f"""
        <div class='reply-box'>
        {recommend_reply}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 📅 접속 시간")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    st.markdown(
        f"""
        <div class='buddy-card'>
        {now}
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# 하단
# -----------------------------
st.markdown("---")
st.caption("💖 BuddyLove v1.0 | 버디버디 감성 연애 코칭 앱")
