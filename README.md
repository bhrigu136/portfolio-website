# Portfolio Website — Tamanna Bhrigunath

🌐 **Live Portfolio:** https://portfolio-website-sroy.onrender.com  
💻 **GitHub:** https://github.com/bhrigu136  

---

## 📌 Overview

This repository contains my **personal portfolio website** built using **Flask**.  
It showcases my projects, experience, and skills in **Data Science, Machine Learning, and Python development**.

The website is fully deployed on the cloud and intended for recruiters and reviewers to quickly evaluate my work.

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (Jinja2 Templates)
- **Deployment:** Render
- **Production Server:** Gunicorn
- **Version Control:** Git & GitHub

---

## ✨ Features

- Clean and responsive user interface
- Projects section with GitHub and Live Demo links
- Experience section highlighting internships and applied projects
- Downloadable resume
- Cloud-deployed and publicly accessible

---

## 📂 Project Structure

```

portfolio-website/
│
├── fspp/
│   ├── static/
│   │   ├── style.css
│   │   ├── img_.jpg
│   │   └── Tamanna_Bhrigunath_Resume.pdf
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── projects.html
│   │   ├── experience.html
│   │   └── _project_list.html
│   ├── routes.py
│   └── **init**.py
│
├── fspp_run.py
├── requirements.txt
├── nginx/
│   └── nginx.conf
└── README.md

````

---

## 🧪 Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/bhrigu136/portfolio-website.git
cd portfolio-website
````

### 2️⃣ (Optional) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python fspp_run.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

The application is deployed on **Render** using **Gunicorn**.

Start command used:

```bash
gunicorn fspp:app --bind 0.0.0.0:$PORT
```

---

## 👩‍💻 About Me

I am a **Computer Science undergraduate (B.Tech, 2026)** with hands-on experience in:

* Machine Learning projects
* Data preprocessing and model evaluation
* Flask-based backend development
* Cloud deployment

I am actively seeking **internship and entry-level roles** in:

* Data Science
* Machine Learning
* Python / Backend Development

---

## 📬 Contact

* **Email:** [bhrigunathtamanna@gmail.com](mailto:bhrigunathtamanna@gmail.com)
* **LinkedIn:** [https://www.linkedin.com/in/tamanna-bhrigunath-578b43190](https://www.linkedin.com/in/tamanna-bhrigunath-578b43190)
* **GitHub:** [https://github.com/bhrigu136](https://github.com/bhrigu136)

---

⭐ If you find this project useful, feel free to star the repository.

