# import streamlit as st
# import pandas as pd
# from job_Scraper import run_scraping  # This will use your existing scraping code
# import os

# # Set page configuration
# st.set_page_config(page_title="Job Scraper", layout="wide")

# # Title of the app
# st.title("Job Scraper App")

# # Define the job role and location manually here
# job_role = st.text_input("enter job role")#Manually set job role
# location = st.text_input("enter location")           # Manually set location

# # Display the information
# st.write(f"Job Role: {job_role}")
# st.write(f"Location: {location}")

# # Button to start scraping
# if st.button("Start Scraping"):
#     # Call the scraping function
#     st.write("Scraping in progress, please wait...")
#     run_scraping(job_role, location)  # Call the function from job_scrapper.py
#     st.write("Scraping completed!")

#     # Display download button for the CSV file
#     if os.path.exists("jobs.csv"):
#         with open("jobs.csv", "rb") as f:
#             st.download_button(
#                 label="Download Job Data",
#                 data=f,
#                 file_name="jobs.csv",
#                 mime="text/csv"
#             )
#     else:
#         st.write("No data available to download.")


import streamlit as st
import pandas as pd
from job_Scraper import run_scraping
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

st.set_page_config(page_title="Job Scraper", layout="wide")

st.title("Job Scraper App")

job_role = st.text_input("Enter Job Role")
location = st.text_input("Enter Location")

def start_scraping():
    driver = webdriver.Chrome()

    st.write("Scraping in progress, please wait...")
    jobs, under_review_jobs = run_scraping(job_role, location)
    
    driver.quit()  

    if os.path.exists("real_jobs.csv"):
        with open("real_jobs.csv", "rb") as f:
            st.download_button(
                label="Download Real Job Data",
                data=f,
                file_name="real_jobs.csv",
                mime="text/csv"
            )
    else:
        st.write("No real job data available to download.")

    if os.path.exists("under_review_jobs.csv"):
        with open("under_review_jobs.csv", "rb") as f:
            st.download_button(
                label="Download Under Review Job Data",
                data=f,
                file_name="under_review_jobs.csv",
                mime="text/csv"
            )
    else:
        st.write("No under review job data available to download.")

    if jobs:
        df = pd.DataFrame(jobs)
        st.write("Real Jobs")
        st.dataframe(df)

    if under_review_jobs:
        df_under_review = pd.DataFrame(under_review_jobs)
        st.write("Under Review Jobs")
        st.dataframe(df_under_review)

if st.button("Start Scraping"):
    start_scraping()
    st.write("Scraping has started. Please wait for completion.")






































