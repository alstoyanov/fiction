# Chapter 1: System Failure

*Monday, November 15, 2106. Monitoring floor, Regional Factorepo, Veridica Capital*

---

At 15:01:04 every alarm on the monitoring floor went off at once.

Maya Reeves would remember the time exactly, because she looked at it. It was the first thing she did. Around her the floor had become a single sound, forty consoles and the ceiling panels and the supervisor's desk all shrieking in the same flat tone, and the red integrity bands had come up on every screen in the room, and eleven people who monitored the national record for a living had stopped moving. Greta Szabo, halfway out of her chair, with a cup in her hand. Colm Adeyemi at the next console, his mouth open. Mr. Dunmore at the supervisor's desk with his palms flat on either side of his keyboard, as if the desk might be about to tilt.

Maya looked at the clock in the corner of her screen. *15:01:04.* Then she looked at the alarm codes, and saw that they were all the same code, and that the code was one she had only ever seen in training.

*PRIMARY CONTINUITY FAULT.*

She was twenty-four and the most junior technician on the floor, and she did not wait to be told. She pulled up the integrity suite and ran it herself.

---

The check took forty seconds. She watched it run with her hands in her lap because they had started, very slightly, to shake, and she did not want anyone to see.

It came back green.

Every hash chain verified. Every index reconciled. No contradictions, no corruption, no null records, no failed writes. By every measure the suite knew how to take, the record was perfect.

And the alarms were still going.

She ran the timeline view instead, the plain one they gave to first-year trainees: a single bar of the day's entries in blocks of an hour, thick bands of traffic and transit and sensor data, the ordinary weight of a Monday.

13:00 to 14:00, dense.

14:00 to 15:00.

Nothing.

Not a dark block. Not a red one. There was no block at all. The bar ran up to 13:59:59 and then it simply resumed at 15:00:00, and between them there was no gap on the screen, because the software did not know how to draw a gap. The timeline had closed over the missing hour the way water closes over a stone. You could only see it by reading the numbers.

She read the numbers. She read them again.

Then she opened the primary repository directly, which she was not supposed to do without a supervisor's key, and used Mr. Dunmore's, which she had watched him type every morning for eleven months, and looked.

Nothing. The primary ran to 13:59:59.998 and resumed at 15:00:00.000. She opened the three backups, one after another, each supposedly independent, each on its own hardware in its own building, and each ran to 13:59:59.998 and resumed at 15:00:00.000, and each reconciled perfectly with the other two. She opened the local repositories for the capital, the lakeshore districts, the northern provinces, and, at random, a village in the east whose name she had never heard of. Nothing.

Not corrupted. Not contradictory. *Absent.*

The traffic records for the whole nation between two and three o'clock. Every purchase, every payment. Every camera, every door, every sensor on every street. The broadcast logs. The births. Somewhere in Veridica a child had been born between two and three this afternoon, and there was no record that the child existed. Somewhere someone had died, and had not.

An hour of the country's history had not been damaged. It had never happened.

Maya's stomach turned over. It was a precise, physical sensation, and she recognised it: it was what happens when you go down a staircase in the dark and your foot reaches for a stair that isn't there. That lurch. That sick drop through nothing. She held on to the edge of the console and waited for her foot to land, and it did not land, and it went on not landing.

"Mr. Dunmore," she said. Her voice came out perfectly level, which surprised her. "It's the primary. Fourteen hundred to fifteen hundred. The whole hour. It's gone."

Behind her, somebody laughed. It was a short, frightened sound, and it stopped.

"That's not possible," said Greta Szabo. She had put her cup down at last. "Facts can't be deleted."

"I know."

Mr. Dunmore said it too, a moment later, looking at his own screen with the colour going out of his face. Colm said it. Somebody at the back said it. They said it the way people repeat a thing when they want to hear it said aloud by someone else. Maya had heard the sentence all her life, in school and on the broadcasts and in the induction lectures, and she had never before heard anyone say it as if it might be the last thing holding up the ceiling.

She said nothing. She was reading the numbers again.

---

The Ministry called at 15:20.

Maya knew because the notice came up on the floor feed, and because she had started, without deciding to, a log of her own in a plain text file on the corner of her screen. She had always timestamped things; her mother said she had timed her own baths. The record told you what happened. It did not tell you what order you had found it out in.

*15:01:04. Alarms. PRIMARY CONTINUITY FAULT.*
*15:02:31. Integrity suite. Green. (!!)*
*15:05. Timeline. 14:00–15:00 absent. Primary, 3 backups, locals (all tested).*
*15:20. Ministry notice: investigation lead appointed. WEI, T., Senior Systems Architect.*

"Wei," said Mr. Dunmore, reading it. Some of the colour came back into his face. "Well. Thank God for that."

"Who's Wei?" said Maya.

"Systems Architecture. Ministry district. He's—" Dunmore made a small gesture that took in the whole building, the floor, the country. "He's good. He's the best they've got. He'll be half an hour from over there, at least."

*15:32. WEI arrives.*

She typed it, and then looked at it, because it was wrong.

She knew the Ministry district. From there to the Regional Factorepo was twenty-five minutes at the best of times, on a clear road, with a driver who knew the lights. At three o'clock on a Monday it would be more. And it had been twelve.

He must have been on his way already, she thought. On his way here, or somewhere near here, when they called him. She let the thought go, because he had come through the doors from the lift lobby and was walking onto the floor, and everyone was turning to look at him.

He was tall, and graying at the temples, and he did not hurry. He had a plain coat over his arm, a Ministry lanyard round his neck and a paper cup of tea in his right hand, and his left hand was wrapped in a clean white bandage, across the palm and around the knuckles. He stopped just inside the floor and looked round it once, slowly, and she had the odd impression that in that one look he had counted them.

"Mr. Dunmore," he said. His voice was quiet. It did not need to be anything else; the alarms had been silenced at 15:14 and the floor had gone very still. "Thank you for holding the floor. Greta. Colm." He knew the names of people Maya was fairly sure he had never met. He went on round the room with them, not all of them, but most, and then his eyes came to her, and paused, and dropped to the badge on her jacket.

"Ms. Reeves," he said.

There was the smallest pause. She had grown used, since August, to the pause. It came after her surname the way a flinch comes after a raised hand. People heard *Reeves* now and something went across their faces, and then they asked, *Any relation?* in a joking voice, and she said *It's a common name,* in a joking voice, and they both pretended that was the end of it.

He did not ask. He looked at her face instead.

"I'm told you found it first," he said.

"I ran the integrity check." Her mouth was dry. "It came back clean. That's how I knew."

He came over and pulled out the chair beside hers, the empty one, and sat down in it, and set his tea on the desk by her keyboard.

"You found the gap first," said Thomas Wei. "Walk me through it."

---

She walked him through it.

She showed him the suite coming back green, and the timeline with no hole in it, and the numbers. The primary, the three backups, the locals, the village in the east with its name she still could not pronounce. She talked faster than she meant to. He did not interrupt. When she said something only half right he asked a question that let her find the other half herself.

He listened, she thought, like someone reading.

Once, reaching across her for the second screen, he steadied himself on the edge of the desk with his left hand and drew it back again at once. She glanced at the bandage. It was very white, very neatly done.

"Server rack," he said, and smiled a little, ruefully, the way people smile at their own clumsiness. "My own fault." He picked up his tea with his right hand. "Go on. The backups."

She went on.

When she had finished he sat for a moment without speaking, looking at the place on the screen where the hour should have been.

"It's clean," he said at last. "That's the remarkable thing. Not the size of it. Anyone can break something. This isn't broken. Whoever did this"—he said it very simply, *whoever did this*, as if it had never occurred to him to call it a fault—"did it so that nothing contradicts anything else. The record doesn't know it's missing anything." He looked at her. "You knew. The suite didn't. That's worth remembering."

She did not know what to say to that. She said, "Thank you."

"I'm putting a team together," he said. "Six or seven people, on the ninth floor, from tonight. I'd like you on it." He did not make it sound like a question, but he paused afterwards as though it might be one.

"I'm—I'm a junior technician," said Maya. "Sir."

"I know," said Wei. "You're also the only person on this floor who didn't freeze." He stood, and picked up his coat. "Bring your log. The one in the corner of your screen. I'd like a copy."

She had not known he'd seen it.

---

At 15:40 the second thing happened.

It came up the building the way news does, before any notice: a phone, then two, then a knot of people by the lift lobby, and one of them was crying. Colm came back from it with his face gone gray and said, to no one in particular, that Deputy Minister Singh had been found dead in her office at the Ministry. At five past three. Her aide had found her.

"Dead how?" said Greta.

Colm shook his head. "They're saying—" He stopped. "They're saying somebody killed her."

The floor was silent. Maya looked at her log, and at the two times in it, and at the hour between them that did not exist, and felt the missing stair again, lower down this time, in her chest.

*15:40. Word: Dep. Min. SINGH dead (found 15:05). Ministry. Killed?*

She typed the question mark, and then she deleted it, and then she put it back.

---

Wei briefed them at 16:10, in a borrowed meeting room along the corridor from the monitoring floor, with a long table and a window onto the transit line.

There were seven of them. Maya, and Colm, whom Wei had also taken, and four people she did not know from Systems Architecture who had arrived in a Ministry car at 15:55, and Wei himself at the end of the table with a closed folder in front of him and his tea, a fresh one, at his elbow.

He did not stand to speak. He told them what they knew, which was very little, and then what it meant.

"You'll all have been taught that the factorepo can't be altered," he said. "I was taught it. I believed it. I'd like you to keep believing it for as long as you usefully can, because it's going to make you careful." He turned his cup a quarter-turn on the table. "But understand what we're dealing with in the meantime. No record means no fact. No fact means The Judge can't rule. Whatever happened in the capital between two and three o'clock this afternoon—every conversation, every transaction, every crossing, every crime, including a Deputy Minister's death—is now, in law, nothing. It did not happen. There is no procedure for it. The Judge can't judge what it doesn't know happened."

Nobody spoke.

"So we rebuild it," said Wei. "From whatever survived." He looked round the table at them, one after another, pleasantly, and his eyes rested on each face for a moment, as if it were a thing he wanted to remember. "Or from whoever."

Maya found that she had written it down. *Or from whoever.* She did not know why.

"There are three possibilities, broadly," Wei went on. "A fault in the architecture that none of us understands. An attack from outside, from Chronos, say, which the Ministry will certainly want us to consider and which I'd ask you to consider sceptically. Or someone inside." He paused. "The Ministry will also want us to consider the people who came out of Ashford in August. Continuity's people."

Maya flinched.

It was not much: a tightening across her shoulders, her pen stopping on the page. She had been flinching at that word since the fifth of August, when she had read Isaiah Okonkwo's account on her kitchen floor at two in the morning, and she had got better at hiding it, but not good.

Wei's eyes came to her and stayed there, for perhaps a second. He did not say anything. His face did not change. Then he looked away, back to the whole table, and went on, and she sat with her pen stopped on the page and her face hot and understood that he had seen it, and that he had decided, for whatever reason, to let her keep it.

"I want to be clear," he said, "that those people are officially dead, and that the Ministry is not always right about what it would like to be true. We'll go where the record goes. Where there isn't one, we'll go carefully."

---

Her surname was Reeves.

For twenty-four years it had been an ordinary surname. Since August it had been the most famous surname in Veridica, in every article about Ashford and Wing C and the seven people in their glass cells: *Dr. Reeves*, *Dr. Reeves's programme*, *Dr. Reeves, whose whereabouts remain unknown.* There was no first name. The articles never gave one. It was as though the man had been nothing but a surname all along, and in a way, for her, he had.

She had not spoken to her father in four years. There had been a dinner, and she had walked out of it, and afterwards there had been an old message account that she simply stopped opening, so that whatever he sent, if he sent anything, would go into it and stay there. Since the first of August she had thought about that account more often than in all the four years before, and she had still not opened it. She did not want to know whether it was full or empty. She had noticed that about herself the way you notice a clock has stopped: not at the moment it stopped, but some time afterwards, all at once.

She did not know if he was alive. She told herself she did not care. She sat at the long table in the borrowed room with Wei's voice going on quietly at the end of it and her pen still stopped on the word *Continuity*, and she found that she cared very much, and that she hated it.

---

At 17:10 Wei sent everyone to get something to eat and told them to come back by six.

"And I'd rather nobody watched the broadcasts tonight," he said, as they were getting up. "Not for my sake. For yours. There'll be a great deal of noise by the evening, and we need your heads clear of it. Whatever they're saying, it isn't evidence."

So Maya did not watch the broadcasts. She ate a sandwich at her desk on the monitoring floor, which had emptied, and at 17:30, because she could not stop, she began to go through the scheduling logs.

It was dull work, and she liked it for that. Every job on the factorepo's core was scheduled in advance, with an owner, a window and a reason; it was the first rule of the architecture. You did not touch the core without your name in the record. She went through the fifteenth window by window, looking for anything that touched two to three o'clock.

At 21:48 she found it.

*Scheduled activity: primary repository, core synchronisation. Window: 15 NOV 2106, 14:00–15:00. Owner:*

The field was blank.

She sat very still. She checked the booking record behind the entry, and the booking record said the window had been reserved at 06:12 on Sunday morning, the fourteenth, and that the owner field had been blank from the moment it was made. She checked for a correction, a later amendment, a supervisor's override, and there was none.

Someone had booked the hour. A day in advance. On the core. And left their name off.

And someone had noticed. There was a flag on the entry. A contractor's anomaly note, the kind anyone with schedule access could raise and almost nobody ever did, filed at 23:31 on Sunday night, the fourteenth:

*OWNER FIELD BLANK ON CORE WINDOW 14:00–15:00 (15 NOV). PLEASE CONFIRM OWNER BEFORE WINDOW OPENS. — P. LANG (CONTRACTOR, SYSTEMS MAINTENANCE)*

Nobody had answered it. The note sat there on the schedule exactly as it had been filed, polite and plain and unregarded, fifteen hours before the hour it was warning about.

"Well," said a quiet voice behind her. "Look at that."

She jumped. Wei was standing at her shoulder with his coat over his arm. She had not heard him come onto the floor. He was reading her screen, and his face in its blue light was thoughtful, and very faintly, she thought, pleased.

"The hour was booked," she said. "Nobody owned it. And a contractor flagged it the night before."

"So he did." Wei read the note again. Then he smiled, a small, private smile, as though something had gone the way he had rather hoped it might.

"Find me Mr. Lang," he said.

---

She got home a little after midnight.

Her flat was on the sixth floor of a building in the western districts, and it was cold, because she had forgotten to set the heating. She stood in the dark hall with her coat still on and felt, for the first time since 15:01:04, how tired she was. Her hands had stopped shaking some time in the afternoon. That time she had not logged.

She had not watched the broadcasts, as she had been told, and she was proud of it in a small and slightly foolish way. It was past midnight now. She was no longer on duty. She turned the screen on in the kitchen, with the sound low, and filled the kettle.

The news was already running. It had, she understood after a moment, been running for hours.

It was the Ministry: pictures of the building at dusk with its lights on; enforcers on the steps; a still of Deputy Minister Singh at some official function, a composed woman with reading glasses on a cord around her neck, smiling slightly at someone out of frame. Maya stood with the kettle in her hand and watched.

Forty Ministry employees, the newsreader said, had given statements to enforcers during the afternoon. Forty separate people, interviewed separately. Every one of them had seen the killer walk into the Deputy Minister's office at twenty past two. Every one of them described him. Every one of them named the same man.

The picture changed.

It was a photograph she knew. Everyone knew it. It had been in Isaiah Okonkwo's account in August, and on every broadcast after, one of seven: a thin young man in gray, with glasses, looking into the camera with no expression at all, the way people look in a file photograph when they have stopped expecting anything from the person taking it.

Under it, in the Registry's plain white letters, was his name, and beneath his name the single word the Registry had entered against it on the second of August.

*MARCUS CHEN. STATUS: DECEASED.*

The kettle began to boil in Maya's hand. She did not move to put it down.
