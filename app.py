import requests
import gradio as gd
import json

url="http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

history =[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "prompt": final_prompt,
        "model": "codeguru",
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        final_response = data["response"]
        return final_response
    else:
        print("Error:", response.text)

interface = gd.Interface(
    fn=generate_response,
    inputs=gd.Textbox(lines=4, placeholder="Enter your prompt here..."),
    outputs="text"
    )

interface.launch()