from config import client, model, temperature, max_tokens
from prompts import system_prompt
from examples import examples

# Appends messages to build a conversation history for multi-shot prompting
def build_messages(user_input: str):
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(examples)
    messages.append({"role": "user", "content": user_input})
    return messages

# Gets the response from the OpenAI API based on the user input and conversation history
def get_response(user_input: str) -> str:
    messages = build_messages(user_input)

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content