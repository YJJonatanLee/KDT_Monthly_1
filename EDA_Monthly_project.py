import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Video Games Sales')

df = pd.read_csv("/Users/youngjunlee/프로젝트/KDT/Project/remote_repo/[KDT] 인공지능 5주차 실습/monthly_project/Video_Games_Sales_as_at_22_Dec_2016.csv")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
    
st.subheader('연도별 게임 발매량')

fig = plt.figure(figsize = (10, 4))
sns.histplot(x = 'Year_of_Release', data = df)
st.pyplot(fig)

st.subheader('회사별 각 연도의 발매량')
option = st.selectbox(
    'Publisher', 
    (df['Publisher'].unique()))

fig = plt.figure(figsize = (10, 4))
sns.histplot(x = 'Year_of_Release', data = df.loc[df['Publisher'] == option])
st.pyplot(fig)

st.subheader('회사별 각 연도의 판매액')
option1 = st.selectbox(
    'Sales', 
    (['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']),
    key = '1234')
option2 = st.selectbox(
    'Publisher', 
    (df['Publisher'].unique()),
    key = '5678')

fig = plt.figure(figsize = (10, 4))
sns.lineplot(x = 'Year_of_Release', y = option1, data = df.loc[df["Publisher"] == option2])
st.pyplot(fig)
