import streamlit as st
import PyPDF2

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get an instant ATS analysis.")

st.divider()

# Job roles and required skills
job_roles = {
    "Data Analyst": ["python", "sql", "excel", "power bi", "tableau"],
    "Data Scientist": ["python", "sql", "machine learning", "pandas", "numpy"],
    "Python Developer": ["python", "django", "flask", "git", "sql"],
    "Business Analyst": ["excel", "sql", "power bi", "tableau", "communication"],
    "ML Engineer": ["python", "machine learning", "numpy", "pandas", "tensorflow"]
}

# Skill aliases
skill_names = {
    "python": "Python",
    "sql": "SQL",
    "excel": "Excel",
    "power bi": "Power BI",
    "tableau": "Tableau",
    "machine learning": "Machine Learning",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "django": "Django",
    "flask": "Flask",
    "git": "Git",
    "tensorflow": "TensorFlow",
    "communication": "Communication"
}

# Upload resume
st.subheader("📤 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload PDF Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    # Read PDF
    reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text + " "

    resume_text = resume_text.lower()

    st.success("✅ Resume uploaded successfully!")

    # Detect skills
    detected_skills = []

    for skill in skill_names:
        if skill in resume_text:
            detected_skills.append(skill)

    st.divider()

    # Find best role
    results = []

    for role, required_skills in job_roles.items():

        matched = []

        for skill in required_skills:
            if skill in detected_skills:
                matched.append(skill)

        score = (len(matched) / len(required_skills)) * 100

        results.append({
            "role": role,
            "score": score,
            "matched": matched,
            "required": required_skills
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    best_role = results[0]

    # Dashboard
    st.subheader("📊 Resume Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{best_role['score']:.0f}%"
        )

    with col2:
        st.metric(
            "Matched Skills",
            len(best_role["matched"])
        )

    with col3:
        st.metric(
            "Recommended Role",
            best_role["role"]
        )

    st.divider()

    # Detected skills
    st.subheader("✅ Detected Skills")

    if detected_skills:

        for skill in detected_skills:
            st.success(skill_names[skill])

    else:
        st.warning("No supported skills detected.")

    st.divider()

    # Missing skills
    st.subheader("❌ Skills to Improve")

    missing_skills = [
        skill
        for skill in best_role["required"]
        if skill not in detected_skills
    ]

    if missing_skills:

        for skill in missing_skills:
            st.warning(skill_names[skill])

    else:
        st.success("🎉 Excellent! No major skill gaps found.")

    st.divider()

    # Role comparison
    st.subheader("🎯 Job Role Match")

    for result in results:

        st.write(
            f"**{result['role']} — {result['score']:.0f}%**"
        )

        st.progress(
            int(result["score"])
        )

    st.divider()

    # Recommendation
    st.subheader("💡 AI Recommendation")

    st.info(
        f"Your resume is currently a **{best_role['score']:.0f}% match** "
        f"for the **{best_role['role']}** role. "
        f"Focus on the missing skills to improve your ATS score."
    )

else:

    st.info(
        "👆 Upload a PDF resume above to start the analysis."
    )
