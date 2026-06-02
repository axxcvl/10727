import streamlit as st
from google import genai
from google.genai import types

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="오늘의 다이어리",
    page_icon="🌸",
    layout="centered"
)

# -----------------------------
# 싸이월드 감성 스타일
# -----------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Gaegu', cursive;
}

.stApp {
    background: linear-gradient(
        180deg,
        #dff6ff 0%,
        #f6fcff 50%,
        #ffffff 100%
    );
}

h1 {
    text-align:center;
    color:#ff75a0;
    font-weight:bold;
}

[data-testid="stChatMessage"]{
    border-radius:20px;
    padding:12px;
    margin-bottom:10px;
    box-shadow:0 2px 8px rgba(0,0,0,0.05);
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]){
    background:#ffeef5;
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]){
    background:#eef7ff;
}

.stButton button{
    border-radius:20px;
    background:#8fd3ff;
    color:white;
    border:none;
}

.stButton button:hover{
    background:#72c3ff;
}

section[data-testid="stSidebar"]{
    background:#eaf7ff;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.title("🌸 오늘의 다이어리 🌸")
st.caption("연애 · 스타일 · 글로우업 고민을 편하게 이야기해보세요")

# -----------------------------
# API 키
# -----------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("Secrets에 GEMINI_API_KEY를 등록해주세요.")
    st.stop()

# -----------------------------
# Gemini 클라이언트
# -----------------------------
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Gemini 초기화 실패: {e}")
    st.stop()

# -----------------------------
# 시스템 프롬프트
# -----------------------------
SYSTEM_PROMPT = """
너는 친한 친구처럼 고민을 들어주는 챗봇이다.

주요 역할
- 연애 상담
- 썸 상담
- 이별 상담
- 인간관계 고민
- 글로우업
- 패션 스타일링
- 헤어스타일 추천
- 메이크업 팁
- 피부관리
- 자신감 향상

답변 규칙

1. 사용자의 감정을 먼저 이해한다.
2. 현실적이고 도움이 되는 조언을 제공한다.
3. 외모를 비하하거나 비교하지 않는다.
4. 건강한 자기관리를 우선한다.
5. 짧고 읽기 쉽게 답변한다.
6. 친구처럼 자연스럽게 말한다.
7. 적당한 이모지 사용 가능.
8. 모르는 내용은 추측하지 않는다.

답변은 따뜻하고 편안한 느낌으로 작성한다.
"""

# -----------------------------
# 세션 상태
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# 이전 채팅 출력
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# 입력창
# -----------------------------
user_input = st.chat_input(
    "오늘은 어떤 고민이 있어?"
)

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        try:

            history = ""

            for msg in st.session_state.messages:
                role = "사용자" if msg["role"] == "user" else "챗봇"
                history += f"{role}: {msg['content']}\n"

            prompt = f"""
{SYSTEM_PROMPT}

대화 내용:

{history}

챗봇 답변:
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.8,
                    max_output_tokens=800
                )
            )

            answer = response.text

            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:

            error_msg = f"""
❌ 오류가 발생했어요.

{str(e)}

잠시 후 다시 시도해주세요.
"""

            st.error(error_msg)

# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:

    st.header("💙 Mini Home")

    if st.button("🗑️ 대화 초기화"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown("""
### ✨ 질문 예시

- 썸남이 연락이 줄었어
- 헤어진 전애인이 생각나
- 고백해도 될까?
- 장거리 연애 잘하는 법은?
- 글로우업 하고 싶어
- 내 얼굴형에 맞는 머리 추천해줘
- 여름 코디 추천해줘
- 피부 좋아지는 습관 알려줘
""")
