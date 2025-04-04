import streamlit as st
import pandas as pd
import math
from pathlib import Path

with st.form(key='feedback_form'):
    name = st.text_input("Your Name:")
    rating = st.slider("Rate your satisfaction (1-5):", min_value=1, max_value=5)
    comments = st.text_area("Additional Comments:")
    submit_button = st.form_submit_button(label='Submit')

# Displaying the user's input after submission
if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Rating: {rating}")
    st.write(f"Comments: {comments}")
    
    # Adding conditional messages based on the rating
    if rating <= 2:
        st.warning("We're sorry to hear that you're not satisfied. Please let us know how we can improve.")
    elif rating >= 4:
        st.success("Thank you for your positive feedback!")
