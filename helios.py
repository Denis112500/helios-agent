import os
from litellm import completion

user_messages=[
{"role": "system", "content": "You are Helios, a helpful assistant."},
]

while True:
    user_input = input ("You: ")
    user_messages.append({"role": "user", "content": user_input})

    response = completion(
        model="openai/gpt-4.1",
        api_base="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"],
        messages=user_messages
    )

    reply = response.choices[0].message.content
    user_messages.append({"role": "assistant", "content": reply})
    print ("Helios: " + reply)
