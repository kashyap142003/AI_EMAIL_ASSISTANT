from openai import OpenAI
from config import OPENAI_API_KEY
from prompts import rewrite_prompt

client = OpenAI(api_key=OPENAI_API_KEY, base_url="https://openrouter.ai/api/v1")

def rewrite_email(email_text: str, tone: str = "professional"):
    prompt = rewrite_prompt(email_text, tone)

    response = client.chat.completions.create(
        model='openai/gpt-4o-mini',
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    return response.choices[0].message.content