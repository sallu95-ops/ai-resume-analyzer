import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume and find the best job role.")

st.divider()

st.subheader("📊 Resume Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ATS Score", "100%")

with col2:
    st.metric("Matched Skills", "4")

with col3:
    st.metric("Recommended Role", "Data Analyst")

st.divider()

st.subheader("✅ Your Skills")

skills = ["Python", "SQL", "Excel", "Power BI"]

for skill in skills:
    st.success(skill)

st.subheader("💡 Recommendation")
st.info("Your profile is a strong match for a Data Analyst role.")
