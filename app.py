import streamlit as st
from utils import extract_text_from_pdf, clean_text, calculate_ats_score

st.title("AI Resume Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if resume_file and job_desc:
        resume_text = extract_text_from_pdf(resume_file)
        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(job_desc)

        score = calculate_ats_score(resume_clean, jd_clean)

        st.subheader("ATS Score")
        st.success(f"{score}% Match")

        if score > 75:
            st.write("Strong Resume Match")
        elif score > 50:
            st.write("Moderate Match – Improve keywords")
        else:
            st.write("Low Match – Add relevant skills")
