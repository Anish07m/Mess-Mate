MessMate - Full Stack Mess Management System 🍽️
This is a full-stack web application developed using Flask (Backend) and HTML/CSS/Bootstrap (Frontend).

Features
📋 Menu Display

✍️ Feedback and Complaints

🔒 Admin Management

🌟 Stylish UI

📈 Toast Notifications

🎨 Hover Effects

Tech Stack
*Python (Flask)

HTML5 / CSS3

Bootstrap 5

JavaScript

Jinja2 Template Engine

Git and GitHub

How to Run:
# Clone the repository
git clone https://github.com/Anish07m/Mess-Mate.git

# Navigate to the project folder
cd Mess-Mate

# (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate # For Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python run.py
Then open your browser and go to:
http://127.0.0.1:5000

📁 Project Structure:
messmate/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py          
│   │   ├── models.py           
│   │   ├── forms.py            
│   │   ├── utils.py           
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css       
│   │   │   ├── admin.css        
│   │   ├── js/
│   │   │   ├── main.js          
│   │   ├── images/
│   │   │   ├── avatar.png       
│   │   │   ├── logo.png         
│   │
│   ├── templates/
│   │   ├── layout.html          
│   │   ├── index.html           
│   │   ├── feedback.html       
│   │   ├── menu.html            
│   │   ├── complaints.html      
│   │   └── admin_dashboard.html 
│   │
│   ├── config.py              
│   ├── run.py                 
│   └── requirements.txt       
│
└── README.md                   
