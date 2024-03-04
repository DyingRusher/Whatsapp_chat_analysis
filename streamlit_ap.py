import streamlit as st
import preprocess

st.sidebar.title("AJ")

uploaded_file = st.sidebar.file_uploader("Choose file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode()
    df = preprocess.process(data)
    
    unique_list = df['user'].unique().tolist()
    st.dataframe(df)
    st.sidebar.selectbox("show analyics wrt",unique_list)
    
    if st.sidebar.button("Show analyics"):
        pass