# SQLAlchemy / Pydantic models
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import uuid

Base = declarative_base()

class ChatSession(Base):
    __tablename__ = 'chat_sessions'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String(36), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    language_preference = Column(String(10), default='en')
    is_active = Column(Boolean, default=True)
    
    # Relationships
    messages = relationship("ChatMessage", back_populates="session", cascade="all, delete-orphan")

class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    
    id = Column(Integer, primary_key=True)
    session_id = Column(String(36), ForeignKey('chat_sessions.session_id'), nullable=False)
    message_type = Column(String(10), nullable=False)  # 'user' or 'bot'
    content = Column(Text, nullable=False)
    language = Column(String(10), default='en')
    confidence = Column(Float, default=1.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    session = relationship("ChatSession", back_populates="messages")

class DocumentQuery(Base):
    __tablename__ = 'document_queries'
    
    id = Column(Integer, primary_key=True)
    session_id = Column(String(36), ForeignKey('chat_sessions.session_id'), nullable=False)
    document_type = Column(String(50), nullable=False)
    query_text = Column(Text, nullable=False)
    response_text = Column(Text, nullable=False)
    language = Column(String(10), default='en')
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    session = relationship("ChatSession")

class UserFeedback(Base):
    __tablename__ = 'user_feedback'
    
    id = Column(Integer, primary_key=True)
    session_id = Column(String(36), ForeignKey('chat_sessions.session_id'), nullable=False)
    message_id = Column(Integer, ForeignKey('chat_messages.id'), nullable=False)
    rating = Column(Integer, nullable=False)  # 1-5 stars
    feedback_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    session = relationship("ChatSession")
    message = relationship("ChatMessage")

class LegalDocument(Base):
    __tablename__ = 'legal_documents'
    
    id = Column(Integer, primary_key=True)
    document_type = Column(String(50), unique=True, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    requirements = Column(Text)  # JSON string
    process_steps = Column(Text)  # JSON string
    fees = Column(String(100))
    estimated_time = Column(String(100))
    contact_info = Column(Text)  # JSON string
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CreoleTranslation(Base):
    __tablename__ = 'creole_translations'
    
    id = Column(Integer, primary_key=True)
    english_text = Column(Text, nullable=False)
    creole_text = Column(Text, nullable=False)
    category = Column(String(50))  # 'greeting', 'legal_term', 'common_phrase'
    confidence = Column(Float, default=1.0)
    usage_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)