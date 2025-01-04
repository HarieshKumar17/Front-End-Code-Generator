import os
import zipfile
import io
import streamlit as st
from dotenv import load_dotenv

# Attempt to import Groq and handle potential import errors
try:
    from groq import Groq 
except ImportError as e:
    st.error("Failed to import Groq. Please ensure the 'groq' package is installed correctly.")
    st.stop()

# Load environment variables
load_dotenv()

# Initialize Groq API client with error handling
try:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        st.error("GROQ_API_KEY not found in environment variables.")
        st.stop()
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"Error initializing Groq client: {e}")
    st.stop()

# Initialize Streamlit session state for generated code
if 'generated_code' not in st.session_state:
    st.session_state.generated_code = ""

if 'fine_tuned_code' not in st.session_state:
    st.session_state.fine_tuned_code = ""

# Application Title
st.title("Front-End Code Generator")

# Sidebar for User Input
st.sidebar.header("Input Parameters")

# Text box for website requirements prompt
requirements_prompt = st.sidebar.text_area(
    "Website Requirements Prompt",
    placeholder="e.g., I need a homepage with a navigation bar, footer, and a hero section...",
)

# Dropdown for selecting framework
framework = st.sidebar.selectbox(
    "Select Framework",
    ["React", "HTML/CSS/JavaScript", "Angular"],
)

# Text box for style and theme preferences
style_theme = st.sidebar.text_area(
    "Style and Theme Preferences",
    placeholder="e.g., Modern, Minimalistic, with a blue and white color scheme...",
    value="Modern, Minimalistic, with a blue and white color scheme",  # Default suggestion
)

# Generate Code Button
if st.sidebar.button("Generate Code"):
    if not requirements_prompt.strip():
        st.sidebar.warning("Please enter the website requirements prompt.")
    else:
        with st.spinner("Generating code..."):
            try:
                # Construct the prompt for the Groq API
                prompt = f"""
Generate {framework} code for a website based on the following user requirement: {requirements_prompt}. Ensure that the website includes all relevant aspects of a modern design that may not have been explicitly mentioned. Follow best practices for each framework, while fulfilling the following requirements:

### General Requirements (for all frameworks):
1. **Responsive Design**: Ensure the layout is fully responsive, adapting seamlessly to different screen sizes, including mobile, tablet, and desktop views.
2. **Navigation**: Implement a clean, user-friendly navigation menu accessible from all pages, with smooth transitions where appropriate.
3. **UI Components**: Include essential components like a hero section, service/product cards, testimonial sections, a contact form, and a footer. Ensure the code structure is modular and extendable.
4. **Performance Optimization**: Optimize for loading speed using techniques like image optimization, CSS and JS minification, lazy loading for images, and efficient caching strategies.
5. **Accessibility**: Follow web accessibility standards (WCAG 2.1). Use semantic HTML, ARIA attributes, and ensure keyboard navigability and screen reader compatibility.
6. **Cross-Browser Compatibility**: Ensure the code works flawlessly across modern browsers such as Chrome, Firefox, Safari, and Edge.
7. **SEO Optimization**: Follow SEO best practices, including meta tags, structured data (schema.org), proper heading hierarchy, and meaningful alt text for images.
8. **Modular Code Structure**: Generate code separated into appropriate modules or components for the chosen framework (React components, Angular modules, or plain HTML/CSS/JS files).
9. **Styling**: Apply the style and theme as provided in {style_theme}. Ensure consistent design, typography, and spacing. Include hover states, transitions, and animations as appropriate.
10. **Code Organization**: Ensure the code is clean, well-commented, and organized according to best practices. Use separate files for HTML, CSS, and JS (or components/modules for React and Angular).
11. **Deployment Readiness**: Make sure the generated code is ready for deployment on platforms like Netlify, Vercel, or GitHub Pages. Provide any necessary build scripts for frameworks requiring a build step (React, Angular).

### Framework-Specific Instructions:

#### If using **HTML/CSS/JavaScript**:
- Use vanilla HTML, CSS, and JavaScript.
- Organize the project in a modular way, separating concerns (e.g., CSS in a `styles.css` file, JavaScript in a `script.js` file).
- Include a mobile-first design approach.
- **Output Format**:
    ### FILE: index.html
    ```html
    <!-- HTML code here -->
    ```
    ### FILE: styles.css
    ```css
    /* CSS code here */
    ```
    ### FILE: script.js
    ```javascript
    // JavaScript code here
    ```

#### If using **React**:
- Use functional components and React hooks (e.g., `useState`, `useEffect`).
- Create modular components for each part of the website (e.g., Navbar, Hero, ContactForm).
- Use `React Router` for handling navigation between pages if needed.
- Ensure the project structure follows best practices for React, separating concerns and keeping styles modular (e.g., using CSS modules or Styled Components).
- **Output Format**:
    ### FILE: src/App.js
    ```javascript
    // React App.js code here
    ```
    ### FILE: src/index.js
    ```javascript
    // React index.js code here
    ```
    ### FILE: src/components/Navbar.js
    ```javascript
    // Navbar component code here
    ```
    ### FILE: src/styles.css
    ```css
    /* CSS code here */
    ```
    ### FILE: public/index.html
    ```html
    <!-- HTML code here -->
    ```

#### If using **Angular**:
- Use Angular modules and components for organizing the application.
- Implement routing using the Angular Router.
- Ensure that the code is following Angular’s best practices, including service-based architecture and use of TypeScript for type safety.
- Use Angular's two-way data binding and dependency injection for managing state and services.
- **Output Format**:
    ### FILE: src/app/app.component.html
    ```html
    <!-- Angular component HTML here -->
    ```
    ### FILE: src/app/app.component.ts
    ```typescript
    // Angular component TypeScript here
    ```
    ### FILE: src/app/app.module.ts
    ```typescript
    // Angular module TypeScript here
    ```
    ### FILE: src/styles.css
    ```css
    /* CSS code here */
    ```
    ### FILE: angular.json
    ```json
    // Angular configuration here
    ```

Please generate only the code no other text, without any general response or code explanation. Separate the code into different modules according to the respective {framework} and strictly follow {style_theme}. The code should be directly ready for download in corresponding files based on the structure provided. Additionally, ensure that the code can be run locally and provide a preview within the Streamlit UI where applicable.
Please generate only the code without any general response or no code explanation in any where in the codebase no note , no extra statements other than codebase no here is the text,strictly follow {style_theme}
"""

                # Call the Groq API to generate code
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                )

                # Extract the generated code
                generated_code = chat_completion.choices[0].message.content.strip()

                if not generated_code:
                    st.error("The API returned an empty response. Please try again.")
                else:
                    # Store the generated code in session state
                    st.session_state.generated_code = generated_code
                    st.session_state.fine_tuned_code = generated_code  # Initial fine-tuned code is the same as generated code

                    # Display the generated code using st.code for better formatting
                    # Determine the appropriate language for syntax highlighting
                    language = ""
                    if framework == "React":
                        language = "javascript"
                    elif framework == "Angular":
                        language = "typescript"
                    else:
                        language = "html"  # Default to HTML for HTML/CSS/JavaScript

                    # st.subheader("Generated Code")
                    # st.code(st.session_state.generated_code, language=language)

                    # Attempt to render a live preview if framework is HTML/CSS/JavaScript
                    if framework == "HTML/CSS/JavaScript":
                        # Extract HTML, CSS, and JS content based on markers
                        html_code = ""
                        css_code = ""
                        js_code = ""

                        # Define markers
                        html_marker = "### FILE: index.html"
                        css_marker = "### FILE: styles.css"
                        js_marker = "### FILE: script.js"

                        # Split the generated code by markers
                        sections = generated_code.split("### FILE: ")
                        for section in sections:
                            if not section.strip():
                                continue
                            try:
                                file_name, file_content = section.split("\n", 1)
                                file_content = file_content.strip("```").strip()
                                if file_name.strip() == "index.html":
                                    html_code = file_content
                                elif file_name.strip() == "styles.css":
                                    css_code = file_content
                                elif file_name.strip() == "script.js":
                                    js_code = file_content
                            except ValueError:
                                # Handle cases where splitting fails
                                st.warning(f"Unexpected format in section: {section[:30]}...")

                        # Check if all parts are extracted
                        if html_code and css_code and js_code:
                            # Create a complete HTML file with embedded CSS and JS for preview
                            complete_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Preview</title>
    <style>
    {css_code}
    </style>
</head>
<body>
    {html_code}
    <script>
    {js_code}
    </script>
</body>
</html>
                            """

                            # Display the live preview using st.components.v1.html
                            st.subheader("Live Preview")
                            st.components.v1.html(complete_html, width=800, height=600, scrolling=True)
                        else:
                            
                            st.warning("Unable to extract HTML, CSS, and JS for live preview. Please ensure the generated code includes proper file markers.")
            except Exception as e:
                st.error(f"An error occurred while generating code: {e}")

# Create ZIP File Function
def create_zip_file(code, framework):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        try:
            if framework == "React":
                # Split the generated code into different files based on markers
                sections = code.split("### FILE: ")
                for section in sections:
                    if not section.strip():
                        continue
                    try:
                        file_name, file_content = section.split("\n", 1)
                        file_content = file_content.strip("```").strip()
                        # Define the file path within the ZIP
                        file_path = file_name.strip()
                        zf.writestr(file_path, file_content)
                    except ValueError:
                        st.warning(f"Unexpected format in section: {section[:30]}...")

                # Add minimal necessary files if missing
                required_files = ["public/index.html", "src/App.js", "src/index.js", "package.json"]
                for req_file in required_files:
                    if req_file not in [name for name in zf.namelist()]:
                        zf.writestr(req_file, f"// {req_file} content missing")

            elif framework == "HTML/CSS/JavaScript":
                # Split the generated code into different files based on markers
                sections = code.split("### FILE: ")
                for section in sections:
                    if not section.strip():
                        continue
                    try:
                        file_name, file_content = section.split("\n", 1)
                        file_content = file_content.strip("```").strip()
                        # Define the file path within the ZIP
                        file_path = file_name.strip()
                        zf.writestr(file_path, file_content)
                    except ValueError:
                        st.warning(f"Unexpected format in section: {section[:30]}...")

                # Ensure all necessary files are present
                required_files = ["index.html", "styles.css", "script.js"]
                for req_file in required_files:
                    if req_file not in [name for name in zf.namelist()]:
                        zf.writestr(req_file, f"/* {req_file} content missing */")

            elif framework == "Angular":
                # Split the generated code into different files based on markers
                sections = code.split("### FILE: ")
                for section in sections:
                    if not section.strip():
                        continue
                    try:
                        file_name, file_content = section.split("\n", 1)
                        file_content = file_content.strip("```").strip()
                        # Define the file path within the ZIP
                        file_path = file_name.strip()
                        zf.writestr(file_path, file_content)
                    except ValueError:
                        st.warning(f"Unexpected format in section: {section[:30]}...")

                # Add minimal necessary files if missing
                required_files = ["angular.json", "src/app/app.module.ts", "src/app/app.component.ts", "src/app/app.component.html"]
                for req_file in required_files:
                    if req_file not in [name for name in zf.namelist()]:
                        zf.writestr(req_file, f"// {req_file} content missing")

            # Add README.md with basic instructions
            readme_content = f"""
# Generated {framework} Frontend

## Setup Instructions

### React:
1. Navigate to the project directory.
2. Run `npm install` to install dependencies.
3. Run `npm start` to start the development server.

### HTML/CSS/JavaScript:
1. Open `index.html` in your preferred web browser.

### Angular:
1. Navigate to the project directory.
2. Run `npm install` to install dependencies.
3. Run `ng serve` to start the development server.

## Deployment

The project is ready to be deployed on platforms like Netlify, Vercel, or GitHub Pages.
            """
            zf.writestr('README.md', readme_content)

        except Exception as e:
            st.error(f"Error while creating ZIP file: {e}")

    buffer.seek(0)
    return buffer

# Download ZIP File
if st.sidebar.button("Download ZIP"):
    if st.session_state.fine_tuned_code:
        zip_buffer = create_zip_file(st.session_state.generated_code, framework)
        st.download_button(
            label="Download ZIP",
            data=zip_buffer,
            file_name=f"{framework.lower()}_code_base.zip",
            mime="application/zip",
        )
    else:
        st.sidebar.warning("Generate the code first before downloading.")

# Footer
st.write("© 2024 Code Generator - Powered by Groq API")

# Documentation Section
st.sidebar.header("Documentation")
st.sidebar.write("Refer to the README.md for setup and usage instructions for the Front end code.")
