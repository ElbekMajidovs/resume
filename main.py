import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Elbek Majidov - Senior Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, rgba(147, 51, 234, 0.2), rgba(219, 39, 119, 0.2));
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 2px solid rgba(147, 51, 234, 0.3);
    }
    
    .name-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #a78bfa, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .role-title {
        font-size: 1.8rem;
        color: #c084fc;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .summary-text {
        color: #d1d5db;
        font-size: 1.1rem;
        max-width: 900px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Section headers */
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #a78bfa;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid rgba(167, 139, 250, 0.3);
    }
    
    /* Card styling */
    .custom-card {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(147, 51, 234, 0.2);
        transition: all 0.3s ease;
    }
    
    .custom-card:hover {
        border-color: rgba(147, 51, 234, 0.5);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(147, 51, 234, 0.3);
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #f3f4f6;
        margin-bottom: 0.5rem;
    }
    
    .card-subtitle {
        font-size: 1.1rem;
        color: #c084fc;
        margin-bottom: 0.8rem;
    }
    
    .card-meta {
        color: #9ca3af;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }
    
    .card-text {
        color: #d1d5db;
        line-height: 1.6;
    }
    
    /* Project cards */
    .project-card {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        border: 1px solid rgba(147, 51, 234, 0.2);
        height: 100%;
    }
    
    .project-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .project-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #f3f4f6;
        margin-bottom: 0.5rem;
    }
    
    .project-tech {
        color: #c084fc;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    
    .project-desc {
        color: #d1d5db;
        line-height: 1.5;
    }
    
    /* Skills styling */
    .skill-category {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        border: 1px solid rgba(147, 51, 234, 0.2);
        height: 100%;
    }
    
    .skill-category-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #c084fc;
        margin-bottom: 1rem;
    }
    
    .skill-item {
        color: #d1d5db;
        padding: 0.5rem 0;
        border-bottom: 1px solid rgba(147, 51, 234, 0.1);
    }
    
    /* Contact section */
    .contact-info {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        border: 1px solid rgba(147, 51, 234, 0.2);
        text-align: center;
    }
    
    .contact-item {
        color: #d1d5db;
        font-size: 1.1rem;
        margin: 1rem 0;
    }
    
    .contact-label {
        color: #c084fc;
        font-weight: 600;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #7c3aed, #db2777);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(147, 51, 234, 0.4);
    }
    
    /* Education card */
    .education-card {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #c084fc;
    }
    
    .education-degree {
        font-size: 1.2rem;
        font-weight: 700;
        color: #f3f4f6;
    }
    
    .education-school {
        color: #c084fc;
        font-size: 1rem;
        margin-top: 0.3rem;
    }
    
    /* Bullet points */
    ul {
        color: #d1d5db;
        line-height: 1.8;
    }
    
    li {
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="main-header">
    <div class="name-title">ELBEK MAJIDOV</div>
    <div class="role-title">Senior Data Analyst</div>
    <div class="summary-text">
        Data-driven professional with 3+ years of experience in financial and procurement analytics, 
        dashboard development, and machine learning. Expert in Python, R, SQL, Tableau, and Power BI, 
        passionate about leveraging GenAI, NLP, and LLMs to extract actionable insights and drive innovation.
    </div>
</div>
""", unsafe_allow_html=True)

# Contact buttons row
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown("📧 **majidoverick@gmail.com**")
with col2:
    st.markdown("📍 **Warsaw, Poland**")
with col3:
    st.markdown("📞 **+(48) 514 872 614**")
with col4:
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com)")
with col5:
    st.markdown("[💻 GitHub](https://github.com)")

# Experience Section
st.markdown('<div class="section-header">💼 Work Experience</div>', unsafe_allow_html=True)

experiences = [
    {
        "company": "Alcon",
        "role": "Senior Data Analyst",
        "period": "Jul 2024 - Present",
        "location": "Warsaw, Poland",
        "highlights": [
            "Designed and maintained a Tableau Spend & Savings dashboard driving actionable insights for FP&A and Procurement, earning a Green Belt certification",
            "Managed and delivered 6+ data projects, implementing analytical solutions and optimizing workflows",
            "Partnered with business and technical teams to ensure seamless integration and process standardization"
        ]
    },
    {
        "company": "Alcon",
        "role": "Data Analyst",
        "period": "Feb 2024 - Jul 2024",
        "location": "Warsaw, Poland",
        "highlights": [
            "Developed interactive dashboards and reports for Fleet and M&E categories leading to 20% improvement in data-driven decision-making",
            "Conducted exploratory clustering and dimensionality-reduction analysis on a 190-feature dataset using R & Python",
            "Identified meaningful segments supporting downstream supplier risk modelling for procurement operations"
        ]
    },
    {
        "company": "Philips",
        "role": "Reporting Specialist",
        "period": "Aug 2022 - Jan 2024",
        "location": "Łódź, Poland",
        "highlights": [
            "Conducted in-depth research identifying potential automation areas, resulting in 30% reduction in procurement cycle time",
            "Assisted in developing comprehensive financial models to track vendor performance using Power BI",
            "Achieved 20% increase in supplier accountability through data-driven insights"
        ]
    },
    {
        "company": "Philips",
        "role": "Reporting Intern",
        "period": "Feb 2022 - Jul 2022",
        "location": "Łódź, Poland",
        "highlights": [
            "Developed comprehensive daily and weekly reports providing valuable insights and data-driven recommendations",
            "Optimized purchasing strategies leading to 20% increase in cost savings"
        ]
    },
    {
        "company": "Whirlpool Corporation",
        "role": "Accounting Intern",
        "period": "Mar 2020 - Jan 2022",
        "location": "Łódź, Poland",
        "highlights": [
            "Assisted in developing financial performance reports and implementing data-driven process enhancements",
            "Improved workflow efficiency and reduced processing time through automation initiatives"
        ]
    }
]

for exp in experiences:
    st.markdown(f"""
    <div class="custom-card">
        <div class="card-title">{exp['role']}</div>
        <div class="card-subtitle">{exp['company']}</div>
        <div class="card-meta">{exp['period']} | {exp['location']}</div>
    </div>
    """, unsafe_allow_html=True)
    for highlight in exp['highlights']:
        st.markdown(f"• {highlight}")
    st.markdown("<br>", unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="section-header">🚀 Featured Projects</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

projects = [
    {
        "icon": "📊",
        "title": "Customer Segmentation & Basket Analysis",
        "tech": "Python, K-Means, Hierarchical Clustering, PCA, Apriori, ECLAT, FP-Growth",
        "description": "Performed unsupervised learning to segment customers based on behavior and preferences. Applied association rule mining to uncover patterns in purchasing behavior, improving basket value prediction accuracy by 18%."
    },
    {
        "icon": "🌍",
        "title": "Global Development Clustering Analysis",
        "tech": "Python, R, PCA, K-means, World Bank Dataset",
        "description": "Analyzed World Bank's World Development Indicators covering 190+ countries. Applied clustering and dimensionality reduction to group countries based on developmental characteristics and uncover key drivers of progress in health, education, and infrastructure."
    },
    {
        "icon": "💰",
        "title": "Incremental Cash Flow & Investment Analysis",
        "tech": "DCF, NPV, Payback Period, Financial Modeling",
        "description": "Compared investment strategies through incremental and discounted cash flow analysis. Calculated NPV, Payback Period (≈39 years), and total network cost impacts. Evaluated long-term benefits including 250-year lifespan and sustainability alignment."
    },
    {
        "icon": "👥",
        "title": "Workforce Optimization Model",
        "tech": "R, Linear & Logistic Regression, Statistical Modeling",
        "description": "Built regression models to assess productivity improvements from replacing temporary with full-time staff. Projected +9,000 samples/year and –7% error reduction. Demonstrated temporary staff showed 16 fewer samples/hour and 5× higher error risk."
    }
]

for i, project in enumerate(projects):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-icon">{project['icon']}</div>
            <div class="project-title">{project['title']}</div>
            <div class="project-tech">{project['tech']}</div>
            <div class="project-desc">{project['description']}</div>
        </div>
        """, unsafe_allow_html=True)

# Skills Section
st.markdown('<div class="section-header">🎯 Skills & Expertise</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

skills = {
    "Technical Skills": [
        "Python (Pandas, NumPy, Scikit-learn)",
        "TensorFlow & PyTorch",
        "R, SQL, VBA, Git",
        "Power BI & Tableau",
        "Machine Learning & Deep Learning",
        "NLP, GenAI, LLMs",
        "Jupyter, VS Code"
    ],
    "Analytical Skills": [
        "Data Storytelling & Visualization",
        "Problem-Solving & Critical Thinking",
        "Cross-Functional Collaboration",
        "Stakeholder Engagement",
        "Project Management",
        "Communication & Leadership",
        "Adaptability"
    ],
    "Domain Expertise": [
        "Financial Analytics & FP&A",
        "Procurement Analytics",
        "Supply Chain Management",
        "Vendor Performance Analytics",
        "Risk Analytics & Modeling",
        "Investment Evaluation (DCF, NPV, IRR)",
        "Data-Driven Decision Support"
    ]
}

with col1:
    st.markdown(f"""
    <div class="skill-category">
        <div class="skill-category-title">💻 {list(skills.keys())[0]}</div>
    </div>
    """, unsafe_allow_html=True)
    for skill in skills[list(skills.keys())[0]]:
        st.markdown(f"<div class='skill-item'>▸ {skill}</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="skill-category">
        <div class="skill-category-title">🧠 {list(skills.keys())[1]}</div>
    </div>
    """, unsafe_allow_html=True)
    for skill in skills[list(skills.keys())[1]]:
        st.markdown(f"<div class='skill-item'>▸ {skill}</div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="skill-category">
        <div class="skill-category-title">📈 {list(skills.keys())[2]}</div>
    </div>
    """, unsafe_allow_html=True)
    for skill in skills[list(skills.keys())[2]]:
        st.markdown(f"<div class='skill-item'>▸ {skill}</div>", unsafe_allow_html=True)

# Education Section
st.markdown('<div class="section-header">🎓 Education</div>', unsafe_allow_html=True)

education = [
    {
        "degree": "Master of Science in Data Science (M.Sc.)",
        "school": "University of Warsaw, Poland"
    },
    {
        "degree": "Master of Science in Managerial Decision-Making and Control (M.Sc.)",
        "school": "Maastricht University, Netherlands"
    },
    {
        "degree": "Bachelor in Computer Science (BCS)",
        "school": "University of Lodz, Poland"
    }
]

for edu in education:
    st.markdown(f"""
    <div class="education-card">
        <div class="education-degree">{edu['degree']}</div>
        <div class="education-school">{edu['school']}</div>
    </div>
    """, unsafe_allow_html=True)

# Activities Section
st.markdown('<div class="section-header">🌟 Activities & Interests</div>', unsafe_allow_html=True)

activities_col1, activities_col2, activities_col3 = st.columns(3)

with activities_col1:
    st.markdown("""
    <div class="custom-card" style="text-align: center;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🤝</div>
        <div class="card-subtitle">Volunteer at 4EU+ Alliance</div>
    </div>
    """, unsafe_allow_html=True)

with activities_col2:
    st.markdown("""
    <div class="custom-card" style="text-align: center;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">👨‍🏫</div>
        <div class="card-subtitle">Ex-volunteer Mentor<br>University of Lodz</div>
    </div>
    """, unsafe_allow_html=True)

with activities_col3:
    st.markdown("""
    <div class="custom-card" style="text-align: center;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🎤</div>
        <div class="card-subtitle">Public Speaker<br>& Avid Learner</div>
    </div>
    """, unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="section-header">📬 Get In Touch</div>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-info">
    <div style="font-size: 1.3rem; color: #a78bfa; font-weight: 700; margin-bottom: 1.5rem;">
        Let's Connect!
    </div>
    <div class="contact-item">
        <span class="contact-label">Email:</span> majidoverick@gmail.com
    </div>
    <div class="contact-item">
        <span class="contact-label">Phone:</span> +(48) 514 872 614
    </div>
    <div class="contact-item">
        <span class="contact-label">Location:</span> Warsaw, Poland
    </div>
    <div style="margin-top: 2rem;">
        <span style="color: #d1d5db; font-size: 1.1rem;">
            Open to discussing new opportunities, collaborations, and data science projects
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 2rem 0; border-top: 1px solid rgba(147, 51, 234, 0.2);">
    <p>© 2026 Elbek Majidov. All rights reserved.</p>
    <p style="margin-top: 0.5rem; font-size: 0.9rem;">Built with Streamlit 🎈</p>
</div>
""", unsafe_allow_html=True)
