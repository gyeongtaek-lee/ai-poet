# dotenv 는 로컬에서 사용할 때만 처리
# from dotenv import load_dotenv
# load_dotenv()
from langchain_openai import ChatOpenAI
import streamlit as st

llm = ChatOpenAI()


# # 실행 2
st.title("인공지능 시인")

content = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):
    with st.spinner('시 작성 중...'):
        result = llm.invoke(content + "에 대한 시를 써줘")
        st.write(result.content)
    
