# 💼 RozgarCheck — Delhi NCR Job Market Analyzer

## Why I Built This

Okay so honest story — it was the end of my 2nd year and I was sitting there completely lost about which skills to actually learn for internships. Everyone says "learn Python" but then also "learn SQL" and "do deep learning" and I had no idea what Delhi companies actually want RIGHT NOW.

So instead of just googling it, I thought — I have pandas and Python, let me just build something that tells me. That's literally how this started. No grand plan, just a problem I had personally.

## What It Does

RozgarCheck analyzes job postings across Delhi NCR and shows you:
- Which skills companies are actually asking for (not just what YouTubers say to learn)
- Which companies are hiring interns right now
- How salaries and stipends compare across roles
- A search tool to filter by any skill or company

## What I Found Out (The Actual Insight)

After analyzing 30 job postings — Python shows up in literally every single Data Science internship in Delhi. Every one. SQL and Pandas come right after. So if you are a student and you are overwhelmed about where to start — start there.

## Tech I Used

- Python — main language
- Pandas — for reading and analyzing the job data
- Streamlit — to turn it into an actual website instead of just a boring notebook
- Matplotlib and Seaborn — for the charts
- Git and GitHub — version control (also spent way too long figuring out why git push wasn't working lol)

## How to Run It Yourself

pip install -r requirements.txt
python -m streamlit run app.py

## What I Learned Building This

Honestly the hardest part wasn't the code — it was structuring the project properly. I kept putting everything in one file first and it became a mess. Splitting analyzer.py and app.py separately made everything cleaner and I finally understood why people talk about separation of concerns in software engineering.

Also learned that Streamlit is genuinely magical for someone who doesn't know web development.

## What I Want to Add Next

- Live scraping from Naukri and LinkedIn instead of static CSV
- Email alerts when a new internship matches your skills
- Month by month skill trend tracking
- Filter by stipend amount

## Contact

Akshit Kapoor
B.Tech AI and Data Science — 2nd Year
akshitkapoor14ak@gmail.com
github.com/akshitkapoor14ak
