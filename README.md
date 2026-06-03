# SafeRoute AI 🚦🛡️

SafeRoute AI is an AI-powered women safety and smart route prediction platform that analyzes crime-prone areas and predicts safer travel routes using Machine Learning, Flask APIs, MongoDB, and Mapbox integration.

The platform combines crime analysis, weather monitoring, and intelligent route prediction to help users identify safer travel paths in urban environments. The system leverages machine learning models trained on crime datasets to generate route safety scores and classify routes into safety categories such as Unsafe, Moderate, and Very Safe.

---

# 📌 Problem Statement

The project aims to build an AI-powered safety platform capable of analyzing crime datasets and generating intelligent route safety recommendations for users.

The system is designed as a modular AI platform instead of a simple frontend-backend application. It demonstrates:

- Modular API architecture
- Machine learning pipelines
- Reusable processing logic
- Route safety prediction workflows
- Interactive map-based visualization

The platform automatically:

- Analyzes crime-related datasets
- Predicts route safety scores
- Categorizes routes by safety level
- Displays intelligent route recommendations
- Integrates weather-aware navigation insights

---

# 🚀 Solution Overview

SafeRoute AI is a modular AI-based safety platform developed using Flask, MongoDB, Machine Learning, and Mapbox.

The system predicts route safety by analyzing crime statistics and generating safety scores using trained regression models. Instead of using a single monolithic script, the platform is divided into multiple independent modules responsible for authentication, route prediction, weather analysis, feedback handling, and machine learning inference.

This architecture makes the system:

- Scalable
- Reusable
- Maintainable
- Easy to extend for future improvements

---

# ✨ Features

- AI-powered route safety prediction
- Crime data analysis
- Machine learning safety scoring
- Weather-aware route recommendations
- Interactive Mapbox visualization
- JWT-based authentication system
- User feedback collection module
- Flask REST API integration
- MongoDB database integration
- Multi-city dataset support

---

# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript
- Mapbox GL JS

## Backend
- Flask
- Flask-CORS
- JWT Authentication
- MongoDB

## Machine Learning
- Scikit-learn
- Decision Tree Regressor
- Random Forest Regressor
- Pandas
- NumPy

---

# 📂 Project Structure

```bash
SAFEROUTE-AI/
│
├── backend/
│   ├── auth/
│   ├── data/
│   ├── ml/
│   ├── models/
│   ├── routes/
│   ├── app.py
│   ├── config.py
│   ├── db.py
│   └── requirements.txt
│
├── frontend/
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── app.js
│       └── style.css
│
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ How the System Works

## Authentication Module
Handles secure user registration and login using JWT authentication.

## Weather Module
Fetches real-time weather information for selected routes and locations.

## Safety Prediction Module
Uses trained machine learning models to calculate safety scores for routes.

## Crime Dataset Loader
Loads Bengaluru and Delhi crime datasets into MongoDB for analysis.

## Machine Learning Pipeline
Processes crime datasets, computes safety metrics, trains regression models, and stores the best-performing model.

## Route Analysis Module
Generates safety-aware route predictions based on crime statistics and model inference.

## Frontend Interface
Displays maps, route details, weather information, and safety categories through an interactive user interface.

## Feedback Module
Collects user feedback to improve future route safety recommendations.

---

# System Architecture

```text
User Interface (Frontend)
        │
        ▼
Flask Backend APIs
        │
 ┌───────────────┬───────────────┬───────────────┐
 ▼               ▼               ▼
Auth Module   Weather API   Route Safety Module
                                    │
                                    ▼
                          ML Prediction Engine
                                    │
                                    ▼
                             MongoDB Dataset
                                    │
                                    ▼
                         Safety Score Prediction
                                    │
                                    ▼
                    Safe / Moderate / Unsafe Route
```

---

# 🤖 Machine Learning Pipeline

The platform trains regression models using crime-related datasets to generate route safety scores.

## Models Used
- Decision Tree Regressor
- Random Forest Regressor

## Safety Categories
- Unsafe
- Moderate
- Very Safe

---

# Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/SAFEROUTE-AI.git
cd SAFEROUTE-AI
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows
```bash
.venv\Scripts\activate
```

#### Linux / Mac
```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file inside the `backend/` folder.

```env
MONGO_URI=your_mongodb_connection
JWT_SECRET_KEY=your_secure_secret_key
MAPBOX_TOKEN=your_mapbox_public_token
WEATHER_API_KEY=your_weather_api_key
```

---

# 🧠 Train ML Model

```bash
cd backend
python -m ml.train_model
```

---

# ▶️ Run Application

```bash
python app.py
```

Server runs at:

```bash
http://127.0.0.1:5000
```

---

#  Future Improvements

- Real-time crime monitoring
- Deep learning route optimization
- Mobile application integration
- Emergency SOS functionality
- Live traffic-aware navigation
- CCTV-based safety analytics
- Real-time crowd-density analysis

---

#  Author

**Rakshita G**  
AIML Engineering Student  

# Project Highlights

- End-to-end AI-powered safety platform
- Real-world crime data analysis
- Modular backend architecture
- Machine learning integration
- Interactive route visualization
- Scalable and recruiter-friendly project design
