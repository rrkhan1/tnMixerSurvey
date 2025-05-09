import streamlit as st
import pandas as pd
import os

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
    response = {
        "Rating": rating,
        "Enjoyed Most": enjoy_most,
        "Improvements": improvements,
        "Partner Helpful": partner_helpful,
        "Prompts Useful": prompts_useful,
        "Comfort Level": comfort,
        "Facilitator Feedback": facilitator_feedback,
        "Future Interest": future_interest,
        "Additional Comments": additional_comments
    }

    df = pd.DataFrame([response])

    # Save to CSV (append mode)
    csv_file = "tn_mixer_survey_responses.csv"
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', index=False, header=False)
    else:
        df.to_csv(csv_file, index=False)

    st.success("Thank you for your feedback! Your responses have been recorded.")
