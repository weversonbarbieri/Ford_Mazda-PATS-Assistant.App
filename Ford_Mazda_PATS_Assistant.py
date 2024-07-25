import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="Ford & Mazda PATS Assistant",
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded"
)


pr_required = 'Parameter reset: Required'
pr_not_required = 'Parameter reset: Not Required'
pats_a = 'PATS Type = A'
pats_d = 'PATS Type = D'
pats_b = 'PATS Type = B'
pats_c = 'PATS Type = C'
pats_f = 'PATS Type = F'
pats_g = 'PATS Type = G'
pats_e = 'PATS Type = E'

makes = ['Ford', 'Lincoln', 'Mercury']

selected_make = st.selectbox('Select Make: ', makes)

Ford = ['C-MAX (Hybrid)', 'C-MAX (Hybrid) (Push to Start)', 'Contour (V6-only)', 'Crown Victoria', 'Edge', 'Edge (Push to Start)', 
        'Escape', 'Escape (Push to Start)', 'Escape (Hybrid)', 'E-Series', 'E-Series (Fleet Vehicles)' 'Excursion', 'Expedition', 'Explorer (4dr)', 'Explorer (Push to Start)',
        'Explorer Sport (2dr)', 'Explorer Sport Trac', 'F-150', 'F-150 Harley-Davidson', 'F-150 Heritage', 'F-250 (under 8500# GVW)', 'F-Series Super Duty (350/450/650/750)',
        'F-Series > 8500 (Stripped Chassis/Cab Chassis)', 'Fiesta', 'Fiesta (Push to Start)', 'Five Hundred', 'Flex', 'Flex (Push to Start)', 'Focus', 'Focus (Push to Start)',
        'Focus (Push to Start) / Focus EV (Push to Start)', 'Freestar', 'Freestyle', 'Fusion / Fusion (hybrid)', 'Fusion (Hybrid/Push to Start/EV)', 'GT', 'Mustang', 'Ranger (3.0L & 4.0L ONLY)', 
        'Ranger (2.3L, 3.0L, & 4.0L)', 'Taurus (Duratec & SHO only)', 'Taurus', 'Taurus (Push to Start / X)', 'Thunderbird', 'Transit / Transit (Connect)', 'Windstar']
Lincoln = ['Aviator', 'Blackwood', 'Continental', 'LS']
Mercury = ['Cougar', 'Grand Marquis', 'Marauder', 'Mariner']
year = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

url_pr_c = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PARAMETER_RESET_C.pdf'
url_pr_b_c_f_g = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PARAMETER_RESET_B_C_F_G.pdf'
url_pats_a = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PATS_TYPE_A.pdf'
url_pats_d = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PATS_TYPE_D.pdf'
url_pats_e = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PATS_TYPE_E.pdf' 


file_name_c = 'FORD_PARAMETER_RESET_C.pdf'
file_name_b_c_f_g = 'FORD_PARAMETER_RESET_B_C_F_G.pdf'
file_name_pats_a = 'FORD_PATS_TYPE_A.pdf' 
file_name_pats_d = 'FORD_PATS_TYPE_D.pdf'
file_name_pats_e = 'FORD_PATS_TYPE_E.pdf' 

response_pr_c = requests.get(url_pr_c)
pdf_data_pr_c = response_pr_c.content

response_pr_b_c_f_g = requests.get(url_pr_b_c_f_g)
pdf_data_pr_b_c_f_g = response_pr_b_c_f_g.content

response_pats_a = requests.get(url_pats_a)
pdf_data_pats_a = response_pats_a.content

response_pats_d = requests.get(url_pats_d)
pdf_data_pats_d = response_pats_d.content

response_pats_e = requests.get(url_pats_e)
pdf_data_pats_e = response_pats_e.content




if selected_make == 'Ford':
    selected_model = st.selectbox('Selected Model:', Ford)
    selected_year = st.selectbox('Select year', year)
elif selected_make == 'Lincoln':
    selected_model = st.selectbox('Select Model:', Lincoln)
    selected_year = st.selectbox('Select year:', year)
else:
    selected_model = st.selectbox('Select Model:', Mercury)
    selected_year = st.selectbox('Select year:', year)


if selected_model == 'C-MAX (Hybrid)' and selected_year >= 2013:
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    st.write(pr_required)
    st.write(pats_b)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_b_c_f_g,
    file_name=file_name_b_c_f_g,
    mime="application/pdf"
    )
elif selected_model == 'C-MAX (Hybrid) (Push to Start)' and selected_year >= 2013:
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    st.write(pr_required)
    st.write(pats_c)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_c,
    file_name=file_name_c,
    mime="application/pdf"
    )
    
elif selected_model == 'Contour (V6-only)':
    if selected_year == 1998:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        st.write(pr_not_required)
        st.write(pats_a)
        st.write("Click on the button to download the PATS A Instructions:")
        st.download_button(
        label="PATS A Instructions",
        data=pdf_data_pats_a,
        file_name=file_name_pats_a,
        mime="application/pdf"
        )
    elif selected_year > 1998 and selected_year <= 2000:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        st.write(pr_not_required)
        st.write(pats_e)
        st.write("Click on the button to download the PATS E Instructions:")
        st.download_button(
        label="PATS E Instructions",
        data=pdf_data_pats_e,
        file_name=file_name_pats_e,
        mime="application/pdf"
        )


elif selected_model == 'Crown Victoria':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        st.write(pr_required)
        st.write(pats_b)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_b_c_f_g,
        file_name=file_name_b_c_f_g,
        mime="application/pdf"
        ) 
    elif selected_year >= 2003 and selected_year <= 2012:
        st.write(pr_not_required)
        st.write(pats_e)
        st.write("Click on the button to download the PATS E Instructions:")
        st.download_button(
        label="PATS E Instructions",
        data=pdf_data_pats_e,
        file_name=file_name_pats_e,
        mime="application/pdf"
        )

elif selected_model == 'Edge':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2010:
       st.write(pr_required)
       st.write(pats_b)
       st.write("Click on the button to download the Parameter Reset Instructions:")
       st.download_button(
       label="Parameter Reset Instructions",
       data=pdf_data_pr_c,
       file_name=file_name_c,
       mime="application/pdf"
       )
    elif selected_year >= 2011:
       st.write(pr_required)
       st.write(pats_b)
       st.write("Click on the button to download the Parameter Reset Instructions:")
       st.download_button(
       label="Parameter Reset Instructions",
       data=pdf_data_pr_b_c_f_g,
       file_name=file_name_b_c_f_g,
       mime="application/pdf"
       )
elif selected_model == 'Edge (Push to Start)' and selected_year >= 2011:
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    st.write(pr_required)
    st.write(pats_b)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_c,
    file_name=file_name_c,
    mime="application/pdf"
    )
   

elif selected_model == 'Escape':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2007:
        st.write(pr_not_required)
        st.write(pats_e)
        st.write("Click on the button to download the PATS E Instructions:")
        st.download_button(
        label="PATS E Instructions",
        data=pdf_data_pats_e,
        file_name=file_name_pats_e,
        mime="application/pdf"
        )
    elif selected_year >= 2008:
        st.write(pr_required)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_b_c_f_g,
        file_name=file_name_b_c_f_g,
        mime="application/pdf"
        )

elif selected_model == 'Escape (Push to Start)' and selected_year >= 2013:
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    st.write(pr_required)
    st.write(pats_b)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_c,
    file_name=file_name_c,
    mime="application/pdf"
    )

elif selected_model == 'Escape (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2007:
        st.write(pr_required)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_b_c_f_g,
        file_name=file_name_b_c_f_g,
        mime="application/pdf"
        )
    elif selected_year >= 2008 and selected_year <= 2012:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        st.write(pr_required)
        st.write(pats_b)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_c,
        file_name=file_name_c,
        mime="application/pdf"
        )


elif selected_model == 'E-Series (Fleet Vehicles)':
    if selected_year >= 2008 and selected_year <= 2010:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        st.write(pr_required)
        st.write(pats_g)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_b_c_f_g,
        file_name=file_name_b_c_f_g,
        mime="application/pdf"
        )

elif selected_model == 'E-Series':
    if selected_year >= 2008 and selected_year <= 2010:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        st.write(pr_required)
        st.write(pats_c)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_c,
        file_name=file_name_c,
        mime="application/pdf"
        )
    elif selected_year >= 2011:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        st.write(pr_required)
        st.write(pats_a)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_c,
        file_name=file_name_c,
        mime="application/pdf"
        )


elif selected_model == 'Excursion':
    if selected_year >= 2000 and selected_year <= 2005:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        st.write(pr_required)
        st.write(pats_b)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_b_c_f_g,
        file_name=file_name_b_c_f_g,
        mime="application/pdf"
        )

elif selected_model == 'Expedition':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1997 and selected_year <= 1998:
        st.write(pr_not_required)
        st.write(pats_a)
        st.write("Click on the button to download the PATS A Instructions:")
        st.download_button(
        label="PATS A Instructions",
        data=pdf_data_pats_a,
        file_name=file_name_pats_a,
        mime="application/pdf"
        )
    elif selected_year >= 1999 and selected_year <= 2002:
        st.write(pr_required)
        st.write(pats_c)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_c,
        file_name=file_name_c,
        mime="application/pdf"
        )
    elif selected_year >= 2003 and selected_year <= 2006:
        st.write(pr_not_required)
        st.write(pats_e)
        st.write("Click on the button to download the PATS E Instructions:")
        st.download_button(
        label="PATS E Instructions",
        data=pdf_data_pats_e,
        file_name=file_name_pats_e,
        mime="application/pdf"
        )
    elif selected_year >= 2007 and selected_year <= 2008:
        st.write(pr_required)
        st.write(pats_c)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_c,
        file_name=file_name_c,
        mime="application/pdf"
        )
    elif selected_year >= 2009 and selected_year <= 2013:
        st.write(pr_required)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_c,
        file_name=file_name_c,
        mime="application/pdf"
        )


elif selected_model == 'Explorer (4dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        st.write(pr_required)
        st.write(pats_b)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_b_c_f_g,
        file_name=file_name_b_c_f_g,
        mime="application/pdf"
        )
    elif selected_year >= 2002 and selected_year <= 2005:
        st.write(pr_not_required)
        st.write(pats_e)
        st.write("Click on the button to download the PATS E Instructions:")
        st.download_button(
        label="PATS E Instructions",
        data=pdf_data_pats_e,
        file_name=file_name_pats_e,
        mime="application/pdf"
        )
    elif selected_year >= 2006 and selected_year <= 2010:
        st.write(pr_required)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_c,
        file_name=file_name_c,
        mime="application/pdf"
        )
    elif selected_year >= 2011:
        st.write(pr_required)
        st.write(pats_b)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_b_c_f_g,
        file_name=file_name_b_c_f_g,
        mime="application/pdf"
        )


elif selected_model == 'Explorer (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    st.write(pr_required)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_c,
    file_name=file_name_c,
    mime="application/pdf"
    )

elif 'Explorer Sport (2dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        st.write(pr_required)
        st.write(pats_b)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_b_c_f_g,
        file_name=file_name_b_c_f_g,
        mime="application/pdf"
        )
    elif selected_year > 2001 and selected_year <= 2003:
        st.write(pr_not_required)
        st.write(pats_e)
        st.write("Click on the button to download the PATS E Instructions:")
        st.download_button(
        label="PATS E Instructions",
        data=pdf_data_pats_e,
        file_name=file_name_pats_e,
        mime="application/pdf"
        )

elif selected_model == 'Explorer Sport Trac':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2001:
        st.write(pr_required)
        st.write(pats_b)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_b_c_f_g,
        file_name=file_name_b_c_f_g,
        mime="application/pdf"
        )
    elif selected_year > 2001 and selected_year <= 2005:
        st.write(pr_not_required)
        st.write(pats_e)
        st.write("Click on the button to download the PATS E Instructions:")
        st.download_button(
        label="PATS E Instructions",
        data=pdf_data_pats_e,
        file_name=file_name_pats_e,
        mime="application/pdf"
        )
    elif selected_year >= 2007 and selected_year <= 2010:
        st.write(pr_required)
        st.write(pats_c)
        st.write("Click on the button to download the Parameter Reset Instructions:")
        st.download_button(
        label="Parameter Reset Instructions",
        data=pdf_data_pr_c,
        file_name=file_name_c,
        mime="application/pdf"
        )
