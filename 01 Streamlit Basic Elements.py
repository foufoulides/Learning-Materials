# To run app, at the terminal in same directory as the .py file:
# Enter command: streamlit run "app_name.py"

import streamlit as st

st.title("01. Intro to Streamlit")
st.write("This app is to learn the various elements of Streamlit")

st.markdown('''## Hello there''')

st.header("Action: Button")
# Creating a button
button1 = st.button("Click Me!")

# If button is pressed (i.e. ==True) write text
# Note: If you are going to take a lot of user input, you want to
# do this inside a form! We will look at that at a later video.
if button1:
    st.write("The button has been pushed!")

# Take in user input with a check box
st.header("User Input: Checkboxes")

# A checkbox is also a boolean (True/False)
like = st.checkbox(label="Do you like this app?")

# Button to do something based on checkbox when pressed.
button2 = st.button("Submit")

if button2:
    if like:
        st.write("Thank you, I like it too!")
    else:
        st.write("I am sorry to hear that.")

st.header("User Input: Radio Button")

animal = st.radio(label="What is your favourite animal?", 
                  options=("Lion", "Tiger", "Bear"))

button3 = st.button("Submit Animal")

if button3:
    st.write("Your favoutite animal is " + animal)
    if animal == "Lion":
        st.write("ROAR!")


st.header("User Input: Select Box")
animal2 = st.selectbox(label="What is your favourite animal?", 
                       options=("Lion", "Tiger", "Bear"))

button4 = st.button("Select Animal")

if button4:
    st.write("Your favoutite animal is " + animal2)
    if animal2 == "Lion":
        st.write("ROAR!")

st.header("User Input: Multi Select Box")
# Note that the multi-select box also keeps the ORDER of the 
# input data, which you can also make user of.
options =st.multiselect(label="What animals do you like?", 
                        options=("Lion", "Tiger", "Bear"))

button5 = st.button("Print Selected Animals")

if button5:
    st.write(options)

st.header("User Input: Numerical - Slider")
# value here is the default value.
epochs_num = st.slider(label="Select number of epochs", 
                        min_value=1, max_value=100, value=10)

# You can implicitly create a button, by refering it in conditional
if st.button("Slider Button"):
    st.write(epochs_num)

st.header("User Input: Text")
# Again, value is a suggested, example, default value!
# Note: a numerical input will be returned as a numerical string!
user_text = st.text_input(label="What is your favourite movie?", 
                          value = "Matrix")

if st.button("Print Text"):
    st.write(user_text)

st.header("User Input: Number")

user_num = st.number_input(label="What's your favourite number?", 
                           min_value=1, max_value=100)

if st.button("Number Button"):
    st.write("Your favourite number is " + str(user_num))

st.header("User Input: Text Area")

def run_sentiment_analysis(text):
    st.write(f"Analysis done: {text}")

my_text = st.text_area(label="The Text to analyze", 
value='''It was the best of times, it was the worse of times,
it was the age of wisdom, it was the age of foolishness, it was
the epoch of belied, it was the eopch of increduluty, it was the
season of Light, it was the seasn of Darknes, it was the spring
of hope, it was the winter of despair''')

st.write("Sentiment Analysis:", run_sentiment_analysis(my_text))