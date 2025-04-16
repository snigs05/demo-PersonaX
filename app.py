# Generating the updated Streamlit app code with multiple views in the sidebar and designation filter only in the Main Dashboard

import streamlit as st
import pandas as pd
from datetime import datetime

# ------------------ Sidebar View Selector -------------------
st.sidebar.title("Navigation")
view = st.sidebar.radio("Choose View", ["Main Dashboard", "Consultant View", "Project Allocation", "TL View", "Chatbot"])

# ------------------ Dummy Data -------------------

consultants = pd.DataFrame([
    {"Name": "Snigdha Singh", "Designation": "Project Lead I", "Skills": "Startup Sourcing, Management Consulting", "Current Project": "Panasonic", "Availability": "2025-05-10", "OKRs": "Upskill in Tech", "L&D Plan": "AI for Consultants", "Projects": "NetApp, Panasonic, NASSCOM", "Status": "Occupied", "Manager Feedback": "Great on stakeholder engagement", "Client Feedback": "Strong research skills", "Suggestions": "Upcoming Zinnov Academy session on AI"},
    {"Name": "Aditya Gopalakrishnan", "Designation": "Project Lead I", "Skills": "Report, Automotive", "Current Project": "Flexera", "Availability": "2025-04-30", "OKRs": "Productivity, Tech Fluency", "L&D Plan": "Financial Modeling", "Projects": "MBRDI, Flexera, NASSCOM", "Status": "Occupied", "Manager Feedback": "Strong documentation", "Client Feedback": "Dependable and quick", "Suggestions": "Upcoming Google event on Automotive Tech"},
    {"Name": "Chirag Batra", "Designation": "Consultant II", "Skills": "Japanese Clients, Emerging Tech", "Current Project": "Sony", "Availability": "2025-05-20", "OKRs": "Client Engagement", "L&D Plan": "Blockchain Basics", "Projects": "Sumitomo, Marubeni, Sony", "Status": "Occupied", "Manager Feedback": "Cross-border strength", "Client Feedback": "Responsive", "Suggestions": "Upcoming session on GenAI Trends"},
    {"Name": "Gautham Savio", "Designation": "Senior Associate", "Skills": "Marketing, Events", "Current Project": "Zinnov Confluence", "Availability": "2025-04-15", "OKRs": "Digital Reach", "L&D Plan": "Marketing Analytics", "Projects": "Zinnov Awards", "Status": "Occupied", "Manager Feedback": "Great visibility work", "Client Feedback": "N/A", "Suggestions": "Social Media Mastery Workshop"},
    {"Name": "Jane Smith", "Designation": "Consultant I", "Skills": "Cloud, Research", "Current Project": "", "Availability": "Available", "OKRs": "Upskill in GenAI", "L&D Plan": "GenAI + Cloud", "Projects": "AWS Pitch", "Status": "Available", "Manager Feedback": "Quick learner", "Client Feedback": "N/A", "Suggestions": "Cloud AI Bootcamp"},
])

upcoming_projects = pd.DataFrame([
    {"Project": "MedInsights", "Required Skills": "Digital Health", "Start Date": "2025-05-15", "Project Fit Score": 85},
    {"Project": "CarsNova", "Required Skills": "Automotive, Report", "Start Date": "2025-05-10", "Project Fit Score": 76},
    {"Project": "ZetaBank", "Required Skills": "Cloud, Research", "Start Date": "2025-05-20", "Project Fit Score": 90},
])

# ------------------ Main Dashboard -------------------
if view == "Main Dashboard":
    st.title("Workforce Intelligence Dashboard")

    designation_filter = st.selectbox("Filter by Designation", consultants["Designation"].unique())
    filtered = consultants[consultants["Designation"] == designation_filter]

    st.subheader("Team Overview")
    st.dataframe(filtered[["Name", "Designation", "Skills", "Current Project", "Availability", "Status"]])

# ------------------ Consultant View -------------------
elif view == "Consultant View":
    st.title("Consultant View")

    consultant_names = consultants["Name"].tolist()
    selected_name = st.selectbox("Select Consultant", consultant_names)
    person = consultants[consultants["Name"] == selected_name].iloc[0]

    st.markdown(f"## {person['Name']}")
    st.markdown(f"**Designation:** {person['Designation']}")
    st.markdown(f"**Current Project:** {person['Current Project']}")
    st.markdown(f"**Availability:** {person['Availability']}")
    st.markdown(f"**Skills:** {person['Skills']}")
    st.markdown(f"**Learning Path**")
    st.info(f"OKRs: {person['OKRs']}")
    st.info(f"L&D Plan: {person['L&D Plan']}")
    st.success(f"Manager Feedback: {person['Manager Feedback']}")
    st.success(f"Client Feedback: {person['Client Feedback']}")
    st.warning(f"Suggestions: {person['Suggestions']}")
    st.markdown(f"**Project History:** {person['Projects']}")

# ------------------ Project Allocation -------------------
elif view == "Project Allocation":
    st.title("Project Allocation")

    st.subheader("Team Members & Status")
    consultants["AI Project Score"] = [82, 88, 80, 79, 85]
    st.dataframe(consultants[["Name", "Designation", "Current Project", "Availability", "Status", "AI Project Score"]])

    st.subheader("Upcoming Transitions")
    upcoming = consultants[consultants["Availability"] != "Available"]
    upcoming["Availability Date"] = pd.to_datetime(upcoming["Availability"], errors='coerce')
    upcoming = upcoming.sort_values(by="Availability Date")
    st.table(upcoming[["Name", "Availability", "Current Project"]].head(5))

# ------------------ TL View -------------------
elif view == "TL View":
    st.title("TL View")

    st.subheader("Upcoming Projects & Skill Needs")
    st.dataframe(upcoming_projects)

    st.subheader("Consultant Mapping Suggestions")
    for _, row in upcoming_projects.iterrows():
        st.markdown(f"**Project:** {row['Project']}")
        st.markdown(f"Required Skill: {row['Required Skills']}")
        match = consultants[(consultants["Skills"].str.contains(row["Required Skills"].split(",")[0])) & (consultants["Status"] == "Available")]
        if not match.empty:
            st.success(f"🟢 Potential Match: {match.iloc[0]['Name']}")
        else:
            st.error("🔴 No available consultant with required skill. Hiring or Upskilling Needed.")

# ------------------ Chatbot -------------------
elif view == "Chatbot":
    st.title("PersonaX Chatbot")
    question = st.text_input("Ask something like: Who is available next week?")

    if question:
        if "available" in question.lower():
            available = consultants[consultants["Status"] == "Available"]
            names = ", ".join(available["Name"].tolist())
            st.write(f"Available consultants: {names}")
        elif "skills" in question.lower():
            st.write("We track skills like Strategy, Retail, Fintech, Digital Health, SaaS, etc.")
        else:
            st.write("I'm still learning! Try asking about consultant availability or skillsets.")


# --- Footer ---
st.markdown("Crafted with ❤️ by PersonaX")
