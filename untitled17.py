import streamlit as st
import pandas as pd
import numpy as np
import tabula as tb
import glob, os
import pdfplumber

st.title('Test')

DATE_COLUMN = 'date/time'

notice = st.selectbox(
     'What notice is this file?',
     ('First Notice', 'Second Notice', 'Final Notice'))

st.write('Please upload the proofs in the first uploader and the State Contact Shet in the second uploader')

proofs_data = st.file_uploader("Upload Proofs PDF", type=["pdf"])
state_data = st.file_uploader("Upload the State Contact Info Sheet", type = ["csv"])
print_data = st.file_uploader("Upload Print Files", type=["csv"])


total_lines = []
def string_cleaning(s):
    try:
        s = s.replace(" ", "")
        s = s.lower()
    except:
        pass
    return s
def string_stripping(s):
    try:
        s = s.strip()
    except:
        pass
    return s
def xa_cleaning(s):
    try:
        s = s.replace('\n', ' ')
        s = s.replace('\xad', '-')
        s = s.replace('\xa0', ' ')
    except:
        pass
    return s

def show_pdf(file_path):
    with open(file_path) as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
     
def compare_dict(df6, proofs_dictionary):
    counter = 0
    if (proofs_dictionary['Form Identification'] == 'BLS 3023 - Industry Verification Form'):
        pass
    else:
        st.write('Wrong Identification')
        st.write("Proof's Form Identification = " + proofs_dictionary['Form Identification'])
        st.write("Correct Form Identification = BLS 3023 - Industry Verification Form")
        counter = 1
    if (proofs_dictionary['OMB Clearance Information'] == 'O.M.B. No. 1220-0032'):
        pass
    else:
        st.write('Wrong OMB info')
        st.write("Proof's OMB Clearance Information = " + proofs_dictionary['OMB Clearance Information'])
        st.write("Correct Form Identification = O.M.B. No. 1220-0032")
        counter = 1
    if (string_cleaning(df6['State Agency Name (50 char)'].iloc[0]) == string_cleaning(proofs_dictionary['State Agency Name'])):
        pass
        if (df6['Abbreviation'].iloc[0] == proofs_dictionary['Abbreviation']):
            pass
        else:
            pass
        if (string_cleaning(df6['Department Name (50 char)'].iloc[0]) == string_cleaning(proofs_dictionary['Department Name'])):
            pass
        else:
            st.write('Different Department Name')
            st.write("Proof's Department Name = " + proofs_dictionary['Department Name'])
            st.write("Print File's Department Name = " + df6['Department Name (50 char)'].iloc[0])
            counter = 1
        if (string_cleaning(df6['Return Address'].iloc[0]) == string_cleaning(proofs_dictionary['Return Address'])):
            pass
        else:
            st.write('Different Return Address')
            st.write("Proof's Return Address = " + proofs_dictionary['Return Address'])
            st.write("Print File's Return Address = " + df6['Return Address'].iloc[0])
            counter = 1
        if (string_cleaning(df6['Return Address Line 2'].iloc[0]) == xa_cleaning(string_cleaning(proofs_dictionary['Return Address Line 2']))):
            pass
        else:
            st.write('Different Return Address 2')
            st.write("Proof's Return Address Line 2 = " + proofs_dictionary['Return Address Line 2'])
            st.write("Print File's Return Address Line 2 = " + df6['Return Address Line 2'].iloc[0])
            counter = 1
        if (df6['Return Address Zip Code'].iloc[0] == proofs_dictionary['Return Address Zip Code']):
            pass
        else:
            st.write('Different Return Zip Code')
            st.write("Proof's Return Zip Code = " + proofs_dictionary['Return Address Zip Code'])
            st.write("Print File's Return Zip Code = " + df6['Return Address Zip Code'].iloc[0])
            counter = 1
        if (df6['Phone Number'].iloc[0] == proofs_dictionary['Phone Number']):
            pass
        else:
            st.write('Different Phone Number')
            st.write("Proof's Phone Number = " + proofs_dictionary['Phone Number'])
            st.write("Print File's Phone Number = " + df6['Phone Number'].iloc[0])
            counter = 1
        if (df6['Print (Y/N)'].iloc[0] == proofs_dictionary['Print Email']):
            if (df6['Print (Y/N)'].iloc[0] == 'N'):
                pass
            else:
                if (df6['Email Address to be printed on ARS Letters'].iloc[0] == proofs_dictionary['Email']):
                    pass
                else:
                    st.write('Different Email')
                    st.write("Proof's Email = " + proofs_dictionary['Email'])
                    st.write("Print File's Email = " + df6['Email Address to be printed on ARS Letters'].iloc[0])
                    counter = 1
    else:
        st.write('Different State Agency Name')
        st.write("Proof's State Agency Name = " + proofs_dictionary['State Agency Name'])
        st.write("Print File's State Agency Name = " + df6['State Agency Name (50 char)'].iloc[0])
        counter = 1
    if (df6['BMA_Area_Code_1'].iloc[0] == proofs_dictionary['BA_ZIP_5']):
        pass
    else:
        st.write('Different ZIP 5')
        st.write("Proof's ZIP 5 = " + proofs_dictionary['BA_ZIP_5'])
        st.write("Print File's ZIP 5 = " + df6['BMA_Area_Code_1'].iloc[0])
        counter = 1
    if (df6['BMA_Area_Code_2'].iloc[0] == proofs_dictionary['BA_ZIP_4']):
        pass
    else:
        st.write('Different ZIP 4')
        st.write("Proof's ZIP 4 = " + proofs_dictionary['BA_ZIP_4'])
        st.write("Print File's ZIP 4 = " + df6['BMA_Area_Code_2'].iloc[0])
        counter = 1
    if (df6['State Agency Name'].iloc[0] == proofs_dictionary['the State Agency Name 1']):
        pass
    else:
        st.write('Different the State Agency Name 1')
        counter = 1
    if (df6['State Agency Name'].iloc[0] == proofs_dictionary['the State Agency Name 2']):
        pass
    else:
        st.write('Different the State Agency Name 2')
        counter = 1
    if (string_stripping(df6['BMA_City'].iloc[0]) == proofs_dictionary['BA_City']):
        pass
    else:
        st.write('Different BMA City')
        st.write("Proof's BMA City = " + proofs_dictionary['BA_City'])
        st.write("Print File's BMA City = " + df6['BMA_City'].iloc[0])
        counter = 1
    if (string_stripping(df6['BMA_State'].iloc[0]) == proofs_dictionary['BA_State']):
        pass
    else:
        st.write('Different BMA State')
        st.write("Proof's BMA State = " + proofs_dictionary['BA_State'])
        st.write("Print File's BMA State = " + df6['BMA_State'].iloc[0])
        counter = 1
    if (df6['Mandatory (Y or N only)'].iloc[0] == proofs_dictionary['Is_Mandatory']):
        pass
    else:
        st.write('Different Mandatory Status')
        st.write("Proof's Mandatory Status = " + proofs_dictionary['Is_Mandatory'])
        st.write("Print File's Mandatory Status = " + df6['Mandatory (Y or N only)'].iloc[0])
        counter = 1
    if (df6['Mandatory (Y or N only)'].iloc[0] == 'Y'):
        if (df6['State Law (Mandatory Only)'].iloc[0] == xa_cleaning(proofs_dictionary['State_Law'])):
            pass
        else:
            st.write('Different State Law')
            st.write("Proof's State Law = " + proofs_dictionary['State_Law'])
            st.write("Print File's State Law = " + df6['State Law (Mandatory Only)'].iloc[0])
            counter = 1
    if (df6['Print Spanish Instructions link?'].iloc[0] == proofs_dictionary['spanish_link']):
        pass
    else:
        st.write('Different Spanish Link')
        st.write("Proof's Spanish Link = " + proofs_dictionary['spanish_link'])
        st.write("Print File's Spanish Link = " + df6['Print Spanish Instructions link?'].iloc[0])
        counter = 1
    if (string_stripping(df6['Mail_Address_1'].iloc[0]) == proofs_dictionary['BA_Address_1']):
        pass
    else:
        st.write('Different Mail Address 1')
        st.write("Proof's Mail Address 1 = " + proofs_dictionary['BA_Address_1'])
        st.write("Print File's Mail Address 1 = " + df6['Mail_Address_1'].iloc[0])
        counter = 1
    if (string_stripping(df6['Mail_Address_2'].iloc[0]) == ''):
        df6['Mail_Address_2'].iloc[0] = 'Empty'
    if (string_stripping(df6['Mail_Address_2'].iloc[0]) == proofs_dictionary['BA_Address_2']):
        pass
    else:
        if (string_stripping(df6['Trade_Name'].iloc[0]) == proofs_dictionary['BA_Address_2']):
            pass
        else:
            st.write('Different Mail Address 2')
            st.write("Proof's Mail Address 2 = " + proofs_dictionary['BA_Address_2'])
            st.write("Print File's Mail Address 2 = " + df6['Trade_Name'].iloc[0])
            counter = 1
    if (string_stripping(df6['Legal_Name'].iloc[0]) == ''):
        df6['Legal_Name'].iloc[0] = 'Empty'
    if (string_stripping(df6['Legal_Name'].iloc[0]) == proofs_dictionary['Legal_Name']):
        pass
    else:
        if (string_stripping(df6['Trade_Name'].iloc[0]) == proofs_dictionary['Legal_Name']):
            pass
        else:
            st.write('Different Legal Name')
            st.write("Proof's Legal Name = " + proofs_dictionary['Legal_Name'])
            st.write("Print File's Legal Name = " + df6['Trade_Name'].iloc[0])
            counter = 1
    if (string_stripping(df6['Trade_Name'].iloc[0]) == ''):
        df6['Trade_Name'].iloc[0] = 'Empty'
    if (string_stripping(df6['Trade_Name'].iloc[0]) == proofs_dictionary['Trade_Name']):
        pass
    else:
        if (string_stripping(df6['Trade_Name'].iloc[0]) == proofs_dictionary['Legal_Name']):
            pass
        else:
            if (string_stripping(df6['Mail_Address_2'].iloc[0]) == proofs_dictionary['Trade_Name']):
                pass
            else:
                st.write('Different Trade Name')
                st.write("Proof's Trade Name = " + proofs_dictionary['Trade_Name'])
                st.write("Print File's Trade Name = " + df6['Mail_Address_2'].iloc[0])
                counter = 1
    if counter == 1:
        pass
    else:
        st.write("None")
    

if st.button("Run Script"):
     show_pdf(proofs_data)
     df = pd.read_csv(print_data)
     df['Web_ID'] = df['Web_ID'].astype('int')
     df = df.applymap(str)
     df2 = pd.read_csv(state_data)
     df2 = df2.applymap(str)
     df2 = df2.drop([2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,43,44,45])
     df2_transposed = df2.T
     df3 = df2_transposed.reset_index(drop = True)
     df3.columns = df3.iloc[1]
     df3 = df3.drop([0,1])
     df3 = df3.rename(columns = {'FIPS': 'Abbreviation_list'})
     df3 = df3.iloc[: , :21]
     df3 = df3.iloc[:-2]
     for i in range(len(df3)):
          s = df3['Abbreviation_list'].iloc[i]
          if s[0] == '0':
               df3['Abbreviation_list'].iloc[i] = s[1]
     df = df.drop(columns = ['Unnamed: 0'])
     df4 = pd.merge(df3, df, on = 'Abbreviation_list', how = 'outer')
     df4 = df4[df4['Web_ID'].notna()]
     for i in range(1, 51, 2):
          st.write('Errors with page ' + str(i) + ' of proofs:')
          proofs_dictionary = {}
          with pdfplumber.open(proofs_data) as pdf:
               page = pdf.pages[i-1]
               output = page.extract_text()
               output = xa_cleaning(output)
          PSWD = output[output.index('PASSWORD:') + 10: output.index('PASSWORD:') + 18]
          df5 = df4[df4['Password'].str.contains(PSWD)]
          for j in range(len(df5)):
               while len(df5['UI_Number'].iloc[j]) < 10:
                    df5['UI_Number'].iloc[j] = '0' + df5['UI_Number'].iloc[j]
               while len(df5['Web_ID'].iloc[j]) < 12:
                    df5['Web_ID'].iloc[j] = '0' + df5['Web_ID'].iloc[j]
               while len(df5['BMA_Area_Code_1'].iloc[j]) < 5:
                    df5['BMA_Area_Code_1'].iloc[j] = '0' + df5['BMA_Area_Code_1'].iloc[j]
               while len(df5['BMA_Area_Code_2'].iloc[j]) < 4:
                    df5['BMA_Area_Code_2'].iloc[j] = '0' + df5['BMA_Area_Code_2'].iloc[j]
          WEB_ID = str(output[output.index('WEB ID:') + 8: output.index('WEB ID: ') + 20])
          df6 = df5[df5['Web_ID'].str.contains(WEB_ID)]
          df6['Form Identification'] = 'BLS 3023 - Industry Verification Form'
          df6['OMB_Clearance_Information'] = 'O.M.B. No. 1220-0032'
          df6 = df6.reset_index(drop = True)
          data = tb.read_pdf(proofs_data, area = (150, 400, 180, 600), pages = i)
          if (notice == 'Second Notice'):
               if (data[0].columns[0] == 'SECOND NOTICE'):
                    pass
               else:
                    st.write("Incorrect Notice")
          elif (notice == 'Third Notice'):
               if (data[0].columns[0] == 'THIRD NOTICE'):
                    pass
               else:
                    st.write("Incorrect Notice")
          else:
               if (data == []):
                    pass
               else:
                    st.write("Incorrect Notice")
          data = tb.read_pdf(proofs_data, area = (23, 52, 144, 333), pages = i)
          if (df6['Return Address Line 2'].iloc[0] == 'nan'):
               df6['Return Address Line 2'].iloc[0] = np.nan
          if (df6['Department Name (50 char)'].iloc[0] == 'nan'):
               df6['Department Name (50 char)'].iloc[0] = np.nan
          if (df6['State Agency Name (50 char)'].iloc[0].lower().strip() == data[0].columns[0].lower().strip()):
               proofs_dictionary['State Agency Name'] = data[0].columns[0]
               if (pd.isnull(df6['Return Address Line 2'].iloc[0]) and pd.isnull(df6['Department Name (50 char)'].iloc[0])):
                    proofs_dictionary['Department Name'] = "Empty"
                    proofs_dictionary['Return Address'] = data[0].iloc[0][0]
                    proofs_dictionary['Return Address Line 2'] = "Empty"
                    proofs_dictionary['City'] = data[0].iloc[1][0][0:data[0].iloc[1][0].index(',')]
                    proofs_dictionary['Abbreviation'] = data[0].iloc[1][0][data[0].iloc[1][0].index(',') + 2:data[0].iloc[1][0].index(',') + 4]
                    zip_codes = data[0].iloc[1][0][data[0].iloc[1][0].index(',') + 6:]
                    zip_codes = xa_cleaning(zip_codes)
                    proofs_dictionary['Return Address Zip Code'] = zip_codes
                    proofs_dictionary['Phone Number'] = xa_cleaning(data[0].iloc[2][0][7:])
               if (pd.isnull(df6['Return Address Line 2'].iloc[0]) and not pd.isnull(df6['Department Name (50 char)'].iloc[0])):
                    proofs_dictionary['Department Name'] = xa_cleaning(data[0].iloc[0][0])
                    proofs_dictionary['Return Address'] = data[0].iloc[1][0]
                    proofs_dictionary['Return Address Line 2'] = "Empty"
                    proofs_dictionary['City'] = data[0].iloc[2][0][0:data[0].iloc[2][0].index(',')]
                    proofs_dictionary['Abbreviation'] = data[0].iloc[2][0][data[0].iloc[2][0].index(',') + 2:data[0].iloc[2][0].index(',') + 4]
                    zip_codes = data[0].iloc[2][0][data[0].iloc[2][0].index(',') + 6:]
                    zip_codes = xa_cleaning(zip_codes)
                    proofs_dictionary['Return Address Zip Code'] = zip_codes
                    proofs_dictionary['Phone Number'] = xa_cleaning(data[0].iloc[3][0][7:])
               if (not pd.isnull(df6['Return Address Line 2'].iloc[0]) and pd.isnull(df6['Department Name (50 char)'].iloc[0])):
                    proofs_dictionary['Department Name'] = "Empty"
                    proofs_dictionary['Return Address'] = data[0].iloc[0][0]
                    proofs_dictionary['Return Address Line 2'] = data[0].iloc[1][0]
                    proofs_dictionary['City'] = data[0].iloc[2][0][0:data[0].iloc[2][0].index(',')]
                    proofs_dictionary['Abbreviation'] = data[0].iloc[2][0][data[0].iloc[2][0].index(',') + 2:data[0].iloc[2][0].index(',') + 4]
                    zip_codes = data[0].iloc[2][0][data[0].iloc[2][0].index(',') + 6:]
                    zip_codes = xa_cleaning(zip_codes)
                    proofs_dictionary['Return Address Zip Code'] = zip_codes
                    proofs_dictionary['Phone Number'] = xa_cleaning(data[0].iloc[3][0][7:])
               if (not pd.isnull(df6['Return Address Line 2'].iloc[0]) and not pd.isnull(df6['Department Name (50 char)'].iloc[0])):
                    proofs_dictionary['Department Name'] = xa_cleaning(data[0].iloc[0][0])
                    proofs_dictionary['Return Address'] = data[0].iloc[1][0]
                    proofs_dictionary['Return Address Line 2'] = data[0].iloc[2][0]
                    proofs_dictionary['City'] = data[0].iloc[3][0][0:data[0].iloc[3][0].index(',')]
                    proofs_dictionary['Abbreviation'] = data[0].iloc[3][0][data[0].iloc[3][0].index(',') + 2:data[0].iloc[3][0].index(',') + 4]
                    zip_codes = data[0].iloc[3][0][data[0].iloc[3][0].index(',') + 6:]
                    zip_codes = xa_cleaning(zip_codes)
                    proofs_dictionary['Return Address Zip Code'] = zip_codes
                    proofs_dictionary['Phone Number'] = xa_cleaning(data[0].iloc[4][0][7:])
               if (df6['Print (Y/N)'].iloc[0] == 'Y'):
                    proofs_dictionary['Print Email'] = 'Y'
                    proofs_dictionary['Email'] = xa_cleaning(data[0].iloc[len(data[0])-1][0][7:])
               else:
                    proofs_dictionary['Print Email'] = 'N'
                    proofs_dictionary['Email'] = "Empty"
                    if (data[0].iloc[len(data[0])-1][0][0:6] == 'Email:'):
                         proofs_dictionary['Email'] = "Extra Email"
          else:
               proofs_dictionary['State Agency Name'] = 'Empty'

          mandatory_data = tb.read_pdf(proofs_data, area = (130, 420, 150, 590), pages = i)
          if (mandatory_data == []):
               proofs_dictionary['Is_Mandatory'] = 'N'
               proofs_dictionary['State_Law'] = 'Empty'
          elif (mandatory_data[0].columns[0] == 'MANDATORY'):
               proofs_dictionary['Is_Mandatory'] = 'Y'
               proofs_dictionary['State_Law'] = output[output.index('in accordance with') + 19: output.index('and is authorized') - 1]

          proofs_dictionary['U.I.'] = output[output.index('U.I. Number:') + 12: output.index('U.I. Number:') + 23]

          new_data = tb.read_pdf(proofs_data, area = (115, 80, 250, 400), pages = i)
          test_df = new_data[0]
          if (len(test_df) == 6):
               proofs_dictionary['Legal_Name'] = xa_cleaning(test_df.iat[0,0])
               proofs_dictionary['Trade_Name'] = xa_cleaning(test_df.iat[1,0])
               proofs_dictionary['BA_Address_1'] = test_df.iat[3,0]
               proofs_dictionary['BA_Address_2'] = test_df.iat[2,0]
               proofs_dictionary['BA_City'] = test_df.iat[4,0][0:test_df.iat[4,0].index(',')]
               proofs_dictionary['BA_State'] = test_df.iat[4,0][test_df.iat[4,0].index(',') + 2:test_df.iat[4,0].index(',') + 4]
               proofs_dictionary['BA_ZIP'] = xa_cleaning(test_df.iat[4,0][test_df.iat[4,0].index(',') + 6:])
          if (len(test_df) == 4):
               proofs_dictionary['Legal_Name'] = xa_cleaning(test_df.iat[0,0])
               proofs_dictionary['Trade_Name'] = "Empty"
               proofs_dictionary['BA_Address_1'] = test_df.iat[1,0]
               proofs_dictionary['BA_Address_2'] = "Empty"
               proofs_dictionary['BA_City'] = test_df.iat[2,0][0:test_df.iat[2,0].index(',')]
               proofs_dictionary['BA_State'] = test_df.iat[2,0][test_df.iat[2,0].index(',') + 2:test_df.iat[2,0].index(',') + 4]
               proofs_dictionary['BA_ZIP'] = xa_cleaning(test_df.iat[2,0][test_df.iat[2,0].index(',') + 6:])
          if (len(test_df) == 5):
               proofs_dictionary['Legal_Name'] = xa_cleaning(test_df.iat[0,0])
               proofs_dictionary['Trade_Name'] = xa_cleaning(test_df.iat[1,0])
               proofs_dictionary['BA_Address_1'] = test_df.iat[2,0]
               proofs_dictionary['BA_Address_2'] = test_df.iat[1,0]
               proofs_dictionary['BA_City'] = test_df.iat[3,0][0:test_df.iat[3,0].index(',')]
               proofs_dictionary['BA_State'] = test_df.iat[3,0][test_df.iat[3,0].index(',') + 2:test_df.iat[3,0].index(',') + 4]
               proofs_dictionary['BA_ZIP'] = xa_cleaning(test_df.iat[3,0][test_df.iat[3,0].index(',') + 6:])
          spanish_data = tb.read_pdf(proofs_data, area = (720, 310, 750, 530), pages = i)
          if (spanish_data == []):
               proofs_dictionary['spanish_link'] = 'N'
          elif (spanish_data[0].columns[0] == 'En Español: www.bls.gov/respondents/ars/espanol.pdf'):
               proofs_dictionary['spanish_link'] = 'Y'
          code_data = tb.read_pdf(proofs_data, area = (70, 380, 110, 550), pages = i)
          if code_data == []:
               proofs_dictionary['Form Identification'] = 'Empty'
          else:
               proofs_dictionary['Form Identification'] = code_data[0].columns[0]
          if 'approved with' in output:
               proofs_dictionary['OMB Clearance Information'] = output[output.index('approved with') + 14: output.index('approved with') + 34]
          else:
               proofs_dictionary['OMB Clearance Information'] = 'Empty'
          if 'Every three years' and 'and the U.S. Bureau of Labor' in output:
               proofs_dictionary['the State Agency Name 1'] = output[output.index('Every three years') + 19:output.index('and the U.S. Bureau of Labor') - 1]
          else:
               proofs_dictionary['the State Agency Name 1'] = 'Empty'
          if 'The information collected by' and 'and BLS will' in output:
               proofs_dictionary['the State Agency Name 2'] = output[output.index('The information collected by') + 29:output.index('and BLS will') - 1]
          else:
               proofs_dictionary['the State Agency Name 2'] = 'Empty'
          if '-' in proofs_dictionary['BA_ZIP']:
               proofs_dictionary['BA_ZIP_5'] = proofs_dictionary['BA_ZIP'][0:5]
               proofs_dictionary['BA_ZIP_4'] = proofs_dictionary['BA_ZIP'][6:10]
          else:
               proofs_dictionary['BA_ZIP_5'] = proofs_dictionary['BA_ZIP']
               proofs_dictionary['BA_ZIP_4'] = 'Empty'
          df6 = df6.fillna('Empty')
          compare_dict(df6, proofs_dictionary)
          st.write('_____________________________')
        
