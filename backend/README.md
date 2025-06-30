# NutmegAI Backend

AI-powered legal assistant backend for Grenadians, supporting Grenadian Creole language understanding.

## Features

- **Grenadian Creole Support**: Natural language processing for Grenadian Creole and English
- **Legal Document Assistance**: Comprehensive knowledge base for all major legal documents
- **AI Chat Interface**: OpenAI-powered conversational AI
- **RAG System**: Retrieval-Augmented Generation for accurate document information
- **Session Management**: Persistent chat sessions with conversation history
- **Translation Services**: Bidirectional translation between English and Creole

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **OpenAI GPT-4**: Advanced language model for natural conversations
- **SQLAlchemy**: Database ORM for data persistence
- **PostgreSQL/SQLite**: Database storage
- **Pydantic**: Data validation and serialization
- **Python 3.8+**: Core programming language

## Setup Instructions

### 1. Environment Setup

Create a virtual environment and install dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file in the backend directory:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4

# Database Configuration
DATABASE_URL=sqlite:///./nutmegai.db
# For PostgreSQL: postgresql://user:password@localhost/nutmegai

# Security
SECRET_KEY=your_secret_key_here

# CORS Origins (comma-separated)
BACKEND_CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### 3. Database Initialization

Initialize the database with sample data:

```bash
cd database
python init_db.py
```

### 4. Run the Application

Start the FastAPI server:

```bash
# Development mode
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

### Base URL
```
http://localhost:8000/api/v1
```

### Endpoints

#### Chat Endpoints

**POST** `/chatbot/chat`
- Send a message to the AI chatbot
- Supports both English and Grenadian Creole
- Returns AI response with confidence score and suggested actions

**Request Body:**
```json
{
  "message": "How to get birth certificate?",
  "session_id": "optional-session-id",
  "language": "auto"
}
```

**Response:**
```json
{
  "response": "To get a birth certificate in Grenada...",
  "session_id": "generated-session-id",
  "language": "en",
  "confidence": 0.95,
  "suggested_actions": [
    "Get birth certificate requirements",
    "Get contact information"
  ]
}
```

#### Document Endpoints

**GET** `/chatbot/documents`
- Get list of available document types

**POST** `/chatbot/documents/{document_type}`
- Get specific information about a legal document

**Request Body:**
```json
{
  "document_type": "birth_certificate",
  "query": "What documents do I need?",
  "language": "en"
}
```

**Response:**
```json
{
  "information": "Birth certificates are official documents...",
  "requirements": [
    "Parent's identification",
    "Hospital birth record"
  ],
  "process_steps": [
    "Visit the Civil Registry Office",
    "Submit required documents"
  ],
  "contact_info": {
    "office": "Civil Registry Office",
    "address": "Ministerial Complex, St. George's",
    "phone": "+1 (473) 440-2251"
  },
  "estimated_time": "3-5 business days",
  "fees": "EC$25.00"
}
```

#### Translation Endpoints

**POST** `/chatbot/translate`
- Translate between English and Grenadian Creole

**Request:**
```
POST /chatbot/translate?message=good morning&target_language=en
```

**Response:**
```json
{
  "original": "good mornin",
  "translated": "good morning",
  "target_language": "en"
}
```

#### Language Support

**GET** `/chatbot/languages`
- Get supported languages

**Response:**
```json
{
  "supported_languages": ["en", "en-GD", "en-US"],
  "primary_language": "en-GD",
  "description": "Grenadian Creole and English support"
}
```

## Supported Document Types

- Birth Certificates
- Death Certificates
- Marriage Certificates
- Divorce Decrees
- Property Deeds
- Business Registration
- Passport Applications
- National ID Cards
- Voter Registration
- Tax Documents

## Grenadian Creole Support

The system recognizes and responds to common Grenadian Creole patterns:

### Greetings
- "good mornin" (good morning)
- "how yuh doin" (how are you)
- "wha happen" (what's happening)

### Common Words
- "yuh" (you)
- "nah" (no)
- "wah" (what)
- "deh" (there)
- "gyal" (girl)
- "bwoy" (boy)
- "tings" (things)
- "nuff" (enough)
- "liming" (hanging out)
- "irie" (good)

### Legal Terms
- "birth paper" (birth certificate)
- "death paper" (death certificate)
- "marriage paper" (marriage certificate)
- "property paper" (property deed)
- "business paper" (business registration)
- "tax paper" (tax documents)

## Development

### Project Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   │   ├── __init__.py
│   │   └── chatbot.py       # Chat API routes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm.py           # OpenAI integration
│   │   └── rag.py           # Document retrieval
│   └── utils/
│       ├── __init__.py
│       └── helpers.py       # Utility functions
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

### Adding New Features

1. **New Document Type**: Add to `config.py` LEGAL_CATEGORIES and update RAG service
2. **New Creole Patterns**: Add to `utils/helpers.py` CREOLE_PATTERNS
3. **New API Endpoint**: Create new route in `routes/` directory

### Testing

Run tests (when implemented):
```bash
pytest
```

### Code Quality

Format code with black:
```bash
black .
```

## Deployment

### Docker Deployment

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables for Production

```env
OPENAI_API_KEY=your_production_openai_key
DATABASE_URL=postgresql://user:password@host/database
SECRET_KEY=your_secure_secret_key
BACKEND_CORS_ORIGINS=https://yourdomain.com
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is proprietary software for NutmegAI.

## Support

For support and questions, contact the development team.
