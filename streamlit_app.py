import streamlit as st

if 'slider' not in st.session_state:
    if 'slider' in st.query_params:
        st.session_state['slider'] = int(st.query_params['slider'])
    else:
        st.session_state['slider'] = 50

st.title("Slider State in URL")

slider = st.slider("Choose a value", min_value=0, max_value=100, key='slider')

st.query_params['slider'] = str(slider)