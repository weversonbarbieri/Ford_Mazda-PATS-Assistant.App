import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="Ford & Mazda PATS Assistant",
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded"
)


makes = ['Ford', 'Lincoln', 'Mercury']

selected_make = st.selectbox('Select Make: ', makes)

url = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PARAMETER_RESET_INS.pdf'

file_name = 'FORD_PARAMETER_RESET_INS.pdf'

response = requests.get(url)
pdf_data = response.content

Ford = ['C-MAX', 'Contour (V6-only)', 'Crown Victoria', 'Edge']
Lincoln = ['Aviator', 'Blackwood', 'Continental', 'LS']
Mercury = ['Cougar', 'Grand Marquis', 'Marauder', 'Mariner']
year = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]


if selected_make == 'Ford':
    selected_model = st.selectbox('Selected Model:', Ford)
    selected_year = st.selectbox('Select year', year)
elif selected_make == 'Lincoln':
    selected_model = st.selectbox('Select Model:', Lincoln)
    selected_year = st.selectbox('Select year:', year)
else:
    selected_model = st.selectbox('Select Model:', Mercury)
    selected_year = st.selectbox('Select year:', year)



if selected_model == 'C-MAX' and selected_year > 2010:
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    st.write('Parameter reset: Required')
    st.write('PATS Type = B/C')
    
    st.download_button(
        label="Baixar PDF",
        data=pdf_data,
        file_name=file_name,
        mime="application/pdf"
        )
    

elif selected_model == 'Contour (V6-only)' and selected_year == 1998:
    st.write("Not Required")
elif selected_model == 'Crown Victoria':
    if selected_year >= 1998 and selected_year <= 2002:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        st.write('Parameter reset: Required')
        st.write('PATS Type = B')
    elif selected_year >= 2003 and selected_year <= 2012:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        st.write('Parameter reset: Not Required')
        st.write('PATS Type = E')
