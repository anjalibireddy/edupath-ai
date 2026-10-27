"""Sample data for EduPath AI. Extend these dicts to add exams, roles or careers."""

# exam -> subject -> topics
SYLLABI = {
    "JEE Main": {
        "Physics": ["Mechanics", "Thermodynamics", "Electrostatics", "Optics", "Modern Physics"],
        "Chemistry": ["Atomic Structure", "Chemical Bonding", "Organic Basics", "Chemical Equilibrium"],
        "Mathematics": ["Calculus", "Algebra", "Coordinate Geometry", "Probability", "Vectors & 3D"],
    },
    "NEET": {
        "Physics": ["Kinematics", "Laws of Motion", "Current Electricity", "Ray Optics"],
        "Chemistry": ["Mole Concept", "Periodic Table", "Hydrocarbons", "Biomolecules"],
        "Biology": ["Cell Structure", "Genetics", "Human Physiology", "Plant Physiology", "Ecology"],
    },
    "Coding Interviews": {
        "DSA": ["Arrays & Strings", "Linked Lists", "Trees & Graphs", "Dynamic Programming", "Sorting & Searching"],
        "CS Fundamentals": ["OOP", "DBMS & SQL", "Operating Systems", "Computer Networks"],
        "System Design": ["REST API Design", "Caching", "Database Scaling"],
    },
}

# Free learning resources: skill -> (title, url)
RESOURCES = {
    "SQL": ("W3Schools SQL", "https://www.w3schools.com/sql/"),
    "Excel": ("ExcelJet tutorials", "https://exceljet.net/"),
    "Python": ("Official Python Tutorial", "https://docs.python.org/3/tutorial/"),
    "Pandas": ("Kaggle Learn: Pandas", "https://www.kaggle.com/learn/pandas"),
    "Statistics": ("Khan Academy Statistics", "https://www.khanacademy.org/math/statistics-probability"),
    "Data Visualization": ("Kaggle Learn: Data Viz", "https://www.kaggle.com/learn/data-visualization"),
    "Power BI": ("Microsoft Learn: Power BI", "https://learn.microsoft.com/training/powerbi/"),
    "Java": ("dev.java Learn", "https://dev.java/learn/"),
    "Spring Boot": ("Spring Guides", "https://spring.io/guides"),
    "REST APIs": ("RESTfulAPI.net", "https://restfulapi.net/"),
    "Git": ("Pro Git Book", "https://git-scm.com/book"),
    "Data Structures": ("NeetCode Roadmap", "https://neetcode.io/roadmap"),
    "System Design": ("System Design Primer", "https://github.com/donnemartin/system-design-primer"),
    "Docker": ("Docker Get Started", "https://docs.docker.com/get-started/"),
    "Testing": ("JUnit 5 User Guide", "https://junit.org/junit5/docs/current/user-guide/"),
    "Machine Learning": ("Kaggle: Intro to ML", "https://www.kaggle.com/learn/intro-to-machine-learning"),
    "Deep Learning": ("fast.ai", "https://www.fast.ai/"),
    "PyTorch": ("PyTorch Tutorials", "https://pytorch.org/tutorials/"),
    "NumPy": ("NumPy Learn", "https://numpy.org/learn/"),
    "HTML": ("MDN Learn Web Dev", "https://developer.mozilla.org/docs/Learn"),
    "CSS": ("MDN Learn Web Dev", "https://developer.mozilla.org/docs/Learn"),
    "JavaScript": ("javascript.info", "https://javascript.info/"),
    "React": ("React Docs: Learn", "https://react.dev/learn"),
    "Node.js": ("Node.js Learn", "https://nodejs.org/en/learn"),
}

# Alternative spellings used when scanning a resume
ALIASES = {
    "JavaScript": ["js"], "Machine Learning": ["ml"], "REST APIs": ["rest", "restful", "rest api"],
    "Spring Boot": ["spring"], "Data Structures": ["dsa", "data structure"], "Node.js": ["node", "nodejs"],
    "Power BI": ["powerbi"], "Deep Learning": ["dl", "neural network"], "SQL": ["mysql", "postgresql"],
    "Data Visualization": ["tableau", "matplotlib"], "Testing": ["junit", "unit test"],
}

ROLES = {
    "Data Analyst": ["SQL", "Excel", "Python", "Pandas", "Statistics", "Data Visualization", "Power BI"],
    "Software Developer (Java)": ["Java", "Spring Boot", "SQL", "REST APIs", "Git", "Data Structures", "System Design", "Docker", "Testing"],
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "PyTorch", "NumPy", "Statistics", "SQL", "Git"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git", "REST APIs", "Node.js"],
}

INTERVIEW_QUESTIONS = {
    "Data Analyst": {
        "Fresher": ["What is the difference between INNER JOIN and LEFT JOIN?", "How do you handle missing values in a dataset?", "Explain mean vs median and when to use each.", "Walk me through a data project you did."],
        "Experienced": ["How would you design a dashboard for a sales team?", "How do you validate data quality in a pipeline?", "Explain A/B testing and p-values.", "Describe a time your analysis changed a decision."],
    },
    "Software Developer (Java)": {
        "Fresher": ["Explain OOP principles with examples.", "What is the difference between ArrayList and LinkedList?", "What is dependency injection in Spring Boot?", "Explain how a REST API works and name the HTTP methods."],
        "Experienced": ["How do you handle transactions and isolation levels in Spring?", "How would you scale a REST service to 10x traffic?", "Explain the JVM memory model and garbage collection.", "How do you design for fault tolerance?"],
    },
    "AI Engineer": {
        "Fresher": ["Explain overfitting and how to prevent it.", "What is the difference between supervised and unsupervised learning?", "What is gradient descent?", "Describe an ML project you built."],
        "Experienced": ["How do you monitor models in production?", "Explain the bias-variance trade-off.", "How would you deploy and version a model?", "How do you handle class imbalance?"],
    },
    "Web Developer": {
        "Fresher": ["What is the CSS box model?", "Explain var, let and const in JavaScript.", "What is the virtual DOM in React?", "How does the browser render a page?"],
        "Experienced": ["How do you optimise web performance?", "Explain state management trade-offs in React.", "How do you secure a web app against XSS/CSRF?", "Describe your approach to testing front-end code."],
    },
}
BEHAVIORAL = ["Tell me about yourself.", "Describe a challenge you faced and how you solved it.", "Why do you want this role?", "Tell me about a time you worked in a team."]

INTERESTS = ["Coding", "Maths", "Biology", "Design", "Business", "Research", "Teaching", "Problem Solving", "Writing", "Data"]
STAGES = ["After 12th", "After Graduation"]

CAREERS = [
    {"name": "B.Tech / BE in Computer Science", "stage": ["After 12th"], "interests": ["Coding", "Maths", "Problem Solving"], "min_score": 70, "skills": ["Python", "Java"],
     "desc": "Strong demand across software, AI and cloud.", "next": "Prepare for JEE Main / state CETs; learn a language like Python."},
    {"name": "MBBS / Life Sciences", "stage": ["After 12th"], "interests": ["Biology", "Research", "Teaching"], "min_score": 75, "skills": [],
     "desc": "Healthcare, medicine and biomedical research.", "next": "Prepare for NEET; strengthen Biology & Chemistry."},
    {"name": "Data Science & Analytics", "stage": ["After 12th", "After Graduation"], "interests": ["Data", "Maths", "Coding"], "min_score": 65, "skills": ["Python", "SQL", "Statistics"],
     "desc": "Turn data into decisions: analyst, BI and data science roles.", "next": "Learn SQL + Python, build 2-3 dashboard projects."},
    {"name": "UI/UX & Product Design", "stage": ["After 12th", "After Graduation"], "interests": ["Design", "Problem Solving", "Writing"], "min_score": 55, "skills": ["HTML", "CSS"],
     "desc": "Design products people love using.", "next": "Learn Figma, build a case-study portfolio."},
    {"name": "Business & Management (BBA/MBA)", "stage": ["After 12th", "After Graduation"], "interests": ["Business", "Writing", "Problem Solving"], "min_score": 55, "skills": ["Excel"],
     "desc": "Management, consulting, marketing and entrepreneurship.", "next": "Prepare for CAT/CUET; take internships."},
    {"name": "AI / ML Engineer", "stage": ["After Graduation"], "interests": ["Coding", "Maths", "Data", "Research"], "min_score": 70, "skills": ["Python", "Machine Learning", "PyTorch"],
     "desc": "Build and deploy intelligent systems.", "next": "Finish Kaggle ML courses, ship an end-to-end project."},
    {"name": "Backend Developer", "stage": ["After Graduation"], "interests": ["Coding", "Problem Solving"], "min_score": 60, "skills": ["Java", "Spring Boot", "SQL", "REST APIs"],
     "desc": "APIs, databases and scalable services.", "next": "Build REST projects, learn Docker and system design basics."},
    {"name": "Teaching & Academia", "stage": ["After Graduation"], "interests": ["Teaching", "Research", "Writing"], "min_score": 60, "skills": [],
     "desc": "Higher studies, research and education roles.", "next": "Prepare for NET/GATE or masters; assist in research."},
]
