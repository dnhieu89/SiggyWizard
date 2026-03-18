import random
from siggy_config import SIGGIES

def create_race():
    return [
        {
            "info": s,
            "progress": 0
        }
        for s in SIGGIES
    ]

def update_race(race):
    for cat in race:
        boost = random.randint(1, 8)

        if random.random() < 0.1:
            boost += 10  # turbo

        cat["progress"] += boost

        if cat["progress"] > 100:
            cat["progress"] = 100

def render_race(race):
    lines = []

    for cat in race:
        bar = "▰" * (cat["progress"] // 10) + "▱" * (10 - cat["progress"] // 10)
        lines.append(
            f"**{cat['info']['id']}. {cat['info']['name']}**\n{bar} {cat['progress']}%"
        )

    return "\n\n".join(lines)