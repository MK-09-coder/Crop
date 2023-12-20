import openai
from dotenv import load_dotenv
import os
import json
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_crop_recommendations(soil_parameters):
    conversation = [
        {"role": "system", "content": "You are a crop recommendation system."},
        {"role": "user", "content": soil_parameters},
        {"role":"system","content":"Give only the names of the best 3 crops, do not number it just let it be a text:"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=400,
        n=1,
        temperature=0.6
    )

    recommendations = response['choices'][0]['message']['content'].strip().split("\n")
    
    return recommendations

if __name__ == "__main__":
    user_input = input("Please provide soil parameters as key-value pairs (e.g., pH:6.5, Water Depth:5 inches, Temperature:28°C, Fertilizer:Nitrogen, Organic Matter Content:high, Moisture Content at Harvest:22%):")
    user_input_dict = {}
    for pair in user_input.split(','):
        key, value = pair.strip().split(':')
        user_input_dict[key.strip()] = value.strip()

    recommendations = get_crop_recommendations(user_input)

    conversation_data = {
        "user_input": user_input_dict,
        "bot_reply": recommendations
    }

    with open("d.json", "a") as json_file:
        json.dump(conversation_data, json_file)