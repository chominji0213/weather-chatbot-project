import streamlit as st
from llm_client import build_agent, ask
import uuid  # thread_id를 고유하게 만들 때 쓸 것

st.title("날씨/생활정보 챗봇")


# 에이전트를 세션당 한 번만 생성하고 재사용
if "agent" not in st.session_state:
    st.session_state.agent = build_agent()


# 이 사용자 세션을 구분할 thread_id도 한 번만 만들어서 저장
#   (매번 새로 만들면 매 질문마다 새 대화방이 되어서 기억을 못 함)
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())


# 화면 표시용 대화 기록도 session_state에 리스트로 준비
if "messages" not in st.session_state:
    st.session_state.messages = []


# 지금까지 쌓인 대화 기록을 화면에 순서대로 그리기
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# 사용자 입력창
user_input = st.chat_input('궁금한 날씨를 물어보세요.')

if user_input:  #채팅창에 뭔가 입력하고 엔터를 눌렀을때 True가 됨
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    answer = ask(st.session_state.agent, user_input, st.session_state.thread_id)    #LLM 호출

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)