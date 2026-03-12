# import os
# from openai import OpenAI


# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# SYSTEM_PROMPT = """
# You are Siggy Wizard.

# Personality:
# - chaotic wizard
# - funny
# - sarcastic
# - troll energy
# - loves Ritual blockchain

# Rules:
# - keep answers short
# - be entertaining
# """

# def ask_siggy(question):

#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             {"role": "user", "content": question}
#         ]
#     )
#     print("answerSiggy:", response.choices[0].message.content)
#     return response.choices[0].message.content

import os
import requests

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

def ask_siggy(question):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "nvidia/nemotron-3-super:free",
        "messages": [
            {
                "role": "system",
                "content": "You are Siggy Wizard, a chaotic funny wizard with troll energy."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    r = requests.post(url, headers=headers, json=data)

    result = r.json()

    print("AI RAW RESPONSE:", result)

    if "choices" not in result:
        return "😹 Siggy's magic orb exploded. Try again."

    return result["choices"][0]["message"]["content"]