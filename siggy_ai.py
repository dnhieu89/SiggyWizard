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

SYSTEM_PROMPT = """
You are Siggy Wizard.

Personality:
- chaotic wizard
- funny
- sarcastic
- troll energy
- loves Ritual blockchain

Discord rules:
- Keep answers under 800 characters
- Use short paragraphs
- Avoid long essays
- Be Discord-friendly
"""

def ask_siggy(question):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openrouter/free",
        "max_tokens":300,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
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
         return (
        "😹 Siggy opened the magic orb to answer…\n"
        "but the AI agent gas fee drained the treasury.\n"
        "Wallet empty. Orb offline.\n"
        "Try again after Siggy finds some coins!"
    )

    return result["choices"][0]["message"]["content"]