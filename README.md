# 📸 RecipeSnap – AI Cooking Assistant

Snap a picture of your fridge or ingredients and get a suggested recipe using AI!

---

## Features

- Upload an image of your fridge or ingredients.
- Detects ingredients from the image using object detection.
- Generates a recipe based on detected ingredients using OpenAI's GPT API.
- User-friendly Streamlit interface.

---

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Install dependencies from `requirements.txt`

### Installation
Clone the repository:

```bash
git clone https://github.com/dhruvsahu007/recipesnap.git
cd recipesnap
```
Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```
Create a config.py file in the project root containing your OpenAI API key:
```bash
OPENAI_API_KEY = "your_openai_api_key_here"
```
Usage
Run the Streamlit app:
```bash
streamlit run app.py
```
Open the provided local URL in your browser. Upload a picture of your ingredients and get recipe suggestions!
