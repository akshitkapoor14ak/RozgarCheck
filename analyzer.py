import pandas as pd
from collections import Counter

# loading the dataset — kept this in a separate function so I can
# easily swap the CSV with live scraped data later
def load_data():
    df = pd.read_csv("data/jobs.csv")
    return df

# this was the most interesting function to build — basically each
# job has multiple skills separated by | so I had to split them all
# first before counting. took me a while to figure out extend() vs append()
def get_top_skills(df, top_n=15):
    all_skills = []
    for skills in df["skills"]:
        all_skills.extend(skills.split("|"))
    skill_counts = Counter(all_skills)
    skills_df = pd.DataFrame(skill_counts.most_common(top_n),
                             columns=["Skill", "Count"])
    return skills_df

# simple one — just grouping by city
# delhi, gurgaon, noida are the 3 main hubs for tech in NCR
def get_jobs_by_location(df):
    return df["location"].value_counts().reset_index()

# full time vs internship split
def get_job_type_split(df):
    return df["job_type"].value_counts().reset_index()

# filtering only internships — this is the most useful one for me
# personally since I am literally looking for internships right now
def get_internships(df):
    internships = df[df["job_type"] == "Internship"].copy()
    return internships[["job_title", "company",
                        "location", "skills", "salary_range"]]

# same logic as get_top_skills but only looking at internship rows
# wanted to see if internship skill requirements differ from full time
# turns out they do — internships want more pandas and sklearn,
# full time wants more tensorflow and aws
def get_skills_for_internships(df):
    intern_df = df[df["job_type"] == "Internship"]
    all_skills = []
    for skills in intern_df["skills"]:
        all_skills.extend(skills.split("|"))
    skill_counts = Counter(all_skills)
    skills_df = pd.DataFrame(skill_counts.most_common(10),
                             columns=["Skill", "Count"])
    return skills_df

# search function — checks job title, skills, and company name
# using | as OR operator in pandas, learned this the hard way
# first tried doing 3 separate filters and merging them, this is cleaner
def search_jobs(df, keyword):
    keyword = keyword.lower()
    mask = (
        df["job_title"].str.lower().str.contains(keyword) |
        df["skills"].str.lower().str.contains(keyword) |
        df["company"].str.lower().str.contains(keyword)
    )
    return df[mask]

# one thing I want to add later — a function that compares
# skill demand month over month once I have live data
# for now this static CSV works fine to prove the concept
def get_top_hiring_companies(df):
    return df["company"].value_counts().reset_index()