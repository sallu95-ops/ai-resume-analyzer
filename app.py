import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get personalized job recommendations.")

st.divider()

# Job roles and required skills
job_roles = {
    "Data Analyst": [
        "python", "sql", "excel", "power bi"
    ],
    "Data Scientist": [
        "python", "sql", "machine learning", "pandas", "numpy"
    ],
    "Python Developer": [
        "python", "django", "flask", "git"
    ],
    "Business Analyst": [
        "excel", "sql", "power bi", "communication"
    ],
    "ML Engineer": [
        "python", "machine learning", "numpy", "pandas", "tensorflow"
    ]
}

# Skills that can be detected
all_skills = [
    "python",
    "sql",
    "excel",
    "power bi",
    "machine learning",
    "pandas",
    "numpy",
    "django",
    "flask",
    "git",
    "communication",
    "tensorflow"
]

# Upload PDF
uploaded_file = st.file_uploader(
    "📤 Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    # Read PDF
    pdf_reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text + " "

    resume_text = resume_text.lower()

    # Detect skills
    detected_skills = []

    for skill in all_skills:
        if skill in resume_text:
            detected_skills.append(skill)

    st.divider()

    # Show detected skills
    st.subheader("🧠 Detected Skills")

    if detected_skills:
        for skill in detected_skills:
            st.success("✅ " + skill.title())
    else:
        st.warning("No matching skills found.")

    # Calculate role scores
    results = []

    for role, required_skills in job_roles.items():

        matched = []

        for skill in required_skills:
            if skill in detected_skills:
                matched.append(skill)

        score = (
            len(matched) / len(required_skills)
        ) * 100

        missing = [
            skill
            for skill in required_skills
            if skill not in detected_skills
        ]

        results.append({
            "role": role,
            "score": score,
            "matched": matched,
            "missing": missing
        })

    # Find best role
    best_role = max(
        results,
        key=lambda x: x["score"]
    )

    st.divider()

    st.subheader("🎯 Best Job Recommendation")

    st.success(
        "Recommended Role: " + best_role["role"]
    )

    st.metric(
        "ATS Match Score",
        f"{best_role['score']:.0f}%"
    )

    # Matched skills
    st.subheader("✅ Matched Skills")

    if best_role["matched"]:

        for skill in best_role["matched"]:
            st.write("✅", skill.title())

    else:
        st.write("No matched skills.")

    # Missing skills
    st.subheader("❌ Missing Skills")

    if best_role["missing"]:

        for skill in best_role["missing"]:
            st.write("❌", skill.title())

    else:

        st.success(
            "🎉 No major missing skills!"
        )

    # All role scores
    st.divider()

    st.subheader("📊 Job Role Match")

    for result in results:

        st.write(
            f"**{result['role']} — "
            f"{result['score']:.0f}%**"
        )

        st.progress(
            int(result["score"])
        )

else:

    st.info(
        "👆 Upload a PDF resume to start analysis."
    )
