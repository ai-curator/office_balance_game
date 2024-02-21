import streamlit as st
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

st.set_page_config(
    page_title="사무실 밸런스 게임",
    page_icon="👋",
)

st.write("# Welcome 사무실 찾기 밸런스 게임! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
#### 🙅‍♂️ 네이버부동산의 수많은 광고를 일일이 찾아보시나요?
#### 🧐 부동산 플랫폼 통합 DB로 한 번에 해결 가능합니다.
#### 🙆‍♂️ 스마트한 중개서비스를 지금 경험하세요.
#### 🔍 허위 매물로 시간 낭비하실 필요가 전혀 없어요.
#### 🚀 고객님 시간은 더 가치 있는 일에 사용할 수 있습니다.
"""
)
st.button("구글로그인")


response = supabase.table('Oder').select("*").execute()

st.text_input(label="선호지역", placeholder="역삼역")

st.button("제출")