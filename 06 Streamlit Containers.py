# STREAMLIT CONTAINERS 
# Containers allow us to display things on the app in a different
# order than what they are appear in the script. 

import streamlit as st

st.title("Streamlit Session States")

# We put the main container higher in the app so that things 
# written in it appear higher up in the app. 
# So we can place things more dynamically in the app.
main_container = st.container()

if "counter" not in st.session_state:
    st.session_state.counter = 0  # the two counters need to match

# Press button to increment the counter and print its value
if st.button("Up"):
    st.session_state.counter += 1

# Now here we are writting in the main container which is further 
# up in the app. 
# The container above can be placed anywhere in the app, but 
# commands to write into it must be after it, so that it is
# already defined.
main_container.write(st.session_state.counter)
     
if st.button("reset"):
    st.session_state.counter = 0