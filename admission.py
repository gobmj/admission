import streamlit as st
import pandas as pd
import pickle
st.write("""
# Checking Admission Status
 """)
svm_classifier = open('svm_model.pkl','rb')
classifier = pickle.load(svm_classifier)
#Text Input
gre = st.text_input("Enter the GRE Score:")
toefl = st.text_input("Enter the TOEFL Score:")
ur =  st.text_input("Enter the University Rating:")
sop =  st.text_input("Enter the SOP:")
lor =  st.text_input("Enter the LOR:")
cgpa =  st.text_input("Enter the CGPA:")
research =  st.text_input("Enter the Research:")
submit = st.button("Check")

if submit:
        result = classifier.predict([[gre,toefl,ur,sop,lor,cgpa,research]])
        if result ==1:
                st.write("Will Get Admission")
        else:
                st.write("No Admission")                
                #st.write(result)