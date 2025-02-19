import json
import requests
import subprocess
import os

OLLAMA_URL = "http://localhost:11434/api/generate"

def send_prompt_to_llm(prompt, model_name="gemma"):
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"model": model_name, "prompt": prompt, "stream": False})

    try:
        response = requests.post(OLLAMA_URL, headers=headers, data=data)
        response.raise_for_status()
        return response.json().get('response', 'No response received')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "Error in LLM response"

def get_changed_files():
    result = subprocess.run(["git", "diff", "--name-only", "HEAD^", "HEAD"], capture_output=True, text=True)
    return result.stdout.strip().split("\n")

if __name__ == "__main__":
    print("Starting AI Code Review...")

    changed_files = get_changed_files()
    cs_files = [file for file in changed_files if file.endswith(".cs")]

    if not cs_files:
        print("No C# files changed, skipping review.")
        exit()

    for file in cs_files:
        print(f"Reviewing {file}...")
        with open(file, 'r') as f:
            code = f.read()

        prompt = f"Review this C# code:\n{code}"
        response = send_prompt_to_llm(prompt)
        print(f"AI Review for {file}:\n{response}\n")
