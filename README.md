# 🚀 Propertyloop Interview Boilerplate

A minimal FastAPI boilerplate designed for **technical interviews**.  
This template gives candidates a clean starting point so they can focus on solving API problems instead of setting up a project.

---

## 📦 Features
- FastAPI app with `/health` endpoint  
- Example CRUD routes (`/api/v1/example`)  
- Pydantic models for validation  
- Ready-to-run with `uvicorn`  
- Clean structure for quick extensibility  

## ⚡ Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/fastapi-interview-boilerplate.git
cd fastapi-interview-boilerplate
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the server
bash
Copy code
uvicorn app.main:app --reload
🌍 API Endpoints
Health Check → GET /health

List Items → GET /api/v1/example

Create Item → POST /api/v1/example
