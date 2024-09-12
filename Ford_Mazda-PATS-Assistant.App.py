import streamlit as st
import requests
from PIL import Image
from io import BytesIO


st.set_page_config(
    # Shows the page title.
    page_title="Ford & Mazda PATS Assistant",
    # Shows the page icon on the browser tab.
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded"
)

#---------------------------------------------------------------------------------------------#
#                                    VARIABLES                                                #
#---------------------------------------------------------------------------------------------#


# These variables determine the maximum keys ALLOWED to be programmed.
max_keys_na = 'N/A'
max_keys_8 = 8
max_keys_16 = 16

# These variables determine the Minimum keys REQUIRED to be programmed.
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

# Variable used on the functions to show the PATS status on the vehicle. 
pats_not_available = "The year/make/model selected is not available."
# Variable used on the functions to show the parameter reset is required.
pr_required = 'Parameter reset: Required'
# Variable used on the functions to show the parameter reset IS NOT required.
pr_not_required = 'Parameter reset: Not Required'

# These variables are used on the functions to show which the PATS type the vehicle is equipped with.
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


# This Variable stores the makes to show in the select box.
makes = ['Ford', 'Lincoln', 'Mercury', 'Mazda']

# This variable stores all Ford models to show in the select box.
Ford = ['C-MAX (Hybrid)', 'C-MAX (Hybrid) (Push to Start)', 'Contour (V6-only)', 'Crown Victoria', 'Edge', 'Edge (Push to Start)', 
        'Escape', 'Escape (Push to Start)', 'Escape (Hybrid)', 'E-Series', 'E-Series (Fleet Vehicles)', 'Excursion', 'Expedition', 'Explorer (4dr)', 'Explorer (Push to Start)',
        'Explorer Sport (2dr)', 'Explorer Sport Trac', 'F-150', 'F-150 Harley-Davidson', 'F-150 Heritage', 'F-250 (under 8500# GVW)', 'F-250 Super Duty', 'F-350 Super Duty', 'F-450 Super Duty', 'F-650 Super Duty', 'F-750 Super Duty',
        'F-Series > 8500 (Stripped Chassis/Cab Chassis)', 'Fiesta', 'Fiesta (Push to Start)', 'Five Hundred', 'Flex', 'Flex (Push to Start)', 'Focus', 'Focus (Push to Start) / Focus EV (Push to Start)', 'Freestar', 
        'Freestyle', 'Fusion / Fusion (hybrid)', 'Fusion (Push to Start)', 'Fusion (Hybrid) (Push to Start)', 'Fusion EV (Push to Start)', 'GT', 'Mustang', 'Ranger (3.0L & 4.0L ONLY)', 'Ranger (2.3L, 3.0L, & 4.0L)', 'Taurus (Duratec & SHO only)', 'Taurus', 'Taurus (Push to Start / X)', 
        'Thunderbird', 'Transit', 'Transit Connect', 'Windstar']

# This variable stores all Lincoln models to show in the select box.
Lincoln = ['Aviator', 'Blackwood', 'Continental', 'LS', 'Mark LT', 'Mark VIII', 'MKS / MKS (Push to Start)', 'MKT', 'MKX', 
           'MKZ', 'MKZ (Push to Start)', 'Navigator', 'Town Car', 'Zephyr']

# This variable stores all Mercury models to show in the select box.
Mercury = ['Cougar', 'Grand Marquis', 'Marauder', 'Mariner', 'Mariner (Hybrid)', 'Milan', 'Milan (Hybrid)', 'Montego', 'Monterey', 'Mountaineer (4dr)',
           'Mystique (V-6 only)', 'Sable (Duratec only)', 'Sable']

# This variable stores all Mazda models to show in the select box.
Mazda = ['626', 'B-Series', 'CX-3', 'CX-5', 'CX-7', 'CX-7 (Advanced Keyless)', 'CX-9', 'CX-9 (Advanced Keyless)', 'CX-30', 'Mazda2', 'Mazda2 (Advanced Keyless)', 
         'Mazda3', 'Mazda3 (Advanced Keyless)', 'Mazda5', 'Mazda6', 'Mazda6 (Advanced Keyless)', 'Millenia', 'MPV', 'MX-5 (Miata)', 
         'MX-5 (Miata) (Advanced Keyless Entry/Start)', 'MX-5 (Miata) (Keyless Entry, Without Keyless Start)',
         'Protege', 'RX-8', 'RX-8 (Advanced Keyless)', 'Tribute']

# This variable stores years from 1996 to 2023 to show in the select box.
year = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]


#---------------------------------------------------------------------------------------------#
#                                       FORD FILES                                            #
#---------------------------------------------------------------------------------------------#

# Stores the links from the GitHub raw file with Ford relearn procedures from PATS type A to PATS type G.
# Needs to replace /blob/ for /raw/ on the GitHub, and then the variable will get the raw file (the PDF file).
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

# Stores the links from the GitHub raw file with Mazda procedure from MA to MH.
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

# These functions shows the max (allowed) and mininum keys (required), the status of the starter and the security light.

# Shows the information: 16 max keys are ALLOWED to be programmed, 1 minimum key REQUIRED, starter is interrupted and the security light blinks.
def keys_starter_theft_161yesno (max_keys_16, min_keys_1, starter_interrupt_yes, theft_light_yes):
    # Max keys allowed to be programmed.
    st.write('Max Keys:', max_keys_16)
    # Minimum keys required to be programmed.
    st.write('Minimum Keys Required:', min_keys_1)
    # Whether or not the starter interrupt when there is a theft condition.
    st.write('Starter Interrupt Present:', starter_interrupt_yes)
    # Whether or not theft light flashes with at ignition off.
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)

# Shows the information: 8 max keys are ALLOWED to be programmed, 2 minimum keys REQUIRED, starter is interrupted and the security light blinks.
def keys_starter_theft_82yesyes (max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes):
    st.write('Max Keys:', max_keys_8)
    st.write('Minimum Keys Required:', min_keys_2)
    st.write('Starter Interrupt Present:', starter_interrupt_yes)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)

# Shows the information: 8 max keys are ALLOWED to be programmed, 2 minimum keys REQUIRED, starter IS NOT interrupted and the security light blinks.
def keys_starter_theft_82noyes (max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes):
    st.write('Max Keys:', max_keys_8)
    st.write('Minimum Keys Required:', min_keys_2)
    st.write('Starter Interrupt Present:', starter_interrupt_no)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)

# Shows the information: 8 max keys are ALLOWED to be programmed, 2 OR 3 minimum keys REQUIRED, starter is interrupted and the security light blinks.
def keys_starter_theft_823yesyes (max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes):
    st.write('Max Keys:', max_keys_8)
    st.write('Minimum Keys Required:', min_keys_23)
    st.write('Starter Interrupt Present:', starter_interrupt_yes)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)

# Shows the information: 16 max keys are ALLOWED to be programmed, 1 minimum keys REQUIRED, starter IS NOT interrupted and the security light DOES NOT blink.
def keys_starter_theft_161nono (max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no):
    st.write('Max Keys:', max_keys_16)
    st.write('Minimum Keys Required:', min_keys_1)
    st.write('Starter Interrupt Present:', starter_interrupt_no)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)

# Shows the information: 8 max keys are ALLOWED to be programmed, 2 minimum keys REQUIRED, starter IS NOT interrupted and the security light DOES NOT blink.
def keys_starter_theft_82nono (max_keys_8, min_keys_2, starter_interrupt_no, theft_light_no):
    st.write('Max Keys:', max_keys_8)
    st.write('Minimum Keys Required:', min_keys_2)
    st.write('Starter Interrupt Present:', starter_interrupt_no)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)

# Shows the information: max keys ALLOWED and minimum key REQUIRED are n/a, starter IS interrupted and the security light DOES NOT blink.
def keys_starter_theft_nanayesno (max_keys_na, min_keys_na, starter_interrupt_yes, theft_light_no):
    st.write('Max Keys:', max_keys_na)
    st.write('Minimum Keys Required:', min_keys_na)
    st.write('Starter Interrupt Present:', starter_interrupt_yes)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)

# Shows the information: 8 max keys are ALLOWED to be programmed, 2 minimum keys REQUIRED, starter IS interrupted and the security light DOES NOT blink.
def keys_starter_theft_82yesno (max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_no):
    st.write('Max Keys:', max_keys_8)
    st.write('Minimum Keys Required:', min_keys_2)
    st.write('Starter Interrupt Present:', starter_interrupt_yes)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)

# Shows the information: 16 max keys are ALLOWED to be programmed, 2 minimum keys REQUIRED, starter IS interrupted and the security light DOES NOT blink.
def keys_starter_theft_162yesno (max_keys_16, min_keys_2, starter_interrupt_yes, theft_light_no):
    st.write('Max Keys:', max_keys_16)
    st.write('Minimum Keys Required:', min_keys_2)
    st.write('Starter Interrupt Present:', starter_interrupt_yes)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_no)

# Shows the information: 16 max keys are ALLOWED to be programmed, 1 minimum key REQUIRED, starter IS interrupted and the security light blinks.
def keys_starter_theft_161yesyes (max_keys_16, min_keys_1, starter_interrupt_yes, theft_light_yes):
    st.write('Max Keys:', max_keys_16)
    st.write('Minimum Keys Required:', min_keys_1)
    st.write('Starter Interrupt Present:', starter_interrupt_yes)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_yes)

# Shows the information: 8 max keys are ALLOWED to be programmed, 2 minimum keys REQUIRED, starter IS NOT interrupted and the security light is N/A.
def keys_starter_theft_82nona (max_keys_8, min_keys_2, starter_interrupt_no, theft_light_na):
    st.write('Max Keys:', max_keys_8)
    st.write('Minimum Keys Required:', min_keys_2)
    st.write('Starter Interrupt Present:', starter_interrupt_no)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_na)

# Shows the information: 8 max keys are ALLOWED to be programmed, 2 minimum keys REQUIRED, starter IS interrupted and the security light is N/A.
def keys_starter_theft_82yesna (max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na):
    st.write('Max Keys:', max_keys_8)
    st.write('Minimum Keys Required:', min_keys_2)
    st.write('Starter Interrupt Present:', starter_interrupt_yes)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_na)

# Shows the information: 8 max keys are ALLOWED to be programmed, 2 minimum keys REQUIRED, starter IS interrupted and the security light for 10 SECONDS.
def keys_starter_theft_82yes10s (max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_10s):
    st.write('Max Keys:', max_keys_8)
    st.write('Minimum Keys Required:', min_keys_2)
    st.write('Starter Interrupt Present:', starter_interrupt_yes)
    st.write('Theft Indicator Flashes at Ignition OFF:', theft_light_10s)

# These funtions show whether or not the parameter reset is required, an instruction and the sets up a button to download the procedure required.  
def pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g):
    # Shows parameter reset IS required.
    st.write(pr_required)
    # Shows a message to the user.
    st.write("Click on the button to download the Parameter Reset Instructions:")
    # Sets up the button to download the procedure required.
    st.download_button(
    # Labels the button.
    label="Parameter Reset Instructions",
    # Stores PDF data file with parameter reset PATS b_c_f_g type.
    data=pdf_data_pr_b_c_f_g,
    # Labels the file after downloading.
    file_name=file_name_b_c_f_g,
    # File data type.
    mime="application/pdf"
    )

def pr_required_pats_a(pr_required, pats_a, pdf_data_pr_c, file_name_c):
    st.write(pr_required)
    # Shows the vehicle is equipped with the PATS A type.
    st.write(pats_a)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    # Stores PDF data file with parameter reset PATS C type.
    data=pdf_data_pr_c,
    file_name=file_name_c,
    mime="application/pdf"
    )

def pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g):
    st.write(pr_required)
    # Shows the vehicle is equipped with the PATS A type.h.
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
    # Shows the vehicle is equipped with the PATS C type.
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
    # Shows the vehicle is equipped with the PATS G type.
    st.write(pats_g)
    st.write("Click on the button to download the Parameter Reset Instructions:")
    st.download_button(
    label="Parameter Reset Instructions",
    data=pdf_data_pr_b_c_f_g,
    file_name=file_name_b_c_f_g,
    mime="application/pdf"
    )

def pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a):
    # Shows parameter reset IS NOT required.
    st.write(pr_not_required)
    # Shows the vehicle is equipped with the PATS A type.
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
    # Shows the vehicle is equipped with the PATS C type.
    st.write(pats_c)
    st.write("Click on the button to download the PATS Instructions:")
    st.download_button(
    label="PATS Instructions",
    data=pdf_data_pats_a,
    file_name=file_name_pats_a,
    mime="application/pdf"
    )

def pr_not_required_pats_d(pr_not_required, pats_d, pdf_data_pats_d, file_name_pats_d):
    # Shows parameter reset IS NOT required.
    st.write(pr_not_required)
    # Shows the vehicle is equipped with the PATS D type.
    st.write(pats_d)
    st.write("Click on the button to download the PATS D Instructions:")
    st.download_button(
    label="PATS A Instructions",
    data=pdf_data_pats_d,
    file_name=file_name_pats_d,
    mime="application/pdf"
    )
    
def pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e):
    # Shows parameter reset IS NOT required.
    st.write(pr_not_required)
    # Shows the vehicle is equipped with the PATS E type.
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
    # Shows parameter reset IS NOT required.
    st.write(pr_not_required)
    # Shows a message to the user.
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-A):")
    # Sets up the button to download the procedure required.
    st.download_button(
    # Labels the button,
    label="Mazda M-A Instructions",
    # Stores PDF data file with Mazda M-A procedure.
    data=pdf_data_mazda_ma,
    # Labels the file after downloading. 
    file_name=file_name_ma,
    # File data type.
    mime="application/pdf"
    )

def pr_not_required_mazda_mb(pr_not_required, pdf_data_mazda_mb, file_name_mb):
    st.write(pr_not_required)
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-B):")
    st.download_button(
    label="Mazda M-B Instructions",
    # Stores PDF data file with Mazda M-B procedure.
    data=pdf_data_mazda_mb,
    file_name=file_name_mb,
    mime="application/pdf"
    )

def pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc):
    # Shows parameter reset IS required.
    st.write(pr_required)
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-C):")
    st.download_button(
    label="Mazda M-C Instructions",
    # Stores PDF data file with Mazda M-C procedure.
    data=pdf_data_mazda_mc,
    file_name=file_name_mc,
    mime="application/pdf"
    )

def pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md):
    st.write(pr_required)
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-D):")
    st.download_button(
    label="Mazda M-D Instructions",
    # Stores PDF data file with Mazda M-D procedure.
    data=pdf_data_mazda_md,
    file_name=file_name_md,
    mime="application/pdf"
    )

def pr_required_mazda_me(pr_required, pdf_data_mazda_me, file_name_me):
    st.write(pr_required)
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-E):")
    st.download_button(
    label="Mazda M-E Instructions",
    # Stores PDF data file with Mazda M-E procedure.
    data=pdf_data_mazda_me,
    file_name=file_name_me,
    mime="application/pdf"
    )

def pr_required_mazda_mf(pr_required, pdf_data_mazda_mf, file_name_mf):
    st.write(pr_required)
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-F):")
    st.download_button(
    label="Mazda M-F Instructions",
    # Stores PDF data file with Mazda M-F procedure.
    data=pdf_data_mazda_mf,
    file_name=file_name_mf,
    mime="application/pdf"
    )

def pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg):
    st.write(pr_required)
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-G):")
    st.download_button(
    label="Mazda M-G Instructions",
    # Stores PDF data file with Mazda M-G procedure.
    data=pdf_data_mazda_mg,
    file_name=file_name_mg,
    mime="application/pdf"
    )

def pr_not_required_mazda_mh(pr_required, pdf_data_mazda_mh, file_name_mh):
    st.write(pr_required)
    st.write("Click on the button to download the Immobilizer Programming Procedure (M-H):")
    st.download_button(
    label="Mazda M-H Instructions",
    # Stores PDF data file with Mazda M-H procedure.
    data=pdf_data_mazda_mh,
    file_name=file_name_mh,
    mime="application/pdf"
    )

#---------------------------------------------------------------------------------------------#
#                                  SIDE BAR + SELECT BOXES AND LOGO                           #
#---------------------------------------------------------------------------------------------#

# Stores the links from the GitHub raw file with make logos.
# Needs to remove /blob/ and replace https://github.com/... for https://raw.githubusercontent.com..., then the variable stores the raw file.   
url_fordlogo = "https://raw.githubusercontent.com/weversonbarbieri/Ford_Mazda-PATS-Assistant.App/main/ford_logo.jpg"
url_lincolnlogo = "https://raw.githubusercontent.com/weversonbarbieri/Ford_Mazda-PATS-Assistant.App/main/lincoln_logo.jpeg"
url_mercurylogo = "https://raw.githubusercontent.com/weversonbarbieri/Ford_Mazda-PATS-Assistant.App/main/mercury_logo.jpeg"
url_mazdalogo = "https://raw.githubusercontent.com/weversonbarbieri/Ford_Mazda-PATS-Assistant.App/main/mazdalogo.png"

# The response vairables get the links info and confirms whether it is readable (200) or not (404).
response_fordlogo = requests.get(url_fordlogo)
response_lincolnlogo = requests.get(url_lincolnlogo)
response_mercurylogo = requests.get(url_mercurylogo)
response_mazdalogo = requests.get(url_mazdalogo)

# Opens the image using PIL and response..._logo.content where the image content was got after reading the URL. 
image_fordlogo = Image.open(BytesIO(response_fordlogo.content))
image_lincolnlogo = Image.open(BytesIO(response_lincolnlogo.content))
image_mercurylogo = Image.open(BytesIO(response_mercurylogo.content))
image_mazdalogo = Image.open(BytesIO(response_mazdalogo.content))

# Shows a side bar containing the Makes.
selected_make = st.sidebar.selectbox("Make:",(makes))

if selected_make == 'Ford':
    # Shows the header based on the make selected using HTML.
    st.write("<div align='center'><h2><i>Ford Anti-theft System</i></h2></div>", unsafe_allow_html=True)
    st.write("")
    # Shows the Ford logo when the make Ford is selected.
    st.image(image_fordlogo, width=100)
    # If make Ford is selected, shows a side bar containing the Ford models.
    selected_model = st.sidebar.selectbox('Model:',(Ford))
    # Shows years from 1996 to 2023 to select the vehicle's year. 
    selected_year = st.sidebar.selectbox("Year:",(year))
elif selected_make == 'Lincoln':
    st.write("<div align='center'><h2><i>Lincoln Anti-theft System</i></h2></div>", unsafe_allow_html=True)
    st.write("")
    # Shows the Lincoln logo when the make Lincoln is selected.
    st.image(image_lincolnlogo, width=100)
    # If make Lincoln is selected, shows a side bar containing the Lincoln models.
    selected_model = st.sidebar.selectbox("Model:",(Lincoln)) 
    selected_year = st.sidebar.selectbox("Year:",(year))
elif selected_make == 'Mazda':
    st.write("<div align='center'><h2><i>Mazda Anti-theft System</i></h2></div>", unsafe_allow_html=True)
    st.write("")
    # Shows the Mazda logo when the make Lincoln is selected.
    st.image(image_mazdalogo, width=100)
    # If make Mazda is selected, shows a side bar containing the Mazda models.
    selected_model = st.sidebar.selectbox("Model:",(Mazda)) 
    selected_year = st.sidebar.selectbox("Year:",(year))
else:
    st.write("<div align='center'><h2><i>Mercury Anti-theft System</i></h2></div>", unsafe_allow_html=True)
    st.write("")
    # Shows the Mercury logo when the make Lincoln is selected.
    st.image(image_mercurylogo, width=100)
    # In case none of the above options were selected, shows a side bar containing the Mercury models.
    selected_model = st.sidebar.selectbox("Model:",(Mercury)) 
    selected_year = st.sidebar.selectbox("Year:",(year))


#---------------------------------------------------------------------------------------------#
#                                    FORD MODELS                                              #
#---------------------------------------------------------------------------------------------#

# The information of the anti-theft system is displayed according to the selected model and year.
# This condition was created for each Ford model

if selected_model == 'C-MAX (Hybrid)':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        # If the above options are selected, shows whether or not the parameter reset is required, 
        # the PATS type the vehicle is equipped with and the button to download the procedure. 
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)   
    else: 
        # If none of the above options variables are selected, shows that the PATS system is not available.                                                                              
        st.write(pats_not_available)

if selected_model == 'C-MAX (Hybrid) (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'Contour (V6-only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
        # Shows the maximum keys allowed to be programmed, the minimum keys required to be programmed,
        # whether or not the starter interrupt when there is a theft condition,
        # and whether or not theft light flashes with at ignition off.   
        keys_starter_theft_161yesno (max_keys_16, min_keys_1, starter_interrupt_yes, theft_light_yes)
    elif selected_year > 1998 and selected_year <= 2000:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)  
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(pats_not_available)

if selected_model == 'Crown Victoria':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year >= 2003 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_823yesyes(max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Edge':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2010:
       pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
       keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2011:
       pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
       keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
       st.write(pats_not_available)

if selected_model == 'Edge (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    else:
        st.write(pats_not_available)
   
if selected_model == 'Escape':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2008:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Escape (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    else:
        st.write(pats_not_available)

if selected_model == 'Escape (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2007:
        pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    elif selected_year >= 2008 and selected_year <= 2012:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'E-Series (Fleet Vehicles)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_g(pr_required, pats_g, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    else:
        st.write(pats_not_available)

if selected_model == 'E-Series':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2011:
        st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
        pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    else:
        st.write(pats_not_available)

if selected_model == 'Excursion':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2005:
        # If the above options are selected, shows whether or not the parameter reset is required, 
        # the PATS type the vehicle is equipped with and the button to download the procedure.
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
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)
    elif selected_year >= 1999 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year >= 2003 and selected_year <= 2006:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2007 and selected_year <= 2008:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2009 and selected_year <= 2013:
        pr_required_no_pats(pr_required, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yes10s(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_10s)
    else:
        st.write(pats_not_available)

if selected_model == 'Explorer (4dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year >= 2002 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2006 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    else:
        st.write(pats_not_available)

if selected_model == 'Explorer (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)

if selected_model == 'Explorer Sport (2dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year > 2001 and selected_year <= 2003:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Explorer Sport Trac':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year > 2001 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2007 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'F-150':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2008:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2009 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    elif selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'F-150 Harley-Davidson':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2003:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year >= 2006 and selected_year <= 2008:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'F-150 Heritage':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2006:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    else:
        st.write(pats_not_available)

# Stores the url used to check the GVW.
VIN_decode_url = 'https://www.ford-trucks.com/forums/vindecoder.php'

if selected_model == 'F-250 (under 8500# GVW)':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2000:
        # Shows a message to click on the lick and follow the steps to check the GVW.  
        st.write(f'Open the link {VIN_decode_url} and follow the steps below to confirm the GVW:')
        # Shows a message with the step 1.
        st.write('1. Copy and paste the VIN# below the field "Enter VIN"')
        # Shows a message with the step 2.
        st.write('2. Click on the "Decode" button to open the vehicle info.')
        # Shows a message with the step 3.
        st.write('3. Select the the TAB Tech Specs.') 
        # Shows a message with the step 4.
        st.write('4. Go to the field "Gross Vehicle Weight Rating Cap" to see the GVW.')
        # After confirming the GVW, shows a question.
        st.write("Is the Gross Vehicle Weight Rating Cap > 8500?")
        # Shows the option to be checked marked if the GVW is > 8500. 
        gvw_result1 = st.checkbox('Yes.')
        # Shows the option to be checked marked if the GVW is < 8500.
        gvw_result2 = st.checkbox('No.')
        # This condition is needed to show the information regarding the security system based on GVW answer.
        if gvw_result1 == True and gvw_result2 == False:
           # If the above options are selected, shows whether or not the parameter reset is required, 
           # the PATS type the vehicle is equipped with and the button to download the procedure.
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
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'F-350 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'F-450 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'F-650 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'F-750 Super Duty':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
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
        else:
            st.write(pats_not_available)
        
if selected_model == 'Fiesta':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_a(pr_required, pats_a, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'Fiesta (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'Five Hundred':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Flex':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2009 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'Flex (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'Focus':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2008:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'Focus (Push to Start) / EV (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'Freestar':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Freestyle':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'Fusion / Fusion (hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82nona(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'Fusion (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    else:
        st.write(pats_not_available)

if selected_model == 'Fusion (Hybrid) (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    else:
        st.write(pats_not_available)

if selected_model == 'Fusion EV (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    else:
        st.write(pats_not_available)

if selected_model == 'GT':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2006:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82nono(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_no)
    else:
        st.write(pats_not_available)

if selected_model == 'Mustang':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1996 and selected_year <= 1997:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)
    elif selected_year == 1998:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82nono(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_no)
    elif selected_year >= 1999 and selected_year <= 2004:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year >= 2005 and selected_year <= 2009:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2010 and selected_year <= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Ranger (3.0L & 4.0L ONLY)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2000:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year == 2006:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Ranger (2.3L, 3.0L, & 4.0L)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2001 and selected_year <= 2004:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2007 and selected_year <= 2010:
        pr_required_pats_g(pr_required, pats_g, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_nanayesno(max_keys_na, min_keys_na, starter_interrupt_yes, theft_light_no)
    else:
        st.write(pats_not_available)

if selected_model == 'Taurus (Duratec & SHO only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1996 and selected_year <= 1997:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)
    elif selected_year >= 1998 and selected_year <= 1999:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Taurus':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2006:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2008 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesna(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_na)
    else:
        st.write(pats_not_available)

if selected_model == 'Taurus (Push to Start / X)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'Thunderbird':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2002 and selected_year <= 2006:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Transit':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Transit Connect':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2010 and selected_year <= 2013:
        pr_required_pats_a(pr_required, pats_a, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Windstar':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2000:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2001 and selected_year <= 2003:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

#---------------------------------------------------------------------------------------------#
#                                    LINCOLN MODELS                                           #
#---------------------------------------------------------------------------------------------#

# The information of the anti-theft system is displayed according to the selected model and year.
# This condition was created for each LINCOLN model

if selected_model == 'Aviator':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2003 and selected_year <= 2005:
        # If the above options are selected, shows whether or not the parameter reset is required, 
        # the PATS type the vehicle is equipped with and the button to download the procedure.
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
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Continental':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'LS':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2007:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesno(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_no)
    else:
        st.write(pats_not_available)

if selected_model == 'Mark LT':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Mark VIII':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1997 and selected_year <= 1998:
        pr_not_required_pats_d(pr_not_required, pats_d, pdf_data_pats_d, file_name_pats_d)
        keys_starter_theft_162yesno(max_keys_16, min_keys_2, starter_interrupt_yes, theft_light_no)
    else:
        st.write(pats_not_available)

if selected_model == 'MKS':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2009 and selected_year <= 2012:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'MKS / MKS (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2009:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)   
    else:
        st.write(pats_not_available)   

if selected_model == 'MKT':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'MKX':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007:
        # If the above options are selected, shows whether or not the parameter reset is required, 
        # the PATS type the vehicle is equipped with and the button to download the procedure.
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
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'MKZ (Push to Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
    else:
        st.write(pats_not_available)

if selected_model == 'Navigator':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)
    elif selected_year >= 1999 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year >= 2003 and selected_year <= 2006:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2007 and selected_year <= 2013:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Town Car':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2002:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year >= 2003 and selected_year <= 2011:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_823yesyes(max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Zephyr':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2006:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)  
    else:
        st.write(pats_not_available)  

#---------------------------------------------------------------------------------------------#
#                                    MERCURY MODELS                                           #
#---------------------------------------------------------------------------------------------#

# The information of the anti-theft system is displayed according to the selected model and year.
# This condition was created for each MERCURY model.

if selected_model == 'Cougar':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2002:
        # If the above options are selected, shows whether or not the parameter reset is required, 
        # the PATS type the vehicle is equipped with and the button to download the procedure.
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
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year >= 2003 and selected_year <= 2010:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_823yesyes(max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Marauder':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2003 and selected_year <= 2004:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_823yesyes(max_keys_8, min_keys_23, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Mariner':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e,pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'Mariner (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2008 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'Milan':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Milan (Hybrid)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

if selected_model == 'Montego':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2005 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Monterey':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2007:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Mountaineer (4dr)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1998 and selected_year <= 2001:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82noyes(max_keys_8, min_keys_2, starter_interrupt_no, theft_light_yes)
    elif selected_year >= 2002 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2006 and selected_year <= 2010:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
        keys_starter_theft_82yesno(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_no)
    else:
        st.write(pats_not_available)

if selected_model == 'Mystique (V-6 only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 1998:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
        keys_starter_theft_161yesyes(max_keys_16, min_keys_1, starter_interrupt_yes, theft_light_yes)
    elif selected_year > 1998 and selected_year <= 2000:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesyes(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Sable (Duratec only)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1996 and selected_year <= 1997:
        pr_not_required_pats_a(pr_not_required, pats_a, pdf_data_pats_a, file_name_pats_a)
        keys_starter_theft_161nono(max_keys_16, min_keys_1, starter_interrupt_no, theft_light_no)
    elif selected_year >= 1998 and selected_year <= 1999:
        pr_required_pats_b(pr_required, pats_b, pdf_data_pr_b_c_f_g, file_name_b_c_f_g)
        keys_starter_theft_82yesno(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    else:
        st.write(pats_not_available)

if selected_model == 'Sable':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2005:
        pr_not_required_pats_e(pr_not_required, pats_e, pdf_data_pats_e, file_name_pats_e)
        keys_starter_theft_82yesno(max_keys_8, min_keys_2, starter_interrupt_yes, theft_light_yes)
    elif selected_year >= 2008 and selected_year <= 2009:
        pr_required_pats_c(pr_required, pats_c, pdf_data_pr_c, file_name_c)
    else:
        st.write(pats_not_available)

#---------------------------------------------------------------------------------------------#
#                                    MAZDA MODELS                                             #
#---------------------------------------------------------------------------------------------#

# The information of the anti-theft system is displayed according to the selected model and year.
# This condition was created for each MAZDA model.

if selected_model == '626':
    # Shows the year, make and model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows whether or not the parameter reset is required and the button to download the procedure required. 
    pr_not_required_mazda_ma(pr_not_required, pdf_data_mazda_ma, file_name_ma)

if selected_model == 'B-Series':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 1999 and selected_year <= 2010:
        # This model year/model matches the security system the same as Ford Ranger. 
        st.write("See Ford Ranger.")
    else:
        st.write(no_security_system)

if selected_model == 'CX-3':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2016 and selected_year <= 2020:
        # Shows whether or not the parameter reset is required and the button to download the procedure required.
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    else:
        st.write(no_security_system)

if selected_model == 'CX-5':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2013 and selected_year <= 2016:
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    else:
        st.write(no_security_system)

if selected_model == 'CX-7':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2008:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2009 and selected_year <= 2012:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    else:
        st.write(no_security_system)

if selected_model == 'CX-7 (Advanced Keyless)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2008:
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    elif selected_year >= 2009 and selected_year <= 2012:
        pr_required_mazda_me(pr_required, pdf_data_mazda_me, file_name_me)
    else:
        st.write(no_security_system)

if selected_model == 'CX-9':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2009:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2010 and selected_year <= 2015:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2016 and selected_year <= 2020:
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    else:
        st.write(no_security_system)

if selected_model == 'CX-9 (Advanced Keyless)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2009:
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    elif selected_year >= 2010 and selected_year <= 2015:
        pr_required_mazda_mf(pr_required, pdf_data_mazda_mf, file_name_mf)
    else:
        st.write(no_security_system)

if selected_model == 'CX-30':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2020:
        pr_not_required_mazda_mh(pr_not_required, pdf_data_mazda_mh, file_name_mh)
    else:
        st.write(no_security_system)

if selected_model == 'Mazda2':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2011 and selected_year <= 2015:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    else:
        st.write(no_security_system)

if selected_model == 'Mazda2 (Advanced Keyless)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year == 2015:
        pr_required_mazda_me(pr_required, pdf_data_mazda_me, file_name_me)
    else:
        st.write(no_security_system)

if selected_model == 'Mazda3':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2013:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2014 and selected_year <= 2018:
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    elif selected_year >= 2019 and selected_year <= 2020:
        pr_not_required_mazda_mh(pr_not_required, pdf_data_mazda_mh, file_name_mh)
    else:
        st.write(no_security_system)

if selected_model == 'Mazda3 (Advanced Keyless)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2010 and selected_year <= 2013:
        pr_required_mazda_mf(pr_required, pdf_data_mazda_mf, file_name_mf)
    else:
        st.write(no_security_system)

if selected_model == 'Mazda5':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2007 and selected_year <= 2017:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    else:
        st.write(no_security_system)

if selected_model == 'Mazda6':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2003 and selected_year <= 2008:
        pr_not_required_mazda_mb(pr_not_required, pdf_data_mazda_mb, file_name_mb)
    elif selected_year >= 2009 and selected_year <= 2013:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    elif selected_year >= 2014 and selected_year <= 2020:
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    else:
        st.write(no_security_system)

if selected_model == 'Mazda6 (Advanced Keyless)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2008:
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    elif selected_year >= 2009 and selected_year <= 2013:
        pr_required_mazda_mf(pr_required, pdf_data_mazda_mf, file_name_mf)
    else:
        st.write(no_security_system)

if selected_model == 'Millenia':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    st.write(no_security_system)

if selected_model == 'MPV':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2000 and selected_year <= 2006:
        pr_not_required_mazda_ma(pr_not_required, pdf_data_mazda_ma, file_name_ma)
    else:
        st.write(no_security_system)

if selected_model == 'MX-5 (Miata)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year <= 2000:
        st.write(no_security_system)
    elif selected_year >= 2001 and selected_year <= 2005:
        pr_not_required_mazda_ma(pr_not_required, pdf_data_mazda_ma, file_name_ma)
    elif selected_year >= 2016:
        pr_required_mazda_mg(pr_required, pdf_data_mazda_mg, file_name_mg)
    else:
        st.write(no_security_system)

if selected_model == 'MX-5 (Miata) (Advanced Keyless Entry/Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2015:
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    else:
        st.write(no_security_system)

if selected_model == 'MX-5 (Miata) (Keyless Entry, Without Keyless Start)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2015:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    else:
        st.write(no_security_system)

if selected_model == 'Protege':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    st.write(no_security_system)

if selected_model == 'RX-8':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2004 and selected_year <= 2011:
        pr_required_mazda_mc(pr_required, pdf_data_mazda_mc, file_name_mc)
    else:
        st.write(no_security_system)

if selected_model == 'RX-8 (Advanced Keyless)':
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    if selected_year >= 2006 and selected_year <= 2011:
        pr_required_mazda_md(pr_required, pdf_data_mazda_md, file_name_md)
    else:
        st.write(no_security_system)

if selected_model == 'Tribute':
    # Shows the year/make/model selected.
    st.write('Vehicle Selected:', selected_year, selected_make, selected_model)
    # Shows a select box with year from 1996 to 2023.
    if selected_year >= 2001 and selected_year <= 2007:
        # This model year/model matches the security system the same as Ford Ranger. 
        st.write("See Ford Escape.")
    # If none of the above options variables are selected, shows that the PATS system is not available.
    else:
        st.write(no_security_system)
