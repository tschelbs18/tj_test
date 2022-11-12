import streamlit as st
import random

st.title("TJ Model Test")

initials = st.text_input('Reviewer Initials')

st.subheader('Copy and paste input text below')
input_text = st.text_area('')

st.subheader('Review results here')
samples = ['Green Job','Not a Green Job', 'Has potential']
classification = random.choice(samples)
st.text(f'Classification : {classification}')

st.subheader('Annotate Results')
annotation = st.radio('',['Good','Bad'])

saved = st.button('Add results to Google Sheet')

if saved:
    import gsheet
    gsheet.append_to_sheet(initials, input_text, classification, annotation)
    st.success("Added!")