# Generating the updated Streamlit app code with multiple views in the sidebar and designation filter only in the Main Dashboard

import streamlit as st
import pandas as pd
import random

# Dummy consultant data
consultants = [
    {"Name": "Snigdha Singh", "Designation": "Project Lead I", "Skills": ["Startup Sourcing", "Consulting", "Basic Tech"],
     "Current Project": "NetApp", "Next Project": "Panasonic", "Available From": "2025-06-01",
     "OKRs": ["Upskill in Tech", "Improve Productivity"], "Suggested Projects": ["Market Sizing", "Report Making"],
     "L&D Plan": ["Python Basics", "Excel Modelling"], "Expertise": "Startups, Strategy",
     "Past Projects": ["NetApp", "Panasonic", "NASSCOM Report"]},
    {"Name": "Aditya Gopalakrishnan", "Designation": "Project Lead I", "Skills": ["Reports", "Automotive", "Basic Tech"],
     "Current Project": "MBRDI", "Next Project": "Flexera", "Available From": "2025-05-15",
     "OKRs": ["Improve Report Quality", "Mentor Juniors"], "Suggested Projects": ["Financial Projections", "Benchmarking"],
     "L&D Plan": ["Data Visualization", "Storytelling"], "Expertise": "Automotive, Research",
     "Past Projects": ["MBRDI", "NASSCOM Report", "Flexera"]},
    {"Name": "Chirag Batra", "Designation": "Consultant II", "Skills": ["Japanese Clients", "Emerging Tech", "Basic Tech"],
     "Current Project": "Sumitomo", "Next Project": "Sony", "Available From": "2025-06-10",
     "OKRs": ["Strengthen Client Relationships", "Explore AI Use Cases"], "Suggested Projects": ["Emerging Tech Scouting"],
     "L&D Plan": ["Client Communication", "Innovation Trends"], "Expertise": "Japan Market, Tech",
     "Past Projects": ["Sumitomo", "Marubeni", "Sony"]},
    {"Name": "Gautham Savio", "Designation": "Senior Associate", "Skills": ["Marketing", "Branding", "Basic Tech"],
     "Current Project": "Internal", "Next Project": None, "Available From": "2025-04-20",
     "OKRs": ["Build Brand Presence"], "Suggested Projects": ["Digital Campaign Planning"],
     "L&D Plan": ["SEO Basics", "AdWords"], "Expertise": "Marketing Strategy",
     "Past Projects": ["Rebranding Campaign", "Newsletter Series", "Email Funnels"]},
]

# Dummy upcoming projects (HR View)
upcoming_projects = [
    {"Project": "Healthcare Tech GTM", "Required Skills": ["Consulting", "Market Sizing"], "Duration": "2 months"},
    {"Project": "EV Strategy Deck", "Required Skills": ["Automotive", "Financial Projections"], "Duration": "3 months"},
    {"Project": "Tech Trends Report", "Required Skills": ["Emerging Tech", "Report Making"], "Duration": "1.5 months"},
]

# App title
st.set_page_config(page_title="Workforce Intelligence Platform", layout="wide")
st.title("🧠 Workforce Intelligence Platform")

# Sidebar view switcher
view = st.sidebar.radio("Select View", ["Main Dashboard", "Consultant View", "Manager View", "HR View", "Chatbot"])

# Main Dashboard
if view == "Main Dashboard":
    st.header("📊 Team Overview")

    # Designation filter inside dashboard
    designations = sorted(set([c["Designation"] for c in consultants]))
    selected_designation = st.selectbox("Filter by Designation", ["All"] + designations)

    for c in consultants:
        if selected_designation != "All" and c["Designation"] != selected_designation:
            continue
        st.subheader(f"{c['Name']} ({c['Designation']})")
        st.write(f"**Current Project:** {c['Current Project']}")
        st.write(f"**Next Project:** {c['Next Project']}")
        st.write(f"**Available From:** {c['Available From']}")
        st.write(f"**Skills:** {', '.join(c['Skills'])}")
        st.write("---")

# Consultant View
elif view == "Consultant View":
    st.header("🧑‍💼 Consultant View")

    selected_name = st.selectbox("Select Your Name", [c["Name"] for c in consultants])
    consultant = next((c for c in consultants if c["Name"] == selected_name), None)

    if consultant:
        st.subheader(f"Welcome, {consultant['Name']} ({consultant['Designation']})")
        st.write(f"**OKRs:**")
        st.markdown("- " + "<br>- ".join(consultant["OKRs"]), unsafe_allow_html=True)
        st.write("**Suggested Projects:**")
        st.markdown("- " + "<br>- ".join(consultant["Suggested Projects"]), unsafe_allow_html=True)
        st.write("**Learning & Development Plan:**")
        st.markdown("- " + "<br>- ".join(consultant["L&D Plan"]), unsafe_allow_html=True)
        st.write("**Past Projects:**")
        st.markdown("- " + "<br>- ".join(consultant["Past Projects"]), unsafe_allow_html=True)

# Manager View (placeholder)
elif view == "Manager View":
    st.header("👩‍💻 Manager View")
    st.info("This section will include team load, project allocation, and performance insights. Coming soon!")

# HR View
elif view == "HR View":
    st.header("🧑‍💼 HR View: Upcoming Projects & Skill Matching")

    for p in upcoming_projects:
        st.subheader(f"📌 {p['Project']}")
        st.write(f"**Required Skills:** {', '.join(p['Required Skills'])}")
        st.write(f"**Duration:** {p['Duration']}")

        # Skill matching logic
        matched = []
        needs_hiring = True
        for c in consultants:
            if any(skill in c["Skills"] for skill in p["Required Skills"]):
                if pd.to_datetime(c["Available From"]) <= pd.to_datetime("2025-06-01"):
                    matched.append(c["Name"])
                    needs_hiring = False

        if matched:
            st.success(f"Matched Consultants: {', '.join(matched)}")
        if needs_hiring:
            st.warning("⚠️ No available consultants fully match. Recommend upskilling or hiring.")

# Chatbot View (placeholder with sample Q&A)
elif view == "Chatbot":
    st.header("🤖 Workforce Chatbot")
    question = st.text_input("Ask a question:")

    # Simple response logic
    sample_qna = {
        "who is available in june": "Snigdha Singh and Chirag Batra are available in June.",
        "suggest projects for aditya": "Based on Aditya's expertise, suggested projects include Financial Projections and Benchmarking.",
        "skills needed for tech trends report": "The required skills are Emerging Tech and Report Making.",
        "who can work on healthcare tech": "Snigdha Singh has Consulting and Market Sizing experience. She is a good fit.",
    }

    if question:
        response = sample_qna.get(question.lower(), "I'm still learning! Please try another question.")
        st.write(f"💬 {response}")

# --- Footer ---
st.markdown("Crafted with ❤️ by PersonaX")
