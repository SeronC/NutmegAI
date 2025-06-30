import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_health():
    """Test the health endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print("✅ Health Check:", response.json())
        return True
    except Exception as e:
        print("❌ Health Check Failed:", e)
        return False

def test_chat():
    """Test the chat endpoint with Grenadian Creole"""
    try:
        # Test with Creole
        creole_message = {
            "message": "Good mornin, I need help with birth paper",
            "language": "auto"
        }
        response = requests.post(f"{BASE_URL}/api/v1/chatbot/chat", json=creole_message)
        print("✅ Creole Chat Test:")
        print(json.dumps(response.json(), indent=2))
        
        # Test with English
        english_message = {
            "message": "How much does a passport cost?",
            "language": "en"
        }
        response = requests.post(f"{BASE_URL}/api/v1/chatbot/chat", json=english_message)
        print("\n✅ English Chat Test:")
        print(json.dumps(response.json(), indent=2))
        
        return True
    except Exception as e:
        print("❌ Chat Test Failed:", e)
        return False

def test_documents():
    """Test the documents endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/api/v1/chatbot/documents")
        print("✅ Documents Test:")
        print(json.dumps(response.json(), indent=2))
        return True
    except Exception as e:
        print("❌ Documents Test Failed:", e)
        return False

def test_translation():
    """Test the translation endpoint"""
    try:
        # Test English to Creole
        response = requests.post(f"{BASE_URL}/api/v1/chatbot/translate?message=good morning&target_language=en-GD")
        print("✅ Translation Test:")
        print(json.dumps(response.json(), indent=2))
        return True
    except Exception as e:
        print("❌ Translation Test Failed:", e)
        return False

def main():
    print("🚀 Testing NutmegAI API...\n")
    
    # Test all endpoints
    tests = [
        ("Health Check", test_health),
        ("Documents", test_documents),
        ("Translation", test_translation),
        ("Chat", test_chat),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Testing: {test_name}")
        print('='*50)
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print(f"\n{'='*50}")
    print("TEST SUMMARY")
    print('='*50)
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    if all(result for _, result in results):
        print("\n🎉 All tests passed! NutmegAI is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the backend server.")

if __name__ == "__main__":
    main() 