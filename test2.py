from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def ask_llm(prompt):
    try:
        response = client.chat.completions.create(
            model='openai/gpt-4o-mini',
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"API Error: {str(e)}"
    
prompt = input("Enter your prompt: ")
answer = ask_llm(prompt)
print(answer)
