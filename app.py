import streamlit as st

from pathlib import Path

from PIL import Image

# --- PATH SETTINGS ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "prem.jpg"


# --- GENERAL SETTINGS ---

NAME = "Premsagar Patra"
DESCRIPTION = """

Always learning, growing, dreaming and trying to be a better person than who I'm today.
My aim is to work as a Data Scientist and continue the process of acquiring knowledge in my domain.

"""

EMAIL = "prempatra15@gmail.com" 

SOCIAL_MEDIA = {

    "LinkedIn": "https://www.linkedin.com/in/premspatra/",
    "GitHub": "https://github.com/Prempatra15",
    "Contact No": "8917629568"
}


# --- LOAD PDF & PROFIL PIC ---

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE ---

st.write('\n')
st.subheader("Experience")
st.write(
    """
-  1 Year expereince extracting actionable insights from data
-  Strong hands on experience and knowledge in Python
-  Good understanding of statistical principles and their respective applications

"""
)


# --- SKILLS ---

st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Numpy, Pandas), SQL
- 📊 Data Visulization: Matplotlib, Seaborn, Tableau
- 📚 Modeling: Regression, Classification, Clustering, Dimensionality Reduction, Deep learning
- 🗄️ Databases: MySQL
"""
)



