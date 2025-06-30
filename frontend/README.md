# NutmegAI Frontend

Modern React frontend for the NutmegAI Grenadian Legal Assistant, featuring a beautiful chat interface with Grenadian Creole support.

## Features

- **Modern UI/UX**: Beautiful, responsive design with Grenadian color scheme
- **Real-time Chat**: Interactive chat interface with AI assistant
- **Language Support**: Automatic detection and support for Grenadian Creole
- **Document Assistance**: Quick access to legal document information
- **Mobile Responsive**: Optimized for all device sizes
- **Accessibility**: WCAG compliant design

## Tech Stack

- **React 18**: Modern React with hooks and functional components
- **Vite**: Fast build tool and development server
- **Tailwind CSS**: Utility-first CSS framework
- **React Router**: Client-side routing
- **Axios**: HTTP client for API communication
- **Lucide React**: Beautiful icon library
- **Framer Motion**: Smooth animations
- **React Hot Toast**: Toast notifications

## Setup Instructions

### 1. Install Dependencies

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
# or
yarn install
```

### 2. Environment Configuration

Create a `.env` file in the frontend directory:

```env
# API Configuration
VITE_API_BASE_URL=http://localhost:8000/api/v1

# App Configuration
VITE_APP_NAME=NutmegAI
VITE_APP_DESCRIPTION=Grenadian Legal Assistant
```

### 3. Development Server

Start the development server:

```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`

### 4. Build for Production

```bash
npm run build
# or
yarn build
```

## Project Structure

```
frontend/
├── public/                 # Static assets
├── source/
│   ├── components/         # Reusable React components
│   │   ├── ChatWindow.jsx  # Main chat interface
│   │   └── Navbar.jsx      # Navigation component
│   ├── pages/              # Page components
│   │   └── Home.jsx        # Landing page
│   ├── App.jsx             # Main app component
│   ├── index.js            # React entry point
│   └── index.css           # Global styles
├── package.json            # Dependencies and scripts
├── vite.config.js          # Vite configuration
├── tailwind.config.js      # Tailwind CSS configuration
└── README.md              # This file
```

## Components

### ChatWindow

The main chat interface component with the following features:

- **Real-time messaging** with AI assistant
- **Language detection** for Grenadian Creole
- **Quick action buttons** for common queries
- **Message history** with timestamps
- **Loading states** and error handling
- **Suggested actions** from AI responses

**Props**: None (self-contained)

**State Management**:
- `messages`: Array of chat messages
- `inputMessage`: Current input text
- `isLoading`: Loading state for API calls
- `sessionId`: Unique session identifier
- `language`: Selected language preference

### Navbar

Navigation component with:

- **Brand logo** and company name
- **Navigation links** (Home, Chat)
- **Language indicator** showing Creole support
- **Mobile responsive** hamburger menu

**Props**: None (uses React Router)

### Home

Landing page component featuring:

- **Hero section** with call-to-action
- **Features overview** with icons
- **Document types** grid
- **Testimonials** section
- **Grenadian branding** and colors

## Styling

### Color Scheme

The application uses a Grenadian-inspired color palette:

```css
/* Grenadian Orange (Primary) */
--grenada-500: #f2751f;
--grenada-600: #e35d15;

/* Nutmeg Brown (Secondary) */
--nutmeg-500: #e0753d;
--nutmeg-600: #d15e2e;

/* Creole Blue (Accent) */
--creole-500: #0ea5e9;
--creole-600: #0284c7;
```

### Tailwind Classes

Common utility classes used throughout the application:

```css
/* Buttons */
.btn-primary: bg-grenada-500 hover:bg-grenada-600 text-white
.btn-secondary: bg-gray-100 hover:bg-gray-200 text-gray-900

/* Cards */
.card: bg-white rounded-xl shadow-lg border border-gray-200 p-6

/* Input fields */
.input-field: w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-grenada-500

/* Chat bubbles */
.chat-bubble-user: bg-grenada-500 text-white ml-auto
.chat-bubble-bot: bg-gray-100 text-gray-900
```

## API Integration

### Chat Endpoints

The frontend communicates with the backend API for:

- **POST** `/api/v1/chatbot/chat` - Send messages to AI
- **GET** `/api/v1/chatbot/documents` - Get document types
- **POST** `/api/v1/chatbot/translate` - Translate messages

### Error Handling

The application includes comprehensive error handling:

- **Network errors** with user-friendly messages
- **API timeouts** with retry options
- **Fallback responses** when AI is unavailable
- **Toast notifications** for user feedback

## Grenadian Creole Support

### Language Detection

The application automatically detects Grenadian Creole patterns:

```javascript
// Common Creole words
const creoleWords = ["yuh", "nah", "wah", "deh", "gyal", "bwoy", "tings", "nuff"];

// Greeting patterns
const greetings = ["good mornin", "how yuh doin", "wha happen"];

// Legal terms
const legalTerms = ["birth paper", "death paper", "marriage paper"];
```

### Quick Actions

Pre-defined quick action buttons include:

- "How to get birth certificate?"
- "What documents do I need for marriage?"
- "Good mornin, I need help"
- "How yuh doin? I want to know about property papers"

## Responsive Design

### Breakpoints

The application is responsive across all device sizes:

- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px

### Mobile Features

- **Touch-friendly** buttons and inputs
- **Swipe gestures** for navigation
- **Optimized chat interface** for small screens
- **Collapsible navigation** menu

## Performance

### Optimization Features

- **Code splitting** with React Router
- **Lazy loading** for components
- **Optimized images** and assets
- **Minified builds** for production
- **Caching strategies** for API responses

### Bundle Analysis

```bash
# Analyze bundle size
npm run build -- --analyze
```

## Accessibility

### WCAG Compliance

The application follows WCAG 2.1 guidelines:

- **Keyboard navigation** support
- **Screen reader** compatibility
- **Color contrast** ratios
- **Focus indicators** for interactive elements
- **Alt text** for images
- **Semantic HTML** structure

### ARIA Labels

```jsx
// Example of accessible button
<button
  aria-label="Send message"
  aria-describedby="message-input"
  onClick={handleSubmit}
>
  <Send className="w-4 h-4" />
</button>
```

## Testing

### Unit Tests

```bash
# Run tests
npm test

# Run tests with coverage
npm test -- --coverage
```

### E2E Tests

```bash
# Run end-to-end tests
npm run test:e2e
```

## Deployment

### Build Process

```bash
# Create production build
npm run build

# Preview production build
npm run preview
```

### Deployment Options

1. **Vercel** (Recommended)
   ```bash
   npm install -g vercel
   vercel
   ```

2. **Netlify**
   - Connect repository
   - Set build command: `npm run build`
   - Set publish directory: `dist`

3. **Static Hosting**
   - Upload `dist` folder to any static hosting service

### Environment Variables for Production

```env
VITE_API_BASE_URL=https://api.nutmegai.com/api/v1
VITE_APP_NAME=NutmegAI
VITE_APP_DESCRIPTION=Grenadian Legal Assistant
```

## Development

### Code Style

The project uses:

- **ESLint** for code linting
- **Prettier** for code formatting
- **Husky** for pre-commit hooks

### Git Hooks

```bash
# Install git hooks
npm run prepare

# Pre-commit will run:
# - ESLint
# - Prettier
# - Type checking (if TypeScript)
```

### Adding New Features

1. **New Component**: Create in `source/components/`
2. **New Page**: Create in `source/pages/` and add route
3. **New API Call**: Add to appropriate service file
4. **New Styling**: Use Tailwind classes or add to `index.css`

## Troubleshooting

### Common Issues

1. **API Connection Error**
   - Check backend server is running
   - Verify API URL in environment variables
   - Check CORS configuration

2. **Build Errors**
   - Clear node_modules and reinstall
   - Check for syntax errors in components
   - Verify all imports are correct

3. **Styling Issues**
   - Check Tailwind CSS is properly configured
   - Verify custom CSS classes are defined
   - Check for conflicting styles

### Debug Mode

```bash
# Enable debug logging
DEBUG=true npm run dev
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is proprietary software for NutmegAI.

## Support

For support and questions, contact the development team. 