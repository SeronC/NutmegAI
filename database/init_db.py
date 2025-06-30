# DB setup script (PostgreSQL/MongoDB)

import os
import sys
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from models import Base, LegalDocument, CreoleTranslation
from config import settings

def init_database():
    """Initialize the database with tables and sample data"""
    
    # Create database engine
    engine = create_engine(settings.DATABASE_URL)
    
    # Create all tables
    Base.metadata.create_all(engine)
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Check if data already exists
        if session.query(LegalDocument).count() == 0:
            print("Populating legal documents...")
            populate_legal_documents(session)
        
        if session.query(CreoleTranslation).count() == 0:
            print("Populating Creole translations...")
            populate_creole_translations(session)
        
        session.commit()
        print("Database initialized successfully!")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        session.rollback()
    finally:
        session.close()

def populate_legal_documents(session):
    """Populate legal documents table with sample data"""
    
    documents = [
        {
            "document_type": "birth_certificate",
            "title": "Birth Certificate",
            "description": "Official document that records a person's birth. Essential for school enrollment, passport applications, and government services.",
            "requirements": json.dumps([
                "Completed birth registration form",
                "Parent's valid identification (passport, national ID, or driver's license)",
                "Hospital birth record or midwife's certificate",
                "Witness statement (if applicable)",
                "Payment of EC$25.00 fee"
            ]),
            "process_steps": json.dumps([
                "Visit the Civil Registry Office in St. George's",
                "Submit all required documents",
                "Pay the application fee",
                "Wait for processing (3-5 business days)",
                "Collect the certificate in person or arrange for delivery"
            ]),
            "fees": "EC$25.00",
            "estimated_time": "3-5 business days",
            "contact_info": json.dumps({
                "office": "Civil Registry Office",
                "address": "Ministerial Complex, Botanical Gardens, St. George's",
                "phone": "+1 (473) 440-2251",
                "email": "civilregistry@gov.gd",
                "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
            })
        },
        {
            "document_type": "death_certificate",
            "title": "Death Certificate",
            "description": "Official document that records a person's death. Required for legal proceedings, insurance claims, and estate matters.",
            "requirements": json.dumps([
                "Medical certificate of death from a doctor",
                "Funeral director's statement",
                "Next of kin's identification",
                "Completed application form",
                "Payment of EC$20.00 fee"
            ]),
            "process_steps": json.dumps([
                "Obtain medical certificate of death",
                "Contact funeral director for statement",
                "Visit Civil Registry Office",
                "Submit all documents and payment",
                "Wait for processing (2-3 business days)",
                "Collect certificate"
            ]),
            "fees": "EC$20.00",
            "estimated_time": "2-3 business days",
            "contact_info": json.dumps({
                "office": "Civil Registry Office",
                "address": "Ministerial Complex, Botanical Gardens, St. George's",
                "phone": "+1 (473) 440-2251",
                "email": "civilregistry@gov.gd",
                "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
            })
        },
        {
            "document_type": "marriage_certificate",
            "title": "Marriage Certificate",
            "description": "Official document that proves a legal marriage. Required for name changes, insurance, and other legal purposes.",
            "requirements": json.dumps([
                "Marriage license (obtained before ceremony)",
                "Officiant's certificate of marriage",
                "Witness statements",
                "Both parties' identification",
                "Payment of EC$30.00 fee"
            ]),
            "process_steps": json.dumps([
                "Apply for marriage license (21 days notice required)",
                "Conduct marriage ceremony with licensed officiant",
                "Submit marriage certificate to Civil Registry",
                "Wait for official registration",
                "Obtain certified copy of marriage certificate"
            ]),
            "fees": "EC$30.00",
            "estimated_time": "5-7 business days",
            "contact_info": json.dumps({
                "office": "Civil Registry Office",
                "address": "Ministerial Complex, Botanical Gardens, St. George's",
                "phone": "+1 (473) 440-2251",
                "email": "civilregistry@gov.gd",
                "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
            })
        },
        {
            "document_type": "business_registration",
            "title": "Business Registration",
            "description": "Required for operating a business in Grenada. Provides legal recognition and tax identification.",
            "requirements": json.dumps([
                "Business name reservation",
                "Completed registration form",
                "Business plan",
                "Identification documents",
                "Registration fee payment"
            ]),
            "process_steps": json.dumps([
                "Reserve business name",
                "Complete registration application",
                "Submit required documents",
                "Pay registration fees",
                "Obtain business license",
                "Register for taxes"
            ]),
            "fees": "EC$200.00 - EC$500.00",
            "estimated_time": "5-10 business days",
            "contact_info": json.dumps({
                "office": "Companies Registry",
                "address": "Ministerial Complex, Botanical Gardens, St. George's",
                "phone": "+1 (473) 440-2251",
                "email": "companies@gov.gd",
                "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
            })
        },
        {
            "document_type": "passport_application",
            "title": "Passport Application",
            "description": "Grenadian passports are travel documents issued to citizens. Required for international travel and serve as proof of citizenship.",
            "requirements": json.dumps([
                "Completed passport application form",
                "Birth certificate",
                "National ID or previous passport",
                "Two passport photos",
                "Payment of passport fee"
            ]),
            "process_steps": json.dumps([
                "Complete application form",
                "Gather required documents",
                "Visit Passport Office",
                "Submit application and payment",
                "Wait for processing",
                "Collect passport"
            ]),
            "fees": "EC$150.00",
            "estimated_time": "10-15 business days",
            "contact_info": json.dumps({
                "office": "Passport Office",
                "address": "Ministerial Complex, Botanical Gardens, St. George's",
                "phone": "+1 (473) 440-2251",
                "email": "passports@gov.gd",
                "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
            })
        }
    ]
    
    for doc_data in documents:
        doc = LegalDocument(**doc_data)
        session.add(doc)

def populate_creole_translations(session):
    """Populate Creole translations table with sample data"""
    
    translations = [
        # Greetings
        {"english_text": "good morning", "creole_text": "good mornin", "category": "greeting"},
        {"english_text": "how are you", "creole_text": "how yuh doin", "category": "greeting"},
        {"english_text": "what's happening", "creole_text": "wha happen", "category": "greeting"},
        {"english_text": "good afternoon", "creole_text": "good afternoon", "category": "greeting"},
        {"english_text": "good evening", "creole_text": "good evening", "category": "greeting"},
        
        # Common words
        {"english_text": "you", "creole_text": "yuh", "category": "common_word"},
        {"english_text": "no", "creole_text": "nah", "category": "common_word"},
        {"english_text": "what", "creole_text": "wah", "category": "common_word"},
        {"english_text": "there", "creole_text": "deh", "category": "common_word"},
        {"english_text": "girl", "creole_text": "gyal", "category": "common_word"},
        {"english_text": "boy", "creole_text": "bwoy", "category": "common_word"},
        {"english_text": "things", "creole_text": "tings", "category": "common_word"},
        {"english_text": "enough", "creole_text": "nuff", "category": "common_word"},
        {"english_text": "hanging out", "creole_text": "liming", "category": "common_word"},
        {"english_text": "good", "creole_text": "irie", "category": "common_word"},
        
        # Legal terms
        {"english_text": "birth certificate", "creole_text": "birth paper", "category": "legal_term"},
        {"english_text": "death certificate", "creole_text": "death paper", "category": "legal_term"},
        {"english_text": "marriage certificate", "creole_text": "marriage paper", "category": "legal_term"},
        {"english_text": "divorce decree", "creole_text": "divorce paper", "category": "legal_term"},
        {"english_text": "property deed", "creole_text": "property paper", "category": "legal_term"},
        {"english_text": "business registration", "creole_text": "business paper", "category": "legal_term"},
        {"english_text": "tax documents", "creole_text": "tax paper", "category": "legal_term"},
        {"english_text": "government documents", "creole_text": "government paper", "category": "legal_term"},
        
        # Common phrases
        {"english_text": "i need help", "creole_text": "i need help", "category": "common_phrase"},
        {"english_text": "i want to", "creole_text": "i want to", "category": "common_phrase"},
        {"english_text": "how to", "creole_text": "how to", "category": "common_phrase"},
        {"english_text": "where to go", "creole_text": "where to go", "category": "common_phrase"},
        {"english_text": "what i need", "creole_text": "what i need", "category": "common_phrase"},
        {"english_text": "how much it cost", "creole_text": "how much it cost", "category": "common_phrase"},
        {"english_text": "how long it take", "creole_text": "how long it take", "category": "common_phrase"}
    ]
    
    for trans_data in translations:
        trans = CreoleTranslation(**trans_data)
        session.add(trans)

if __name__ == "__main__":
    init_database()