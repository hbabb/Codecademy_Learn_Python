# Flask Mini-Projects Collection

A collection of interactive Python Flask mini-projects from Codecademy, deployed on Vercel. This repository showcases how to convert simple Python console programs into interactive web applications using Flask.

![Flask Logo](https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png)

## 📋 Project Overview

This project demonstrates how to:
- Convert Python console programs into web applications
- Structure a Flask application with multiple routes
- Implement a clean, responsive design with CSS
- Deploy a Flask application to Vercel's serverless platform

## 🚀 Live Demo

[View the live application](https://your-vercel-app-url.vercel.app) 
*Update this link after deployment*

## 🧩 Included Projects

### 1. Magic 8 Ball
Ask the Magic 8 Ball any question and receive a mystical answer. This project demonstrates:
- Form handling with Flask
- Random response generation
- Stylized UI with animations

### 2. Sal's Shipping Calculator
Calculate and compare shipping costs across different shipping methods. This project showcases:
- Form validation
- Cost calculations based on weight
- Comparison displays
- Highlighting the recommended option

## 🛠️ Project Structure

```
FlaskProject/
├── api/
│   └── index.py          # Main Flask application with routes
├── scripts/
│   ├── magic8ball.py     # Magic 8 Ball logic
│   └── shipping.py       # Shipping calculator logic
├── static/
│   └── css/
│       ├── main.css      # Shared styles
│       ├── magic8ball.css # Magic 8 Ball specific styles
│       └── shipping.css  # Shipping calculator specific styles
├── templates/
│   ├── home.html         # Home page template
│   ├── magic8ball.html   # Magic 8 Ball template
│   └── shipping.html     # Shipping calculator template
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel configuration
└── README.md             # Project documentation
```
## 🔧 Technologies Used

- **Python**: Core programming language
- **Flask**: Web framework
- **HTML/CSS**: Frontend structure and styling
- **Vercel**: Serverless deployment platform

## 💻 Local Development

1. Clone the repository:
    ```bash
    git clone https://github.com/hbabb/Codecademy_Learn_Python.git 
    cd Codecademy_Learn_Python
    ```
2. Create and activate a virtual environment:
    ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
   ```bash
   pip install -r requirements
   ```
4. Run the development server:
   ```bash
   python -m flask --app api/index run --debug
   ```
5. Visit `http://127.0.0.1:5000` in your browser

## 📤 Deployment

This project is set up for easy deployment to Vercel:

1. Push your code to GitHub
2. Connect your GitHub repository to Vercel
3. Configure the build settings to use the Python runtime
4. Deploy!

## 📝 Original Codecademy Projects

These web applications are based on the following Codecademy Python projects:
- [Magic 8 Ball](https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/modules/cspath-python-control-flow/projects/python-magic-8-ball)
- [Sal's Shipping](https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/modules/cspath-python-control-flow/projects/python-sals-shipping)

## 📜 License

This project is created for educational purposes and is available under the MIT License.

## 👤 Author

Your Name
- GitHub: [@hbabb](https://github.com/hbabb)
- LinkedIn: [Heath Babb](https://linkedin.com/in/heath-babb)
- X: [Heath](https://x.com/heath2420)

---

*Created as part of Codecademy's Python Course, 2025*