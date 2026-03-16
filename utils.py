import os.path

import streamlit_authenticator as stauth
import streamlit as st
# streamlit run C:\Users\c1049033\PycharmProjects\phd_apps\welcome.py

import yaml
from yaml.loader import SafeLoader


def my_authenticator():
    try:
        with open('other/usr.yml') as file:
            config = yaml.load(file, Loader=SafeLoader)
    except:
        with open(r'C:\Users\c1049033\PycharmProjects\phd_apps\other\usr.yml') as file:
            config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized']
    )
    authenticator.login(location='sidebar')

    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f'Welcome *{st.session_state["name"]}*')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')
import pandas as pd

import datetime
import numpy as np
def delete_today():
    df_full=pd.read_csv(r"H:\Downloads\2025-06-03T10-59_export.csv")
    print(df_full.shape)

    today = datetime.date.today()


    # df['date_column'] = pd.to_datetime(df['date'], utc=True)
    # timestamp_value = pd.Timestamp(today, tz='UTC')
    df_full['date'] = pd.to_datetime(df_full['date'])
    df = df_full[df_full['date'].dt.date != today]

    cutoff_date = pd.Timestamp.now() - pd.Timedelta(days=8)
    #df[date_column] = pd.to_datetime(df[date_column])
    df=df[df['date'].values.astype(np.datetime64) >= cutoff_date]

    # # Now the comparison should work
    # df[df['date_column'] < timestamp_value]


    print(df.shape)
    df.to_csv(r"H:\Downloads\2025-06-03_export_{}.csv".format(df.shape[0]), index=False, encoding='utf-8-sig')
    # mydiff=df_full.drop(df.index, axis=0)
    # print(mydiff.shape)
    # mydiff.to_csv(r"H:\Downloads\mydiff.csv")

delete_today()