# STREAMLIT SESSION STATES
# Session state is a way to share variables between RERUNS, 
# for each user session. (every time Streamlit RERUNS the script)

# Session state allows you to store a variable outside a RERUN.
# So you can have an object (e.g. number, string, list, etc.)
# that can be manipulated and changed, but can be maintained
# after a RERUN. 

import streamlit as st

st.title("Streamlit Session States")

# counter = 0 
# st.write("The counter equals: " + str(counter))

# if st.button("Up"):
#     counter += 1
#     st.write(counter)

# In the commented code above, every time the button is pressed
# the script reruns, so it gets reassigned every time to zero (0)
# and as a resutl, the "Up" button will allways return 1. 

# So we need to create a SESSION STATE VARIABLE

# It is always good practice to check if that variable exists, 
# and if it doesn't, to create it. 
if "counter" not in st.session_state:
    st.session_state.counter = 0  # the two counters need to match

# Print the saved stored (session state) value of counter
st.write(st.session_state.counter)

# Press button to increment the counter and print its value
if st.button("Up"):
    st.session_state.counter += 1
    st.write(st.session_state.counter)
    

# So the variable in session_state is saved in a cache.
# One way to RESET it is to go to: Menu --> Clear cache.
# Alternatively, we need to reassign it directly with a button: 
if st.button("reset"):
    st.session_state.counter = 0
