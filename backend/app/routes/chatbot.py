# API routes for chatbot
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import sys
import os

# Add parent directory to path to import services
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from services.llm import LLMService
from services.rag import RAGService
from utils.helpers import detect_language, translate_creole
from config import settings

router = APIRouter(prefix="/chatbot", tags=["chatbot"])

# Initialize services
llm_service = LLMService()
rag_service = RAGService()

class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = None
    language: Optional[str] = "en"

class ChatResponse(BaseModel):
    response: str
    session_id: str
    language: str
    confidence: float
    suggested_actions: List[str]

class DocumentRequest(BaseModel):
    document_type: str
    query: str
    language: str = "en"

class DocumentResponse(BaseModel):
    information: str
    requirements: List[str]
    process_steps: List[str]
    contact_info: dict
    estimated_time: str
    fees: str

@router.post("/chat", response_model=ChatResponse)
async def chat_with_bot(chat_message: ChatMessage):
    """
    Main chat endpoint that handles conversations in Grenadian Creole and English
    """
    try:
        # Detect language if not specified
        if not chat_message.language or chat_message.language == "auto":
            detected_lang = detect_language(chat_message.message)
            chat_message.language = detected_lang
        
        # Generate response using LLM service
        response = await llm_service.generate_response(
            message=chat_message.message,
            language=chat_message.language,
            session_id=chat_message.session_id
        )
        
        return ChatResponse(
            response=response["response"],
            session_id=response["session_id"],
            language=chat_message.language,
            confidence=response["confidence"],
            suggested_actions=response["suggested_actions"]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")

@router.post("/documents/{document_type}", response_model=DocumentResponse)
async def get_document_help(document_type: str, request: DocumentRequest):
    """
    Get specific help for legal documents and registry processes
    """
    try:
        if document_type not in settings.LEGAL_CATEGORIES:
            raise HTTPException(status_code=400, detail="Invalid document type")
        
        # Get document information using RAG service
        doc_info = await rag_service.get_document_info(
            document_type=document_type,
            query=request.query,
            language=request.language
        )
        
        return DocumentResponse(**doc_info)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Document help error: {str(e)}")

@router.get("/documents")
async def get_available_documents():
    """
    Get list of available document types for assistance
    """
    return {
        "document_types": settings.LEGAL_CATEGORIES,
        "descriptions": {
            "birth_certificate": "Birth registration and certificate requests",
            "death_certificate": "Death certificate applications",
            "marriage_certificate": "Marriage registration and certificates",
            "divorce_decree": "Divorce proceedings and decrees",
            "property_deed": "Property registration and deeds",
            "business_registration": "Business and company registration",
            "passport_application": "Passport applications and renewals",
            "national_id": "National ID card applications",
            "voter_registration": "Voter registration and updates",
            "tax_documents": "Tax-related documents and filings"
        }
    }

@router.post("/translate")
async def translate_message(message: str, target_language: str = "en"):
    """
    Translate messages between English and Grenadian Creole
    """
    try:
        translated = translate_creole(message, target_language)
        return {
            "original": message,
            "translated": translated,
            "target_language": target_language
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@router.get("/languages")
async def get_supported_languages():
    """
    Get list of supported languages
    """
    return {
        "supported_languages": settings.SUPPORTED_LANGUAGES,
        "primary_language": "en-GD",
        "description": "Grenadian Creole and English support"
    }