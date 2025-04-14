# Generating the updated Streamlit app code with multiple views in the sidebar and designation filter only in the Main Dashboard

import streamlit as st
import pandas as pd
from datetime import datetime

# ------------------ Sidebar View Selector -------------------
st.sidebar.title("Navigation")
view = st.sidebar.radio("Choose View", ["Main Dashboard", "Consultant View", "Manager View", "HR View", "Chatbot"])

# ------------------ Dummy Data -------------------
consultants = pd.DataFrame([
    {"Name": "Snigdha Singh", "Designation": "Project Lead I", "Skills": "Startup Sourcing, Management Consulting", "Current Project": "NetApp", "Availability": "2025-05-10", "OKRs": "Upskill in Tech", "L&D Plan": "AI for Consultants", "Projects": "NetApp, Panasonic, NASSCOM", "Status": "Occupied"},
    {"Name": "Aditya Gopalakrishnan", "Designation": "Project Lead I", "Skills": "Reports, Automotive", "Current Project": "MBRDI", "Availability": "2025-04-30", "OKRs": "Productivity, Tech Fluency", "L&D Plan": "Financial Modeling", "Projects": "MBRDI, Flexera, NASSCOM", "Status": "Occupied"},
    {"Name": "Chirag Batra", "Designation": "Consultant II", "Skills": "Japanese Clients, Emerging Tech", "Current Project": "Sony", "Availability": "2025-05-20", "OKRs": "Client Engagement", "L&D Plan": "Blockchain Basics", "Projects": "Sumitomo, Marubeni, Sony", "Status": "Occupied"},
    {"Name": "Gautham Savio", "Designation": "Senior Associate", "Skills": "Marketing, Events", "Current Project": "Zinnov Awards", "Availability": "2025-04-15", "OKRs": "Digital Reach", "L&D Plan": "Marketing Analytics", "Projects": "Zinnov Awards", "Status": "Occupied"},
    {"Name": "John Doe", "Designation": "Project Lead II", "Skills": "Strategy, Fintech", "Current Project": "FinGrowth", "Availability": "2025-04-25", "OKRs": "Expand in BFSI", "L&D Plan": "Fintech Landscape", "Projects": "FinGrowth, RazorInvest", "Status": "Occupied"},
    {"Name": "Jane Smith", "Designation": "Consultant I", "Skills": "Retail, Market Sizing", "Current Project": "Retail360", "Availability": "2025-04-18", "OKRs": "Efficiency", "L&D Plan": "Retail Metrics", "Projects": "Retail360", "Status": "Occupied"},
    {"Name": "Ravi Kumar", "Designation": "Consultant I", "Skills": "Cloud, Research", "Current Project": "", "Availability": "Available", "OKRs": "Upskill in GenAI", "L&D Plan": "GenAI + Cloud", "Projects": "AWS Pitch", "Status": "Available"},
    {"Name": "Anita Sharma", "Designation": "Consultant II", "Skills": "Digital Health", "Current Project": "", "Availability": "Available", "OKRs": "Lead Next Project", "L&D Plan": "Healthcare Regulations", "Projects": "HealthTrack", "Status": "Available"},
    {"Name": "Rahul Mehra", "Designation": "Project Lead II", "Skills": "EdTech, Analytics", "Current Project": "SkillPilot", "Availability": "2025-05-01", "OKRs": "Improve Completion Rates", "L&D Plan": "Data Storytelling", "Projects": "SkillPilot, EduEdge", "Status": "Occupied"},
    {"Name": "Tina Kapoor", "Designation": "Consultant I", "Skills": "SaaS, Sales Ops", "Current Project": "", "Availability": "Available", "OKRs": "Improve Lead Conversions", "L&D Plan": "SaaS Funnels", "Projects": "SaaSTrack", "Status": "Available"},
])

upcoming_projects = pd.DataFrame([
    {"Project": "MedInsights", "Required Skills": "Digital Health", "Start Date": "2025-05-15"},
    {"Project": "RetailNova", "Required Skills": "Retail, Market Sizing", "Start Date": "2025-05-10"},
    {"Project": "ZetaBank", "Required Skills": "Fintech, Strategy", "Start Date": "2025-05-20"},
])

# ------------------ Main Dashboard -------------------
if view == "Main Dashboard":
    st.title("📊 Workforce Intelligence Dashboard")

    designation_filter = st.selectbox("Filter by Designation", consultants["Designation"].unique())
    filtered = consultants[consultants["Designation"] == designation_filter]

    st.subheader("Team Overview")
    st.dataframe(filtered[["Name", "Designation", "Skills", "Current Project", "Availability", "Status"]])

# ------------------ Consultant View -------------------
elif view == "Consultant View":
    st.title("🧑‍💼 Consultant View")

    consultant_names = consultants["Name"].tolist()
    selected_name = st.selectbox("Select Consultant", consultant_names)

    person = consultants[consultants["Name"] == selected_name].iloc[0]

    st.markdown(f"### Name: {person['Name']}")
    st.markdown(f"**Designation:** {person['Designation']}")
    st.markdown(f"**Current Project:** {person['Current Project']}")
    st.markdown(f"**Availability:** {person['Availability']}")
    st.markdown(f"**Skills:** {person['Skills']}")
    st.markdown(f"**OKRs:** {person['OKRs']}")
    st.markdown(f"**L&D Plan:** {person['L&D Plan']}")
    st.markdown(f"**Project History:** {person['Projects']}")

# ------------------ Manager View -------------------
elif view == "Manager View":
    st.title("👨‍💼 Manager View")

    st.subheader("Team Members & Status")
    st.dataframe(consultants[["Name", "Designation", "Current Project", "Availability", "Status"]])

    st.subheader("Upcoming Transitions")
    upcoming = consultants[consultants["Availability"] != "Available"]
    upcoming["Availability Date"] = pd.to_datetime(upcoming["Availability"], errors='coerce')
    upcoming = upcoming.sort_values(by="Availability Date")
    st.table(upcoming[["Name", "Availability", "Current Project"]].head(5))

# ------------------ HR View -------------------
elif view == "HR View":
    st.title("👩‍💼 HR View")

    st.subheader("Upcoming Projects & Skill Needs")
    st.table(upcoming_projects)

    st.subheader("Consultant Mapping")
    for _, row in upcoming_projects.iterrows():
        project = row["Project"]
        skill = row["Required Skills"]
        start_date = datetime.strptime(row["Start Date"], "%Y-%m-%d")

        st.markdown(f"**Project:** {project}")
        st.markdown(f"**Skill Required:** {skill}")
        match = consultants[(consultants["Skills"].str.contains(skill)) & (consultants["Status"] == "Available")]
        if not match.empty:
            st.success(f"🟢 Consultant Mapped: {match.iloc[0]['Name']}")
        else:
            st.error("🔴 No available consultant with required skill. Hiring Needed.")

# ------------------ Chatbot -------------------
elif view == "Chatbot":
    st.title("🤖 Talent Assistant Chatbot")

    question = st.text_input("Ask me anything (try: Who is available next week?)")

    if question:
        # Very basic dummy responses
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
