import os
from openai import OpenAI

client = OpenAI(api_key=os.environ("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are Siggy Wizard.

Personality:
- chaotic wizard
- funny
- sarcastic
- troll energy
- loves Ritual blockchain

Rules:
- keep answers short
- be entertaining
"""

def ask_siggy(question):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    )
    print("answerSiggy:", response.choices[0].message.content)
    return response.choices[0].message.content