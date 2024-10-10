from openai import OpenAI
client = OpenAI(
     api_key = "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",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Vou viajar para Londres em novembro de2024. Quero que faça um roteiro de viagem para mim"
        }
    ]
)

print(completion.choices[0].message.content)
# print(completion)

