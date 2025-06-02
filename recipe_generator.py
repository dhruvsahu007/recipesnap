from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_recipe(ingredients):
    prompt = f"""
You are a helpful cooking assistant. Given these ingredients: {', '.join(ingredients)}, suggest a simple recipe with ingredients and steps.

Format:
Title:
Ingredients:
Steps:
"""

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful cooking assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error from OpenAI: {str(e)}"
