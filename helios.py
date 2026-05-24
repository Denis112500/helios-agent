import os
from litellm import completion

response = completion(
    model="openai/gpt-4.1",
    api_base="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
    messages=[
        {"role": "system", "content": "Say hello and tell me what model you are."},
    ]
)

print (response.choices[0].message.content)