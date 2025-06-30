import React, { useState, useRef, useEffect } from 'react'
import { Send, Bot, User, FileText, Loader2, Globe, MessageCircle } from 'lucide-react'
import toast from 'react-hot-toast'
import axios from 'axios'

const ChatWindow = () => {
  const [messages, setMessages] = useState([])
  const [inputMessage, setInputMessage] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [sessionId, setSessionId] = useState(null)
  const [language, setLanguage] = useState('auto')
  const messagesEndRef = useRef(null)
  const inputRef = useRef(null)

  // Sample quick actions for common legal documents
  const quickActions = [
    { text: "How to get birth certificate?", icon: FileText },
    { text: "What documents do I need for marriage?", icon: FileText },
    { text: "How much does passport cost?", icon: FileText },
    { text: "Where to register my business?", icon: FileText },
    { text: "Good mornin, I need help", icon: MessageCircle },
    { text: "How yuh doin? I want to know about property papers", icon: MessageCircle }
  ]

  useEffect(() => {
    // Generate session ID on component mount
    setSessionId(crypto.randomUUID())
    
    // Add welcome message
    setMessages([
      {
        id: 1,
        type: 'bot',
        content: "Good mornin! I'm NutmegAI, your Grenadian legal assistant. I can help you with birth certificates, marriage papers, business registration, and more. You can chat with me in English or Grenadian Creole. How can I help you today?",
        timestamp: new Date(),
        language: 'en-GD'
      }
    ])
  }, [])

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  const sendMessage = async (messageText) => {
    if (!messageText.trim()) return

    const userMessage = {
      id: Date.now(),
      type: 'user',
      content: messageText,
      timestamp: new Date(),
      language: language === 'auto' ? 'auto' : language
    }

    setMessages(prev => [...prev, userMessage])
    setInputMessage('')
    setIsLoading(true)

    try {
      const response = await axios.post('/api/v1/chatbot/chat', {
        message: messageText,
        session_id: sessionId,
        language: language === 'auto' ? 'auto' : language
      })

      const botMessage = {
        id: Date.now() + 1,
        type: 'bot',
        content: response.data.response,
        timestamp: new Date(),
        language: response.data.language,
        confidence: response.data.confidence,
        suggestedActions: response.data.suggested_actions
      }

      setMessages(prev => [...prev, botMessage])
    } catch (error) {
      console.error('Error sending message:', error)
      toast.error('Sorry, I\'m having trouble connecting. Please try again.')
      
      const errorMessage = {
        id: Date.now() + 1,
        type: 'bot',
        content: "Sorry, I'm having some technical difficulties right now. Could you try asking your question again in a few minutes? Or you could call the Civil Registry Office directly for immediate help.",
        timestamp: new Date(),
        language: 'en-GD',
        isError: true
      }
      
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    sendMessage(inputMessage)
  }

  const handleQuickAction = (action) => {
    sendMessage(action.text)
  }

  const formatTimestamp = (timestamp) => {
    return timestamp.toLocaleTimeString('en-US', { 
      hour: '2-digit', 
      minute: '2-digit' 
    })
  }

  const getLanguageBadge = (lang) => {
    if (lang === 'en-GD') {
      return <span className="creole-badge text-xs">🇬🇩 Creole</span>
    }
    return <span className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-800">🇺🇸 English</span>
  }

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      {/* Header */}
      <div className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-4xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-br from-grenada-500 to-grenada-600 rounded-lg flex items-center justify-center">
                <Bot className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900">NutmegAI Chat</h1>
                <p className="text-sm text-gray-500">Grenadian Legal Assistant</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-2">
              <Globe className="w-4 h-4 text-gray-400" />
              <select
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                className="text-sm border border-gray-300 rounded-md px-2 py-1 focus:outline-none focus:ring-2 focus:ring-grenada-500"
              >
                <option value="auto">Auto Detect</option>
                <option value="en">English</option>
                <option value="en-GD">Grenadian Creole</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      {/* Chat Container */}
      <div className="flex-1 max-w-4xl mx-auto w-full px-4 py-6">
        <div className="bg-white rounded-xl shadow-lg border border-gray-200 h-[600px] flex flex-col">
          {/* Messages Area */}
          <div className="flex-1 overflow-y-auto p-6 space-y-4">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div className={`flex items-start space-x-3 max-w-xs lg:max-w-md ${message.type === 'user' ? 'flex-row-reverse space-x-reverse' : ''}`}>
                  <div className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
                    message.type === 'user' 
                      ? 'bg-grenada-500' 
                      : 'bg-gray-100'
                  }`}>
                    {message.type === 'user' ? (
                      <User className="w-4 h-4 text-white" />
                    ) : (
                      <Bot className="w-4 h-4 text-gray-600" />
                    )}
                  </div>
                  
                  <div className={`chat-bubble ${message.type === 'user' ? 'chat-bubble-user' : 'chat-bubble-bot'}`}>
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-xs opacity-75">
                        {formatTimestamp(message.timestamp)}
                      </span>
                      {message.language && getLanguageBadge(message.language)}
                    </div>
                    <p className="text-sm leading-relaxed">{message.content}</p>
                    
                    {/* Suggested Actions */}
                    {message.suggestedActions && message.suggestedActions.length > 0 && (
                      <div className="mt-3 pt-3 border-t border-gray-200">
                        <p className="text-xs text-gray-500 mb-2">Suggested actions:</p>
                        <div className="flex flex-wrap gap-2">
                          {message.suggestedActions.map((action, index) => (
                            <button
                              key={index}
                              onClick={() => sendMessage(action)}
                              className="text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 px-2 py-1 rounded transition-colors"
                            >
                              {action}
                            </button>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))}
            
            {/* Loading indicator */}
            {isLoading && (
              <div className="flex justify-start">
                <div className="flex items-start space-x-3">
                  <div className="w-8 h-8 bg-gray-100 rounded-full flex items-center justify-center">
                    <Bot className="w-4 h-4 text-gray-600" />
                  </div>
                  <div className="chat-bubble chat-bubble-bot">
                    <div className="flex items-center space-x-2">
                      <Loader2 className="w-4 h-4 animate-spin text-gray-400" />
                      <span className="text-sm text-gray-500">NutmegAI is typing...</span>
                    </div>
                  </div>
                </div>
              </div>
            )}
            
            <div ref={messagesEndRef} />
          </div>

          {/* Quick Actions */}
          {messages.length <= 1 && (
            <div className="border-t border-gray-200 p-4">
              <p className="text-sm text-gray-500 mb-3">Quick questions you can ask:</p>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                {quickActions.map((action, index) => {
                  const Icon = action.icon
                  return (
                    <button
                      key={index}
                      onClick={() => handleQuickAction(action)}
                      className="flex items-center space-x-2 p-3 text-left bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors text-sm"
                    >
                      <Icon className="w-4 h-4 text-grenada-600" />
                      <span className="text-gray-700">{action.text}</span>
                    </button>
                  )
                })}
              </div>
            </div>
          )}

          {/* Input Area */}
          <div className="border-t border-gray-200 p-4">
            <form onSubmit={handleSubmit} className="flex space-x-3">
              <input
                ref={inputRef}
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder="Ask me about legal documents, government services, or anything else..."
                className="flex-1 input-field"
                disabled={isLoading}
              />
              <button
                type="submit"
                disabled={isLoading || !inputMessage.trim()}
                className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <Send className="w-4 h-4" />
              </button>
            </form>
            
            <div className="mt-2 flex items-center justify-between text-xs text-gray-500">
              <span>Press Enter to send</span>
              <span>Session: {sessionId?.slice(0, 8)}...</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ChatWindow
