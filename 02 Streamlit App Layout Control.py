import streamlit as st 

st.title("Intro to Streamlit Layouts and Images")

st.header("Layout: Side Bar")

st.header("Layout: Columns")

st.header("Layour: Expander")

# Import image into the sidepar
st.sidebar.image(image="optimization.png", caption="Optimization")

# Note: The side bar functions the same way as the main app!
# We simply start with "st.sidebar" as opposed to "st."
st.sidebar.header("Options")

def clean_text(text):
    text = text.replace("`", "").replace("-\n", "").replace("\n", " ").strip()
    return text

text = st.sidebar.text_area(label="Enter Text Here")

button1 = st.sidebar.button("Clean Text")

if button1:
    # Create two columns to enter page elements in
    # Much like side bar, they work the same way as without columns
    # We simply start with the column name (e.g. "col1."")
    # instead of "st."
    col1, col2 = st.columns(2)
    # Create expanders to hide text, unless expanded (+)
    # Make sure you wrap them inside the columns! (col1, col2)
    col1_exp = col1.expander(label="Expand Original")
    with col1_exp:
        col1_exp.header("Original Text")
        col1_exp.write(text)
    
    col2_exp = col2.expander(label="Expand Cleaned")
    with col2_exp:
        col2_exp.header("Cleaned Text")
        clean = clean_text(text)
        col2_exp.write(clean)