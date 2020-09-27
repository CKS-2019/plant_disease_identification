# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:44:05 2020

@author: CHINMAY
"""

import streamlit as st
from classification import pred
from PIL import Image, ImageOps

st.image("./media/coeai.png","BHUBANESWAR,ODISHA", width=70)
st.title("Plant Disease Identification (PDI) ")
st.header("PDI can identify twelve types of plant diseases with its causes")
st.text("Upload a healthy or disease leaf (of apple or corn or cherry or grape) to check ")
#st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Choose an Image ...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded.', use_column_width=True)
    st.write("")
    st.write("Identifying......")
    label = pred(image)
    Classes = ["Apple___Apple_scab : Apple scab is a common disease of plants in the rose family (Rosaceae) that is caused by the ascomycete fungus Venturia inaequalis.","Apple___Black_rot : Black rot is a disease of apples that infects fruit, leaves and bark caused by the fungus Botryosphaeria obtusa.",
               "Apple___Cedar_apple_rust : Cedar apple rust (Gymnosporangium juniperi-virginianae) is a fungal disease that requires juniper plants to complete its complicated two year life-cycle.",
                  "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot : Grey leaf spot (GLS) is a foliar fungal disease that affects maize, also known as corn. GLS is considered one of the most significant yield-limiting diseases of corn worldwide.",
                      "Corn_(maize)___Common_rust : Common rust is caused by the fungus Puccinia sorghi and occurs every growing season. It is seldom a concern in hybrid corn.","Corn_(maize)___Northern_Leaf_Blight : Northern corn leaf blight is a foliar disease of corn caused by Exserohilum turcicum, the anamorph of the ascomycete Setosphaeria turcica."]
    st.write( Classes[label] )
    
    
   
