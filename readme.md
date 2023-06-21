# Streamlit Data Editor Regression in Firefox v1.23.0

In streamlit version 1.23.0, I am experiencing a regression in both the data_editor and the dataframe display in streamlit apps viewed in Firefox. I can no longer select multiple cells at once in the dataframe either with click and drag or shift + arrow keys. I can only select one cell at a time. 

In the data editor, I can no longer copy and paste multiple cells at once. In addition, the "bulk editor handle" and fill via ctrl+d is not working in the data editor anymore.

To replicate this, run the bash script `env_setup.sh` to create two virtual environments, one with streamlit 1.22.0 and one with streamlit 1.23.0. Then run `streamlit run app_v_22.py` in the 1-22 environment and `streamlit run app_v_23.py` in the 1-23 environment.

I only see the issue in Firefox. I also tested Chrome and Edge and the issue is not present.