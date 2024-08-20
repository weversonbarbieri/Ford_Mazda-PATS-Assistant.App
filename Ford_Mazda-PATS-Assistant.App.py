import streamlit as st
import requests
from PIL import Image
from io import BytesIO


st.set_page_config(
    page_title="Ford & Mazda PATS Assistant",
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded"
)


#---------------------------------------------------------------------------------------------#
#                                    APPLICATION LOGO                                         #
#---------------------------------------------------------------------------------------------#

# The variable url_logo contains the link from GitHub.
url_logo = "https://raw.githubusercontent.com/weversonbarbieri/Ford-Mazda-Assistant-App/main/project_logo.JPG"

# The response vairable gets link info and confirms whether it is readable (200) or not (404).
response = requests.get(url_logo)

# Opens the image using PIL and response.content where the image content was got after reading the URL. 
image_ford = Image.open(BytesIO(response.content))

# This shows the image once the application is opened and width sets the size of the image.
st.image(image_ford, width=500) 
st.write("<div align='center'><h2><i>Ford PATS Assistant</i></h2></div>", unsafe_allow_html=True)
st.write("")


#---------------------------------------------------------------------------------------------#
#                                    VARIABLES                                                #
#---------------------------------------------------------------------------------------------#


# These variables determine the maximum keys required to be programmed.
max_keys_na = 'N/A'
max_keys_8 = 8
max_keys_16 = 16

# These variables determine the Minimum keys required to be programmed.
min_keys_na = 'N/A'
min_keys_1 = 1
min_keys_2 = 2
min_keys_23 = "2 or 3"

# These variables determine whether or not "starter interrupt present".
starter_interrupt_no = 'No'
starter_interrupt_yes = 'Yes'

# These variables determine whether or not the "Theft Indicator Flashes at Ignition OFF".
theft_light_10s = "10 sec."
theft_light_yes = 'Yes'
theft_light_no = "No"
theft_light_na = 'N/A'


pats_not_available = "PATS isn't available for this year/model"
pr_required = 'Parameter reset: Required'
pr_not_required = 'Parameter reset: Not Required'
pats_a = 'PATS Type = A'
pats_d = 'PATS Type = D'
pats_b = 'PATS Type = B'
pats_c = 'PATS Type = C'
pats_f = 'PATS Type = F'
pats_g = 'PATS Type = G'
pats_e = 'PATS Type = E'

# These variables contains the file names of Ford procedures c, b_c_f_g, a, d and e.
file_name_c = 'FORD_PARAMETER_RESET_C.pdf'
file_name_b_c_f_g = 'FORD_PARAMETER_RESET_B_C_F_G.pdf'
file_name_pats_a = 'FORD_PATS_TYPE_A.pdf' 
file_name_pats_d = 'FORD_PATS_TYPE_D.pdf'
file_name_pats_e = 'FORD_PATS_TYPE_E.pdf'

# These variables contains the file names of Mazda procedures from MA to MH.
file_name_ma = 'Mazda_procedure_M-A.pdf'
file_name_mb = 'Mazda_procedure_M-B.pdf'
file_name_mc = 'Mazda_procedure_M-C.pdf'
file_name_md = 'Mazda_procedure_M-D.pdf'
file_name_me = 'Mazda_procedure_M-E.pdf'
file_name_mf = 'Mazda_procedure_M-F.pdf'
file_name_mg = 'Mazda_procedure_M-G.pdf'
file_name_mh =  'Mazda_procedure_M-H.pdf'

# When the vehicle is not equipped with security system.
no_security_system = "Security isn't available for this year/model"



makes = ['Ford', 'Lincoln', 'Mercury', 'Mazda']

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

Mazda = ['626', 'B-Series', 'CX-3', 'CX-5', 'CX-7', 'CX-7 (Advanced Keyless)', 'CX-9', 'CX-9 (Advanced Keyless)', 'CX-30', 'Mazda2', 'Mazda2 (Advanced Keyless)', 
         'Mazda3', 'Mazda3 (Advanced Keyless)', 'Mazda5', 'Mazda6', 'Mazda6 (Advanced Keyless)', 'Millenia', 'MPV', 'MX-5 (Miata)', 
         'MX-5 (Miata) (Advanced Keyless Entry/Start)', 'MX-5 (Miata) (Keyless Entry, Without Keyless Start)',
         'Protege', 'RX-8', 'RX-8 (Advanced Keyless)', 'Tribute']

year = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]


VIN_decode_url = 'https://www.ford-trucks.com/forums/vindecoder.php'


#---------------------------------------------------------------------------------------------#
#                                       FORD FILES                                            #
#---------------------------------------------------------------------------------------------#

url_pr_c = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PARAMETER_RESET_C.pdf'
url_pr_b_c_f_g = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PARAMETER_RESET_B_C_F_G.pdf'
url_pats_a = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PATS_TYPE_A.pdf'
url_pats_d = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PATS_TYPE_D.pdf'
url_pats_e = 'https://github.com/weversonbarbieri/Ford-Mazda-Assistant-App/raw/main/FORD_PATS_TYPE_E.pdf'

# Requests the HTTP from the URL saved on GitHub where the parameter reset c PDF file is saved. 
response_pr_c = requests.get(url_pr_c)
# Save the parameter reset c PDF file content after the download.
pdf_data_pr_c = response_pr_c.content

# Requests the HTTP from the URL saved on GitHub where the parameter reset b_c_f_g PDF file is saved. 
response_pr_b_c_f_g = requests.get(url_pr_b_c_f_g)
# Save the parameter reset b_c_f_g PDF file content after the download.
pdf_data_pr_b_c_f_g = response_pr_b_c_f_g.content

# Requests the HTTP from the URL saved on GitHub where the PATS A procedure PDF file is saved. 
response_pats_a = requests.get(url_pats_a)
# Save the PATS A procedure PDF file content after the download.
pdf_data_pats_a = response_pats_a.content

# Requests the HTTP from the URL saved on GitHub where the PATS D procedure PDF file is saved. 
response_pats_d = requests.get(url_pats_d)
# Save the PATS D procedure PDF file content after the download.
pdf_data_pats_d = response_pats_d.content

# Requests the HTTP from the URL saved on GitHub where the PATS E procedure PDF file is saved. 
response_pats_e = requests.get(url_pats_e)
# Save the PATS D procedure PDF file content after the download.
pdf_data_pats_e = response_pats_e.content


#---------------------------------------------------------------------------------------------#
#                                       MAZDA FILES                                            #
#---------------------------------------------------------------------------------------------#

# These variables get the 8 links from the GitHub raw file of the Mazda procedure from MA to MH.
# Needs to replace /blob/ for /raw/ on the GitHub, and then the variable will get the raw file (the PDF file).
url_mazda_ma = 'https://github.com/weversonbarbieri/Ford-PATS-App/raw/main/Mazda_procedure_M-A.pdf'
url_mazda_mb = 'https://github.com/weversonbarbieri/Ford-PATS-App/raw/main/Mazda_procedure_M-B.pdf'
url_mazda_mc = 'https://github.com/weversonbarbieri/Ford-PATS-App/raw/main/Mazda_procedure_M-C.pdf'
url_mazda_md = 'https://github.com/weversonbarbieri/Ford-PATS-App/raw/main/Mazda_procedure_M-D.pdf'
url_mazda_me = 'https://github.com/weversonbarbieri/Ford-PATS-App/raw/main/Mazda_procedure_M-E.pdf'
url_mazda_mf = 'https://github.com/weversonbarbieri/Ford-PATS-App/raw/main/Mazda_procedure_M-F.pdf'
url_mazda_mg = 'https://github.com/weversonbarbieri/Ford-PATS-App/raw/main/Mazda_procedure_M-G.pdf'
url_mazda_mh = 'https://github.com/weversonbarbieri/Ford-PATS-App/raw/main/Mazda_procedure_M-H.pdf'

# Requests the HTTP from the URL saved on GitHub where the Mazda M-A procedure PDF file is saved. 
response_mazda_ma = requests.get(url_mazda_ma)
# Save the Mazda M-A procedure PDF file content after the download.
pdf_data_mazda_ma = response_mazda_ma.content

# Requests the HTTP from the URL saved on GitHub where the Mazda M-B procedure PDF file is saved. 
response_mazda_mb = requests.get(url_mazda_mb)
# Save the Mazda M-B procedure PDF file content after the download.
pdf_data_mazda_mb = response_mazda_mb.content

# Requests the HTTP from the URL saved on GitHub where the Mazda M-C procedure PDF file is saved. 
response_mazda_mc = requests.get(url_mazda_mc)
# Save the Mazda M-C procedure PDF file content after the download.
pdf_data_mazda_mc = response_mazda_mc.content

# Requests the HTTP from the URL saved on GitHub where the Mazda M-D procedure PDF file is saved. 
response_mazda_md = requests.get(url_mazda_md)
# Save the Mazda M-D procedure PDF file content after the download.
pdf_data_mazda_md = response_mazda_md.content

# Requests the HTTP from the URL saved on GitHub where the Mazda M-E procedure PDF file is saved. 
response_mazda_me = requests.get(url_mazda_me)
# Save the Mazda M-E procedure PDF file content after the download.
pdf_data_mazda_me = response_mazda_me.content

# Requests the HTTP from the URL saved on GitHub where the Mazda M-F procedure PDF file is saved. 
response_mazda_mf = requests.get(url_mazda_mf)
# Save the Mazda M-F procedure PDF file content after the download.
pdf_data_mazda_mf = response_mazda_mf.content

# Requests the HTTP from the URL saved on GitHub where the Mazda M-G procedure PDF file is saved. 
response_mazda_mg = requests.get(url_mazda_mg)
# Save the Mazda M-G procedure PDF file content after the download.
pdf_data_mazda_mg = response_mazda_mg.content

# Requests the HTTP from the URL saved on GitHub where the Mazda M-H procedure PDF file is saved. 
response_mazda_mh = requests.get(url_mazda_mh)
# Save the Mazda M-H procedure PDF file content after the download.
pdf_data_mazda_mh = response_mazda_mh.content


#---------------------------------------------------------------------------------------------#
#                                      FORD FUNCTIONS                                         #
#---------------------------------------------------------------------------------------------#


def keys_starter_theft_161yesno (max_keys_16, min_keys_1, starter_interrupt_yes, theft_light_yes):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_16)
    
    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_1)
    
    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)


def keys_starter_theft_82yesyes (max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_8)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_2)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)


def keys_starter_theft_82noyes (max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_8)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_2)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_no)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)


def keys_starter_theft_823yesyes (max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_8)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_23)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)


def keys_starter_theft_161nono (max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_16)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_1)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_no)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)


def keys_starter_theft_82nono (max_keys_8, min_keys_2, starter_interrupt_no, theft_light_no):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_8)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_2)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_no)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)


def keys_starter_theft_nanayesno (max_keys_na, min_keys_na, starter_interrupt_yes, theft_light_no):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_na)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_na)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)


def keys_starter_theft_82yesno (max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_no):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_8)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_2)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)


def keys_starter_theft_162yesno (max_keys_16, min_keys_2, starter_interrupt_yes, theft_light_no):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_16)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_2)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)

def keys_starter_theft_161yesyes (max_keys_16, min_keys_1, starter_interrupt_yes, theft_light_yes):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_16)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_1)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)

def keys_starter_theft_82nona (max_keys_8, min_keys_2, starter_interrupt_no, theft_light_na):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_8)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_2)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_no)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_na)

def keys_starter_theft_82yesna (max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_8)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_2)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_na)

def keys_starter_theft_82yes10s (max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_10s):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_8)

    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_2)

    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)

    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_10s)

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


#---------------------------------------------------------------------------------------------#
#                                      MAZDA FUNCTIONS                                         #
#---------------------------------------------------------------------------------------------#

def pr_not_required_mazda_ma(pr_not_required, pdf_data_mazda_ma, file_name_ma):
    # Shows whether or not the parameter reset is required
    st.write(pr_not_required)
    # Shows a message to click on the button to download PDF file.
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-A):")
    # Shows the button where the PDF file can be downloaded:
    st.download_button(
    # Labels the button,
    label="Mazda M-A Instructions",
    # contains the PDF file content/data.
    data=pdf_data_mazda_ma,
    # Gets the file name from the respective variable created above. 
    file_name=file_name_ma,
    # PDF file data type.
    mime="application/pdf"
    )

def pr_not_required_mazda_mb(pr_not_required, pdf_data_mazda_mb, file_name_mb):
    # Shows whether or not the parameter reset is required
    st.write(pr_not_required)
    # Shows a message to click on the button to download PDF file.
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-B):")
    # Shows the button where the PDF file can be downloaded:
    st.download_button(
    # Labels the button,
    label="Mazda M-B Instructions",
    # contains the PDF file content/data.
    data=pdf_data_mazda_mb,
    # Gets the file name from the respective variable created above. 
    file_name=file_name_mb,
    # PDF file data type.
    mime="application/pdf"
    )

def pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc):
    # Shows whether or not the parameter reset is required
    st.write(pr_required)
    # Shows a message to click on the button to download PDF file.
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-C):")
    # Shows the button where the PDF file can be downloaded:
    st.download_button(
    # Labels the button,
    label="Mazda M-C Instructions",
    # contains the PDF file content/data.
    data=pdf_data_mazda_mc,
    # Gets the file name from the respective variable created above. 
    file_name=file_name_mc,
    # PDF file data type.
    mime="application/pdf"
    )

def pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md):
    # Shows whether or not the parameter reset is required
    st.write(pr_required)
    # Shows a message to click on the button to download PDF file.
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-D):")
    # Shows the button where the PDF file can be downloaded:
    st.download_button(
    # Labels the button,
    label="Mazda M-D Instructions",
    # contains the PDF file content/data.
    data=pdf_data_mazda_md,
    # Gets the file name from the respective variable created above. 
    file_name=file_name_md,
    # PDF file data type.
    mime="application/pdf"
    )

def pr_required_mazda_me(pr_required, pdf_data_mazda_me, file_name_me):
    # Shows whether or not the parameter reset is required
    st.write(pr_required)
    # Shows a message to click on the button to download PDF file.
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-E):")
    # Shows the button where the PDF file can be downloaded:
    st.download_button(
    # Labels the button,
    label="Mazda M-E Instructions",
    # contains the PDF file content/data.
    data=pdf_data_mazda_me,
    # Gets the file name from the respective variable created above. 
    file_name=file_name_me,
    # PDF file data type.
    mime="application/pdf"
    )

def pr_required_mazda_mf(pr_required, pdf_data_mazda_mf, file_name_mf):
    # Shows whether or not the parameter reset is required
    st.write(pr_required)
    # Shows a message to click on the button to download PDF file.
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-F):")
    # Shows the button where the PDF file can be downloaded:
    st.download_button(
    # Labels the button,
    label="Mazda M-F Instructions",
    # contains the PDF file content/data.
    data=pdf_data_mazda_mf,
    # Gets the file name from the respective variable created above. 
    file_name=file_name_mf,
    # PDF file data type.
    mime="application/pdf"
    )

def pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg):
    # Shows whether or not the parameter reset is required
    st.write(pr_required)
    # Shows a message to click on the button to download PDF file.
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-G):")
    # Shows the button where the PDF file can be downloaded:
    st.download_button(
    # Labels the button,
    label="Mazda M-G Instructions",
    # contains the PDF file content/data.
    data=pdf_data_mazda_mg,
    # Gets the file name from the respective variable created above. 
    file_name=file_name_mg,
    # PDF file data type.
    mime="application/pdf"
    )

def pr_not_required_mazda_mh(pr_required, pdf_data_mazda_mh, file_name_mh):
    # Shows whether or not the parameter reset is required
    st.write(pr_required)
    # Shows a message to click on the button to download PDF file.
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-H):")
    # Shows the button where the PDF file can be downloaded:
    st.download_button(
    # Labels the button,
    label="Mazda M-H Instructions",
    # contains the PDF file content/data.
    data=pdf_data_mazda_mh,
    # Gets the file name from the respective variable created above. 
    file_name=file_name_mh,
    # PDF file data type.
    mime="application/pdf"
    )
#---------------------------------------------------------------------------------------------#
#                                    SIDE BAR + SELECT BOXES                                  #
#---------------------------------------------------------------------------------------------#

# Shows a side bar containing the Makes.
selected_make = st.sidebar.selectbox("Make:",(makes))

if selected_make == 'Ford':
    # If make Ford is selected, shows a side bar containing the Ford models.
    selected_model = st.sidebar.selectbox("Model:",(Ford))
    # Side bar to select the vehicle's year. 
    selected_year = st.sidebar.selectbox("Year:",(year))
elif selected_make == 'Lincoln':
    # If make Lincoln is selected, shows a side bar containing the Lincoln models.
    selected_model = st.sidebar.selectbox("Model:",(Lincoln))
    # Side bar to select the vehicle's year. 
    selected_year = st.sidebar.selectbox("Year:",(year))
elif selected_make == 'Mazda':
    # If make Mazda is selected, shows a side bar containing the Mazda models.
    selected_model = st.sidebar.selectbox("Model:",(Mazda))
    # Side bar to select the vehicle's year. 
    selected_year = st.sidebar.selectbox("Year:",(year))
else:
    # In case none of the above options were selected, shows a side bar containing the Mercury models.
    selected_model = st.sidebar.selectbox("Model:",(Mercury))
    # Side bar to select the vehicle's year. 
    selected_year = st.sidebar.selectbox("Year:",(year))


#---------------------------------------------------------------------------------------------#
#                                    FORD MODELS                                              #
#---------------------------------------------------------------------------------------------#

 
if selected_model == 'C-MAX (Hybrid)':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)

    # Shows a select box from year 1996 to 2023: 
    if selected_year >= 2013:

        # If the above options are selected, shows the parameter reset is required, 
        # PATS type B and the button to download the procedure. 
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)   
    else: 
        # If none of the above options variables are selected, shows that the PATS system is not available.                                                                              
        st.write(pats_not_available)


if selected_model == 'C-MAX (Hybrid) (Push to Start)':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Contour (V6-only)':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.   
        keys_starter_theft_161yesno (max_keys_16, min_keys_1, starter_interrupt_yes, theft_light_yes)

    elif selected_year > 1998 and selected_year <= 2000:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.  
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Crown Victoria':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year >= 2003 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_823yesyes(max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)

if selected_model == 'Edge':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2010:
       pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

       # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
       # whether or not the starter interrupt when there is a theft condition,
       # and whether or not theft light flashes with at ignition off.
       keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2011:
       pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

       # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
       # whether or not the starter interrupt when there is a theft condition,
       # and whether or not theft light flashes with at ignition off.
       keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
       st.write(pats_not_available)

       
if selected_model == 'Edge (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)


    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)
   

if selected_model == 'Escape':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2008:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Escape (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)


    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Escape (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2007:
        pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year >= 2008 and selected_year <= 2012:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'E-Series (Fleet Vehicles)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_g(pr_required, pats_g, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)


    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)

if selected_model == 'E-Series':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2011:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)


    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Excursion':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2005:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Expedition':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1997 and selected_year <= 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)

    elif selected_year >= 1999 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year >= 2003 and selected_year <= 2006:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2007 and selected_year <= 2008:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2009 and selected_year <= 2013:
        pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yes10s(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_10s)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Explorer (4dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year >= 2002 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2006 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Explorer (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)


if selected_model == 'Explorer Sport (2dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year > 2001 and selected_year <= 2003:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Explorer Sport Trac':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year > 2001 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2007 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-150':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2008:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2009 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-150 Harley-Davidson':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2003:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year >= 2006 and selected_year <= 2008:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-150 Heritage':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2006:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-250 (under 8500# GVW)':
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

           # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
           # whether or not the starter interrupt when there is a theft condition,
           # and whether or not theft light flashes with at ignition off.
           keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
        
        # Shows the message "No key relearn required" when selected "No".  
        elif gvw_result1 == False and gvw_result2 == True:
           st.write("No key relearn required")

        # Shows nothing when none of the options are selected.
        elif gvw_result1 == False and gvw_result2 == False:
            st.write()

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-250 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-350 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-450 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-650 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-750 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        
        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'F-Series > 8500 (Stripped Chassis/Cab Chassis)':
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

        # If none of the above options variables are selected, shows that the PATS system is not available.
        else:
            st.write(pats_not_available)
        

if selected_model == 'Fiesta':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_a(pr_required, pats_a, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Fiesta (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)



    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Five Hundred':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Flex':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2009 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)

if selected_model == 'Flex (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Focus':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2008:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Focus (Push to Start) / EV (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)


    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Freestar':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Freestyle':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Fusion / Fusion (hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82nona(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_na)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Fusion (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Fusion (Hybrid) (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Fusion EV (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'GT':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2006:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82nono(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_no)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Mustang':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1996 and selected_year <= 1997:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)

    elif selected_year == 1998:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82nono(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_no)

    elif selected_year >= 1999 and selected_year <= 2004:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year >= 2005 and selected_year <= 2009:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2010 and selected_year <= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Ranger (3.0L & 4.0L ONLY)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2000:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year == 2006:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Ranger (2.3L, 3.0L, & 4.0L)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2004:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2007 and selected_year <= 2010:
        pr_required_pats_g(pr_required, pats_g, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_nanayesno(max_keys_na, min_keys_na, starter_interrupt_yes, theft_light_no)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Taurus (Duratec & SHO only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1996 and selected_year <= 1997:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)

    elif selected_year >= 1998 and selected_year <= 1999:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

   # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Taurus':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2006:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2008 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)

        
if selected_model == 'Taurus (Push to Start / X)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Thunderbird':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2002 and selected_year <= 2006:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Transit':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Transit Connect':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2010 and selected_year <= 2013:
        pr_required_pats_a(pr_required, pats_a, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Windstar':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2000:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2001 and selected_year <= 2003:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


#---------------------------------------------------------------------------------------------#
#                                    LINCOLN MODELS                                           #
#---------------------------------------------------------------------------------------------#

if selected_model == 'Aviator':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2003 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Blackwood':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2002 and selected_year <= 2003:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Continental':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'LS':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2007:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesno(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_no)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Mark LT':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Mark VIII':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1997 and selected_year <= 1998:
        pr_not_required_pats_d(pr_not_required, pats_d, pdf_data_pats_d, file_name_pats_d)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_162yesno(max_keys_16, min_keys_2, starter_interrupt_yes, theft_light_no)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'MKS':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2009 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)

if selected_model == 'MKS / MKS (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2009:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

    # If none of the above options variables are selected, shows that the PATS system is not available.   
    else:
        st.write(pats_not_available)   


if selected_model == 'MKT':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'MKX':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'MKZ':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'MKZ (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Navigator':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)

    elif selected_year >= 1999 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year >= 2003 and selected_year <= 2006:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2007 and selected_year <= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Town Car':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year >= 2003 and selected_year <= 2011:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_823yesyes(max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Zephyr':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2006:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.  
    else:
        st.write(pats_not_available)  


#---------------------------------------------------------------------------------------------#
#                                    MERCURY MODELS                                           #
#---------------------------------------------------------------------------------------------#

if selected_model == 'Cougar':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2002:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Grand Marquis':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year >= 2003 and selected_year <= 2010:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_823yesyes(max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Marauder':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2003 and selected_year <= 2004:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_823yesyes(max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Mariner':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Mariner (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Milan':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Milan (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Montego':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Monterey':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Mountaineer (4dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)

    elif selected_year >= 2002 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2006 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesno(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_no)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Mystique (V-6 only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_161yesyes(max_keys_16, min_keys_1, starter_interrupt_yes, theft_light_yes)

    elif selected_year > 1998 and selected_year <= 2000:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


if selected_model == 'Sable (Duratec only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1996 and selected_year <= 1997:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)

    elif selected_year >= 1998 and selected_year <= 1999:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesno(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    # If none of the above options variables are selected, shows that the PATS system is not available..
    else:
        st.write(pats_not_available)


if selected_model == 'Sable':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)

        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.
        keys_starter_theft_82yesno(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)

    elif selected_year >= 2008 and selected_year <= 2009:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)


#---------------------------------------------------------------------------------------------#
#                                    MAZDA MODELS                                             #
#---------------------------------------------------------------------------------------------#

# Shows a select box with Mazda's models.
if selected_model == '626':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows whether or not the parameter reset is required and the button to download the procedure required. 
    pr_not_required_mazda_ma(pr_not_required, pdf_data_mazda_ma, file_name_ma)

# Shows a select box with Mazda's models.
if selected_model == 'B-Series':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 1999 and selected_year <= 2010:
        # This model year/model matches the security system the same as Ford Ranger. 
        st.write("See Ford Ranger.")
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'CX-3':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2016 and selected_year <= 2020:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'CX-5':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2013 and selected_year <= 2016:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'CX-7':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2007 and selected_year <= 2008:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2009 and selected_year <= 2012:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'CX-7 (Advanced Keyless)':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2007 and selected_year <= 2008:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    elif selected_year >= 2009 and selected_year <= 2012:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_me(pr_required, pdf_data_mazda_me, file_name_me)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'CX-9':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2007 and selected_year <= 2009:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2010 and selected_year <= 2015:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2016 and selected_year <= 2020:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'CX-9 (Advanced Keyless)':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2007 and selected_year <= 2009:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    elif selected_year >= 2010 and selected_year <= 2015:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mf(pr_required, pdf_data_mazda_mf, file_name_mf)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'CX-30':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year == 2020:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_not_required_mazda_mh(pr_not_required, pdf_data_mazda_mh, file_name_mh)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'Mazda2':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2011 and selected_year <= 2015:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'Mazda2 (Advanced Keyless)':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year == 2015:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_me(pr_required, pdf_data_mazda_me, file_name_me)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'Mazda3':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2004 and selected_year <= 2013:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2014 and selected_year <= 2018:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    elif selected_year >= 2019 and selected_year <= 2020:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_not_required_mazda_mh(pr_not_required, pdf_data_mazda_mh, file_name_mh)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'Mazda3 (Advanced Keyless)':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2010 and selected_year <= 2013:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mf(pr_required, pdf_data_mazda_mf, file_name_mf)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'Mazda5':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2007 and selected_year <= 2017:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'Mazda6':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2003 and selected_year <= 2008:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_not_required_mazda_mb(pr_not_required, pdf_data_mazda_mb, file_name_mb)
    elif selected_year >= 2009 and selected_year <= 2013:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2014 and selected_year <= 2020:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'Mazda6 (Advanced Keyless)':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2006 and selected_year <= 2008:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    elif selected_year >= 2009 and selected_year <= 2013:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mf(pr_required, pdf_data_mazda_mf, file_name_mf)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'Millenia':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a message the vehicle is not equipped with security system.
    st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'MPV':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2000 and selected_year <= 2006:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_not_required_mazda_ma(pr_not_required, pdf_data_mazda_ma, file_name_ma)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'MX-5 (Miata)':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year <= 2000:
        # Shows a message the vehicle is not equipped with security system.
        st.write(no_security_system)
    elif selected_year >= 2001 and selected_year <= 2005:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_not_required_mazda_ma(pr_not_required, pdf_data_mazda_ma, file_name_ma)
    elif selected_year >= 2016:
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'MX-5 (Miata) (Advanced Keyless Entry/Start)':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2006 and selected_year <= 2015:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'MX-5 (Miata) (Keyless Entry, Without Keyless Start)':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2006 and selected_year <= 2015:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'Protege':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a message the vehicle is not equipped with security system.
    st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'RX-8':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2004 and selected_year <= 2011:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)

# Shows a select box with Mazda's models.
if selected_model == 'RX-8 (Advanced Keyless)':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2006 and selected_year <= 2011:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)
        
# Shows a select box with Mazda's models.
if selected_model == 'Tribute':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year <= 2001 and selected_year <= 2007:
        # This model year/model matches the security system the same as Ford Ranger. 
        st.write("See Ford Escape.")
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)
