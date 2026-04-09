# Flask-Login-System-with-Image-CAPTCHA

A simple and secure **Python Flask** web application demonstrating **user registration, login, and image-based CAPTCHA verification**. Ideal for beginners and intermediate developers to learn Flask, session management, and web app security.

## 🔹 Features
- User Registration & Login System  
- Interactive Image-based CAPTCHA for bot prevention  
- Session management using Flask  
- Dynamic CAPTCHA categories: Car, Bike, Bus, Zebra, Traffic  
- Responsive interface using HTML & CSS  
- File-based user storage (`users.txt`)

## 🔹 Project Structure

project/
│
├── app.py
├── users.txt
├── templates/
│ ├── index.html # Login page
│ ├── register.html # Registration page
│ ├── captcha.html # CAPTCHA page
│ └── result.html # Result page
├── static/
│ ├── style.css
│ └── images/
│ ├── car1.png ... car3.png
│ ├── bike1.png ... bike3.png
│ ├── bus1.png ... bus3.png
│ ├── zebra1.png ... zebra3.png
│ └── traffic1.png ... traffic3.png


## 🔹 How It Works
1. **User Registration/Login:** Users create an account or login with existing credentials.  
2. **CAPTCHA Verification:** After login, a 9-image CAPTCHA grid appears. Users select all images matching the specified category.  
3. **Access Control:** Correct selection grants access; wrong selection prompts a retry.

## 🔹 Technologies Used
- Python 3  
- Flask Framework  
- HTML, CSS (Bootstrap optional)  
- File-based user storage (`users.txt`)  
- Randomized image CAPTCHA

## 🔹 How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/akinnovationhub3-star/Flask-Login-System-with-Image-CAPTCHA.git

Navigate to the project folder:

cd <project-folder>

Install Flask: pip install flask

Run the app: python app.py

Open your browser and visit: http://127.0.0.1:5000/

Open your browser and visit:

http://127.0.0.1:5000/
