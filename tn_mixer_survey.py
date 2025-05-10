import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account

st.set_page_config(page_title="TN Mixer Feedback Survey", layout="centered")

st.title("TN Mixer Feedback Survey")
st.markdown("Please take a moment to share your experience with the TN Mixer sessions.")

# Section 1: Overall Experience
st.header("1. Overall Experience")
rating = st.radio("How would you rate your overall experience?", ["Excellent", "Good", "Neutral", "Fair", "Poor"])
enjoy_most = st.text_area("What did you enjoy most about the TN Mixer experience?")
improvements = st.text_area("What could be improved for future sessions?")

# Section 2: Partner Conversations
st.header("2. Partner Conversations")
partner_helpful = st.radio("How helpful were the 1-on-1 partner conversations?", ["Very helpful", "Somewhat helpful", "Neutral", "Not very helpful", "Not helpful at all"])
prompts_useful = st.radio("Did the conversation prompts support meaningful discussion?", ["Yes", "Somewhat", "No"])

# Section 3: Group Dynamics & Facilitation
st.header("3. Group Dynamics & Facilitation")
comfort = st.radio("How comfortable did you feel participating in the group sessions?", ["Very comfortable", "Somewhat comfortable", "Neutral", "Uncomfortable"])
facilitator_feedback = st.text_area("Do you have any feedback for your group facilitator?")

# Section 4: Future Participation
st.header("4. Future Participation")
future_interest = st.radio("Would you be interested in participating in a future TN Mixer?", ["Yes", "Maybe", "No"])
additional_comments = st.text_area("Any other comments, ideas, or suggestions?")

# Submit button
if st.button("Submit"):
    # Authenticate using secrets
    creds_dict = st.secrets["gcp_service_account"]
    creds = service_account.Credentials.from_service_account_info(creds_dict)
    scoped_creds = creds.with_scopes(["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(scoped_creds)

    # Open Google Sheet and append row
    sheet = client.open("TN Mixer Survey Responses").sheet1
    response = [
        rating,
        enjoy_most,
        improvements,
        partner_helpful,
        prompts_useful,
        comfort,
        facilitator_feedback,
        future_interest,
        additional_comments
    ]
    sheet.append_row(response)
    st.success("Thank you! Your response has been submitted to Google Sheets.")