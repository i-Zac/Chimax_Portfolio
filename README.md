# 🌐 Chimax Portfolio

Welcome to my **Chimax portfolio website**, built with **Flask**, **HTML/CSS**, and **JavaScript** — showcasing my work, resume, and contact form with email automation.

![Screenshot](static/Images/Img-3.jpg)

---

## 🚀 Features

- 🎨 Responsive and modern UI
- 📄 About Me, Services, Resume & Contact sections
- 📬 Contact form with automatic email response
- 🔐 Secure environment using `.env`
- 💾 Submissions saved to `CSV` file

---

## 📁 Project Structure

chimax_portfolio/
│
├── main.py # Flask app entry point
├── database.csv # Stores form submissions
├── templates/ # HTML files
│ ├── index.html
│ ├── about.html
│ ├── contact.html
│ └── ...
├── static/ # CSS, images, and JS
│ ├── style.css
│ └── Images/
├── .env # Environment variables (ignored)
├── .gitignore
├── requirements.txt
└── render.yaml # Render deployment config

---

## ⚙️ Technologies

- Python (Flask)
- HTML5, CSS3, JavaScript
- Git & GitHub
- SMTP for email
- Render for deployment

---

## 📧 Contact Form Features

- Real-time email verification
- Auto-response confirmation to the user
- Stores submissions in CSV for backup

---

## 🚀 Deployment

Hosted on **Render**.

> You can visit the live demo here (add your link):
> **🔗 [Live Portfolio](https://blessingchimax.onrender.com/)**

---

## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://https://github.com/i-Zac/Chimax_Portfolio.git

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py

🛡️ Environment Variables
Store these in .env:
    EMAIL_USER=your_email@example.com
    EMAIL_PASSWORD=your_password
    RECEIVER_EMAIL=your_email@example.com

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

📜 License
feel free to use and customize.
```
