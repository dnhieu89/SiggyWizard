import discord
from discord.ext import commands
import random
import siggy_data
from siggy_ai import ask_siggy

# ===============================
# BOT CONFIG
# ===============================
import os
from dotenv import load_dotenv

#load_dotenv()
TOKEN = os.environ["DISCORD_TOKEN"]#os.getenv("DISCORD_TOKEN")
print("TOKEN:", TOKEN)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# ===============================
# SIGGY PERSONALITY RESPONSES
# ===============================

siggy_idle_lines = [

"😹 Siggy is floating through the Ritual dimension...",
"🔮 Siggy is studying forbidden Ritual scrolls...",
"🧙 Siggy whispers: Ritual knowledge is powerful magic...",
"🐙 Siggy is calculating decentralized AI spells...",
"✨ Siggy believes Ritual will summon AI agents...",
"😼 Siggy is watching Infernet nodes like a wizard council..."

]

# ===============================
# BOT EVENTS
# ===============================

@bot.event
async def on_ready():
    print("===================================")
    print(f"Siggy Bot is ONLINE as {bot.user}")
    print("Ritual knowledge database loaded.")
    print("===================================")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("😹 Siggy got confused. Try `!help`")
#===============================
# SIGGY BATTLE
#===============================

@bot.command()
async def ritualbattle(ctx):

    player_hp = 100
    ai_hp = 100

    ai_agents = [
            
        "Siggy Wizard",
    ]

    ai = random.choice(ai_agents)

    player_attacks = [
        "throws a rubber chicken at the enemy",
"bonks the enemy with a frying pan",
"throws a loaf of bread like a ninja star",
"hits the enemy with a giant pillow",
"throws a slipper with perfect accuracy",
"smacks the enemy with a rolled newspaper",
"launches a flying sandwich attack",
"throws a bucket of water dramatically",
"bonks the enemy with a broom",
"throws a banana peel hoping they slip",
"hits the enemy with a cooking pot",
"throws a random chair across the room",
"smacks the enemy with a giant teddy bear",
"throws a plate of spaghetti everywhere",
"bonks the enemy with a watermelon"
    ]

    ai_attacks = [
        "throws a rubber chicken at the enemy",
"bonks the enemy with a frying pan",
"throws a loaf of bread like a ninja star",
"hits the enemy with a giant pillow",
"throws a slipper with perfect accuracy",
"smacks the enemy with a rolled newspaper",
"launches a flying sandwich attack",
"throws a bucket of water dramatically",
"bonks the enemy with a broom",
"throws a banana peel hoping they slip",
"hits the enemy with a cooking pot",
"throws a random chair across the room",
"smacks the enemy with a giant teddy bear",
"throws a plate of spaghetti everywhere",
"bonks the enemy with a watermelon"
    ]

    siggy_comments = [
        "😹 Siggy can't stop laughing.",
"🍿 Siggy grabs popcorn.",
"🐱 Siggy wonders why this fight is so chaotic.",
"😼 Siggy nods like this makes perfect sense.",
"🐙 Siggy writes this down as a historical battle.",
"😹 Siggy thinks the rubber chicken was a strong move.",
"🧙 Siggy pretends to understand the strategy.",
"🐱 Siggy is slightly concerned about the furniture.",
"🍿 Siggy enjoys the chaos.",
"😼 Siggy declares this a legendary fight."
    ]

    battle_log = []
    battle_log.append("⚔️ **RITUAL AI BATTLE INITIATED**")
    battle_log.append(f"{ctx.author.name} vs **{ai}**")
    battle_log.append("")

    round_num = 1

    while player_hp > 0 and ai_hp > 0 and round_num <= 5:

        player_dmg = random.randint(10, 20)
        ai_dmg = random.randint(8, 18)

        ai_hp -= player_dmg
        player_hp -= ai_dmg

        player_action = random.choice(player_attacks)
        ai_action = random.choice(ai_attacks)

        battle_log.append(
            f"🔹 **Round {round_num}**\n"
            f"{ctx.author.name} {player_action} dealing **{player_dmg} dmg**\n"
            f"{ai} {ai_action} dealing **{ai_dmg} dmg**\n"
            f"HP → {ctx.author.name}: {max(player_hp,0)} | {ai}: {max(ai_hp,0)}"
        )

        if random.random() < 0.5:
            battle_log.append(random.choice(siggy_comments))

        battle_log.append("")
        round_num += 1

    if player_hp > ai_hp:
        battle_log.append(f"🏆 **{ctx.author.name} defeated the {ai}!**")
        battle_log.append("😹 Siggy declares you a Ritual AI warrior.")
    else:
        battle_log.append(f"💀 **{ai} defeated {ctx.author.name}!**")
        battle_log.append("🔮 Siggy says the Ritual AI grows stronger today.")

    await ctx.send("\n".join(battle_log))

# ===============================
# BASIC COMMANDS
# ===============================

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Siggy ping magic works!")

@bot.command()
async def siggytalk(ctx):
    await ctx.send(random.choice(siggy_idle_lines))

# ===============================
# HELP COMMAND
# ===============================

@bot.command()
async def help(ctx):

    help_text = """
🐱 **Siggy Bot Command Guide**

🔮 **Ritual Knowledge**
`!ritual explain`
→ Siggy explains what Ritual is.

`!ritual roadmap`
→ Siggy reveals the Ritual roadmap.

⚔️ **Mini Games**
`!ritualbattle`
→ Battle a random AI agent in a chaotic fight.

🎲 **Fun Commands**
`!siggycoin heads/tails`
→ Flip a coin with Siggy.

🔮 **Siggy Fun**
`!ask [question]`
→ Ask Siggy anything and receive a response from the AI agent..


ℹ️ **Help**
`!help`
→ Show this command list.

😹 Siggy hopes you survive the battle.
"""

    await ctx.send(help_text)

# ===============================
# RITUAL COMMAND
# ===============================

@bot.command()
async def ritual(ctx, arg=None):

    if arg == "explain":

        response = siggy_data.get_random("ritual_explain")
        await ctx.send(response)

    elif arg == "roadmap":

        response = siggy_data.get_random("ritual_roadmap")
        await ctx.send(response)

    else:

        await ctx.send(
            "🔮 Siggy says:\n"
            "`!ritual explain` — learn about Ritual\n"
            "`!ritual roadmap` — see Ritual future plans"
        )

# ===============================
# FUN SIGGY RANDOM RESPONSES
# ===============================
@bot.command()
async def siggycoin(ctx, guess=None):

    if guess not in ["heads", "tails"]:
        await ctx.send("😹 Guess `heads` or `tails`!\nExample: `!siggycoin heads`")
        return

    import random
    result = random.choice(["heads", "tails"])

    if guess == result:
        await ctx.send(f"🪙 Coin landed on **{result}** — Siggy blesses you with luck!")
    else:
        await ctx.send(f"🪙 Coin landed on **{result}** — Siggy laughs at your prediction 😹")

@bot.command()
async def prophecy(ctx):

    prophecies = [

        "🔮 Siggy prophecy: Ritual will summon thousands of AI agents.",
        "🧙 Siggy prophecy: Ritual may become the intelligence layer of Web3.",
        "🐙 Siggy prophecy: Infernet nodes will power decentralized AI.",
        "😹 Siggy prophecy: one day Ritual bots will outsmart traders.",
        "✨ Siggy prophecy: Ritual builders will unlock strange AI magic."

    ]

    await ctx.send(random.choice(prophecies))


# ===============================
#  SIGGY AI AGENT RESPONSES
# =============================== 


@bot.command()
async def ask(ctx, *, question):

    await ctx.send("🔮 Siggy is thinking...")

    try:
        answer = ask_siggy(question)
        await ctx.send(answer)

    except Exception as e:
        print("AI ERROR:", e)
        await ctx.send("😹 Siggy got confused. Try again!")

# ===============================
# BOT START
# ===============================

bot.run(TOKEN)