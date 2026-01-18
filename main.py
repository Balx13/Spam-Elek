# Spam Elek

import discord
import asyncio
import random
import os

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN nincs beállítva!")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# A hülye üzenetek listája
messages = [
    "Ébresztő! A macskák át akarják venni a hatalmat!",
    "Pizzaaa… valaki rendelt pizzát?",
    "Ki hagyta nyitva a kávéfőzőt??",
    "Vigyázat! Meme robbanás közeleg!",
    "Hurrá, péntek van! 🎉",
    "A számítógépem azt mondta, kell egy szünet… én is egyetértek.",
    "Random tény: a banán egy bogyó. 🍌",
    "Mindenki menjen el meditálni… vagy csak igyon kávét.",
    "Valaki látta a WiFi-jelünket elveszni?",
    "Figyelem! Képzeletbeli ninja támadás!",
    "Csirke vagy tojás? 💭",
    "Az univerzum ma reggel kávé nélkül indult… baj lesz!",
    "Ki nevet a végén? Remélhetőleg nem én…",
    "Sütőtök szezon van, mindenki vigyázzon a lábára!",
    "Riasztás! Meme invázió a csatornán!",
    "Random üzenet, csak hogy feldobjam a napod!",
    "Állati jó hír: a macskák még mindig aranyosak!",
    "Hurrá, valaki hozott kekszet!",
    "Ki akar csatlakozni a táncforradalomhoz? 💃🕺",
    "Spam incoming… de legalább vicces spam!",
    "Képzeld el, hogy egy unikornis táncol az irodádban. 🦄",
    "Valaki hallotta az éjfél harangját? Vagy csak a szomszédok dobolnak?",
    "Random tény: a polipnak három szíve van. 🐙",
    "Csapjunk bele a napba egy kis energiával!",
    "Ne feledd: mindenki szeret egy jó viccet!",
    "A múltkor a bot azt mondta… de aztán elfelejtette.",
    "Figyelem, új meme érkezik!",
    "Szerintem a kávé ma is a hősünk.",
    "Veszély! Túl sok cukor a csatornában!",
    "Ha olvasod ezt, mosolyogj! 🙂",
    "Random spam, de legalább barátságos spam!",
    "Ki hozta a pizzát? Mert én éhes vagyok.",
    "Ma reggel minden macska aranyosabb volt a szokásosnál.",
    "Hurrá, hétvége közeleg! 🎉",
    "A napom tele volt vicces hibákkal… és számítógépes bugokkal.",
    "Random üzenet, csak hogy feldobjam a hangulatot.",
    "Képzeld el, hogy a kanapé beszél hozzád. 😲",
    "Valaki rendelt nevetést? 😂",
    "Az univerzum üzenetet küldött: egyél süteményt!",
    "Spam alert! De legalább aranyos spam!",
    "Random spam, random öröm!",
    "Ha olvasod ezt, köszönöm, hogy itt vagy!",
    "A macskám most pont az asztalon táncol…",
    "Vigyázat! Meme vihar közeleg!",
    "Random érdekesség: a flamingók rózsaszínűek a kajájuk miatt.",
    "Képzelj el egy táncoló robotot. Igen, most pont így érzem magam.",
    "Hurrá! Valaki hozott csokit! 🍫",
    "Ma minden vicc 10/10-esre sikerült!",
    "Random spam, random mosoly! 😎",
    "Figyelem! Vicces üzenet a csatornában!",
    "Ha a pizza kör alakú, akkor miért csomagoljuk négyzet alakú dobozba és vágjuk háromszögekre?",
    "| SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM | SPAM |",
    "Írj 500 000 🎮 emojit, hogyha azt akarod, hogy hagyjam abba a semelést!(UI: SOHA sem fogom abbahagyni a spamelést!)"
]

async def send_random_messages():
    await client.wait_until_ready()
    cannel_id = os.getenv("CHANNEL_ID")
    if not channel_id:
        raise RuntimeError("CHANNEL_ID nincs beállítva!")
    channel_id = int(channel_id)
    channel = client.get_channel(channel_id)
    while not client.is_closed():
        await asyncio.sleep(random.randint(1200, 3600))
        await channel.send(random.choice(messages))

@client.event
async def on_ready():
    print(f'Bejelentkezve: {client.user}')
    client.loop.create_task(send_random_messages())
    
@client.event
async def on_message(message):
    # Ne reagáljon saját magára
    if message.author == client.user:
        return

    # Ha megjelölik a botot (@Spam Elek)
    if client.user in message.mentions:
        await message.channel.send(random.choice(messages))

while True:
    try:
        client.run(TOKEN)
    except:

        continue
