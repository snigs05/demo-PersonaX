import streamlit as st
import pandas as pd
import random

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

def get_available_consultants(skills_needed):
    available_consultants = df[df['Skills'].str.contains(skills_needed)]
    return available_consultants

# --- App Layout ---
st.set_page_config(page_title="Consultant Dashboard", page_icon=":guardsman:", layout="wide")

# Title
st.title("Consultant Workforce Dashboard")

# Sidebar for View Selection (Main Dashboard, Consultant View, HR View, Manager View, Chatbot)
view_selection = st.sidebar.radio("Select View", ["Main Dashboard", "Consultant View", "HR View", "Manager View", "Chatbot"])

# --- Main Dashboard ---
if view_selection == "Main Dashboard":
    st.header("Welcome to the Consultant Dashboard! 🎉")
    st.subheader("Filter consultants by designation and explore available data.")
    
    # Designation Filter
    designation_filter = st.selectbox("Filter by Designation", ["All", "Project Lead I", "Consultant II", "Senior Associate in Marketing", "Consultant I", "Project Lead II"])
    
    # Display filtered data based on designation
    filtered_df = get_filtered_data(designation_filter)
    st.write(filtered_df)

    st.write("### Explore the sections below to interact with specific views.")

# --- Consultant View ---
elif view_selection == "Consultant View":
    st.header("Consultant Profile 🧑‍💼")
    selected_consultant = st.selectbox("Select Consultant", df['Name'].unique())
    consultant_data = df[df['Name'] == selected_consultant].iloc[0]
    
    st.write(f"**Name**: {consultant_data['Name']}")
    st.write(f"**Designation**: {consultant_data['Designation']}")
    st.write(f"**Skills**: {consultant_data['Skills']}")
    st.write(f"**OKRs**: {consultant_data['OKRs']}")
    st.write(f"**Projects**: {consultant_data['Projects']}")
    st.write(f"**L&D Plan**: {consultant_data['L&D Plan']}")
    st.write(f"**Project Status**: {consultant_data['Project Status']}")
    st.write(f"**Last Feedback**: {get_random_feedback()}")

# --- HR View ---
elif view_selection == "HR View":
    st.header("HR View - Upcoming Projects & Consultant Mapping")
    
    # List of upcoming projects with skills needed
    upcoming_projects = {
        "NetApp": "Tech, Consulting, Startup Sourcing",
        "Panasonic": "Tech, Consulting, Market Sizing",
        "NASSCOM Report": "Reports, Market Analysis, Tech Sourcing",
        "Sumitomo": "Japanese Clients, Market Research, Tech",
        "Flexera": "Reports, Financial Projections",
        "Tesla": "Tech, Leadership, Financial Strategy",
        "Microsoft": "Reports, Market Research, Tech",
        "Google": "Tech, Leadership, Innovation"
    }
    
    # Display upcoming projects and skills needed
    for project, skills in upcoming_projects.items():
        st.write(f"**{project}:** {skills}")
        
        # Get available consultants based on skills needed
        available_consultants = get_available_consultants(skills)
        
        if len(available_consultants) > 0:
            st.write(f"Available Consultants: {', '.join(available_consultants['Name'])}")
        else:
            st.write("No consultants available for this project. HR needs to hire or upskill consultants.")

# --- Manager View ---
elif view_selection == "Manager View":
    st.header("Manager View - Consultant Management")
    st.subheader("Oversee project allocation, feedback, and team performance.")
    
    # List of consultants
    st.write(df[['Name', 'Designation', 'Project Status', 'Last Feedback']])

# --- Chatbot ---
elif view_selection == "Chatbot":
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

# --- Footer ---
st.markdown("---")
st.markdown("Crafted with ❤️ by PersonaX")
