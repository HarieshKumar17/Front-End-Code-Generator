# Front-End Code Generator

## Project Overview

A powerful web application built with Streamlit and Groq API that automatically generates production-ready frontend code based on user requirements. The application supports multiple frameworks (React, Angular, HTML/CSS/JavaScript) and provides instant live preview for HTML/CSS/JS implementations.

## Key Features

- **Multi-Framework Support**: Generate code for React, Angular, and HTML/CSS/JavaScript
- **Live Preview**: Instant visualization for HTML/CSS/JavaScript implementations
- **Customizable Styling**: Input custom style preferences and theme requirements
- **Download Options**: One-click download of complete project structure in ZIP format
- **Production-Ready Code**: Generated code follows industry best practices and modern standards
- **Responsive Design**: All generated code is mobile-first and fully responsive

## Technical Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Integration**: Groq API with LLaMA 3.3 70B Versatile model
- **Code Generation**: Automated generation with framework-specific best practices
- **Version Control**: Git/GitHub
- **Code Export**: ZIP file generation with proper project structure

## Implementation Details

### Core Components

1. **Framework Selection**
    - Support for React, Angular, and HTML/CSS/JavaScript
    - Framework-specific code generation with appropriate file structure
    - Built-in best practices for each framework
2. **Code Generation Engine**
    - Integration with Groq API
    - LLaMA 3.3 70B Versatile model for code generation
    - Prompt engineering for framework-specific requirements
3. **Live Preview System**
    - Real-time rendering of HTML/CSS/JavaScript code
    - Interactive preview window with scrolling capability
    - Responsive design testing
4. **Project Export**
    - Automated ZIP file creation
    - Framework-specific file structure
    - Included README with setup instructions

## Code Generation Specifications

### HTML/CSS/JavaScript

- Live preview functionality
- Separated files for HTML, CSS, and JavaScript
- Mobile-first responsive design
- Cross-browser compatibility

### React

- Functional components with hooks
- Modular component architecture
- React Router integration
- Proper project structure with src/ directory

### Angular

- TypeScript implementation
- Component-based architecture
- Angular modules and services
- Routing configuration

## Installation & Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

**Requirements.txt**

```
streamlit
groq
python-dotenv
```

Set up environment variables:

```bash
GROQ_API_KEY=your_api_key_here
```

## Usage Guide

1. **Select Framework**
    - Choose between React, Angular, or HTML/CSS/JavaScript
    - Each framework generates appropriate file structure
2. **Input Requirements**
    - Enter website requirements in the prompt field
    - Specify style and theme preferences
3. **Generate Code**
    - Click "Generate Code" button
    - Review generated code and preview (for HTML/CSS/JS)
4. **Download Project**
    - Click "Download ZIP" button
    - Extract and follow README instructions for setup

### Running the Chatbot

Run the Streamlit application with the following command:

```python
streamlit run app.py
```

## Contributing

Contributions are welcome! Please read our contributing guidelines and code of conduct before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
