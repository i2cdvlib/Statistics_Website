import streamlit as st
import pandas as pd
import plotly.express as px

st.write(
    '<link href="https://googleapis.com" rel="stylesheet">',
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>Marks Statistics</h1>", unsafe_allow_html=True)
st.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

col,col2,col3,col4,col5 = st.columns(5)

with col:
    st.markdown("<p style='font-family:Lora; font-size: 25px;'>English</p>", unsafe_allow_html=True)
    English = st.number_input("",key="e")


with col2:
    st.markdown("<p style='font-family:Lora; font-size: 25px;'>Science</p>", unsafe_allow_html=True)
    Science = st.number_input("",key="s")   
    

with col3:
    st.markdown("<p style='font-family:Lora; font-size: 25px;'>Social</p>", unsafe_allow_html=True)
    Social_science= st.number_input("", key="O")

with col4:
    st.markdown("<p style='font-family:Lora; font-size: 25px;'>Maths</p>", unsafe_allow_html=True)
    Maths = st.number_input("",key="M")

with col5:
    st.markdown("<p style='font-family:Lora; font-size: 25px;'>Language</p>", unsafe_allow_html=True)
    Ln = st.number_input("",key="L")

data = {
    "Science": Science,
    "Social Science": Social_science,
    "English": English,
    "Language": Ln,
    "Maths": Maths
}

chart = px.bar(
    x = list(data.keys()),
    y= list(data.values()),
    labels={'x':'Subjects', 'y':'Marks'}

)

chart.update_layout(yaxis_range=[0,100])

st.plotly_chart(chart)
Average= (Science + Social_science + English + Ln + Maths) / 5
st.write("Average Percentage:",Average)
highest_mark = max(data.values())
highest_subject = max(data, key=data.get)
st.write("Highest: ",highest_subject ," ",highest_mark)

st.markdown("<h1 style='text-align: center;'>Solver</h1>", unsafe_allow_html=True)
st.subheader("Enter Your Target Marks")
Target= st.number_input("", key= "Target")
st.write("Enter the Marks of subjects that you expect to get and keep the subjects blank for which you have to find the minimum marks required")


st.markdown("<p style='font-family:Lora; font-size: 25px;'>English</p>", unsafe_allow_html=True)
TEnglish = st.number_input("",key="Te")



st.markdown("<p style='font-family:Lora; font-size: 25px;'>Science</p>", unsafe_allow_html=True)
TScience = st.number_input("",key="Ts")   
    


st.markdown("<p style='font-family:Lora; font-size: 25px;'>Social</p>", unsafe_allow_html=True)
TSocial_science= st.number_input("", key="TO")


st.markdown("<p style='font-family:Lora; font-size: 25px;'>Maths</p>", unsafe_allow_html=True)
TMaths = st.number_input("",key="TM")


st.markdown("<p style='font-family:Lora; font-size: 25px;'>Language</p>", unsafe_allow_html=True)
TLn = st.number_input("",key="TL")

tsub = [TLn,TSocial_science,TScience,TMaths,TEnglish].count(0)
Marks_req = ((Target*5) - (TLn+TMaths+TSocial_science+TScience+TEnglish))/tsub

if Marks_req > 100 or Marks_req < 0:
    st.subheader("The Target Marks is impossible to acheive with the current marks") 

else:
    st.subheader("Marks Required:")
    st.subheader(Marks_req)

