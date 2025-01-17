import streamlit as st

def initialize_session_state():
    if 'step' not in st.session_state:
        st.session_state.step = 1

    if 'cpr_step' not in st.session_state:
        st.session_state.cpr_step = 0  

    if 'selected_tooth' not in st.session_state:
        st.session_state.selected_tooth = []
    
    if 'tooth_result' not in st.session_state:
        st.session_state.tooth_result = ""

    if 'selected_bone' not in st.session_state:
        st.session_state.selected_bone = ""

    if 'cpr_step' not in st.session_state:
        st.session_state.cpr_step = 0
        
    if 'second' not in st.session_state:
        st.session_state.second = 0
        
    if 'colic_result' not in st.session_state:
        st.session_state.colic_result = ""
        
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = []
        
    if 'heat' not in st.session_state:
        st.session_state.heat = []
        
    if 'heat_text' not in st.session_state:
        st.session_state.heat_text = ""
        
    if 'heat_result' not in st.session_state:
        st.session_state.heat_result = ""
        
    if 'trauma_input' not in st.session_state:
        st.session_state.trauma_input = []
        