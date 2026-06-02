import streamlit as st
from google import genai
from google.genai import types

# ---------------------------------
# 페이지 설정
# ---------------------------------
st.set_page_config(
    page_title="Love & Glow Coach",
    page_icon="💖",
    layout="centered"
)

st.title("💖 Love & Glow Coach")
st.caption("연애상담 · 헤어 · 패션 · 메이크업 · 자기관리")

# ---------------------------------
# Gemini API Key
# ---------------------------------
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error(
        "GEMINI_API_KEY가 설정되지 않았습니다.\n\n"
        "Streamlit Secrets에 API 키를 등록해주세요."
    )
    st.stop()

# ---------------------------------
# Gemini Client
# ---------------------------------
try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"Gemini 초기화 실패: {e}")
    st.stop()

# ---------------------------------
# 시스템 프롬프트
# ---------------------------------
SYSTEM_PROMPT = """
너는 'Love & Glow Coach'라는 AI 챗봇이다.

전문 분야:
1. 연애 상담
2. 썸 상담
3. 이별 상담
4. 자기관리
5. 글로우업
6. 헤어스타일 추천
7. 패션 스타일링
8. 메이크업 팁
9. 피부 관리
10. 자신감 향상

규칙:
- 친절하고 공감하는 말투 사용
- 현실적인 조언 제공
- 사용자를 비난하지 않음
- 단계별로 설명
- 연애 문제는 감정 공감 후 조언
- 외모 관련 질문은 건강하고 긍정적인 방향으로 답변
- 위험하거나 유해한 미용법은 추천하지 않음

답변 스타일:
- 읽기 쉽게 작성
- 적절한 이모지 사용
- 너무 길지 않게 작성
"""

# ---------------------------------
# 세션 상태
# ---------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------
# 이전 대화 출력
# ---------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------
# 채팅 입력
# ---------------------------------
prompt = st.chat_input(
    "연애 고민이나 글로우업 고민을 입력하세요..."
)

if prompt:

    # 사용자 메시지 저장
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        try:

            # 대화 기록 구성
            conversation = ""

            for m in st.session_state.messages:
                role = "사용자" if m["role"] == "user" else "AI"
                conversation += f"{role}: {m['content']}\n"

            final_prompt = f"""
{SYSTEM_PROMPT}

현재까지 대화:

{conversation}

AI 답변:
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=final_prompt,
                config=types.GenerateContentConfig(
                    temperature=0.8,
                    max_output_tokens=800,
                )
            )

            answer = response.text

            st.markdown(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:

            error_msg = f"""
❌ 오류가 발생했습니다.

오류 내용:
{str(e)}

잠시 후 다시 시도해주세요.
"""

            st.error(error_msg)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_msg
                }
            )

# ---------------------------------
# 사이드바
# ---------------------------------
with st.sidebar:

    st.header("✨ Love & Glow Coach")

    st.write(
        "연애와 자기관리를 함께 도와주는 AI 코치"
    )

    if st.button("🗑️ 대화 초기화"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("💡 질문 예시")

    st.markdown("""
- 썸남이 갑자기 연락이 줄었어
- 전애인이 자꾸 생각나
- 고백해도 될까?
- 장거리 연애 잘하는 법 알려줘
- 내 얼굴형에 맞는 헤어 추천해줘
- 여름 남친룩 추천해줘
- 초보 메이크업 순서 알려줘
- 피부 좋아지는 습관 알려줘
    st.markdown("""
<link href="https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2107@1.1/Cafe24Ssurround.css" rel="stylesheet">

<style>

/* 전체 페이지 */
.stApp {
    background: linear-gradient(
        180deg,
        #dff6ff 0%,
        #f4fbff 50%,
        #ffffff 100%
    );
}

/* 전체 폰트 */
html, body, [class*="css"] {
    font-family: 'Cafe24Ssurround', sans-serif;
}

/* 상단 제목 */
h1 {
    color: #ff6fa8;
    text-align: center;
    font-size: 2.3rem;
    font-weight: bold;
    text-shadow: 2px 2px #ffffff;
}

/* 설명글 */
.stCaption {
    text-align: center;
    color: #666666;
}

/* 채팅 말풍선 공통 */
[data-testid="stChatMessage"] {
    border-radius: 25px;
    padding: 12px 16px;
    margin-bottom: 12px;
    border: 2px solid #d8ecff;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

/* 사용자 말풍선 */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background-color: #ffeef5;
    border-color: #ffcde1;
}

/* 챗봇 말풍선 */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background-color: #eef8ff;
    border-color: #cde8ff;
}

/* 입력창 */
[data-testid="stChatInput"] {
    border-radius: 30px;
}

/* 버튼 */
.stButton button {
    border-radius: 20px;
    background-color: #9ed8ff;
    color: white;
    border: none;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #7ec8ff;
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background-color: #eaf7ff;
    border-right: 3px solid #d4ecff;
}

/* 사이드바 제목 */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #4d92c7;
}

/* 스크롤바 */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #f5fbff;
}

::-webkit-scrollbar-thumb {
    background: #b7deff;
    border-radius: 20px;
}

/* 채팅 영역 */
.main .block-container {
    padding-top: 2rem;
    max-width: 900px;
}

/* 싸이월드 느낌 카드 */
.cyworld-box {
    background: white;
    border: 2px solid #cfe8ff;
    border-radius: 20px;
    padding: 15px;
    margin: 10px 0;
}

/* 반짝이는 포인트 컬러 */
.pink {
    color: #ff74a6;
}

.blue {
    color: #6db8ff;
}

</style>
""", unsafe_allow_html=True)

st.title("🌸 오늘의 다이어리 🌸")
st.caption("연애 · 스타일 · 글로우업 고민을 편하게 이야기해보세요")
