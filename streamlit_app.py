import streamlit as st
import pandas as pd
#import requests
#from st_anggrid import AgGrid

house = pd.read_csv('house_clean.csv')


def main() :
    st.write('Halaman Streamlit Azizah')
    st.subheader('This is Subheader')
    st.markdown('# Rendering Markdown ')
    st.write('Some Pyhtagorean Equation : ')
    st.latex('c^2 = a^2+b^2')

if _name_ == '_main_' :
    main()

 st.dataframe(house)
if _name_ == '_main_' : 
    main()
