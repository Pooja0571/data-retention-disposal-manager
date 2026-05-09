# Data Retention & Disposal Manager (AI Service)

##  Overview

This AI service is a Flask-based backend that generates data retention and disposal policies based on record type, retention period, and risk level.
It provides structured outputs for descriptions, recommendations, and reports to support data lifecycle management.

---

##  Features

* Generate data retention descriptions
* Provide actionable recommendations
* Generate structured summary reports
* Input validation and error handling
* Security headers (XSS, CSP, clickjacking protection)
* Modular and scalable API architecture

---

## Tech Stack

* Python (Flask)
* REST APIs
* Flask-Caching
* Postman (API testing)

---

## Project Structure

```
ai-service/
├── app.py
├── extensions.py
├── routes/
│   ├── describe.py
│   ├── recommend.py
│   └── report.py
├── prompts/
├── services/
└── requirements.txt
```

---

##  How to Run

```bash
cd ai-service
pip install -r requirements.txt
python app.py
```

Server will run at:

```
http://localhost:5000
```

---

##  API Endpoints

### 1. Health Check

```
GET /health
```

---

### 2. Describe

```
POST /describe
```

**Request Body:**

```json
{
  "recordType": "Employee Data",
  "retentionPeriod": "5 years",
  "riskLevel": "High"
}
```

---

### 3. Recommend

```
POST /recommend
```

---

### 4. Generate Report

```
POST /generate-report
```

---

## Security

* X-Frame-Options (Clickjacking protection)
* X-Content-Type-Options (MIME protection)
* X-XSS-Protection (XSS prevention)
* Content Security Policy (CSP)

---

##  Performance

* Optimized API responses
* Efficient validation and error handling
* Caching strategy implemented (for performance understanding)

---

##  My Contribution

* Developed Flask-based AI backend service
* Implemented `/describe`, `/recommend`, and `/generate-report` APIs
* Added input validation and structured JSON responses
* Implemented global security headers using middleware
* Resolved circular import issue using extensions module
* Improved performance and handled caching-related issues
* Tested APIs using Postman

---
