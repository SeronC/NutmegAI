# API keys, environment config
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "NutmegAI - Grenadian Legal Assistant"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./nutmegai.db")
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]
    
    # Grenadian Creole Settings
    CREOLE_LANGUAGE_CODE: str = "en-GD"
    SUPPORTED_LANGUAGES: list = ["en", "en-GD", "en-US"]
    
    # Legal Document Categories
    LEGAL_CATEGORIES: list = [
        "birth_certificate",
        "death_certificate", 
        "marriage_certificate",
        "divorce_decree",
        "property_deed",
        "business_registration",
        "passport_application",
        "national_id",
        "voter_registration",
        "tax_documents"
    ]

settings = Settings()