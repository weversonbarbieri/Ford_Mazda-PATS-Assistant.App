import streamlit as st
import requests
import pandas as pd
from PIL import Image
from io import BytesIO


st.set_page_config(
    page_title="Ford & Mazda PATS Assistant",
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded"
)


# This code displays the presentation image at the top of the application as its symbol.
# The variable url_logo contains the link from GitHub.

url_logo = "https://raw.githubusercontent.com/weversonbarbieri/Ford-Mazda-Assistant-App/main/project_logo.JPG"
response = requests.get(url_logo) # The response vairable gets link info and confirms whether it is readable (200) or not (404).
image_ford = Image.open(BytesIO(response.content)) # Opens the image using PIL and response.content where the image content was got after reading the URL.
st.image(image_ford, width=1150) # This shows the image once the application is opened and width sets the size of the image.
st.write("<div align='center'><h2><i>Ford PATS Assistant</i></h2></div>", unsafe_allow_html=True)
st.write("")


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
        'Escape', 'Escape (Push to Start)', 'Escape (Hybrid)', 'E-Series', 'E-Series (Fleet Vehicles)', 'Excursion', 'Expedition', 'Explorer (4dr)', 'Explorer (Push to Start)',
        'Explorer Sport (2dr)', 'Explorer Sport Trac', 'F-150', 'F-150 Harley-Davidson', 'F-150 Heritage', 'F-250 (under 8500# GVW)', 'F-250 Super Duty', 'F-350 Super Duty', 'F-450 Super Duty', 'F-650 Super Duty', 'F-750 Super Duty',
        'F-Series > 8500 (Stripped Chassis/Cab Chassis)', 'Fiesta', 'Fiesta (Push to Start)', 'Five Hundred', 'Flex', 'Flex (Push to Start)', 'Focus', 'Focus (Push to Start) / Focus EV (Push to Start)', 'Freestar', 
        'Freestyle', 'Fusion / Fusion (hybrid)', 'Fusion (Push to Start)', 'Fusion (Hybrid) (Push to Start)', 'Fusion EV (Push to Start)', 'GT', 'Mustang', 'Ranger (3.0L & 4.0L ONLY)', 'Ranger (2.3L, 3.0L, & 4.0L)', 'Taurus (Duratec & SHO only)', 'Taurus', 'Taurus (Push to Start / X)', 
        'Thunderbird', 'Transit', 'Transit (Connect)', 'Windstar']

Lincoln = ['Aviator', 'Blackwood', 'Continental', 'LS', 'Mark LT', 'Mark VIII', 'MKS / MKS (Push to Start)', 'MKT', 'MKX', 
           'MKZ', 'MKZ (Push to Start)', 'Navigator', 'Town Car', 'Zephyr']

Mercury = ['Cougar', 'Grand Marquis', 'Marauder', 'Mariner', 'Mariner (Hybrid)', 'Milan', 'Milan (Hybrid)', 'Montego', 'Monterey', 'Mountaineer (4dr)',
           'Mystique (V-6 only)', 'Sable (Duratec only)', 'Sable']

year = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]


VIN_decode_url = 'https://www.ford-trucks.com/forums/vindecoder.php'


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


def pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g):
    st.write(pr_required)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_b_c_f_g,
    file_name=file_name_b_c_f_g,
    mime="application/pdf"
    )

def pr_required_pats_a(pr_required, pats_a, pdf_data_pr_c, file_name_c):
    st.write(pr_required)
    st.write(pats_a)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_c,
    file_name=file_name_c,
    mime="application/pdf"
    )


def pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g):
    st.write(pr_required)
    st.write(pats_b)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_b_c_f_g,
    file_name=file_name_b_c_f_g,
    mime="application/pdf"
    )

def pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c):
    st.write(pr_required)
    st.write(pats_c)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_c,
    file_name=file_name_c,
    mime="application/pdf"
    )

def pr_required_pats_g(pr_required, pats_g, pdf_data_pr_b_c_f_g, file_name_b_c_f_g):
    st.write(pr_required)
    st.write(pats_g)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_b_c_f_g,
    file_name=file_name_b_c_f_g,
    mime="application/pdf"
    )

def pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a):
    st.write(pr_not_required)
    st.write(pats_a)
    st.write("Click on the button to download the PATS A Instructions:")
    st.download_button(
    label="PATS A Instructions",
    data=pdf_data_pats_a,
    file_name=file_name_pats_a,
    mime="application/pdf"
    )

def pr_not_required_pats_c(pr_not_required, pats_c, pdf_data_pats_a, file_name_pats_a):
    st.write(pr_not_required)
    st.write(pats_c)
    st.write("Click on the button to download the PATS Instructions:")
    st.download_button(
    label="PATS Instructions",
    data=pdf_data_pats_a,
    file_name=file_name_pats_a,
    mime="application/pdf"
    )

def pr_not_required_pats_d(pr_not_required, pats_d, pdf_data_pats_d, file_name_pats_d):
    st.write(pr_not_required)
    st.write(pats_d)
    st.write("Click on the button to download the PATS D Instructions:")
    st.download_button(
    label="PATS A Instructions",
    data=pdf_data_pats_d,
    file_name=file_name_pats_d,
    mime="application/pdf"
    )
    
def pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e):
    st.write(pr_not_required)
    st.write(pats_e)
    st.write("Click on the button to download the PATS E Instructions:")
    st.download_button(
    label="PATS E Instructions",
    data=pdf_data_pats_e,
    file_name=file_name_pats_e,
    mime="application/pdf"
    )


if selected_make == 'Ford':
    selected_model = st.selectbox('Selected Model:', Ford)
    selected_year = st.selectbox('Select year', year)
elif selected_make == 'Lincoln':
    selected_model = st.selectbox('Select Model:', Lincoln)
    selected_year = st.selectbox('Select year:', year)
else:
    selected_model = st.selectbox('Select Model:', Mercury)
    selected_year = st.selectbox('Select year:', year)


#---------------------------------------------------------------------------------------------#
#                                    FORD                                                     #
#---------------------------------------------------------------------------------------------#

if selected_model == 'C-MAX (Hybrid)' and selected_year >= 2013:
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'C-MAX (Hybrid) (Push to Start)' and selected_year >= 2013:
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    
elif selected_model == 'Contour (V6-only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
    elif selected_year > 1998 and selected_year <= 2000:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)


elif selected_model == 'Crown Victoria':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year >= 2003 and selected_year <= 2012:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Edge':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2010:
       pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year >= 2011:
       pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
       
elif selected_model == 'Edge (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
   

elif selected_model == 'Escape':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2008:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Escape (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Escape (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2007:
        pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year >= 2008 and selected_year <= 2012:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)


elif selected_model == 'E-Series (Fleet Vehicles)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_g(pr_required, pats_g, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'E-Series':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2011:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)


elif selected_model == 'Excursion':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2005:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Expedition':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1997 and selected_year <= 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
    elif selected_year >= 1999 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2003 and selected_year <= 2006:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2007 and selected_year <= 2008:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2009 and selected_year <= 2013:
        pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)


elif selected_model == 'Explorer (4dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year >= 2002 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2006 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)


elif selected_model == 'Explorer (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Explorer Sport (2dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year > 2001 and selected_year <= 2003:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Explorer Sport Trac':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year > 2001 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2007 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'F-150':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2008:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2009 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'F-150 Harley-Davidson':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2003:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2006 and selected_year <= 2008:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'F-150 Heritage':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2006:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'F-250 (under 8500# GVW)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2000:
        st.write(f'Open the link {VIN_decode_url} and follow the steps below to confirm the GVW:')
        st.write('1. Copy and paste the VIN# below the field "Enter VIN"') 
        st.write('2. Click on the "Decode" button to open the vehicle info.')
        st.write('3. Select the the TAB Tech Specs.') 
        st.write('4. Go to the field "Gross Vehicle Weight Rating Cap" to see the GVW.')
        st.write("Is the Gross Vehicle Weight Rating Cap > 8500?")
        gvw_result1 = st.checkbox('Yes.')
        gvw_result2 = st.checkbox('No.')
        if gvw_result1 == True and gvw_result2 == False:
           pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        elif gvw_result1 == False and gvw_result2 == True:
           st.write("No key relearn required")
        elif gvw_result1 == False and gvw_result2 == False:
            st.write()

elif selected_model == 'F-250 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'F-350 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'F-450 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'F-650 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'F-750 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'F-Series > 8500 (Stripped Chassis/Cab Chassis)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        st.write(f'Open the link {VIN_decode_url} and follow the steps below to confirm the GVW:')
        st.write('1. Copy and paste the VIN# below the field "Enter VIN"') 
        st.write('2. Click on the "Decode" button to open the vehicle info.')
        st.write('3. Select the the TAB Tech Specs.') 
        st.write('4. Go to the field "Gross Vehicle Weight Rating Cap" to see the GVW.')
        st.write("Is the Gross Vehicle Weight Rating Cap > 8500?")
        gvw_result1 = st.checkbox('Yes.')
        gvw_result2 = st.checkbox('No.')
        if gvw_result1 == True and gvw_result2 == False:
           pr_required_pats_g(pr_required, pats_g, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        elif gvw_result1 == False and gvw_result2 == True:
           st.write("No key relearn required")
        elif gvw_result1 == False and gvw_result2 == False:
            st.write()
        
elif selected_model == 'Fiesta':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_a(pr_required, pats_a, pdf_data_pr_c, file_name_c)

elif selected_model == 'Fiesta (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Five Hundred':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Flex':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2009 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Flex (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Focus':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2008:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Focus (Push to Start) / EV (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Freestar':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Freestyle':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Fusion / Fusion (hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Fusion (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Fusion (Hybrid) (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Fusion EV (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'GT':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2006:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Mustang':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1996 and selected_year <= 1997:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
    elif selected_year == 1998:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year >= 1999 and selected_year <= 2004:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2005 and selected_year <= 2009:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2010 and selected_year <= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Ranger (3.0L & 4.0L ONLY)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2000:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year == 2006:
        pr_not_required_pats_c(pr_not_required, pats_c, pdf_data_pats_a, file_name_pats_a)

elif selected_model == 'Ranger (2.3L, 3.0L, & 4.0L)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2004:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2007 and selected_year <= 2010:
        pr_required_pats_g(pr_required, pats_g, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Taurus (Duratec & SHO only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1996 and selected_year <= 1997:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
    elif selected_year >= 1998 and selected_year <= 1999:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Taurus':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2006:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2008 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Taurus (Push to Start / X)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Thunderbird':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2002 and selected_year <= 2006:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Transit':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Transit Connect':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2010 and selected_year <= 2013:
        pr_required_pats_a(pr_required, pats_a, pdf_data_pr_c, file_name_c)

elif selected_model == 'Windstar':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2000:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2001 and selected_year <= 2003:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)


#---------------------------------------------------------------------------------------------#
#                                    LINCOLN                                                  #
#---------------------------------------------------------------------------------------------#

elif selected_model == 'Aviator':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2003 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Blackwood':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2002 and selected_year <= 2003:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Continental':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'LS':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2007:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Mark LT':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2008:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Mark VIII':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1997 and selected_year <= 1998:
        pr_not_required_pats_d(pr_not_required, pats_d, pdf_data_pats_d, file_name_pats_d)

elif selected_model == 'MKS':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2009 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'MKS / MKS (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2009:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)      

elif selected_model == 'MKT':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'MKX':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'MKZ':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'MKZ (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Navigator':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
    elif selected_year >= 1999 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2003 and selected_year <= 2006:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2007:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Town Car':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2003 and selected_year <= 2011:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Zephyr':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2006:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)    


#---------------------------------------------------------------------------------------------#
#                                    MERCURY                                                  #
#---------------------------------------------------------------------------------------------#

elif selected_model == 'Cougar':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2002:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Grand Marquis':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year >= 2003 and selected_year <= 2010:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Marauder':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2003 and selected_year <= 2004:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Mariner':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Mariner (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Milan':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Milan (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Montego':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Monterey':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Mountaineer (4dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year >= 2002 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2006 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

elif selected_model == 'Mystique (V-6 only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
    elif selected_year > 1998 and selected_year <= 2000:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

elif selected_model == 'Sable (Duratec only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1996 and selected_year <= 1997:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
    elif selected_year >= 1998 and selected_year <= 1999:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

elif selected_model == 'Sable':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
    elif selected_year >= 2008 and selected_year <= 2009:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
