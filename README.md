# NutmegAI - Grenadian Legal Assistant

An AI-powered chatbot website that helps Grenadians with legal registry documents and government services, featuring native Grenadian Creole language support.

## 🌟 Features

### 🤖 AI-Powered Legal Assistant
- **OpenAI GPT-4 Integration**: Advanced conversational AI for natural interactions
- **Grenadian Creole Support**: Native language understanding and response generation
- **Document-Specific Guidance**: Comprehensive help for all major legal documents
- **Real-time Chat Interface**: Instant responses with conversation history

### 🇬🇩 Grenadian Cultural Integration
- **Creole Language Detection**: Automatic recognition of Grenadian Creole patterns
- **Local Terminology**: Understanding of "birth paper", "marriage paper", etc.
- **Cultural Context**: Responses tailored to Grenadian customs and procedures
- **Government Office Knowledge**: Accurate information about local offices and processes

### 📋 Legal Document Support
- **Birth Certificates**: Registration, requirements, and process guidance
- **Death Certificates**: Application procedures and documentation
- **Marriage Certificates**: License applications and ceremony requirements
- **Divorce Decrees**: Court procedures and legal requirements
- **Property Deeds**: Land registration and transfer processes
- **Business Registration**: Company formation and licensing
- **Passport Applications**: Travel document procedures
- **National ID Cards**: Identification document applications
- **Voter Registration**: Electoral process assistance
- **Tax Documents**: Revenue and compliance guidance

### 🎨 Modern Web Interface
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Grenadian Branding**: Beautiful orange and blue color scheme
- **Intuitive Navigation**: Easy-to-use chat interface
- **Quick Actions**: Pre-defined buttons for common queries
- **Language Toggle**: Switch between English and Creole modes

## 🏗️ Architecture

### Backend (FastAPI + Python)
```
backend/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── routes/
│   │   └── chatbot.py       # API endpoints for chat and documents
│   ├── services/
│   │   ├── llm.py           # OpenAI integration and AI logic
│   │   └── rag.py           # Document retrieval and knowledge base
│   └── utils/
│       └── helpers.py       # Language detection and translation
├── database/
│   ├── models.py            # SQLAlchemy database models
│   └── init_db.py           # Database initialization script
└── config.py                # Configuration and settings
```

### Frontend (React + Vite)
```
frontend/
├── source/
│   ├── components/
│   │   ├── ChatWindow.jsx   # Main chat interface
│   │   └── Navbar.jsx       # Navigation component
│   ├── pages/
│   │   └── Home.jsx         # Landing page
│   ├── App.jsx              # Main app component
│   └── index.js             # React entry point
├── package.json             # Dependencies and scripts
└── tailwind.config.js       # Styling configuration
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- OpenAI API key

### 1. Clone the Repository
```bash
git clone <repository-url>
cd NutmegAI
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
# Edit .env with your OpenAI API key

# Initialize database
cd database
python init_db.py
cd ..

# Start backend server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 4. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## �� Configuration

### Environment Variables

**Backend (.env)**
```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4
DATABASE_URL=sqlite:///./nutmegai.db
SECRET_KEY=your_secret_key_here
BACKEND_CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

**Frontend (.env)**
```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
VITE_APP_NAME=NutmegAI
VITE_APP_DESCRIPTION=Grenadian Legal Assistant
```

## 💬 Grenadian Creole Support

### Language Detection
The system automatically detects and responds to Grenadian Creole patterns:

**Greetings:**
- "good mornin" (good morning)
- "how yuh doin" (how are you)
- "wha happen" (what's happening)

**Common Words:**
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

**Legal Terms:**
- "birth paper" (birth certificate)
- "death paper" (death certificate)
- "marriage paper" (marriage certificate)
- "property paper" (property deed)
- "business paper" (business registration)
- "tax paper" (tax documents)

### Example Conversations

**User (Creole):** "Good mornin, I need help with birth paper"
**AI Response:** "Good mornin! I can help you with birth certificate. You'll need to visit the Civil Registry Office in St. George's..."

**User (English):** "How much does a passport cost?"
**AI Response:** "A Grenadian passport costs EC$150.00 and takes 10-15 business days to process..."

## 📚 API Documentation

### Chat Endpoints

**POST** `/api/v1/chatbot/chat`
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

### Document Endpoints

**GET** `/api/v1/chatbot/documents` - List available document types
**POST** `/api/v1/chatbot/documents/{document_type}` - Get specific document information

## 🎯 Use Cases

### For Grenadian Citizens
- **New Parents**: Get birth certificate information and requirements
- **Getting Married**: Understand marriage license and certificate processes
- **Starting Business**: Learn about business registration and licensing
- **Property Transactions**: Navigate property deed and land registration
- **Travel Planning**: Apply for passports and travel documents

### For Legal Professionals
- **Client Assistance**: Provide accurate information to clients
- **Process Guidance**: Streamline document preparation
- **Office Efficiency**: Reduce repetitive inquiries
- **24/7 Availability**: Extend service hours beyond office time

### For Government Offices
- **Reduced Workload**: Handle common inquiries automatically
- **Consistent Information**: Provide standardized responses
- **Language Accessibility**: Serve Creole-speaking citizens
- **Process Transparency**: Make procedures clear and accessible

## 🔒 Security & Privacy

- **Data Encryption**: All communications encrypted in transit
- **Session Management**: Secure session handling with unique IDs
- **Input Sanitization**: Protection against injection attacks
- **Privacy Compliance**: No personal data stored permanently
- **API Rate Limiting**: Protection against abuse

## 🚀 Deployment

### Backend Deployment
```bash
# Production build
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend Deployment
```bash
# Build for production
npm run build

# Deploy to Vercel/Netlify
npm install -g vercel
vercel
```

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up -d
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is proprietary software for NutmegAI. All rights reserved.

## 🆘 Support

- **Documentation**: Check the README files in backend/ and frontend/ directories
- **Issues**: Report bugs and feature requests through the issue tracker
- **Contact**: Reach out to the development team for support

## 🙏 Acknowledgments

- **OpenAI**: For providing the GPT-4 language model
- **Grenadian Community**: For cultural insights and language patterns
- **FastAPI & React**: For excellent development frameworks
- **Tailwind CSS**: For beautiful, responsive styling

---

**Built with ❤️ for the Grenadian community**
