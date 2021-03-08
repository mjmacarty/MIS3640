# pip install streamlit
# streamlit hello
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
# when ready streamlit run file_name at cmd prompt --> can also pass a url
# as in github...


st.write('## [Streamlit Web-based GUI](https://alphabench.com)')

st.write(np.arange(9).reshape(3,3))

st.markdown('[https://reddit.com](https://reddit.com)') # kind of redundent
# doctrings get rendered as markdown
"""
# Here is some markdown
* I like bullets
* **_Streamlit_** is quick and easy
"""
x = 1e6
x

y = np.random.standard_normal(100000)
#plt.rcParams["figure.figsize"] = 4,2
fig, axes = plt.subplots(figsize=(4,2))
axes.hist(y, bins=50, color = 'g', edgecolor= 'w')

st.pyplot(fig) 

st.header("Header lighter weight than HTML")
st.subheader("Subheader")

st.sidebar.selectbox(label = "Choose", options=["Eeny", "meeny", "miny"])


ticker = st.sidebar.text_input(label="Ticker")
st.sidebar.date_input("Start date", f'{start}')
st.sidebar.date_input("End date", f"{today}")
return st.write(pdr.get_data_yahoo(ticker)['Close'], start, today)

#get_data()