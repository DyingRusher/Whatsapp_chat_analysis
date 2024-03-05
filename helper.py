from urlextract import URLExtract
from wordcloud import WordCloud

def fetch_res(user,df):
    
   
    if user !='Overall':
        df = df[df['user']==user]
    
        
    #number of media-3
    media_df = df[df['message'] == "<Media omitted>"]
    media_len = media_df.shape[0]
    
    #number of messages-1
    num_mes = df.shape[0]
    
    #number of words-2
    words =[]
    for mes in df['message']:
        words.extend(mes.split())
    
    #number of links shred-4
    urlExt = URLExtract()
    links = []
    for mes in df['message']:
        links.extend(urlExt.find_urls(mes))
    
    return num_mes,len(words),media_len,len(links)

def busy_user(df):
    
    new_df = round((df['user'].value_counts()/df.shape[0]*100).reset_index().rename(columns={'user':'name','count':'percent'}),2)
    return df['user'].value_counts().head(),new_df

def word_count(user,df):
    
    
    if user !='Overall':
        df = df[df['user']==user]
    
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    wc_img = wc.generate(df['message'].str.cat(sep=" "))
    
    return wc_img
    