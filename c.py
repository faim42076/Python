import openai


openai.api_key = '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'

def get_answer_from_chatgpt(question):
    try:
        
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=question,
            max_tokens=150
        )
        
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"


while True:
    user_input = input("Ask a question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    answer = get_answer_from_chatgpt(user_input)
    print(f"Answer: {answer}")
