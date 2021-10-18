# STREAMLIT MODEL AND DATA CACHING
# In addition to forms, to make an app efficient, we want models and
# datasets which don't change (especially large ones) to not reload every
# time the app reruns. 
# This is where caching comes in. 

import streamlit as st
import spacy

# Everything that needs to be cached, is done in the form of a FUNCION.
# Then we cache the function using a DECORATOR.
# You will get an error from the decorator. One way to fix it is to set
# a parameter "allow_output_mutation=True".  For details on this, go to 
# Streamlit documentation.
@st.cache(allow_output_mutation=True)
def load_model(model_name):
    nlp = spacy.load(model_name)
    return (nlp)
# we change the model call here to the defined function call   
nlp = load_model("en_core_web_lg")
# nlp = spacy.load("en_core_web_lg") # A 780MB ML Model for English

def extract_entities(ent_types, text):
    results = [] # Empty list to save results
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.apprend((ent.text, ent.label_))
    
    return (results)

st.title("Intro to Streamlit Forms")

# In this case, in a multi-select, Streamlit reruns the script every time
# the user enters one parameter for the model. 
# This becomes very computational taxing, as the user parameters for the 
# app increases. This is where Forms come in, where nothing hapens, until a
# button is hit.
# This is done by wrapping all of the parameters into one widget.
form1 = st.sidebar.form(key="Options")
form1.header("Params")
ent_types = []

form1.multiselect(label = "Select the entities you want to extract", 
                       options = ["Person", "ORG", "GPE"])

# Every Streamlit form, needs a FORM SUBMIT BUTTON. 
# You will be getting an error until you enter one.
form1.form_submit_button("Submit Your Options")

text = st.text_area(label="Sample Text",
                    value='''James enjoys basketball in Florida for the
                        salvation army''')

st.write("Life Expectancy Over Time")
st.title("Intro to Streamlit Forms")

