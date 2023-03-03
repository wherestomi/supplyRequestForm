import pandas as pd

import backend as b
import streamlit as st

st.set_page_config(layout='wide', page_title="TOBOLA Program Supply Request Form")

st.header("TOBOLA Supply Request Form")

with st.form('Supply Requests'):

    st.selectbox("Person Submitting Request", options=b.users_df['Assigned.'], key='requestor')

    st.text_input("Email Address", key='email')

    st.selectbox("Select Site", options=b.locations_df['Name'], key='site')

    st.selectbox("Request Type", options=b.request_types, key='r_type')

    st.text_area("Request Information", key='request')

    ack_button = st.checkbox(
        "By checking this box, you acknowledge that all of the information above is correct to"
        " the best of your knowledge.",
        key='acknowledgement')

    submit = st.form_submit_button("Submit", use_container_width=True)

    if ack_button and submit:
        submission = pd.DataFrame()
        submission["Request"] = [st.session_state['request']]
        submission['Requestor'] = [st.session_state['requestor']]
        submission['Email'] = [st.session_state['email']]
        submission['Site'] = [st.session_state['site']]
        submission['Request Type'] = [st.session_state['r_type']]
        submission['Status'] = 'New Submission'
        try:
            submission.to_notion(b.request_db_url, api_key=b.notion_token, title='Test', resolve_relation_values=True)
            with st.sidebar:
                st.success('Request Submitted!', icon="✅")
                st.write("You can now close this screen")
        except:
            st.warning('Please try again', icon="⚠️")
    elif submit and (ack_button == False):
        st.warning('Please confirm the checkbox to continue', icon="⚠️")

