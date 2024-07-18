import streamlit as st
import pandas as pd

from PIL import Image


st.set_page_config(
    page_title="Ford & Mazda PATS Assistant",
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded"
)

#image = Image.open("images/ford_logo.jpg")

makes = ['Ford', 'Lincoln', 'Mercury']

selected_make = st.selectbox('Select Make: ', makes)

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
    st.write('PATS Type = E')
    st.download_button(
        label='Click on this button to download the Parameter Reset Instructions', 
        data='pdf_file', 
        file_name='parameter_reset_instructions.pdf', 
        mime="parameter_reset/pdf")

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
