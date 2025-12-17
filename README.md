# 🚀 Portfolio Website — Tamanna Bhrigunath

Live Portfolio: 👉 **[https://portfolio-website-sroy.onrender.com](https://portfolio-website-sroy.onrender.com)**
GitHub: 👉 **[https://github.com/bhrigu136](https://github.com/bhrigu136)**

---

## 📌 Overview

This is my **personal portfolio website** built using **Flask**, showcasing my projects, experience, and skills in **Data Science, Machine Learning, and Python development**.

The website is fully deployed on the cloud and designed to provide recruiters and reviewers a clear view of my work, technical abilities, and practical experience.

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS (Jinja2 templating)
* **Deployment:** Render
* **Version Control:** Git & GitHub
* **Server:** Gunicorn (production WSGI server)

---

## ✨ Features

* Clean and responsive UI
* Projects section with GitHub and Live Demo links
* Experience timeline highlighting internships and projects
* Downloadable resume
* Cloud-deployed and publicly accessible

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
│   └── __init__.py
│
├── fspp_run.py
├── requirements.txt
├── nginx/
│   └── nginx.conf
└── README.md
```

---

## 🧪 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/bhrigu136/portfolio-website.git
cd portfolio-website
```

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python fspp_run.py
```

Open browser and visit:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

The application is deployed on **Render** using **Gunicorn** with the following start command:

```bash
gunicorn fspp:app --bind 0.0.0.0:$PORT
```

Render automatically handles environment variables and port allocation.

---

## 📄 Resume

The resume is available for download directly from the portfolio website.

---

## 👩‍💻 About Me

I am a **Computer Science undergraduate (B.Tech, 2026)** with hands-on experience in:

* Machine Learning projects
* Data preprocessing & model evaluation
* Flask-based backend development
* Cloud deployment

I am actively seeking **internship and entry-level opportunities** in:

* Data Science
* Machine Learning
* Python / Backend Development

---

## 📬 Contact

* **Email:** [bhrigunathtamanna@gmail.com](mailto:bhrigunathtamanna@gmail.com)
* **LinkedIn:** [https://www.linkedin.com/in/tamanna-bhrigunath-578b43190](https://www.linkedin.com/in/tamanna-bhrigunath-578b43190)
* **GitHub:** [https://github.com/bhrigu136](https://github.com/bhrigu136)

---

## ⭐ Acknowledgement

This project reflects my practical learning journey in building, deploying, and maintaining a real-world web application.
