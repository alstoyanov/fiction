# Chapter 20: Confessions

*Friday, December 10, 2106. Regional Factorepo; a café in the western districts, Veridica Capital*

---

On Friday morning, two days after the dead had testified, the man at the next desk looked at Pieter Lang's face for slightly too long, and then laughed.

"You know who you look like?"

Nikolai did not look up from his screen. He had been waiting for it since Wednesday. He had watched it on the team room's wall display with everyone else, at twelve minutes past noon: the steps, the bright light, his own face twice, and the sound the crowd made. He had sat through it with his noodles going cold and his hands flat on the desk and the bond so cold in him that he thought his fingers might crack.

"Mm?" he said.

"Those two. From the steps. The dead brothers." The man, a cache specialist from the second floor who had been seconded to the team the same week as Pieter, tilted his head. "Round the eyes. If you took the beard off."

"If you took the beard off," said Nikolai, "I'd look like a man who can't grow a beard."

The cache specialist laughed and went back to his screen, and Nikolai went back to his, and his heart went on beating against his ribs like something trying to get out.

The beard was holding. The glasses were holding. The hunched shoulders, the noodles, the hours: all holding. Pieter Lang was still the dullest man in the building. But all morning, whenever he raised his eyes, he found someone looking away. Not suspicion. Nobody on the team suspected a mid-level contractor of being a corpse. It was only that everyone in the country had spent two days looking at the same face, and now they saw it wherever they looked, the way you see a word everywhere once you have learned it.

*If you come back,* he had written to his brothers, *they will look at everyone who shares your face.*

He had been right. It gave him no pleasure at all.

---

Maya came in at ten with two coffees and put one down on his desk without asking.

"The twin's buffer," she said. "Node routing. I want to walk it back."

It was the thing they had been circling for a week. On the twenty-ninth of November she had found the injection point of the carrier on the Ministry district node, at 14:18:40, in the buffer of the node's standby twin, which had survived the erasure because the twin had cut itself off when the hour ended. She had found her father's code in its header. She had told Pieter in a stairwell with her fists clenched, crying and furious in the same breath, and then she had gone home and sent a message she had not sent in four years, and got an answer in forty seconds.

What she had not done yet was follow it home.

"Wei gave you the node," said Nikolai. "Not the routing."

"Wei said *every packet at the edges of the hour*." She pulled her chair over to his desk. "Routing is packets."

He looked at her. She looked back, her jaw set, her coffee held in both hands like a weapon.

"Not on the board," he said.

"Not on the board," she agreed. "Scratch partition. Mine. If anyone asks, I'm checking the flush timings for the report." She set the coffee down. "Pieter. I'm going to do it anyway. I'd rather you were there."

He thought about the audit tables. Every query run on the investigation's systems was logged, and the logs were reviewed weekly, on Mondays, by a process he had watched Wei set up himself on the first day. By Monday someone would see that Maya Reeves had walked the carrier back to its source and not put it on the board.

*Somebody stays in the middle,* he had said once, in Ashford, to his brothers. *For once let it be someone who chose it.*

"All right," he said. "Show me."

---

It took them most of the day.

A carrier signal does not arrive on a broadcast node from nowhere. It has to be put there, and to be put there it has to travel, and travelling leaves traces: hops, handshakes, routing decisions made and cached by every relay it passes through. Most of those caches had been swept clean at 14:00. But not all of them. The erasure had been perfect inside the hour and very nearly perfect at its edges, and *very nearly*, Nikolai had learned in ten years of maintaining border-zone systems for people who did not want their work examined, was the only place anything true was ever found.

Maya worked the way she talked: fast, prickly, dry, with timestamps in every sentence.

"Relay four. Nothing inside the hour, it's clean, but look, a route reservation at 13:57:12 for a path that opens at 14:17. Pass-through, it doesn't originate. Relay nine, reservation at 13:57:04, same path. And a keepalive at 13:58 that nobody cleaned up. *Someone* wasn't careful—"

"Someone was very careful," said Nikolai. "They cleaned the hour. They didn't clean the three minutes before it, where the road was built. Nobody expects you to look at the minutes before."

"You did."

"I always look at the minutes before." He did not add: *it is where I have lived my whole life.*

At 15:40 they had seven hops. At 16:10 they had eleven, and the eleventh did not hand off to anything. It originated.

Maya read the registration out loud, very quietly, as if the terminal might hear her.

"*Terminal RA-N-0412. Registered to: Ministry of Historical Integrity. Research Annex, North District. Access class: restricted.*"

Nikolai pulled up the building on the Ministry's own estate map. It was an unremarkable address in the capital's north district, a four-storey block between a water authority depot and a school, listed as *research annex (neurological), Department of Correction liaison*. It had been leased to the Ministry in 2104. It had no public entrance.

"Continuity," said Maya.

"You don't know that."

"I do." She had another window open already, her own logs, the ones she had been keeping since the twenty-ninth without telling anyone but him. "Power profile. The annex is on the north district grid, and the grid publishes demand by block, because nobody thinks anyone would read it. Look. Treatment-grade load on the annex's second circuit, evenings, nights. Starting the last week of August. Continuity was suspended in August." She turned the screen towards him. "Ashford's Wing C drew exactly that profile. I checked it against the old returns. It's cradles, Pieter. Someone's been running cradles in that building since the week after the escape."

He looked at the graph. Little regular spikes, most nights, between midnight and four. A man who liked to work late, or more than one.

"Your father," he said.

She did not answer. She did not have to. She sat back from the screen and was very still.

"He's there," she said at last. "He's been there the whole time. Four months, twenty minutes from my flat." She laughed, one short breath with nothing in it. "I walk past the school."

---

Wei came by at a quarter to six.

The team room had begun to empty. The cache specialist had gone. The wall display had gone back to its endless reconstruction of the hour from its edges, a map of the Ministry district in which a few small lights came and went, the devices that had not heard that the hour was over. Maya had gone to the washroom to wash her face. Nikolai had closed the scratch partition and opened a flush-timing report in its place, and was looking at it without reading it, when a shadow fell across his desk and he looked up.

"Pieter." Wei smiled down at him: tall, tired, pleasant, a man at the end of a long week. "You dropped this, I think. By the lift."

He put something on the desk.

It was a page. Folded small, in quarters, and then again, the way you fold a thing you intend to carry for a long time. The paper was old and soft, gone furry at the creases, with the faint yellowing of cheap stock made for children. The fold was worn almost through along one edge.

Nikolai knew it before he touched it. He knew it the way he knew the shape of his own hand in the dark.

He unfolded it anyway, because not unfolding it would have been a kind of answer.

*Arithmetic for Young Citizens, Book Two.* A page of long division, a column of problems about a farmer with too many eggs. And under the numbers, under the letters of the problems, where the light from the desk lamp came through the paper, a scatter of tiny bright points. Hundreds of them. Small and even and very careful, the pricks of a man who had spent a whole night on them with a library pin.

*Fog off the lake. The tar still warm. Three of us on the parapet, legs over the edge.*

The roof.

"Arithmetic for young citizens," said Wei pleasantly. "Charming. My father collected old primers."

He patted the corner of the desk, once, the way you might pat the shoulder of a colleague who has had a hard week, and walked away between the desks towards his office, stopping on the way to ask the night technician about her daughter's exam.

---

Nikolai sat very still.

He did not look at the page. He did not look at Wei's back. He looked at the flush-timing report on his screen, and read the first line of it nine times, and did not take in a single word.

*Did he read it?*

The shift was simple. His father had taught it to three boys under a green lamp in a study, and Alexei had taught it to a wing full of prisoners in a week. Anyone could learn it in ten minutes. Anyone who knew there was a message to look for.

*Can he read pinpricks? Does he know what this is? Does he know who—*

His hand went to his jacket, to the inside pocket, to his wallet.

It was there. It was zipped. He took it out under the edge of the desk, below the line of any camera he knew about, and opened the zip with fingers that did not work properly, and looked inside.

The page was there.

Folded small, in quarters and then again. Worn almost through along one edge. He had not dropped it. He had not taken it out since last night, at eleven, in his rented room on the fourth floor, when he had held it up to the lamp the way he did every night and read it, and read it again, and waited for it to come back, and it had not come back, and he had folded it and put it in the wallet and zipped the wallet shut, as he did every night.

He did not take the original out. He did not dare. He only turned the wallet a little in the light, so that the lamp shone through the folded paper, and saw the points of light, and then looked at the page on his desk, and held the two in his mind side by side, the way he would have compared two log files.

The same fold. The same wear along the same edge. The same page, and the same farmer, and the same eggs. The same pinpricks, under the same letters, in the same places. He knew every one of them. He had not written them, and he could not remember the thing they described, but he knew them the way you know a text you have read four hundred times.

It was not his page. His page was in his wallet.

It was an exact copy.

Someone had held the original. Someone had held it long enough, and closely enough, under good enough light, to reproduce every one of several hundred holes made with a library pin by his brother's steady, desperate hand. Someone had found the same edition of a children's primer, and the same page, and aged it, and folded it, and worn it. Someone had done all of that, and then, instead of keeping it, had walked across a room and put it on his desk and told him he had dropped it.

Not to frighten him. Or not only.

*So that I would know,* he thought. *So that I would know that he knows.*

He folded the copy along its creases and put it in the wallet beside the original, because he kept copies. He always had. Then he zipped the wallet and put it back in his jacket and sat with his hands flat on the desk, and when Maya came back from the washroom with her face scrubbed pink and asked if he was all right, he said he was hungry.

Before he left he sent one line, in the shift, to Dmitri. *He has seen the roof.*

He did not wait for an answer.

---

The café was on a corner in the western districts, three streets from Maya's flat and six from his, and it stayed open until two for the shift workers from the depot. It had steamed windows and a long counter and a coffee machine that screamed every forty seconds, and it had one camera, in the corner over the door, which Nikolai had checked the first time Maya brought him here, the way he checked everything. It had no microphone. Audio needed a licence the owner had never bought.

They sat at the back, under the vent, with two bowls of soup they did not eat.

Maya talked.

She had told him most of it in the stairwell on the twenty-ninth, but in pieces, out of order, angry. Tonight she told it in order, the way she would have written up an incident, and he understood that she was doing it on purpose: getting it into a sequence so that it would stay still.

Her father's name. Her mother's side, at ten, in a kitchen. The four years without a word. August, and Isaiah's article, and reading what her father had done at Ashford on her kitchen floor at two in the morning, and being sick in the sink. The months since, with her name on her badge like a stain. The twenty-ninth, and the buffer, and the header, and the bee joke that she had last seen on a yellow note stuck to a fridge when she was ten.

"I sent it at 21:12," she said. "*I know it was you.* The reply came at 21:12 and forty seconds." She had the message on her comm. She did not show him. She had shown it to him before. She recited it. "*No, Maya. It wasn't. But I know who writes like me now.*"

"You've written to him since."

"Four times. *Where are you. Who writes like you. Answer me. Please.*" She looked at the soup. "Nothing. Forty seconds, and then nothing."

"And now you know where he is."

"And now I know where he is." She pushed the bowl away. "And on Monday the audit runs, and Wei sees the routing query, and on Tuesday there are enforcers at a door in the north district. And they take him somewhere, and he's the man who invented seeding, and everyone in the country already thinks he did it. They'll never let me near him." She looked up. Her eyes were wet and furious. "I want to hear it from his mouth, Pieter. Not from the header. Not from a message. From him. I want to stand in front of him and ask him, and look at him when he answers. I'm owed that. He owes me that." A breath. "And then they can have him."

The coffee machine screamed. Somebody at the counter laughed.

Nikolai looked at his hands on the table.

He had spent his life in the middle. Between Dmitri and Alexei. Between the border and the factorepo. Between the partition and the audit table, the truth he restored every night and the flatness he performed every day. He had kept everybody's secrets, including his own, and he had been very good at it, and it had cost him a roof in the border zone and three boys arguing about who was born first, and he could not get them back.

*So that I would know that he knows.*

If Wei knew, then Pieter Lang was already finished. It was only a question of when Wei chose to say so. And if Pieter Lang was already finished, then the only person he was still lying to, at this table, was the one person in the building who had told him the truth.

"Maya," he said.

She waited.

"My name isn't Pieter." He had not said it to anyone outside his family since August. It came out steadier than he expected. "It's Nikolai Volkov. I was C-5. At Ashford." He made himself look up. "Your father studied me."

She did not move.

For a long time she did not move at all. The coffee machine screamed and stopped. She looked at his face, at the beard, at the glasses he did not need, at the eyes behind them, and he watched her do what everyone in the country had been doing for two days, and put the face on the steps over the face in front of her, and see it fit.

"…The third face," she said.

"Yes."

"On Wednesday. On the steps. Two of them. And I thought—" She stopped. "I sat next to you and watched it and I thought, *he's got one of those faces.*"

"Everyone did."

"*Round the eyes,*" she said, in a very good imitation of the cache specialist, and then put her hand over her mouth, and he could not tell for a moment whether she was laughing or crying, and then he could tell that it was both.

When she took her hand away she said, not quite steadily, "He studied you. What did he—" and stopped again. "No. Not now. You'll tell me. Not now."

"I'll tell you," he said.

She reached across the table, past the cold soup, and took his hand.

He had not been touched on purpose by anyone but his brothers since August. He looked down at her hand on his, on the scarred café table, under the vent, in the one room in the capital where nobody was listening, and he found that it was the easiest thing in the world, and the most frightening, to let it stay.

Two people with the same file behind them, he thought. Her father's handwriting on both our lives.

He turned his hand over, and held on.

---

He walked her home at one.

It was cold and clear, the same hard winter light as Wednesday gone blue and silver with the night, and the streets of the western districts were almost empty: a street-cleaning cart, a couple arguing in a doorway, a tram going past lit and vacant. Maya had her hands in her pockets and her shoulder almost against his, not quite touching. Neither of them said anything. It was not an uncomfortable silence. It was the silence of two people who have said the hardest thing and are letting it settle.

They turned into her street.

On the other side of it, under a streetlamp, a man in a good gray coat was standing still, looking at a tablet.

He was not reading it. Nikolai knew the difference; he had spent his life among people pretending to look at screens. The tablet's light was on the man's face, and the man's face was not moving, and his eyes were not moving, and his thumb was not moving on the glass. He was simply standing there, at one in the morning, on a residential street, in a very good coat, holding a lit tablet in front of him like a reason.

Nikolai did not turn his head. He did not break stride. He did not look at the man at all, except in the way that a man who has spent his whole life in the middle can look at something without looking at it.

*He counted to three, Lyosha,* Dmitri had said, in the car on Wednesday, and Alexei had sent it on to him in the shift, and he had read it in his rented room with the page from his wallet in his other hand. *There are only two of us up there.*

Through the bond, faint and far off, he felt his brothers: the steady cold weight that was Dima, the pressure behind the eyes that was Lyosha. Both of them, somewhere, awake.

"Maya," he said quietly, still walking, still not looking. "Tomorrow we find your father." A breath. "Before someone else does."
