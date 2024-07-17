from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def ask_openai(question):
    response = client.chat.completions.create(model="gpt-4o",
    messages=messages
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Welcome to the OpenAI API Assistant! Type 'exit' to quit.")
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    while True:
        user_input = input("Vous: ")
        if user_input.lower() == 'exit':
            break
        # Ajouter le message de l'utilisateur à l'historique
        messages.append({"role": "user", "content": user_input})
        # Obtenir la réponse de l'assistant
        assistant_response = ask_openai(messages)
        # Ajouter la réponse de l'assistant à l'historique
        messages.append({"role": "assistant", "content": assistant_response})
        print(f"Assistant: {assistant_response}")