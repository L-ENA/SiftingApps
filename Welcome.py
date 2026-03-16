#streamlit run C:\Users\c1049033\PycharmProjects\phd_apps\Welcome.py
import streamlit as st
from utils import my_authenticator



#my_authenticator()
st.session_state["authentication_status"]=True

if st.session_state["authentication_status"]:
    st.image(r"C:\Users\c1049033\PycharmProjects\phd_apps\imgs\IO2.jpg")

    st.markdown("# Horizon Scanning Tool Prototypes")
    st.write("Select a tool from the navigation pane on the left side of the screen. ")
    st.write('&nbsp;')  # empty line
    st.write('&nbsp;')  # empty line
    st.write('This project is funded by the National Institute for Health and Care Research (NIHR) [HSRIC-2016-10009/Innovation Observatory]. The views expressed are those of the author(s) and not necessarily those of the NIHR or the Department of Health and Social Care.')  # empty line
    # st.sidebar.markdown("## Navigate page ")
    #
    # st.sidebar.markdown('## [Welcome](#welcome)')
    # st.sidebar.markdown('## [What it is](#what-it-is)')