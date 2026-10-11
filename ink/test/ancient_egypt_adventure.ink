// Ancient Egypt Adventure
// An interactive fiction story

VAR player_name = ""
VAR has_amulet = false
VAR has_torch = false
VAR sphinx_riddle_solved = false
VAR priest_trust = 0
VAR gold_coins = 0
VAR knows_hieroglyphs = false

-> intro

=== intro ===
The golden sands of Egypt stretch endlessly before you. The year is 1923, and you've just arrived in Luxor as an aspiring archaeologist, following rumors of an undiscovered tomb near the Valley of the Kings.

The locals speak in hushed tones of the Tomb of Khamenet, a forgotten pharaoh whose name was erased from history. They say his treasure remains cursed, guarded by ancient magic.

What is your name?
* [Dr. James Harrison]
    ~ player_name = "Dr. Harrison"
    -> arrival
* [Sarah Montgomery]
    ~ player_name = "Sarah"
    -> arrival
* [Ahmed Al-Rashid]
    ~ player_name = "Ahmed"
    ~ knows_hieroglyphs = true
    -> arrival

=== arrival ===
Welcome, {player_name}. Your journey begins at dawn.

You arrive at the excavation site with your equipment: a leather satchel, rope, canteen, and your trusty journal. The desert sun beats down mercilessly as your guide, old Rashid, points to a narrow canyon.

"There," he whispers. "The entrance was revealed by last week's sandstorm. But I will go no further. The old magic still lives."

He leaves you alone. Before you lies a dark opening in the canyon wall, partially obscured by fallen rocks.

* [Examine the entrance carefully]
    -> examine_entrance
* [Light a torch and enter immediately]
    ~ has_torch = true
    -> hasty_entrance
* [Search the surrounding area first]
    -> search_area

=== examine_entrance ===
You brush away sand and examine the entrance. Ancient hieroglyphs are carved around the doorway. {knows_hieroglyphs: You can read them: "Here lies Khamenet, Speaker of Truth. Only the worthy may enter."|The symbols are mysterious, impossible to read without training.}

The entrance is large enough to crawl through. You notice torch brackets on the walls inside.

* [Light a torch and enter carefully]
    ~ has_torch = true
    -> careful_entrance
* [Enter without a light]
    -> dark_entrance
* [Search around outside first]
    -> search_area

=== hasty_entrance ===
You hastily light a torch and duck into the passage. In your haste, you trip over loose stones, and your torch falls from your hand, rolling into the darkness ahead.

~ has_torch = false

Cursing, you're now in dim light. You can see the torch flickering ahead, but the passage seems unstable.

* [Crawl forward carefully to retrieve the torch]
    -> retrieve_torch
* [Continue without the torch]
    -> dark_entrance
* [Go back outside and start over]
    -> examine_entrance

=== retrieve_torch ===
~ has_torch = true

You crawl forward slowly, testing each stone. Your caution pays off—you retrieve the torch just as a section of ceiling collapses behind you, sealing the entrance.

There's no going back now. Only forward into the tomb.

-> first_chamber

=== careful_entrance ===
With torch held high, you enter the passage carefully. The walls are decorated with faded paintings showing the pharaoh's journey to the afterlife.

As you move deeper, you hear a grinding sound behind you. Turning, you see stones settling into place, sealing the entrance.

There's no retreat now. You must find another way out.

-> first_chamber

=== dark_entrance ===
You venture into the darkness, feeling your way along the walls. It's treacherous and frightening.

After several minutes, you see a faint glow ahead. As you round a corner, you find yourself in a chamber lit by shafts of light from above.

-> first_chamber

=== search_area ===
You search the area around the entrance. Behind a large rock, you discover a small shrine with offerings left by ancient visitors. Among them is a bronze amulet with the Eye of Horus.

~ has_amulet = true

You pocket the amulet. It might prove useful.

* [Now enter the tomb]
    -> examine_entrance

=== first_chamber ===
{has_torch: Your torch illuminates|Shafts of light from above reveal} a magnificent chamber. The walls are covered in hieroglyphs and paintings depicting the pharaoh's life. In the center stands a stone altar with four passages leading away in different directions.

On the altar lies a scroll, remarkably well-preserved.

{has_amulet: The amulet around your neck suddenly feels warm.}

* [Read the scroll]
    -> read_scroll
* [Examine the paintings on the walls]
    -> examine_paintings
* [Choose the north passage]
    -> north_passage
* [Choose the east passage]
    -> east_passage
* [Choose the south passage]
    -> south_passage
* [Choose the west passage]
    -> west_passage

=== read_scroll ===
You unroll the scroll carefully. {knows_hieroglyphs: You read:|The hieroglyphs are difficult, but you make out:}

"Four paths lie before the seeker. Wisdom lies in the East, where knowledge is kept. Danger lurks in the North, where guardians sleep. Riches await in the South, for those who dare. Truth resides in the West, where Khamenet rests."

You memorize this information.

* [Examine the paintings]
    -> examine_paintings
* [Choose the north passage (Danger)]
    -> north_passage
* [Choose the east passage (Wisdom)]
    -> east_passage
* [Choose the south passage (Riches)]
    -> south_passage
* [Choose the west passage (Truth)]
    -> west_passage

=== examine_paintings ===
The paintings are exquisite. They show Khamenet as a wise ruler who spoke against corruption in the royal court. This explains why his name was erased—he was likely eliminated by rivals.

One painting shows him holding the same amulet {has_amulet: you found outside|you saw at the shrine}.

* [Read the scroll on the altar]
    -> read_scroll
* [Choose a passage]
    -> choose_passage

=== choose_passage ===
Which way will you go?

* [North passage]
    -> north_passage
* [East passage]
    -> east_passage
* [South passage]
    -> south_passage
* [West passage]
    -> west_passage

=== north_passage ===
You enter the northern passage. The air grows cold and still. After several turns, you emerge into a circular chamber.

In the center stands a massive stone sphinx, its eyes seeming to glow in {has_torch:the torchlight|the dim light}.

As you step forward, the sphinx speaks with a voice like grinding stone:

"I am the Guardian of Khamenet. Answer my riddle correctly, and pass. Answer incorrectly, and join the dust of centuries."

Your heart pounds.

"I never was, am always to be. No one ever saw me, nor ever will. And yet I am the confidence of all who live and breathe. What am I?"

* [Answer: "Tomorrow"]
    -> riddle_correct
* [Answer: "Death"]
    -> riddle_wrong
* [Answer: "The future"]
    -> riddle_correct
* {has_amulet} [Show the amulet instead of answering]
    -> bypass_sphinx

=== riddle_correct ===
~ sphinx_riddle_solved = true

The sphinx's eyes dim to normal stone.

"You are wise, seeker. You may pass—and return this way freely."

A passage opens behind the sphinx, but you can also go back the way you came.

* [Continue through the new passage]
    -> treasure_chamber
* [Return to the first chamber]
    -> first_chamber

=== riddle_wrong ===
"INCORRECT!" the sphinx roars.

The chamber begins to shake. Sand pours from cracks in the ceiling. You run back the way you came, barely escaping as the passage collapses behind you.

You're back in the first chamber, heart racing. The north passage is now blocked.

* [Try the east passage]
    -> east_passage
* [Try the south passage]
    -> south_passage
* [Try the west passage]
    -> west_passage

=== bypass_sphinx ===
~ sphinx_riddle_solved = true

You hold up the amulet. The sphinx's eyes widen in recognition.

"You bear the mark of Khamenet himself! You are deemed worthy. Pass freely, seeker."

The sphinx bows its great head, and a passage opens behind it.

* [Continue through the passage]
    -> treasure_chamber
* [Return to the first chamber]
    -> first_chamber

=== east_passage ===
You enter the eastern passage. It slopes downward, leading to a small library chamber. Shelves carved into the walls hold dozens of ancient scrolls and papyri.

{knows_hieroglyphs: You can read some of these! They contain medical knowledge, astronomical observations, and mathematical calculations far ahead of their time.}

In the corner sits a scribe's desk with writing implements still laid out, as if the scribe just stepped away.

* [Study the scrolls carefully]
    -> study_scrolls
* [Take some scrolls for the museum]
    -> take_scrolls
* [Return to the first chamber]
    -> first_chamber

=== study_scrolls ===
You spend time examining the scrolls. One contains a map of the tomb! You now understand the layout:

The passages connect in a circle, with the burial chamber accessible from multiple routes. The safest path is through the east to the treasure chamber, then to the west where Khamenet lies.

{not knows_hieroglyphs: You also begin to understand the hieroglyphs better after studying them.}
~ knows_hieroglyphs = true

* [Take some scrolls]
    -> take_scrolls
* [Continue exploring]
    -> treasure_chamber
* [Return to the first chamber]
    -> first_chamber

=== take_scrolls ===
You carefully select several scrolls that would be invaluable to science. These alone would make your reputation!

* [Continue deeper into the tomb]
    -> treasure_chamber
* [Return to the first chamber]
    -> first_chamber

=== south_passage ===
You enter the southern passage. It's wider than the others, with more elaborate decorations. Gold leaf glints on the walls.

The passage opens into a dazzling chamber filled with treasures: golden statues, jewelry, alabaster vessels, and chests overflowing with precious items.

It's breathtaking. {has_amulet: But the amulet grows cold against your chest—a warning?}

* [Take only a few gold coins as proof]
    -> take_small_treasure
* [Fill your satchel with treasure]
    -> take_large_treasure
* [Take nothing and continue]
    -> treasure_chamber
* [Return to the first chamber]
    -> first_chamber

=== take_small_treasure ===
~ gold_coins = 5

You pocket a handful of gold coins, enough to prove your discovery without being greedy. As you do, you notice that some of the treasure is actually painted clay—worthless fakes mixed with real gold to test the worthiness of tomb raiders.

You chose wisely.

* [Continue exploring]
    -> treasure_chamber
* [Return to the first chamber]
    -> first_chamber

=== take_large_treasure ===
~ gold_coins = 20

Greed overtakes you. You stuff your satchel with gold, jewelry, and precious gems. 

As you reach for a magnificent golden crown, the floor beneath you gives way! You fall into a pit trap, landing hard on ancient bones.

Looking up, you see the pit is too deep to climb out. Your torch {has_torch: gutters in the stale air below|is far above}. 

The treasure you took weighs you down. In desperation, you must make a choice:

* [Keep the treasure and search for another way out]
    -> pit_death
* [Abandon the treasure and try to climb out]
    -> escape_pit

=== pit_death ===
You refuse to abandon your prize. Hours pass as you search the pit for an exit, but there is none. Your torch dies{has_torch:|, and darkness closes in}.

Eventually, dehydration and exhaustion claim you. Your bones join the countless others who chose greed over wisdom.

THE END

Your adventure ends here. The tomb keeps its secrets—and one more greedy soul.

-> END

=== escape_pit ===
~ gold_coins = 0

You dump the treasure. Lightened, you manage to find handholds and climb out. You're bruised and shaken, but alive.

The amulet {has_amulet: warned you, but you didn't listen fully. |would have warned you, had you found it.}You've learned a valuable lesson about greed.

* [Continue with your quest, wiser now]
    -> treasure_chamber

=== west_passage ===
You enter the western passage. The walls here are painted with scenes of judgment in the afterlife—the weighing of the heart against the feather of Ma'at.

The passage leads to an antechamber guarded by a priest's mummy, seated on a throne. Somehow, you sense it's not quite... dead.

As you approach, the mummy's eyes open with a dusty creak.

"Why do you disturb the rest of Khamenet?" it rasps.

* [Say: "I seek knowledge, not treasure"]
    -> priest_knowledge
* [Say: "I wish to restore Khamenet's name to history"]
    -> priest_restoration
* [Say: "I mean no harm, only to document what's here"]
    -> priest_document
* {has_amulet} [Show the amulet]
    -> priest_amulet

=== priest_knowledge ===
~ priest_trust = priest_trust + 1

The priest's mummy nods slowly.

"Knowledge is worthy. But what will you do with it?"

* [Say: "Share it with the world"]
    -> priest_share
* [Say: "Keep it safe in a museum"]
    -> priest_museum

=== priest_restoration ===
~ priest_trust = priest_trust + 2

The mummy sits forward eagerly, dust falling from its wrappings.

"Yes! Khamenet was a good man, struck down by lies. If you would restore his name, you are a friend indeed."

* [Continue]
    -> priest_approval

=== priest_document ===
~ priest_trust = priest_trust + 1

"A chronicler, then. That too has value. The truth should be recorded."

* [Continue]
    -> priest_approval

=== priest_amulet ===
~ priest_trust = priest_trust + 3

You show the amulet. The priest gasps and bows his head.

"You bear the mark! You are the one foretold—the one who would find the truth and speak it to the world. Enter freely, friend of Khamenet."

* [Continue]
    -> priest_approval

=== priest_share ===
~ priest_trust = priest_trust + 1
-> priest_approval

=== priest_museum ===
~ priest_trust = priest_trust + 1
-> priest_approval

=== priest_approval ===
{priest_trust >= 3: The priest stands and bows. "You have proven yourself worthy. Enter the burial chamber. Learn the truth of Khamenet, and carry it to the world above." The passage behind him opens. | The priest nods. "You may pass, but remember: truth is sacred. Do not betray it." A passage opens behind him, though he watches you warily.}

* [Enter the burial chamber]
    -> burial_chamber
* [Return to explore more first]
    -> first_chamber

=== treasure_chamber ===
You find yourself in a central treasure chamber. Passages lead in multiple directions, and you can see how the tomb connects in a great circle.

Here there are more treasures, but also something more valuable: detailed reliefs showing Khamenet's true history.

* [Study the reliefs]
    -> study_reliefs
* {not sphinx_riddle_solved} [Explore the north section]
    -> north_passage
* [Head west toward the burial chamber]
    -> west_passage
* [Return to the first chamber]
    -> first_chamber

=== study_reliefs ===
The reliefs tell an amazing story. Khamenet discovered corruption among the priests and nobles. He tried to reform the system, to create fair laws and distribute food to the poor during a famine.

For this, his rivals poisoned him and erased his name from history. But his loyal followers built this tomb in secret, preserving the truth.

This is the real treasure—historical truth.

* [Continue to the burial chamber]
    -> west_passage
* [Explore more]
    -> treasure_chamber

=== burial_chamber ===
You enter the burial chamber. It's smaller than you expected, but beautiful. The sarcophagus is made of simple stone, not gold—Khamenet practiced the humility he preached.

On the walls are his final words, written in his own hand:

"To whoever finds this place: I was not perfect, but I tried to speak truth and serve justice. If you carry this truth forward, I will live again through your voice. That is immortality enough."

{has_amulet: The amulet glows warm against your chest.}

You realize you've found something more valuable than gold—a forgotten hero's true story.

* {gold_coins > 0} [Take your small amount of gold and leave]
    -> ending_treasure
* [Leave with only knowledge and truth]
    -> ending_knowledge
* [Search for another exit]
    -> find_exit

=== find_exit ===
Behind the sarcophagus, you discover a hidden passage—an escape route carved by the loyal followers who built the tomb. It leads upward to the desert surface, emerging far from where you entered.

* [Exit through this passage]
    -> final_choice

=== final_choice ===
As you climb toward the light, you must decide what to do with what you've found.

* {gold_coins > 0} [Report the tomb, take credit and the gold]
    -> ending_treasure
* [Report the tomb, focus on Khamenet's story]
    -> ending_knowledge
* [Seal the tomb and tell no one]
    -> ending_secret

=== ending_treasure ===
You emerge into the desert sunset, your pockets heavy with gold. You report the tomb to the authorities and lead an expedition back.

The tomb is excavated, its treasures divided among museums. You become famous and wealthy. Yet sometimes, late at night, you wonder if you honored Khamenet's true wish—or if you became another grave robber with better credentials.

Still, the story gets told, even if the gold gets more attention. Perhaps that's enough.

THE END

{player_name}'s adventure concludes. You found treasure and truth—though perhaps not in equal measure.

-> END

=== ending_knowledge ===
You emerge into the desert sunset, carrying only your notes, scrolls, and the truth of Khamenet's story.

You spend years researching, translating, and writing. Your book about Khamenet becomes a landmark work, restoring his name to history. Museums add him to their pharaoh exhibitions. School children learn about the reformer king who died for justice.

{has_amulet: You donate the amulet to the Cairo Museum, where it's displayed as "The Seal of Khamenet."}

You never became wealthy, but you gave a forgotten hero immortality. On quiet nights, you could swear you feel his gratitude.

THE END

{player_name}'s adventure concludes in triumph. You honored truth over gold, and the world is richer for it.

-> END

=== ending_secret ===
You emerge into the desert sunset and make a difficult choice: you seal the tomb's new entrance with rocks and tell no one.

Some truths, you decide, are too precious to risk. In modern hands, Khamenet's tomb might become a circus—tourists posing with sarcophagi, treasures sold to private collectors.

Let him rest in peace. You'll carry his story in your heart, living by the principles he died for. That's the real treasure.

Years later, on your deathbed, you'll write down the location. Future generations can decide when the time is right.

THE END

{player_name}'s adventure concludes in silence. Sometimes the greatest discoveries are the ones we protect.

-> END

