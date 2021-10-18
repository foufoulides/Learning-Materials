# STREAMLIT FORMS
# Forms is the more important feature if you want to have a 
# propertly structured app.

import streamlit as st
import spacy

# Will use a rudimentary NLP as an example in this section. 
# On models:
# 1. It is expensive to reload models, you must cache them. 
#    This means you won't have to load them every time you rerun.
#    We will learn more on this in the next section. 
# 2. Learn how Steamlit works, that it constantly returns your
#    script. Through this you will see the importance of forms. 

nlp = spacy.load("en_core_web_lg") # A 780MB ML Model for English

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

hits = extract_entities(ent_types, text)

st.write(hits) 

