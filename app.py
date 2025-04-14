import streamlit as st
import pandas as pd
import random
import datetime

# --- Sample Data for Consultants ---
data = {
    'Name': ['Snigdha Singh', 'Aditya Gopalakrishnan', 'Chirag Batra', 'Gautham Savio', 'John Doe', 'Jane Doe'],
    'Designation': ['Project Lead I', 'Project Lead I', 'Consultant II', 'Senior Associate in Marketing', 'Consultant I', 'Project Lead II'],
    'Skills': ['Management Consulting, Basic Tech', 'Reports, Automotive Sector', 'Japanese Clients, Emerging Technologies', 'Marketing Strategy', 'Market Research, Financial Projections', 'Leadership, Financial Strategy'],
    'OKRs': ['Delivery & Upskilling in Tech', 'Delivery & Upskilling in Tech', 'Delivery & Upskilling in Tech', 'Marketing Strategy & Brand Growth', 'Up-skill in Market Research', 'Delivery & Leadership Development'],
    'Projects': ['NetApp, Panasonic, NASSCOM Report', 'MBRDI, NASSCOM Report, Flexera', 'Sumitomo, Marubeni, Sony', 'Sumitomo, Marubeni', 'Project X, Market Research', 'Tesla, Microsoft, Google'],
    'L&D Plan': ['Tech Upskilling, Leadership', 'Tech Upskilling, Leadership', 'Tech Upskilling, Emerging Technologies', 'Leadership & Marketing', 'Market Research, Financial Projections', 'Leadership, Financial Strategy'],
    'Project Status': ['In Progress', 'Completed', 'In Progress', 'Pending', 'Completed', 'In Progress'],
    'Last Feedback': ['Positive', 'Needs Improvement', 'Excellent', 'Positive', 'Good', 'Excellent'],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# --- Helper Functions ---
def get_filtered_data(designation_filter):
    if designation_filter == "All":
        return df
    return df[df['Designation'].str.contains(designation_filter)]

def get_random_feedback():
    feedbacks = ['Great work', 'Good progress, but needs more effort', 'Excellent delivery', 'Pending review', 'Needs improvement']
    return random.choice(feedbacks)

def get_skills_needed(project):
    skills_needed = {
        "NetApp": "Tech, Consulting, Startup Sourcing",
        "Panasonic": "Tech, Consulting, Market Sizing",
        "NASSCOM Report": "Reports, Market Analysis, Tech Sourcing",
        "Sumitomo": "Japanese Clients, Market Research, Tech",
        "Flexera": "Reports, Financial Projections",
        "Tesla": "Tech, Leadership, Financial Strategy",
        "Microsoft": "Reports, Market Research, Tech",
        "Google": "Tech, Leadership, Innovation"
    }
    return skills_needed.get(project, "Unknown Skills")

# --- App Layout ---
st.set_page_config(page_title="Consultant Dashboard", page_icon=":guardsman:", layout="wide")

# Title
st.title("Consultant Workforce Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Consultants")
designation_filter = st.sidebar.selectbox("Select Designation", ["All", "Project Lead I", "Consultant II", "Senior Associate in Marketing", "Consultant I", "Project Lead II"])

# Apply the filter if selected, else show all
filtered_df = get_filtered_data(designation_filter)

# Display Consultant Information
st.header(f"Consultant Overview: {designation_filter} View")
st.write(f"Showing data for **{designation_filter}**")

# Display the filtered data
st.write(filtered_df)

# --- Chatbot Section ---
st.header("Consultant Chatbot Assistant 🤖")

# List of questions to choose from
questions = [
    "What skills do you want to improve?",
    "What is the most challenging part of your current project?",
    "Do you have any upcoming projects that need additional resources?",
    "How can we support your tech upskilling?",
    "Would you prefer virtual or in-person training for your L&D plan?",
    "What do you think of the current company processes?",
    "Do you see any gaps in your OKRs?",
    "What other skills would you like to learn this year?",
    "How can management improve project allocation?",
    "Do you need help with market projections?"
]

# Create the chatbot question interaction
selected_question = st.selectbox("Select a question for the chatbot", questions)

# User provides their answer
answer = st.text_area("Your answer:")

if st.button('Submit Response'):
    st.write(f"Question: **{selected_question}**")
    st.write(f"Answer: {answer}")
    st.write("Thank you for your feedback! This will help us improve your experience.")

# --- Project Details for Consultant View ---
st.header("Project Status and Feedback")

# Display project information for consultants
project_column = st.selectbox("Select a Consultant to View Project Status", df['Name'].unique())
consultant_projects = df[df['Name'] == project_column]

st.write(f"**Projects for {project_column}:**")
for _, row in consultant_projects.iterrows():
    st.write(f"- **{row['Projects']}**")
    st.write(f"  Status: {row['Project Status']}")
    st.write(f"  Last Feedback: {get_random_feedback()}")

# --- HR Skills Section ---
st.header("Skills Required for Upcoming Projects (HR View)")

# Sample upcoming project skill needs
project_skills = {
    "NetApp": "Tech, Consulting, Startup Sourcing",
    "Panasonic": "Tech, Consulting, Market Sizing",
    "NASSCOM Report": "Reports, Market Analysis, Tech Sourcing",
    "Sumitomo": "Japanese Clients, Market Research, Tech",
    "Flexera": "Reports, Financial Projections",
    "Tesla": "Tech, Leadership, Financial Strategy",
    "Microsoft": "Reports, Market Research, Tech",
    "Google": "Tech, Leadership, Innovation"
}

# Display skills needed for each project
st.write("Skills needed for upcoming projects:")
for project, skills in project_skills.items():
    st.write(f"**{project}:** {skills}")

# --- Next Steps for HR ---
st.header("Next Steps: HR Hiring & Upskilling")

# Input field for HR to identify skill gaps
hr_input = st.text_area("HR: Please input a skill or project requirement for hiring/upskilling:", "")
if hr_input:
    st.write(f"HR has identified a requirement for: **{hr_input}**")
    st.write("We will suggest candidates for training or hiring.")

# Display HR skills recommendation
hr_skills_needed = ['Tech Consulting', 'Market Research', 'Leadership Development', 'Financial Projections', 'Emerging Technologies']
st.write("Recommended skills for upskilling or hiring:")
for skill in hr_skills_needed:
    st.write(f"- **{skill}**")

# --- Footer ---
st.markdown("---")
st.markdown("Crafted with ❤️ by PersonaX")
