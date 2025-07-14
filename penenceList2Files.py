import os

penances = [
    "Light a candle, sit in silence for 3 minutes, and practice saying “I’m listening” 12 times.",
    "Bake, buy, or summon a treat for the person you have wronged, and serve it with dramatic flair.",
    "Confess a lie aloud to a houseplant. Promise the plant you’ll do better. Water it. If it perks up, you are absolved. If not, come back here to confess your sin again.",
    "Take a 10-minute walk where you must notice and praise 5 things that are smaller or slower than you. Speak their virtues aloud.",
    "Delete your last Instagram post, then listen to 1 full song that’s either gospel, lo-fi, or Enya. No multitasking. Just vibe and reflect.",
    "Write a haiku about personal responsibility. Recite it while bowing three times to a photo of a noble chicken.",
    "Clean one surface in your living space mindfully while repeating the mantra: “Clarity in word, peace in tone, crumbs of bitterness be gone.”",
    "Give 15 uninterrupted minutes to someone who needs your presence—even if it's just a call, a visit, or listening without checking your phone once.",
    "Take a bath (or shower) by candlelight while reciting an improvised prayer of gratitude to soap, hot water, and the miracle of plumbing.",
    "Make a meal that celebrates simplicity (3 ingredients max). Offer the first bite to an imaginary kitchen saint.",
    "Spend one evening tech-free, light a candle at dusk, and write a “dream offering” in your journal before bed.",
    "Sleep with socks off, in penitent vulnerability.",
    "Drink only herbal tea for a day. When you feel the urge to drink something else, chant “I am dust and dandelion” three times.",
    "Prepare a \"Feast of Intentions\"—a beautifully plated meal where you bless each item aloud before eating. Eat in silence, like a slightly pretentious monk.",
    "Take a midday nap on the floor with a blanket and a soft playlist. Call it “horizontal meditation.” Bonus points if you use a robe or towel as a blanket.",
    "Drink a full glass of water while staring at a houseplant. Say, “We both require moisture to bloom.” Then hum a tune in its honor.",
    "Brush your teeth while reciting three compliments to your own mouth (e.g., “You sing without fear. You speak truth. You ate tacos bravely.”)",
    "Spend a day in your coziest outfit and whisper “blessed be the elastic waistband” every time you sit down.",
    "Fold one toilet paper square into a tiny origami heart. Keep it on your altar (or bathroom shelf) as a symbol of mindful wiping.",
    "Fold and put away clean clothes while listening to choral music. Chant: “May order be restored. May fibers rejoice.”",
    "Offer a spoon of yogurt to your tongue while whispering, “Peace be dairy” Draw a tiny shrine to milk on a napkin.",
    "Bake or share bread with someone else. Tear it with your hands and say, “Take and eat, for this is slightly excessive, but deeply human.”",
    "Compose a short poem in the steam on your bathroom mirror. Read it aloud before it fades.",
    "Prepare a mocktail, hold it while you name five things you’re grateful for before sipping. Drink it like a sacred rite.",
    "Change your sheets while imagining yourself a renaissance saint restoring order to a sacred relic. Bonus if you hum Gregorian chants.",
    "Anoint your underarms with deodorant and say, “May my presence linger in love, not in odor.”",
    "Stand up. Stretch slowly. Whisper, “I am not stone, I am sinew and flow.” Perform a single exaggerated yoga pose like a theatrical statue.",
    "Ascenda uma vela, na sua proxima refeicão, arrume seu ligar com intençǎo, e escreva uma carta de amor pro seu estômago.",
    "Don’t eat any snacks for 2 days. On the third day, eat only snacks.",
    "Don’t use salt, pepper, creamer or butter for 2 days. Praise the penitent saints.",
    "Don’t order your number one choice on the menu, but instead select the Lava Cake as your only item.",
    "Put a small pebble in your shoe for the day. Let the pebble remind you of your transgressions.",
    "Turn the shower to cold before getting out. Stand under the cold stream for 30 seconds. Step forth cleansed in spirit and shriveled in flesh.",
    "Minimize your use of tissue. When you do use a tissue, thank a tree aloud.",
    "Spend 20 minutes looking at the water. Speak nothing. Listen to the current’s counsel.",
    "Sleep on the floor.",
    "Wake up in the middle of the night and say a prayer for the pigeons.",
    "Give away candy for a week. Let joy pass through your hands without tasting it.",
    "Walk barefoot on a pebbly beach. Each step is a prayer. Each wince a confession.",
    "Bind your fingers with rubber bands. Give thanks to the Mayan rubber gods.",
    "Pick up trash wherever you go. Every time you pick up a piece of garbage, repeat the mantra “ashes to ashes, dust to dust, plastic forever”",
    "Sing out loud when you are bored. If anyone looks at you strangely, sing louder.",
    "Stay off your phone for 5 hours. If you must make a phone call, find a land line.",
    "Shut yourself in the closet for 5 minutes. While in there, shout loudly “darkness away!” 5 times.",
    "Go to yoga and only do Downward dog.",
    "Go to yoga and only do savasana.",
    "Hoy, no saque ninguna foto. Mañana, saque fotos de todos a quien hablas.",
    "Take photos all day long of everything you use. From fork to faucet, document your dependencies.",
    "Document all the food you eat, either in song, poem, photo essay, haiku, bullet journal or sketches.",
    "Call your mother. If that is not possible call an elderly person and give them your full attention.",
    "Call your mother.",
    "Smile at 10 strangers. Hug 10 friends. Thank 3 service workers.",
    "Smile at 10 strangers.",
    "Apologize to someone.",
    "That is not a sin at the church of the bathroom confessional.  You are free to go!",
    "Chant “Charity, Prosperity, Clarity, Divinity! Restitution, Absolution, Contribution, Align your spine!” 30 times. Praise be to Malcom in the Middle, Season 1, Episode 4."
]

output_root = "penances"
os.makedirs(output_root, exist_ok=True)

for i, penance in enumerate(penances, start=1):
    folder_name = f"{output_root}/penance{i:02d}"
    os.makedirs(folder_name, exist_ok=True)
    text_file_path = os.path.join(folder_name, "penance.txt")
    with open(text_file_path, "w", encoding="utf-8") as file:
        file.write(penance)
