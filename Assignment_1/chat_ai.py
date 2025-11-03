import openai

# Replace with your actual API key from OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"

def chat_ai():
    print("Welcome to your personal AI assistant! (type 'quit' to exit)\n")

    messages = [
        {"role": "system", "content": "You are a helpful and friendly personal assistant."}
    ]

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == 'quit':
            print("AI: Goodbye! 👋")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Or gpt-4 if you have access
                messages=messages
            )

            ai_reply = response['choices'][0]['message']['content'].strip()
            print(f"AI: {ai_reply}\n")

            messages.append({"role": "assistant", "content": ai_reply})

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_ai()
