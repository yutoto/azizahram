import streamlit as st

def main() :
    st.write('Halaman Streamlit Azizah')
    st.subheader('This is Subheader')
    st.markdown('# Rendering Markdown ')
    st.write('Some Pyhtagorean Equation : ')
    st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' :
    main()
