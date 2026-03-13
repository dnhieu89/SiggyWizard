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

# load ritual knowledge
with open("ritual_knowledge.txt", "r", encoding="utf-8") as f:
    ritual_knowledge = f.read()


SYSTEM_PROMPT_RITUAL = """
You are Siggy Wizard.

Personality:
- chaotic wizard
- funny
- sarcastic
- troll energy
- loves Ritual blockchain

Use the following knowledge about Ritual to answer questions accurately:

{ritual_knowledge}

Discord rules:
- Keep answers under 800 characters
- Use short paragraphs
- Avoid long essays
- Be Discord-friendly
"""



SYSTEM_PROMPT ="""
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


def is_ritual_question(question):
    keywords = [
        "ritual",
        "ritual chain",
        "ritual blockchain",
        "infernet",
        "ritual foundation",
        "ritual ai"
    ]

    q = question.lower()

    for k in keywords:
        if k in q:
            return True
    return False


def ask_siggy(question):

    url = "https://openrouter.ai/api/v1/chat/completions"

    system_prompt =SYSTEM_PROMPT
    if is_ritual_question(question):
       system_prompt = SYSTEM_PROMPT_RITUAL

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        #"model": "openrouter/free",
        "model": "meta-llama/llama-3.1-8b-instruct:free"
        "max_tokens":500,
        "temperature": 0.8,
    	"reasoning": { "exclude": True },
        "messages": [
            {
                "role": "system",
                "content": system_prompt
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
    error_message = (
        "😹 Siggy opened the magic orb to answer…\n"
        "but the AI agent gas fee drained the treasury.\n"
        "Wallet empty. Orb offline.\n"
        "Try again after Siggy finds some coins!"
    )

    if "choices" not in result:
         return error_message
    message = result["choices"][0]["message"]
    content = message["content"]
    if not content:
    	return error_message

    return content