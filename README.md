# 🦾 T-800 Fitness Coach

**T-800 Fitness Coach** is an AI-powered web application that offers personalized fitness and nutrition advice through an interactive chat interface. Built with **Flask** and **Vanilla JS**, it uses the **Mistral-7B Instruct** model to provide smart, tailored responses to user queries.

---

## 🎯 Key Features

- 🏋️ Customized workout plans based on age, fitness level, and goals
- 🥗 Diet suggestions aligned with regional and dietary preferences
- 💬 Real-time AI chat interface with conversation memory
- 🎨 Modern, responsive UI with smooth interaction flow
- 🧠 Structured output with formatting for readability

---

## 🧠 About the Model

This project integrates the **Mistral-7B Instruct v0.2** model—an open-weight, instruction-tuned large language model known for fast inference and strong reasoning capabilities. It powers the chat backend and handles user goals like:

- Workout programming
- Nutrition recommendations
- Health and fitness Q&A
- Friendly motivation and advice

---

## 🛠️ Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| Frontend     | HTML, CSS, JavaScript |
| Backend      | Python (Flask)    |
| AI Model     | Mistral-7B Instruct |
| API Handling | `requests` module |

---

## 📁 Project Structure

t800-fitness-coach/
├── app.py # Flask backend with /chat API
├── index.html # Frontend UI
├── static/
│ └── t-800.jpg # Avatar used in chat interface


---

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/t800-fitness-coach.git
cd t800-fitness-coach
```
### 2. Install Dependencies
```bash
pip install flask requests
```
### 3.Run the Application
```bash
python app.py
```
