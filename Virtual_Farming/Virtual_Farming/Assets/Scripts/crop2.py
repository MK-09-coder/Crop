import openai
from dotenv import load_dotenv
load_dotenv()
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_recommendations(soil_parameters, existing_crop):
    conversation = [
        {"role": "system", "content": "You are a helpful assistant that provides recommendations."},
        {"role": "user", "content": f"Given the soil parameters {soil_parameters} and the existing crop {existing_crop}, what actions can I take to improve crop growth?"},
        {"role":"system","content":"Give maximum 5 points as recommendations."}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=500,
        n=1,
        temperature=0.6
    )

    return response.choices[0].message["content"]

if __name__ == "__main__":
    user_input = input("Please provide soil parameters as key-value pairs (e.g., pH:6.5, Water Depth:5 inches, Temperature:28°C, Fertilizer:Nitrogen, Organic Matter Content:high, Moisture Content at Harvest:22%):")
    user_input_dict = {}
    for pair in user_input.split(','):
        key, value = pair.strip().split(':')
        user_input_dict[key.strip()] = value.strip()
    existing_crop=input("Enter the existing Crop:")
    recommendations = get_recommendations(user_input_dict, existing_crop)
    data = {
        "user_input": user_input_dict,
        "existing_crop": existing_crop,
        "recommendations": recommendations
    }
    with open("data.json", "a") as json_file:
        json.dump(data, json_file, indent=4)

