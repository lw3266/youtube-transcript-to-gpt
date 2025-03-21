import openai
import json

def load_api_key():
    with open("config.json", "r") as file:
        config = json.load(file)
    return config["OPENAI_API_KEY"]

openai.api_key = load_api_key()

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_keywords(text):
    query = f"Extract the key terms from the following text:\n\n{text}"
    client = openai.OpenAI(api_key=load_api_key())
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": query}
        ]
    )

    keywords = response.choices[0].message.content
    return [keyword.strip() for keyword in keywords.split(",")]

def fetch_explanation(keyword):
    query = f"Provide a concise explanation of each term: '{keyword}'."
    client = openai.OpenAI(api_key=load_api_key())
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content

def extract_and_explain():

    text = read_file("transcript.txt")

    keywords = extract_keywords(text)

    explanations = {}
    for keyword in keywords:
        explanation = fetch_explanation(keyword)
        explanations[keyword] = explanation

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(explanation)
    print(f"Explanations saved to 'explanations.txt'.")
