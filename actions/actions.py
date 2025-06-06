import openai

def ask_gpt(prompt):
    openai.api_key = "your-api-key"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
