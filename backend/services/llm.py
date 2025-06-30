# LLM integration logic (e.g., Llama/OpenAI)

import openai
import uuid
import json
from typing import Dict, List, Optional
from config import settings

class LLMService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        self.conversation_history = {}
        
        # Grenadian Creole patterns and responses
        self.creole_patterns = {
            "greetings": [
                "mornin", "good mornin", "good afternoon", "good evening",
                "how you doin", "how yuh doin", "wha happen", "what happen"
            ],
            "legal_terms": [
                "birth paper", "death paper", "marriage paper", "divorce paper",
                "property paper", "business paper", "passport", "id card",
                "voter card", "tax paper"
            ],
            "common_phrases": [
                "i need help", "i want to", "how to", "where to go",
                "what i need", "how much it cost", "how long it take"
            ]
        }
        
        # Legal document knowledge base
        self.legal_knowledge = {
            "birth_certificate": {
                "requirements": [
                    "Parent's identification",
                    "Hospital birth record",
                    "Witness statement",
                    "Application form"
                ],
                "process": [
                    "Visit the Civil Registry Office",
                    "Submit required documents",
                    "Pay applicable fees",
                    "Wait for processing (3-5 business days)"
                ],
                "fees": "EC$25.00",
                "contact": "Civil Registry Office, St. George's"
            },
            "death_certificate": {
                "requirements": [
                    "Medical certificate of death",
                    "Funeral director's statement",
                    "Next of kin identification",
                    "Application form"
                ],
                "process": [
                    "Obtain medical certificate",
                    "Submit to Civil Registry",
                    "Pay fees",
                    "Processing time: 2-3 business days"
                ],
                "fees": "EC$20.00",
                "contact": "Civil Registry Office, St. George's"
            },
            "marriage_certificate": {
                "requirements": [
                    "Marriage license",
                    "Officiant's certificate",
                    "Witness statements",
                    "Both parties' identification"
                ],
                "process": [
                    "Apply for marriage license",
                    "Conduct marriage ceremony",
                    "Submit certificate to registry",
                    "Obtain official certificate"
                ],
                "fees": "EC$30.00",
                "contact": "Civil Registry Office, St. George's"
            }
        }

    async def generate_response(self, message: str, language: str = "en", session_id: Optional[str] = None) -> Dict:
        """
        Generate AI response with Grenadian Creole understanding
        """
        if not session_id:
            session_id = str(uuid.uuid4())
        
        # Initialize conversation history for new session
        if session_id not in self.conversation_history:
            self.conversation_history[session_id] = []
        
        # Detect if message is in Grenadian Creole
        is_creole = self._detect_creole(message)
        
        # Build system prompt based on language
        system_prompt = self._build_system_prompt(language, is_creole)
        
        # Add conversation context
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(self.conversation_history[session_id][-5:])  # Last 5 messages for context
        messages.append({"role": "user", "content": message})
        
        try:
            # Generate response using OpenAI
            response = self.client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            
            # Update conversation history
            self.conversation_history[session_id].append({"role": "user", "content": message})
            self.conversation_history[session_id].append({"role": "assistant", "content": ai_response})
            
            # Extract suggested actions
            suggested_actions = self._extract_suggested_actions(message, ai_response)
            
            # Calculate confidence based on response quality
            confidence = self._calculate_confidence(message, ai_response, is_creole)
            
            return {
                "response": ai_response,
                "session_id": session_id,
                "confidence": confidence,
                "suggested_actions": suggested_actions,
                "language_detected": "en-GD" if is_creole else "en"
            }
            
        except Exception as e:
            # Fallback response if OpenAI fails
            fallback_response = self._generate_fallback_response(message, language, is_creole)
            return {
                "response": fallback_response,
                "session_id": session_id,
                "confidence": 0.6,
                "suggested_actions": ["Contact support", "Try rephrasing your question"],
                "language_detected": "en-GD" if is_creole else "en"
            }

    def _detect_creole(self, message: str) -> bool:
        """
        Detect if message contains Grenadian Creole patterns
        """
        message_lower = message.lower()
        
        # Check for Creole patterns
        for category, patterns in self.creole_patterns.items():
            for pattern in patterns:
                if pattern in message_lower:
                    return True
        
        # Check for common Creole words
        creole_words = ["yuh", "nah", "wah", "deh", "gyal", "bwoy", "tings", "nuff"]
        for word in creole_words:
            if word in message_lower:
                return True
        
        return False

    def _build_system_prompt(self, language: str, is_creole: bool) -> str:
        """
        Build system prompt for the AI model
        """
        base_prompt = """You are NutmegAI, a helpful AI assistant for Grenadians seeking help with legal registry documents and government services. 

You understand and can respond in both English and Grenadian Creole. You are knowledgeable about:
- Birth, death, and marriage certificates
- Property deeds and business registration
- Passport and national ID applications
- Voter registration and tax documents
- Government office locations and procedures

Always be polite, patient, and culturally sensitive. If someone speaks in Grenadian Creole, respond in a way that's respectful and helpful.

Current conversation language: {language}
"""

        if is_creole:
            base_prompt += """
IMPORTANT: The user is speaking in Grenadian Creole. Respond in a warm, helpful manner that acknowledges their language choice. You can mix English and Creole as appropriate, but always ensure clarity.
"""
        
        return base_prompt.format(language=language)

    def _extract_suggested_actions(self, user_message: str, ai_response: str) -> List[str]:
        """
        Extract suggested next actions from the conversation
        """
        actions = []
        message_lower = user_message.lower()
        
        # Document-specific suggestions
        if any(doc in message_lower for doc in ["birth", "certificate", "paper"]):
            actions.append("Get birth certificate information")
        elif any(doc in message_lower for doc in ["death", "passing"]):
            actions.append("Get death certificate information")
        elif any(doc in message_lower for doc in ["marry", "wedding", "marriage"]):
            actions.append("Get marriage certificate information")
        elif any(doc in message_lower for doc in ["property", "house", "land"]):
            actions.append("Get property deed information")
        elif any(doc in message_lower for doc in ["business", "company"]):
            actions.append("Get business registration information")
        
        # General suggestions
        if "how" in message_lower or "what" in message_lower:
            actions.append("Get detailed process information")
        if "where" in message_lower:
            actions.append("Get office location and contact information")
        if "cost" in message_lower or "fee" in message_lower or "money" in message_lower:
            actions.append("Get fee information")
        
        return actions[:3]  # Limit to 3 suggestions

    def _calculate_confidence(self, user_message: str, ai_response: str, is_creole: bool) -> float:
        """
        Calculate confidence score for the response
        """
        confidence = 0.8  # Base confidence
        
        # Boost confidence for Creole detection
        if is_creole:
            confidence += 0.1
        
        # Boost confidence for longer, more detailed responses
        if len(ai_response) > 100:
            confidence += 0.05
        
        # Reduce confidence for very short responses
        if len(ai_response) < 20:
            confidence -= 0.2
        
        return min(confidence, 1.0)

    def _generate_fallback_response(self, message: str, language: str, is_creole: bool) -> str:
        """
        Generate fallback response when OpenAI is unavailable
        """
        if is_creole:
            return "Sorry, I having some technical difficulties right now. Could you try asking your question again in a few minutes? Or you could call the Civil Registry Office directly for immediate help."
        else:
            return "I'm experiencing some technical difficulties at the moment. Please try again in a few minutes, or contact the Civil Registry Office directly for immediate assistance."

    def get_legal_info(self, document_type: str) -> Dict:
        """
        Get legal document information
        """
        return self.legal_knowledge.get(document_type, {})