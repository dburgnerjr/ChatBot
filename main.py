from openai import OpenAI
client = OpenAI()

client.api_key = "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"

def chat_with_gpt(prompt):
    response = client.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content().strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)

