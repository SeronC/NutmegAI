# Retrieval-augmented generation pipeline

import json
from typing import Dict, List, Optional
from config import settings

class RAGService:
    def __init__(self):
        # Comprehensive legal document knowledge base
        self.document_knowledge = {
            "birth_certificate": {
                "information": "Birth certificates are official documents that record a person's birth. They are essential for various legal purposes including school enrollment, passport applications, and government services.",
                "requirements": [
                    "Completed birth registration form",
                    "Parent's valid identification (passport, national ID, or driver's license)",
                    "Hospital birth record or midwife's certificate",
                    "Witness statement (if applicable)",
                    "Payment of EC$25.00 fee"
                ],
                "process_steps": [
                    "Visit the Civil Registry Office in St. George's",
                    "Submit all required documents",
                    "Pay the application fee",
                    "Wait for processing (3-5 business days)",
                    "Collect the certificate in person or arrange for delivery"
                ],
                "contact_info": {
                    "office": "Civil Registry Office",
                    "address": "Ministerial Complex, Botanical Gardens, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "civilregistry@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "3-5 business days",
                "fees": "EC$25.00"
            },
            "death_certificate": {
                "information": "Death certificates are official documents that record a person's death. They are required for legal proceedings, insurance claims, and estate matters.",
                "requirements": [
                    "Medical certificate of death from a doctor",
                    "Funeral director's statement",
                    "Next of kin's identification",
                    "Completed application form",
                    "Payment of EC$20.00 fee"
                ],
                "process_steps": [
                    "Obtain medical certificate of death",
                    "Contact funeral director for statement",
                    "Visit Civil Registry Office",
                    "Submit all documents and payment",
                    "Wait for processing (2-3 business days)",
                    "Collect certificate"
                ],
                "contact_info": {
                    "office": "Civil Registry Office",
                    "address": "Ministerial Complex, Botanical Gardens, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "civilregistry@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "2-3 business days",
                "fees": "EC$20.00"
            },
            "marriage_certificate": {
                "information": "Marriage certificates are official documents that prove a legal marriage. They are required for name changes, insurance, and other legal purposes.",
                "requirements": [
                    "Marriage license (obtained before ceremony)",
                    "Officiant's certificate of marriage",
                    "Witness statements",
                    "Both parties' identification",
                    "Payment of EC$30.00 fee"
                ],
                "process_steps": [
                    "Apply for marriage license (21 days notice required)",
                    "Conduct marriage ceremony with licensed officiant",
                    "Submit marriage certificate to Civil Registry",
                    "Wait for official registration",
                    "Obtain certified copy of marriage certificate"
                ],
                "contact_info": {
                    "office": "Civil Registry Office",
                    "address": "Ministerial Complex, Botanical Gardens, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "civilregistry@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "5-7 business days",
                "fees": "EC$30.00"
            },
            "divorce_decree": {
                "information": "Divorce decrees are court-issued documents that legally end a marriage. They are required for remarriage and other legal proceedings.",
                "requirements": [
                    "Petition for divorce",
                    "Marriage certificate",
                    "Grounds for divorce documentation",
                    "Legal representation (recommended)",
                    "Court filing fees"
                ],
                "process_steps": [
                    "Consult with a lawyer",
                    "File petition with the High Court",
                    "Serve papers to spouse",
                    "Attend court hearings",
                    "Obtain final decree",
                    "Register decree with Civil Registry"
                ],
                "contact_info": {
                    "office": "High Court of Grenada",
                    "address": "Carenage, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "courts@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "3-6 months",
                "fees": "Varies based on complexity"
            },
            "property_deed": {
                "information": "Property deeds are legal documents that prove ownership of real estate. They are essential for property transactions and inheritance matters.",
                "requirements": [
                    "Survey plan of the property",
                    "Title search report",
                    "Transfer documents",
                    "Stamp duty payment",
                    "Legal representation (required)"
                ],
                "process_steps": [
                    "Conduct title search",
                    "Obtain survey plan",
                    "Prepare transfer documents",
                    "Pay stamp duty",
                    "Register with Land Registry",
                    "Obtain certified copy of deed"
                ],
                "contact_info": {
                    "office": "Land Registry Office",
                    "address": "Ministerial Complex, Botanical Gardens, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "landregistry@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "2-4 weeks",
                "fees": "Based on property value"
            },
            "business_registration": {
                "information": "Business registration is required for operating a business in Grenada. It provides legal recognition and tax identification.",
                "requirements": [
                    "Business name reservation",
                    "Completed registration form",
                    "Business plan",
                    "Identification documents",
                    "Registration fee payment"
                ],
                "process_steps": [
                    "Reserve business name",
                    "Complete registration application",
                    "Submit required documents",
                    "Pay registration fees",
                    "Obtain business license",
                    "Register for taxes"
                ],
                "contact_info": {
                    "office": "Companies Registry",
                    "address": "Ministerial Complex, Botanical Gardens, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "companies@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "5-10 business days",
                "fees": "EC$200.00 - EC$500.00"
            },
            "passport_application": {
                "information": "Grenadian passports are travel documents issued to citizens. They are required for international travel and serve as proof of citizenship.",
                "requirements": [
                    "Completed passport application form",
                    "Birth certificate",
                    "National ID or previous passport",
                    "Two passport photos",
                    "Payment of passport fee"
                ],
                "process_steps": [
                    "Complete application form",
                    "Gather required documents",
                    "Visit Passport Office",
                    "Submit application and payment",
                    "Wait for processing",
                    "Collect passport"
                ],
                "contact_info": {
                    "office": "Passport Office",
                    "address": "Ministerial Complex, Botanical Gardens, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "passports@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "10-15 business days",
                "fees": "EC$150.00"
            },
            "national_id": {
                "information": "National ID cards are official identification documents for Grenadian citizens. They are required for various government services and transactions.",
                "requirements": [
                    "Completed ID application form",
                    "Birth certificate",
                    "Proof of address",
                    "Passport photo",
                    "Application fee"
                ],
                "process_steps": [
                    "Complete application form",
                    "Gather required documents",
                    "Visit ID Office",
                    "Submit application and payment",
                    "Wait for processing",
                    "Collect ID card"
                ],
                "contact_info": {
                    "office": "National ID Office",
                    "address": "Ministerial Complex, Botanical Gardens, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "nationalid@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "7-10 business days",
                "fees": "EC$50.00"
            },
            "voter_registration": {
                "information": "Voter registration allows citizens to participate in elections. Registration is required to vote in national and local elections.",
                "requirements": [
                    "Completed voter registration form",
                    "Proof of citizenship",
                    "Proof of address",
                    "Identification document",
                    "Age 18 or older"
                ],
                "process_steps": [
                    "Complete registration form",
                    "Gather required documents",
                    "Visit Electoral Office",
                    "Submit application",
                    "Wait for verification",
                    "Receive voter ID card"
                ],
                "contact_info": {
                    "office": "Electoral Office",
                    "address": "Ministerial Complex, Botanical Gardens, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "electoral@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "5-7 business days",
                "fees": "Free"
            },
            "tax_documents": {
                "information": "Tax documents include various forms and certificates required for tax compliance and business operations in Grenada.",
                "requirements": [
                    "Business registration certificate",
                    "Financial records",
                    "Completed tax forms",
                    "Supporting documentation",
                    "Payment of taxes due"
                ],
                "process_steps": [
                    "Register for tax identification",
                    "Maintain proper records",
                    "Complete tax returns",
                    "Submit to Inland Revenue",
                    "Pay taxes due",
                    "Obtain tax clearance certificate"
                ],
                "contact_info": {
                    "office": "Inland Revenue Department",
                    "address": "Ministerial Complex, Botanical Gardens, St. George's",
                    "phone": "+1 (473) 440-2251",
                    "email": "tax@gov.gd",
                    "hours": "Monday-Friday, 8:00 AM - 4:00 PM"
                },
                "estimated_time": "Varies by document type",
                "fees": "Varies by tax type"
            }
        }

    async def get_document_info(self, document_type: str, query: str, language: str = "en") -> Dict:
        """
        Retrieve information about a specific document type
        """
        if document_type not in self.document_knowledge:
            return {
                "information": "Document type not found. Please check the available document types.",
                "requirements": [],
                "process_steps": [],
                "contact_info": {},
                "estimated_time": "Unknown",
                "fees": "Unknown"
            }
        
        doc_info = self.document_knowledge[document_type].copy()
        
        # Customize response based on query
        if "requirement" in query.lower() or "need" in query.lower():
            return {
                "information": doc_info["information"],
                "requirements": doc_info["requirements"],
                "process_steps": [],
                "contact_info": doc_info["contact_info"],
                "estimated_time": doc_info["estimated_time"],
                "fees": doc_info["fees"]
            }
        elif "process" in query.lower() or "step" in query.lower() or "how" in query.lower():
            return {
                "information": doc_info["information"],
                "requirements": [],
                "process_steps": doc_info["process_steps"],
                "contact_info": doc_info["contact_info"],
                "estimated_time": doc_info["estimated_time"],
                "fees": doc_info["fees"]
            }
        elif "contact" in query.lower() or "where" in query.lower() or "phone" in query.lower():
            return {
                "information": doc_info["information"],
                "requirements": [],
                "process_steps": [],
                "contact_info": doc_info["contact_info"],
                "estimated_time": doc_info["estimated_time"],
                "fees": doc_info["fees"]
            }
        elif "cost" in query.lower() or "fee" in query.lower() or "money" in query.lower():
            return {
                "information": f"The fee for {document_type.replace('_', ' ')} is {doc_info['fees']}.",
                "requirements": [],
                "process_steps": [],
                "contact_info": doc_info["contact_info"],
                "estimated_time": doc_info["estimated_time"],
                "fees": doc_info["fees"]
            }
        else:
            return doc_info

    async def search_documents(self, search_query: str) -> List[Dict]:
        """
        Search through all document types for relevant information
        """
        results = []
        query_lower = search_query.lower()
        
        for doc_type, info in self.document_knowledge.items():
            relevance_score = 0
            
            # Check if query terms appear in document information
            if any(term in info["information"].lower() for term in query_lower.split()):
                relevance_score += 2
            
            # Check requirements
            for req in info["requirements"]:
                if any(term in req.lower() for term in query_lower.split()):
                    relevance_score += 1
            
            # Check process steps
            for step in info["process_steps"]:
                if any(term in step.lower() for term in query_lower.split()):
                    relevance_score += 1
            
            if relevance_score > 0:
                results.append({
                    "document_type": doc_type,
                    "relevance_score": relevance_score,
                    "information": info["information"][:200] + "...",
                    "contact_info": info["contact_info"]
                })
        
        # Sort by relevance score
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        return results[:5]  # Return top 5 results