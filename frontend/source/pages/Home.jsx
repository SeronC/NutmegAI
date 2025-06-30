import React from 'react'
import { Link } from 'react-router-dom'
import { 
  MessageCircle, 
  FileText, 
  Globe, 
  Shield, 
  Clock, 
  Users,
  ArrowRight,
  CheckCircle,
  Star
} from 'lucide-react'

const Home = () => {
  const features = [
    {
      icon: MessageCircle,
      title: "Grenadian Creole Support",
      description: "Chat naturally in Grenadian Creole or English. Our AI understands local language patterns and cultural context."
    },
    {
      icon: FileText,
      title: "Legal Document Assistance",
      description: "Get help with birth certificates, marriage licenses, property deeds, business registration, and more."
    },
    {
      icon: Globe,
      title: "24/7 Availability",
      description: "Access legal assistance anytime, anywhere. No need to wait for office hours or travel to government buildings."
    },
    {
      icon: Shield,
      title: "Secure & Private",
      description: "Your conversations and personal information are protected with enterprise-grade security."
    },
    {
      icon: Clock,
      title: "Instant Responses",
      description: "Get immediate answers to your legal questions without waiting in long queues."
    },
    {
      icon: Users,
      title: "Cultural Understanding",
      description: "Built specifically for Grenadians, understanding local customs, procedures, and government processes."
    }
  ]

  const documentTypes = [
    "Birth Certificates",
    "Death Certificates", 
    "Marriage Certificates",
    "Divorce Decrees",
    "Property Deeds",
    "Business Registration",
    "Passport Applications",
    "National ID Cards",
    "Voter Registration",
    "Tax Documents"
  ]

  const testimonials = [
    {
      name: "Maria Thomas",
      location: "St. George's",
      text: "NutmegAI helped me get my birth certificate in no time. The Creole support made it so easy to understand the process!",
      rating: 5
    },
    {
      name: "David Mitchell",
      location: "Grenville",
      text: "I was confused about business registration requirements. The chatbot explained everything clearly and saved me hours of research.",
      rating: 5
    },
    {
      name: "Sarah Williams",
      location: "Gouyave",
      text: "Finally, a service that speaks our language! The AI understood my questions perfectly and gave me the exact information I needed.",
      rating: 5
    }
  ]

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-grenada-500 via-grenada-600 to-grenada-700 text-white overflow-hidden">
        <div className="absolute inset-0 bg-black opacity-10"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 lg:py-32">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-6 leading-tight">
              Your AI Legal Assistant
              <span className="block text-grenada-200">for Grenada</span>
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-grenada-100 max-w-3xl mx-auto">
              Get instant help with legal documents and government services. 
              Speak naturally in Grenadian Creole or English.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <Link
                to="/chat"
                className="btn-primary text-lg px-8 py-4 flex items-center space-x-2 bg-white text-grenada-600 hover:bg-gray-100"
              >
                <MessageCircle className="w-5 h-5" />
                <span>Start Chatting Now</span>
                <ArrowRight className="w-5 h-5" />
              </Link>
              <div className="flex items-center space-x-2 text-grenada-200">
                <CheckCircle className="w-5 h-5" />
                <span>Free to use • No registration required</span>
              </div>
            </div>
          </div>
        </div>
        
        {/* Wave decoration */}
        <div className="absolute bottom-0 left-0 right-0">
          <svg viewBox="0 0 1200 120" preserveAspectRatio="none" className="w-full h-12">
            <path
              d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z"
              opacity=".25"
              className="fill-gray-50"
            ></path>
            <path
              d="M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z"
              opacity=".5"
              className="fill-gray-50"
            ></path>
            <path
              d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z"
              className="fill-gray-50"
            ></path>
          </svg>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Why Choose NutmegAI?
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Built specifically for Grenadians, our AI assistant understands your needs, 
              speaks your language, and knows your government processes.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => {
              const Icon = feature.icon
              return (
                <div key={index} className="card hover:shadow-xl transition-shadow duration-300">
                  <div className="w-12 h-12 bg-grenada-100 rounded-lg flex items-center justify-center mb-4">
                    <Icon className="w-6 h-6 text-grenada-600" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-3">
                    {feature.title}
                  </h3>
                  <p className="text-gray-600 leading-relaxed">
                    {feature.description}
                  </p>
                </div>
              )
            })}
          </div>
        </div>
      </section>

      {/* Document Types Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Legal Documents We Help With
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              From birth certificates to business registration, we provide guidance for all major legal documents in Grenada.
            </p>
          </div>
          
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
            {documentTypes.map((docType, index) => (
              <div key={index} className="bg-gray-50 rounded-lg p-4 text-center hover:bg-grenada-50 transition-colors duration-200">
                <FileText className="w-8 h-8 text-grenada-600 mx-auto mb-2" />
                <p className="text-sm font-medium text-gray-900">{docType}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              What Grenadians Are Saying
            </h2>
            <p className="text-xl text-gray-600">
              Real feedback from people who've used NutmegAI
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <div key={index} className="card">
                <div className="flex items-center mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star key={i} className="w-5 h-5 text-yellow-400 fill-current" />
                  ))}
                </div>
                <p className="text-gray-600 mb-4 italic">"{testimonial.text}"</p>
                <div className="flex items-center">
                  <div className="w-10 h-10 bg-grenada-100 rounded-full flex items-center justify-center">
                    <span className="text-grenada-600 font-semibold">
                      {testimonial.name.split(' ').map(n => n[0]).join('')}
                    </span>
                  </div>
                  <div className="ml-3">
                    <p className="font-semibold text-gray-900">{testimonial.name}</p>
                    <p className="text-sm text-gray-500">{testimonial.location}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-grenada-600 to-grenada-700 text-white">
        <div className="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl md:text-4xl font-bold mb-6">
            Ready to Get Started?
          </h2>
          <p className="text-xl mb-8 text-grenada-100">
            Join thousands of Grenadians who are already using NutmegAI to simplify their legal processes.
          </p>
          <Link
            to="/chat"
            className="btn-primary text-lg px-8 py-4 flex items-center space-x-2 bg-white text-grenada-600 hover:bg-gray-100 mx-auto w-fit"
          >
            <MessageCircle className="w-5 h-5" />
            <span>Start Your Free Chat</span>
            <ArrowRight className="w-5 h-5" />
          </Link>
        </div>
      </section>
    </div>
  )
}

export default Home
