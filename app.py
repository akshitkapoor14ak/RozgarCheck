import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analyzer import (
    load_data, get_top_skills, get_jobs_by_location,
    get_job_type_split, get_internships,
    get_top_hiring_companies, get_skills_for_internships,
    search_jobs
)

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="RozgarCheck - Delhi Job Market",
    page_icon="💼",
    layout="wide"
)

# --- HEADER ---
st.title("💼 RozgarCheck")
st.subheader("Delhi NCR Job Market Analyzer — Data Science & AI Edition")
st.markdown("*Built this because I was confused about which skills to learn — so I analyzed it myself*")
st.markdown("---")

# --- LOAD DATA ---
df = load_data()

# --- TOP METRICS ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Jobs", len(df))
col2.metric("Internships", len(df[df["job_type"] == "Internship"]))
col3.metric("Companies Hiring", df["company"].nunique())
col4.metric("Cities Covered", df["location"].nunique())

st.markdown("---")

# --- SIDEBAR ---
st.sidebar.title("🔍 Explore")
st.sidebar.markdown("*What do you want to know?*")
section = st.sidebar.radio("Go to section:", [
    "Top Skills in Demand",
    "Internships Available",
    "Jobs by Location",
    "Top Hiring Companies",
    "Skills for Internships",
    "Search Jobs"
])

# --- SECTION 1: TOP SKILLS ---
if section == "Top Skills in Demand":
    st.header("🔥 Top Skills Companies Want")
    st.write("Based on all job postings in Delhi NCR — this is what I found out after analyzing 30 listings")

    skills_df = get_top_skills(df)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=skills_df, x="Count", y="Skill",
                palette="viridis", ax=ax)
    ax.set_title("Most In-Demand Skills - Delhi NCR", fontsize=16)
    ax.set_xlabel("Number of Job Postings")
    st.pyplot(fig)

    st.markdown("**My takeaway:** Python is everywhere. If you learn nothing else, learn Python first.")
    st.dataframe(skills_df, use_container_width=True)

# --- SECTION 2: INTERNSHIPS ---
elif section == "Internships Available":
    st.header("🎓 Internships in Delhi NCR")
    st.write("Filtered specifically for students — all internship opportunities in one place")

    intern_df = get_internships(df)
    st.dataframe(intern_df, use_container_width=True)

    st.subheader("Skills needed for Internships")
    skills_df = get_skills_for_internships(df)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=skills_df, x="Count", y="Skill",
                palette="rocket", ax=ax)
    ax.set_title("Top Skills for Internships")
    st.pyplot(fig)

# --- SECTION 3: JOBS BY LOCATION ---
elif section == "Jobs by Location":
    st.header("📍 Jobs by City")
    st.write("Delhi, Gurgaon, Noida — the three hubs of NCR tech")

    loc_df = get_jobs_by_location(df)
    loc_df.columns = ["Location", "Count"]

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.pie(loc_df["Count"], labels=loc_df["Location"],
           autopct="%1.1f%%", startangle=140,
           colors=sns.color_palette("pastel"))
    ax.set_title("Job Distribution by City")
    st.pyplot(fig)

    st.dataframe(loc_df, use_container_width=True)

# --- SECTION 4: TOP COMPANIES ---
elif section == "Top Hiring Companies":
    st.header("🏢 Top Hiring Companies")
    st.write("Companies actively posting DS and AI roles in NCR")

    comp_df = df["company"].value_counts().reset_index()
    comp_df.columns = ["Company", "Openings"]

    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(data=comp_df.head(10), x="Openings",
                y="Company", palette="mako", ax=ax)
    ax.set_title("Companies with Most Openings")
    st.pyplot(fig)

# --- SECTION 5: INTERNSHIP SKILLS ---
elif section == "Skills for Internships":
    st.header("🛠️ What Skills Do You Need for Internships?")
    st.write("I built this section specifically for myself — focus on these if you are a student")

    skills_df = get_skills_for_internships(df)
    st.dataframe(skills_df, use_container_width=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(skills_df["Count"], labels=skills_df["Skill"],
           autopct="%1.1f%%",
           colors=sns.color_palette("Set3"))
    ax.set_title("Internship Skills Breakdown")
    st.pyplot(fig)

# --- SECTION 6: SEARCH ---
elif section == "Search Jobs":
    st.header("🔎 Search Jobs")
    st.write("Search by skill, company, or job title — type anything")

    keyword = st.text_input("Enter keyword (e.g. Python, NLP, Zomato):")
    if keyword:
        results = search_jobs(df, keyword)
        if len(results) == 0:
            st.warning("No jobs found for that keyword. Try something else!")
        else:
            st.success(f"Found {len(results)} jobs matching '{keyword}'!")
            st.dataframe(results, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.caption("Built by Akshit Kapoor | B.Tech AI & Data Science | github.com/akshitkapoor14ak")