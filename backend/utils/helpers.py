# Common helper functions

import re
from typing import Dict, List, Optional
from config import settings

# Grenadian Creole patterns and vocabulary
CREOLE_PATTERNS = {
    "greetings": [
        r"\b(good\s+mornin|good\s+afternoon|good\s+evening)\b",
        r"\b(how\s+you\s+doin|how\s+yuh\s+doin)\b",
        r"\b(wha\s+happen|what\s+happen)\b",
        r"\b(mornin|evening)\b"
    ],
    "common_words": [
        r"\b(yuh|you)\b",
        r"\b(nah|no)\b",
        r"\b(wah|what)\b",
        r"\b(deh|there)\b",
        r"\b(gyal|girl)\b",
        r"\b(bwoy|boy)\b",
        r"\b(tings|things)\b",
        r"\b(nuff|enough|plenty)\b",
        r"\b(liming|hanging\s+out)\b",
        r"\b(irie|good|fine)\b"
    ],
    "legal_terms": [
        r"\b(birth\s+paper|death\s+paper|marriage\s+paper)\b",
        r"\b(divorce\s+paper|property\s+paper|business\s+paper)\b",
        r"\b(passport|id\s+card|voter\s+card)\b",
        r"\b(tax\s+paper|government\s+paper)\b"
    ],
    "grammar_patterns": [
        r"\b(i\s+want\s+to|i\s+need\s+to)\b",
        r"\b(how\s+to|where\s+to|what\s+to)\b",
        r"\b(how\s+much\s+it\s+cost|how\s+long\s+it\s+take)\b",
        r"\b(what\s+i\s+need|where\s+i\s+go)\b"
    ]
}

# Translation dictionary for common phrases
CREOLE_TRANSLATIONS = {
    "en_to_creole": {
        "good morning": "good mornin",
        "good afternoon": "good afternoon", 
        "good evening": "good evening",
        "how are you": "how yuh doin",
        "what's happening": "wha happen",
        "you": "yuh",
        "no": "nah",
        "what": "wah",
        "there": "deh",
        "girl": "gyal",
        "boy": "bwoy",
        "things": "tings",
        "enough": "nuff",
        "hanging out": "liming",
        "good": "irie",
        "birth certificate": "birth paper",
        "death certificate": "death paper",
        "marriage certificate": "marriage paper",
        "divorce decree": "divorce paper",
        "property deed": "property paper",
        "business registration": "business paper",
        "tax documents": "tax paper",
        "government documents": "government paper"
    },
    "creole_to_en": {
        "good mornin": "good morning",
        "how yuh doin": "how are you",
        "wha happen": "what's happening",
        "yuh": "you",
        "nah": "no",
        "wah": "what",
        "deh": "there",
        "gyal": "girl",
        "bwoy": "boy",
        "tings": "things",
        "nuff": "enough",
        "liming": "hanging out",
        "irie": "good",
        "birth paper": "birth certificate",
        "death paper": "death certificate",
        "marriage paper": "marriage certificate",
        "divorce paper": "divorce decree",
        "property paper": "property deed",
        "business paper": "business registration",
        "tax paper": "tax documents",
        "government paper": "government documents"
    }
}

def detect_language(text: str) -> str:
    """
    Detect if text contains Grenadian Creole patterns
    Returns 'en-GD' for Creole, 'en' for English
    """
    text_lower = text.lower()
    creole_score = 0
    english_score = 0
    
    # Check for Creole patterns
    for category, patterns in CREOLE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text_lower):
                creole_score += 1
    
    # Check for standard English patterns
    english_patterns = [
        r"\b(how\s+are\s+you|good\s+morning|good\s+afternoon|good\s+evening)\b",
        r"\b(what's\s+happening|what\s+is\s+happening)\b",
        r"\b(certificate|document|registration|application)\b",
        r"\b(please|thank\s+you|excuse\s+me)\b"
    ]
    
    for pattern in english_patterns:
        if re.search(pattern, text_lower):
            english_score += 1
    
    # Determine language based on scores
    if creole_score > english_score:
        return "en-GD"
    else:
        return "en"

def translate_creole(text: str, target_language: str = "en") -> str:
    """
    Translate between English and Grenadian Creole
    """
    if target_language == "en":
        # Translate Creole to English
        translated = text
        for creole, english in CREOLE_TRANSLATIONS["creole_to_en"].items():
            translated = re.sub(r'\b' + re.escape(creole) + r'\b', english, translated, flags=re.IGNORECASE)
        return translated
    elif target_language == "en-GD":
        # Translate English to Creole
        translated = text
        for english, creole in CREOLE_TRANSLATIONS["en_to_creole"].items():
            translated = re.sub(r'\b' + re.escape(english) + r'\b', creole, translated, flags=re.IGNORECASE)
        return translated
    else:
        return text

def extract_legal_intent(text: str) -> Dict:
    """
    Extract legal document intent from user message
    """
    text_lower = text.lower()
    intent = {
        "document_type": None,
        "action": None,
        "urgency": "normal",
        "language": detect_language(text)
    }
    
    # Detect document type
    document_keywords = {
        "birth_certificate": ["birth", "birth paper", "birth certificate", "born"],
        "death_certificate": ["death", "death paper", "death certificate", "passing", "died"],
        "marriage_certificate": ["marriage", "marriage paper", "marriage certificate", "married", "wedding"],
        "divorce_decree": ["divorce", "divorce paper", "divorce decree", "divorced"],
        "property_deed": ["property", "property paper", "property deed", "house", "land", "real estate"],
        "business_registration": ["business", "business paper", "business registration", "company", "register business"],
        "passport_application": ["passport", "travel", "travel document"],
        "national_id": ["id card", "national id", "identification", "id"],
        "voter_registration": ["voter", "voter card", "voting", "election"],
        "tax_documents": ["tax", "tax paper", "tax documents", "taxes", "revenue"]
    }
    
    for doc_type, keywords in document_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            intent["document_type"] = doc_type
            break
    
    # Detect action
    action_keywords = {
        "get_info": ["information", "info", "what", "how", "tell me"],
        "get_requirements": ["requirements", "need", "required", "what do i need"],
        "get_process": ["process", "steps", "procedure", "how to", "how do i"],
        "get_contact": ["contact", "where", "phone", "address", "location"],
        "get_fees": ["cost", "fee", "money", "price", "how much"]
    }
    
    for action, keywords in action_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            intent["action"] = action
            break
    
    # Detect urgency
    urgency_keywords = {
        "urgent": ["urgent", "emergency", "asap", "quick", "fast"],
        "normal": ["normal", "regular", "standard"]
    }
    
    for urgency, keywords in urgency_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            intent["urgency"] = urgency
            break
    
    return intent

def format_contact_info(contact_info: Dict) -> str:
    """
    Format contact information for display
    """
    if not contact_info:
        return "Contact information not available."
    
    formatted = f"**{contact_info.get('office', 'Office')}**\n"
    formatted += f"📍 {contact_info.get('address', 'Address not available')}\n"
    formatted += f"📞 {contact_info.get('phone', 'Phone not available')}\n"
    formatted += f"📧 {contact_info.get('email', 'Email not available')}\n"
    formatted += f"🕒 {contact_info.get('hours', 'Hours not available')}"
    
    return formatted

def format_requirements_list(requirements: List[str]) -> str:
    """
    Format requirements list for display
    """
    if not requirements:
        return "No specific requirements listed."
    
    formatted = "**Required Documents:**\n"
    for i, req in enumerate(requirements, 1):
        formatted += f"{i}. {req}\n"
    
    return formatted

def format_process_steps(steps: List[str]) -> str:
    """
    Format process steps for display
    """
    if not steps:
        return "Process steps not available."
    
    formatted = "**Process Steps:**\n"
    for i, step in enumerate(steps, 1):
        formatted += f"{i}. {step}\n"
    
    return formatted

def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent injection attacks
    """
    # Remove potentially dangerous characters
    sanitized = re.sub(r'[<>"\']', '', text)
    # Limit length
    if len(sanitized) > 1000:
        sanitized = sanitized[:1000]
    return sanitized.strip()

def generate_session_id() -> str:
    """
    Generate a unique session ID
    """
    import uuid
    return str(uuid.uuid4())

def validate_document_type(document_type: str) -> bool:
    """
    Validate if document type is supported
    """
    return document_type in settings.LEGAL_CATEGORIES