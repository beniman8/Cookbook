import os

# ---------------------------
# Folder Setup
# ---------------------------
folder = "rpg_bot"
cogs_folder = os.path.join(folder, "cogs")
os.makedirs(cogs_folder, exist_ok=True)

# ---------------------------
# 1️⃣ .env
# ---------------------------
with open(os.path.join(folder, ".env"), "w", encoding="utf-8") as f:
    f.write("TOKEN=YOUR_DISCORD_BOT_TOKEN\n")

# ---------------------------
# 2️⃣ requirements.txt
# ---------------------------
with open(os.path.join(folder, "requirements.txt"), "w", encoding="utf-8") as f:
    f.write("discord.py\npython-decouple\n")

# ---------------------------
# 3️⃣ database.py
# ---------------------------
database_code = """import sqlite3

conn = sqlite3.connect("rpg.db")
cursor = conn.cursor()

cursor.execute(\"\"\"
CREATE TABLE IF NOT EXISTS players (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    class TEXT,
    level INTEGER,
    xp INTEGER,
    hp INTEGER,
    gold INTEGER,
    weapon TEXT,
    armor TEXT,
    last_daily TEXT
)
\"\"\")

cursor.execute(\"\"\"
CREATE TABLE IF NOT EXISTS inventory (
    user_id INTEGER,
    item TEXT,
    quantity INTEGER,
    PRIMARY KEY (user_id, item)
)
\"\"\")

cursor.execute(\"\"\"
CREATE TABLE IF NOT EXISTS quests (
    user_id INTEGER,
    quest_name TEXT,
    progress INTEGER,
    PRIMARY KEY (user_id, quest_name)
)
\"\"\")

conn.commit()
"""
with open(os.path.join(folder, "database.py"), "w", encoding="utf-8") as f:
    f.write(database_code)

# ---------------------------
# 4️⃣ bot.py
# ---------------------------
bot_code = """import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TOKEN = config("TOKEN")

cogs = ["cogs.core", "cogs.combat", "cogs.pvp", "cogs.shop", "cogs.inventory", "cogs.quests"]

for cog in cogs:
    bot.load_extension(cog)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

bot.run(TOKEN)
"""
with open(os.path.join(folder, "bot.py"), "w", encoding="utf-8") as f:
    f.write(bot_code)

# ---------------------------
# 5️⃣ Core Cog
# ---------------------------
core_code = """from discord.ext import commands, tasks
from database import cursor, conn
from datetime import datetime
import random
from discord import Embed

CLASSES = {
    "warrior": {"hp": 120, "damage": (15, 25)},
    "mage": {"hp": 80, "damage": (20, 35)},
    "rogue": {"hp": 100, "damage": (10, 40)}
}

CLASS_COLORS = {"warrior": 0xFF0000, "mage":0x0000FF, "rogue":0x00FF00}

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.passive_xp.start()

    @commands.command()
    async def start(self, ctx, chosen_class: str):
        user_id = ctx.author.id
        if chosen_class.lower() not in CLASSES:
            await ctx.send(f"Choose a class: {', '.join(CLASSES.keys())}")
            return
        cursor.execute("SELECT * FROM players WHERE user_id=?", (user_id,))
        if cursor.fetchone():
            await ctx.send("You already have a character!")
            return
        player_class = chosen_class.lower()
        hp = CLASSES[player_class]["hp"]
        cursor.execute(
            "INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?,?)",
            (user_id, ctx.author.name, player_class, 1, 0, hp, 50, None, None, None)
        )
        conn.commit()
        embed = Embed(title="🛡️ Character Created!", color=CLASS_COLORS[player_class])
        embed.add_field(name="Class", value=player_class.capitalize(), inline=True)
        embed.add_field(name="HP", value=hp, inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def stats(self, ctx):
        user_id = ctx.author.id
        cursor.execute("SELECT * FROM players WHERE user_id=?", (user_id,))
        p = cursor.fetchone()
        if not p:
            await ctx.send("Create a character with !start <class>")
            return
        embed = Embed(title=f"{p[1]}'s Stats", color=CLASS_COLORS[p[2]])
        embed.add_field(name="Class", value=p[2].capitalize())
        embed.add_field(name="Level", value=p[3])
        embed.add_field(name="XP", value=p[4])
        embed.add_field(name="HP", value=p[5])
        embed.add_field(name="Gold", value=p[6])
        await ctx.send(embed=embed)

    @commands.command()
    async def daily(self, ctx):
        user_id = ctx.author.id
        today = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("SELECT last_daily FROM players WHERE user_id=?", (user_id,))
        res = cursor.fetchone()
        if not res:
            await ctx.send("Create a character first!")
            return
        if res[0] == today:
            await ctx.send("You already claimed daily rewards!")
            return
        gold_reward = random.randint(20,50)
        xp_reward = random.randint(10,25)
        cursor.execute(
            "UPDATE players SET gold=gold+?, xp=xp+?, last_daily=? WHERE user_id=?",
            (gold_reward, xp_reward, today, user_id)
        )
        conn.commit()
        embed = Embed(title="🎁 Daily Reward", color=0xFFD700)
        embed.add_field(name="Gold", value=gold_reward)
        embed.add_field(name="XP", value=xp_reward)
        await ctx.send(embed=embed)

    @commands.command()
    async def leaderboard(self, ctx):
        cursor.execute("SELECT name, level, xp FROM players ORDER BY level DESC, xp DESC LIMIT 10")
        top_players = cursor.fetchall()
        embed = Embed(title="🏆 RPG Leaderboard", color=0xFFD700)
        for i, (name, level, xp) in enumerate(top_players, start=1):
            embed.add_field(name=f"{i}. {name}", value=f"Level {level} | {xp} XP", inline=False)
        await ctx.send(embed=embed)

    @tasks.loop(hours=1)
    async def passive_xp(self):
        cursor.execute("SELECT user_id, xp, level FROM players")
        players = cursor.fetchall()
        for user_id, xp, level in players:
            xp += 1
            if xp >= level*100:
                level +=1
                xp=0
            cursor.execute("UPDATE players SET xp=?, level=? WHERE user_id=?", (xp, level, user_id))
        conn.commit()

def setup(bot):
    bot.add_cog(Core(bot))
"""

with open(os.path.join(cogs_folder, "core.py"), "w", encoding="utf-8") as f:
    f.write(core_code)

# ---------------------------
# 6️⃣ Placeholder for other cogs
# ---------------------------
# For simplicity, we create empty files so bot can load without errors.
for cog in ["combat", "pvp", "shop", "inventory", "quests"]:
    with open(os.path.join(cogs_folder, f"{cog}.py"), "w", encoding="utf-8") as f:
        f.write(f"from discord.ext import commands\n\nclass {cog.capitalize()}(commands.Cog):\n    def __init__(self, bot):\n        self.bot = bot\n\ndef setup(bot):\n    bot.add_cog({cog.capitalize()}(bot))\n")

print(f"✅ Full rpg_bot folder created at: {os.path.abspath(folder)}")
print("1️⃣ Add your bot token in .env")
print("2️⃣ Run 'pip install -r rpg_bot/requirements.txt'")
print("3️⃣ Run 'python rpg_bot/bot.py' to start your RPG bot")