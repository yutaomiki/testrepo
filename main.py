import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバー')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
     latest_iteration.text(f'Iteration {i+1}')
     bar.progress(i+1)
     time.sleep(0.1)

st.write('DataFrame')

df = pd.DataFrame(
   np.random.rand(20, 3),
   columns=['1','2','3']
)


st.write(df)

st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)


dfmap = pd.DataFrame(
   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
   columns=['lat','lon']
)

st.map(dfmap)

st.write('Display Image')

if st.checkbox('Show Image', True):
    img = Image.open('著：ねここ先生.png')
    st.image(img, caption='nekoko')

option = st.selectbox(
    'うんこ',
    list(range(1,11))
)
'うんこは', option, 'homo'

text = st.text_input('うんこ')
unko = st.slider('aaaa',0,100,50)
'うんこは', text


'うんこのながさ', unko


left_column, right_column = st.columns(2)
button = left_column.button('unko')
if button:
    right_column.write('右')

expander = st.expander('ああ')

expander.write('これよ')
