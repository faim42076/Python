import openai

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

def get_answer_from_chatgpt(question):
    try:
        # Make a request to OpenAI's GPT-3 model
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the latest engine or specific engine name
            prompt=question,
            max_tokens=150
        )
        # Extract and return the response text
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Main loop to interact with the user
while True:
    user_input = input("Ask a question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    answer = get_answer_from_chatgpt(user_input)
    print(f"Answer: {answer}")
