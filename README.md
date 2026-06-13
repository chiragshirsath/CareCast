<p align="center">
  <h1 align="center">🩺 CareCast</h1>
  <p align="center">
    <strong>AI-Powered Health Prediction Platform</strong>
  </p>
  <p align="center">
    <a href="#features">Features</a> •
    <a href="#tech-stack">Tech Stack</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#getting-started">Getting Started</a> •
    <a href="#ml-models">ML Models</a>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
    <img src="https://img.shields.io/badge/scikit--learn-1.4-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
    <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge" alt="License">
  </p>
</p>

---

## 📋 Overview

**CareCast** is a full-stack Django web application that leverages machine learning models to provide online health predictions for **Mental Disorders**, **PCOS (Polycystic Ovary Syndrome)**, and **Obesity**. The platform connects patients with healthcare professionals through an integrated appointment booking system and generates downloadable health reports.

---

## ✨ Features

### 🔬 For Patients
| Feature | Description |
|---------|-------------|
| **🧠 Health Predictions** | Get AI-powered predictions for mental disorders, PCOS, and obesity using ML models trained on Kaggle datasets |
| **📄 Health Reports** | Download detailed health reports with diagnosis, symptoms, and expert advice |
| **📅 Appointment Booking** | Browse registered doctors and schedule appointments directly through the platform |
| **📊 Test History** | Track all past predictions and results in one place |
| **👤 User Profile** | Manage personal health information (height, weight, BMI, etc.) |

### 👨‍⚕️ For Doctors
| Feature | Description |
|---------|-------------|
| **📋 Appointment Management** | View, accept, and manage patient appointment requests |
| **🏥 Professional Profile** | Showcase specialization, education, experience, and expertise |
| **📅 Scheduled Appointments** | Track all confirmed patient appointments |

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML5, CSS3, Bootstrap 5.3, JavaScript |
| **Backend** | Python 3.10+, Django 5.0.2 |
| **Database** | SQLite3 |
| **ML/AI** | scikit-learn 1.4, NumPy, Pandas, Joblib |
| **Deployment** | Gunicorn, WhiteNoise |

---

## 🏗️ Architecture

```
CareCast/
├── predictHealth/              # Django project configuration
│   ├── settings.py             # Project settings & middleware
│   ├── urls.py                 # Root URL routing
│   ├── wsgi.py                 # WSGI entry point
│   └── asgi.py                 # ASGI entry point
│
├── home/                       # Main application
│   ├── models.py               # Database models (User, Doctor, Appointments, etc.)
│   ├── views.py                # Business logic & ML prediction handlers
│   ├── forms.py                # Django form definitions
│   ├── urls.py                 # App-level URL patterns (22 routes)
│   └── migrations/             # Database migrations
│
├── templates/                  # HTML templates (22 files)
│   ├── base.html               # Public pages base template
│   ├── login_base.html         # Authenticated user base template
│   ├── doctor_base.html        # Doctor panel base template
│   └── ...                     # Feature-specific templates
│
├── static/
│   ├── style.css               # Custom CSS design system
│   ├── models/                 # Pre-trained ML model files (.pkl)
│   ├── encoders/               # Feature & label encoders (.pkl)
│   └── *.csv                   # Training datasets from Kaggle
│
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chiragshirsath/CareCast.git
   cd CareCast
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   # venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** *(optional, for admin panel)*
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## 🤖 ML Models

### Model Details

| Model | Algorithm | Dataset | Classes | Accuracy |
|-------|----------|---------|---------|----------|
| **Mental Disorder** | Classification (scikit-learn) | [Mental Disorder Classification](https://www.kaggle.com/datasets/cid007/mental-disorder-classification) | Bipolar Type-1, Bipolar Type-2, Depression, Normal | ~85% |
| **PCOS** | Classification (scikit-learn) | [PCOS 2023 Dataset](https://www.kaggle.com/datasets/sahilkoli04/pcos2023) | Positive, Negative | ~90% |
| **Obesity** | Classification (scikit-learn) | [Obesity Prediction](https://www.kaggle.com/datasets/mrsimple07/obesity-prediction) | Normal, Overweight, Obese, Underweight | ~88% |

### Prediction Workflow

```
User Input → Form Validation → Feature Encoding → ML Model Prediction → Result Decoding → Report Generation
```

1. User fills out a health assessment form
2. Input data is validated and preprocessed
3. Features are encoded using pre-trained encoders
4. The scikit-learn model generates a prediction
5. Results are decoded and stored in the database
6. A detailed report with expert advice is generated

---

## 📄 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/chiragshirsath">Chirag Shirsath</a>
</p>
