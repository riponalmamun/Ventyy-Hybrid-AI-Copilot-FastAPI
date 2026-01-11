
# Ventyy – Hybrid AI Copilot

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)

A production-ready FastAPI-based intelligent copilot system designed for hybrid AI-powered workflows.

## 📋 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Features](#-features)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Development](#-development)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

Ventyy is a modern, scalable API platform built with FastAPI that provides AI-powered assistance capabilities. The system follows industry best practices for API design, modularity, and maintainability, making it ideal for enterprise-grade applications.

## 📁 Project Structure

```
VENTYY/
├── app/
│   ├── models/
│   │   ├── chat_models.py          # Chat data models
│   │   ├── policy_models.py        # Policy-related schemas
│   │   ├── ticket_models.py        # Ticket management models
│   │   └── user_models.py          # User entity definitions
│   │
│   ├── routers/
│   │   └── resolution.py           # Resolution API endpoints
│   │
│   └── services/
│       ├── ai_copilot.py           # Core AI logic
│       ├── db_service.py           # Database operations
│       ├── config.py               # Application configuration
│       ├── dependencies.py         # Dependency injection
│       └── main.py                 # Application entry point
│
├── data/
│   └── dummy_db.json               # Mock database (dev only)
│
├── .env                            # Environment variables
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## ✨ Features

- **🚀 FastAPI Framework**: High-performance async API with automatic validation
- **🧠 AI Integration**: Modular AI service layer with LLM support
- **📊 Data Models**: Strongly-typed Pydantic models for all entities
- **🔌 Modular Architecture**: Clean separation of concerns (routers, services, models)
- **📚 Auto-generated Docs**: Interactive OpenAPI/Swagger documentation
- **🔧 Configuration Management**: Environment-based configuration
- **🗄️ Database Abstraction**: Service layer for data persistence
- **🧪 Development Ready**: Mock data for rapid local development

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (venv, virtualenv, or conda)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/ventyy.git
   cd ventyy
   ```

2. **Create and activate virtual environment**
   ```bash
   # Using venv
   python -m venv venv
   
   # Activate on Linux/macOS
   source venv/bin/activate
   
   # Activate on Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## ⚙️ Configuration

Create a `.env` file in the root directory:

```env
# Application
APP_NAME="Ventyy Hybrid AI Copilot"
APP_VERSION="1.0.0"
DEBUG=True

# API
API_HOST=0.0.0.0
API_PORT=8000

# Database (for production)
DATABASE_URL=postgresql://user:password@localhost:5432/ventyy

# AI Configuration
AI_PROVIDER=openai
AI_MODEL=gpt-4
AI_API_KEY=your_api_key_here

# Logging
LOG_LEVEL=INFO
```

## 💻 Usage

### Running the Application

```bash
# Development mode with auto-reload
uvicorn app.services.main:app --reload

# Production mode
uvicorn app.services.main:app --host 0.0.0.0 --port 8000
```

### API Example

```python
from fastapi import FastAPI
from app.routers import resolution

app = FastAPI(
    title="Ventyy Hybrid AI Copilot",
    description="AI-powered copilot for intelligent workflows",
    version="1.0.0"
)

# Register routers
app.include_router(
    resolution.router,
    prefix="/api/v1",
    tags=["resolution"]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## 📚 API Documentation

Once the server is running, access the interactive documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

### Example Endpoints

```
GET     /api/v1/resolution              # List all resolutions
POST    /api/v1/resolution              # Create new resolution
GET     /api/v1/resolution/{id}         # Get specific resolution
PUT     /api/v1/resolution/{id}         # Update resolution
DELETE  /api/v1/resolution/{id}         # Delete resolution
```

## 🛠️ Development

### Code Organization Principles

1. **Routers** (`app/routers/`)
   - Define API endpoints and request/response handling
   - Keep thin – delegate business logic to services
   - Use dependency injection for shared resources

2. **Services** (`app/services/`)
   - Contain all business logic
   - `ai_copilot.py`: Isolated AI/LLM functionality
   - `db_service.py`: Database operations and queries
   - `config.py`: Application-wide configuration

3. **Models** (`app/models/`)
   - Pydantic models for validation and serialization
   - Separate models for different domains (chat, tickets, users, policies)

4. **Data** (`data/`)
   - `dummy_db.json`: Mock data for local development
   - **⚠️ Not for production use** – replace with proper database

### Best Practices

```python
# ✅ Good: Service layer handles logic
@router.post("/resolution")
async def create_resolution(data: ResolutionCreate):
    return await resolution_service.create(data)

# ❌ Bad: Business logic in router
@router.post("/resolution")
async def create_resolution(data: ResolutionCreate):
    # Don't do this - move to service layer
    result = complex_business_logic(data)
    ai_response = call_ai_model(result)
    return save_to_db(ai_response)
```

### Testing

```bash
# Run tests (when implemented)
pytest

# With coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_resolution.py
```

### Code Style

```bash
# Format code
black app/

# Lint
flake8 app/

# Type checking
mypy app/
```

## 🗺️ Roadmap

### Phase 1: Core Infrastructure
- [x] FastAPI application setup
- [x] Modular architecture with routers/services
- [x] Pydantic models for type safety
- [ ] **Authentication & Authorization** (JWT/OAuth2)
- [ ] **Database Integration** (PostgreSQL/MongoDB)

### Phase 2: AI Enhancement
- [ ] **LLM Provider Abstraction** (OpenAI, Anthropic, local models)
- [ ] **Streaming Responses** for real-time AI interactions
- [ ] **Context Management** for conversation history
- [ ] **Prompt Engineering** framework

### Phase 3: Production Readiness
- [ ] **Logging & Observability** (structured logging, metrics)
- [ ] **Error Handling** middleware
- [ ] **Rate Limiting** and request throttling
- [ ] **Caching Layer** (Redis)

### Phase 4: Quality & Deployment
- [ ] **Unit Tests** (pytest)
- [ ] **Integration Tests**
- [ ] **Docker Containerization**
- [ ] **CI/CD Pipeline** (GitHub Actions)
- [ ] **API Versioning** strategy
- [ ] **Performance Optimization**

### Phase 5: Advanced Features
- [ ] **WebSocket Support** for real-time updates
- [ ] **Background Tasks** (Celery/RQ)
- [ ] **Multi-tenancy** support
- [ ] **Admin Dashboard**

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and test
pytest

# Format code
black app/

# Commit with descriptive message
git commit -m "feat: add new resolution filtering endpoint"

# Push and create PR
git push origin feature/new-feature
```

## 📄 License

This project is proprietary and confidential.

**Copyright © 2026 Md Ripon Al Mamun. All rights reserved.**

For licensing inquiries, please contact: [riponalmamunrasel@gmail.com](riponalmamunrasel@gmail.com)

---

## 👥 Authors

**Md Ripon Al Mamun**

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Powered by AI-first principles
- Designed for scalability and maintainability

## 📞 Support

For support, email riponalmamunrasel@gmail.com or open an issue in the repository.

---

**⭐ If you find this project useful, please consider giving it a star!**
