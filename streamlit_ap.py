import streamlit as st
import preprocess,helper
import matplotlib.pyplot as mpl

st.sidebar.title("AJ")

uploaded_file = st.sidebar.file_uploader("Choose file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode()
    df = preprocess.process(data)
    
    unique_list = df['user'].unique().tolist()
    # unique_list.remove('group_notification')
    unique_list.sort()
    unique_list.insert(0,'Overall')
    
    st.dataframe(df)
    selected_user = st.sidebar.selectbox("show analyics wrt",unique_list)
    
    if st.sidebar.button("Show analyics"):
        
        col1 ,col2,col3,col4 = st.columns(4)
        
        num_mes,words,num_media,num_links =  helper.fetch_res(selected_user,df)
        
        with col1:
            st.header("Total messages")
            st.title(num_mes)
            
        with col2:
            st.header("Total words")
            st.title(words)
        
        with col3:
            st.header("Media shared")
            st.title(num_media)
            
        with col4:
            st.header("Links shared")
            st.title(num_links)
        
        
        if selected_user=='Overall':
            
            coll1,coll2 = st.columns(2)
            
            x,new_df = helper.busy_user(df)
            fig,ax = mpl.subplots()
            
            with coll1: 
                st.header("Busy user")
                # mpl.xticks(rotation=20)
                ax.bar(x.index,x.values)
                st.pyplot(fig)
            
            with coll2:
                st.dataframe(new_df)
                
        #wordcloud
        wc_img = helper.word_img(selected_user,df)
        fig,ax = mpl.subplots()
        ax.imshow(wc_img)
        st.pyplot(fig)