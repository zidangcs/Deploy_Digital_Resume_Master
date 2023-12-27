# Import Library
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "doc" / "CV-Jumadi.pdf"
profile_pic = current_dir / "doc" / "jumadi.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Jumadi"
PAGE_ICON = ":wave:"
NAME = "Jumadi"
DESCRIPTION = """
Perkenalkan nama saya Jumadi, 
saya adalah seorang praktisi di bidang IT khususnya di Artificial Intelligence, Machine Learning, Data Science, Programming. 
Saya memiliki pengalaman di Konsultan, mengerjakan project di beberapa perusahaan terutama di sektor e-commerce, jasa transportasi.
Saya juga seorang Instruktur Praktisi yang sudah banyak mengajarkan pelatihan 
ke beberapa Perusahaan terutama di Domain AI.

"""
EMAIL = "jumadijumadi470@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@kelasawanpintar",
    "LinkedIn": "https://www.linkedin.com/in/jumadi-01/",
    "GitHub": "https://github.com/jumadi-cloud",
    "Instagram": "https://www.instagram.com/jumadijumadi470/",
}
PROJECTS = {
    "🏆 Belajar Streamlit [Dasar] - Belajar Dasar sampai Membuat Aplikasi Machine Learning": "https://www.youtube.com/watch?v=0PBpAEGuNHM&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l",
    "🏆 Modeling For Chatbot - Web app menggunakan Python Flask": "https://www.youtube.com/watch?v=sImsnaxETYU&list=PLm94WimySTnoFUeg6DatP7SJmj-QyOplj&index=3",
    "🏆 Membuat Chatbot Menggunakan NLP - Web app menggunakan Python Flask": "https://www.youtube.com/watch?v=UG4-ZM8wsLE&list=PLm94WimySTnoFUeg6DatP7SJmj-QyOplj&index=4",
    "🏆 Membuat Chatbot Menggunakan Streamlit - Web app menggunakan Model ChatGPT": "https://www.youtube.com/watch?v=MaheNAPbBGU&list=PLm94WimySTnp8oZhsk_9iB_m92_ssgBbS&index=1",
    "🏆 Deploy Dengan Streamlit Cloud - Web app Multi Page menggunakan Streamlit": "https://www.youtube.com/watch?v=-QhZVIM8H2Y&list=PLm94WimySTnp8oZhsk_9iB_m92_ssgBbS&index=4",
    "🏆 Membuat Auto Machine Learning - Web app menggunakan Streamlit": "https://www.youtube.com/watch?v=mo0qEtwNDA4&list=PLm94WimySTnp8oZhsk_9iB_m92_ssgBbS&index=5",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Bagian pengaturan foto profile ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=270)
    st.write("Programmer | Artificial Intelligence | Content Creator at Kelas Awan Pintar")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Curicullum Vitae",
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


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 9 tahun berpengalaman teknis di bidang Supply Chain Management (SCM).
- ✔️ 5 tahun berpengalaman dalam bidang IT.
- ✔️ Menguasai data mining dan visuaisasi data menggunakan Streamlit.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, Laravel, Codeigniter
- 📊 Data Visulization: KNIME, Streamlit
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Coach Artificial Intelligence | PT Orbit Future Academy**")
st.write("2021 - Sekarang")

# --- JOB 2
st.write('\n')
st.write("🚧", "**Full-Stack Web Developer | PT Prima Armada Raya (PAR)**")
st.write("2020 - 2021")
st.write(
    """
- ► Menjaga dan memantau aplikasi yang ada.
- ► Dukungan mengembangkan fitur baru untuk aplikasi yang ada.
- ► Berkomunikasi dengan user mengenai masalah teknis.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**IT Support Application | PT Datasynthesis**")
st.write("2019 - 2020")
st.write(
    """
- ► Menjaga dan memantau aplikasi yang ada.
- ► Dukungan mengembangkan fitur baru untuk aplikasi yang ada.
- ► Berkomunikasi dengan divisi lain mengenai masalah teknis.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Assistant Trainer | Yayasan Komunitas Open Source**")
st.write("2019 - 2019")
st.write(
    """
- ► Pelatihan dan Pengembangan SDM.
"""
)

# --- JOB 5
st.write('\n')
st.write("🚧", "**Staff Network Operations Center (NOC) | PT. Skyreach**")
st.write("2018 - 2019")
st.write(
    """
- ► Mengontrol dan Monitoring semua site.
- ► Melakukan Troubelshoot dan Membuat report.
"""
)

# --- JOB 6
st.write('\n')
st.write("🚧", "**Supervisor Produksi Premik & Supply Chain | PT. Dapur Solo Sukses Sejati**")
st.write("2009 - 2018")
st.write(
    """
- ► Bertanggung jawab terhadap hal-hal yang berhubungan dengan jalanya oprasional.
- ► Membuat laporan setiap bulan.
- ► Mengontrol proses penimbangan bumbu premik.
- ► Menjaga kualitas dan kuantitas bumbu premik.
- ► Memastikan semua oprasional berjalan dengan baik dan sesuai SOP.
"""
)


# --- Projects & Pencapaian ---
st.write('\n')
st.subheader("Projects & Pencapaian")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
