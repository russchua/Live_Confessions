import openai
import os

openai.api_key_path = '.\openai_key'
# openai.api_key = os.getenv("OPENAI_API_KEY")

openai_output = openai.Completion.create(
    model="text-davinci-003",
    prompt='Hello there!',
    temperature=0.6,
)

# print(openai_output.choices[0].text)
print(openai_output)