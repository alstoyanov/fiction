# Chapter 14: The Carrier

*Monday, November 29, 2106. Regional Factorepo, Veridica Capital*

---

Wei put the drive on her desk at 08:14, and Maya noted the time because she noted every time, and because afterwards she wanted to know exactly when it had started.

"The Ministry district node," he said. "Every packet at the edges of the hour. In and out."

She looked at the drive, and then at him. Everyone in the investigation room knew what was on it. The district node had a twin, a standby transmitter that mirrored everything the live unit carried into a buffer of its own, and at 15:01 on November fifteenth, when every alarm in the country went off, the twin had done what it was designed to do in an emergency: isolated itself, and stopped. Wei had had it pulled and caged on the sixteenth, and the imaging team had spent twelve days copying it without waking it. Its buffer was thirty-one hours deep, and it ended at 15:01:07.

It was the one piece of hardware in Veridica that had not been told the hour was over.

"You want me to do it," she said.

"I want you to do it." He said it the way he said everything, quietly, as though it were an ordinary thing to hand the most junior person in the room the best evidence in the case. "You found the gap first. You'll see the shape of this before anyone else does. Take the whole buffer. Don't start at fourteen hundred. Start at the edges and walk in."

"From both ends?"

"From both ends." He smiled faintly. "Tell me what's there, Maya. Not what ought to be."

He went back to his own desk at the end of the room. She was aware that her face was doing something, and she wanted it to stop before anyone noticed.

It didn't. At the next desk, Pieter Lang looked up from his noodles and his cache tables, looked at the drive, looked at her, and raised his eyebrows a millimetre.

"Don't," she said.

"I didn't say anything."

"You were going to say *teacher's pet*."

"I was going to say congratulations," Pieter said mildly, and went back to his tables. "I'd have said *teacher's pet* after lunch."

She broke the evidence seal on the drive at 08:21.

---

The investigation room had been a conference suite on the ninth floor until two weeks ago. Now it was eleven desks and a wall of screens showing what they had shown for fourteen days: timelines of the fifteenth in dense bands of colour, every band broken by the same clean black bar from 14:00:00 to 14:59:59. Maya had stopped seeing it as a hole. It had become a shape, the way the gap in a hedge becomes a shape if you walk past it every day. She still felt it when she looked at it directly: the drop in her stomach, the stair that wasn't there.

She started at 07:48 on the fourteenth, the far end of the buffer, and walked in.

A broadcast node carried two kinds of traffic: the fact stream, the factorepo's updates going out to every interface in the district, and the maintenance channel, engineers talking to hardware. She knew both by heart. She logged the anomalies as she went, packet ID and offset. *07:52:13, retransmit, cause: congestion. 09:00:04, verification pulse, 0.3 seconds late.* The ordinary untidiness of a machine doing its job.

By two she was at 13:40, and she stopped and drank cold coffee, because she could feel the hour coming the way you feel the edge of a platform in the dark.

13:59:58. 14:00:00.

The fact stream kept running. The live node had kept broadcasting through the hour like every node in the country, and the twin had mirrored it. The facts were gone from every repository now, but here they were, still in the buffer. *A delivery at the east gate, 14:03. A lift fault on the seventh floor of the Ministry, 14:06.* Someone had been stuck in a lift for eleven minutes during the lost hour and nobody would ever know. Except her. She logged it.

At 14:18:40 something came in on the maintenance channel that was not maintenance.

It had the right address block and the right priority flag, and it was the right size for a firmware push. But firmware pushes didn't happen during office hours without a work order, and this one had no work order. It had no owner at all.

She opened it.

It wasn't a push. It was a stream. Something had been injected into the node at 14:18:40 and handed straight across to the broadcast side, and from there it had gone out, on the same band as the fact stream, underneath it, to every interface in the Ministry district's range. A carrier. It ran for thirty-eight minutes. It had a modulation envelope she had never seen on a factorepo node in her life, a long slow shape, climbing and levelling and holding, like a hand that has found the place it wants and settles there.

Its content section was encrypted. She couldn't read it. She didn't need to.

She had read Isaiah Okonkwo's article in August, on her kitchen floor at two in the morning. *A second phase: adaptation of the Continuity method for population-scale delivery via the national neural-interface broadcast network.* She had read *test signals are already running in three districts*, and got up and been sick in the sink.

Forty people had watched a dead man walk into the Deputy Minister's office at 14:20. Forty people who could not all have made the same mistake. The whole building had been saying it for a fortnight, in corridors, the way people say things they don't want to have said: *it's like they were all told.*

*14:18:40,* she thought. *Two minutes before.*

Her mouth was dry. She did what she always did, which was to go on working. She opened the header and went through it field by field. Origin address: masked, routed through two relays, recoverable with time. Build stamp: stripped. Signing block: empty.

And at the bottom, where a developer might leave a note for himself in a build that was never meant to leave his own machine, there was a comment.

*/\* ut apes. bee back in an hour. \*/*

---

The investigation room went on around her. Someone laughed at the far end. A printer ran. Pieter's chopsticks clicked against the side of his carton.

Maya looked at the comment, and the comment looked back at her from the fridge door of a kitchen she hadn't stood in for fourteen years.

Yellow squares. That was how she remembered it: a fridge door covered in small yellow squares, because her father never said anything he could write instead. *Maya: milk. ut apes.* *Gone to the lab, bee back at seven. ut apes.* *Bee good for your mother. ut apes.* He wrote them in lowercase, always, in a small neat hand, and he always ended them the same way, and when she was seven she had asked him what it meant.

"Like the bees," he had said. He had been making toast. He had looked down at her with the expression she had spent the rest of her childhood trying to earn and the rest of her adulthood trying to forget: bright, pleased, *interested*. "Bees go out every morning, and they don't know what the hive is for, and they come back anyway. Every one of them. They always find their way home."

"That's not a joke."

"The joke's the other bit." He had tapped the note. "*Bee back.* You see?"

She had not thought it was funny. She had written *ut apes* at the bottom of her own notes for a year afterwards, and then stopped, the year she was ten, the year the notes stopped.

She sat with it in front of her, at the bottom of a signal that had gone into forty people's heads, and felt the floor tilt under her chair: the drop, the stair that wasn't there, the certainty that if she stood up she would fall.

She didn't stand up.

---

Her parents had divorced when she was ten. It had been quiet, as divorces went. There had been no shouting, because her father didn't shout, and her mother had learned years earlier that shouting at him was like shouting at weather. There had only been a long cold autumn of her mother packing and her father watching her pack, as if the packing were an experiment he had not designed but found worth observing. Maya had gone with her mother. She had taken her mother's side in everything, with the whole of her ten-year-old heart, and gone on taking it, in everything except one thing.

The name. Her mother had gone back to her own name and wanted Maya to take it too. Maya had refused. She had kept *Reeves* out of pure spite, and she had never been able to say, even to herself, which of them the spite was for: her mother, for making her choose, or him, so that he would have to see his name on every form, attached to a daughter who did not call.

For ten years after that there had been birthday messages, and two dinners a year in restaurants he chose, where he asked about her studies with such bright attention that she felt like a slide under glass. At the last one, four years ago, he had talked about his work without saying what it was. It was going well, he said. It was *very interesting*. She had put down her fork and walked out, and he had not followed her, and neither of them had written since.

Then August. Isaiah Okonkwo had not printed the name in his first paragraph. He hadn't needed to. By the evening of the fifth every screen in Veridica had it, and Maya had understood that she would spend the rest of her life being asked whether she was related.

She had told no one. Not Wei, who had noticed her flinch at the word *Continuity* on the first afternoon and had said nothing about it, then or since, which she had been more grateful for than she could have explained. For three and a half months she had carried the name around the building like a stone in her shoe.

And now here he was. Not a name in an article. Here, in her evidence. Lowercase, the way he'd always been.

*He's alive,* she thought. There had been a week in September when she had caught herself reading death notices. *He's alive, and he's hidden, and at 14:18 on the fifteenth he had his hand on a switch.*

It fitted. That was the worst of it. It fitted the way a key fits. The Deputy Minister had opened an inquiry into Continuity the morning after the article. She had been going to finish him. So he had erased an hour and written a murder into forty people and put Marcus Chen's face on it, the face of his own best result. It was exactly the kind of thing the article said he would find *interesting*.

She put her hand over her mouth.

Then she did the next thing, because there was always a next thing. She copied the packet and its header to a partition on her own workstation, under a filename that meant nothing. She did not add it to the shared log where, by Wei's protocol, every finding went the moment it was found.

She sat and looked at what she had just done.

If she flagged it, Wei would read it and go quiet, and thank her, and take it upstairs. By the morning someone in Records would pull her file and see the surname, and she would be the daughter. The daughter who had found her father's code in the Lost Hour: who had turned him in, or who had been put on the team to find it first and bury it. Either way, nobody would ever trust a Reeves near a record again.

And if she didn't flag it, she was hiding evidence of how forty people had been made to see a murder. She was hiding it for him.

She had never wanted so badly to be sick and to hit something at the same time.

---

At 15:06 she got up, walked out of the investigation room without looking at anyone, and went into the east stairwell, because it was the only place on the ninth floor without a camera on the landing. Everyone knew that. It was where people went to cry, or call their mothers, or both.

She stood with her back against the wall between the eighth and ninth floors and pressed the heels of her hands into her eyes.

The door above her opened and closed. She knew it was Pieter before she looked, because he took the stairs the way he did everything, carefully, as if he had once fallen down a flight and never quite forgiven it. He stopped two steps above her. He didn't say anything. He didn't come closer.

"Go away," she said.

"All right."

He didn't go away. He sat down on the step, with his hands between his knees, and looked at them.

She hadn't meant to tell him. She had meant to say *headache*, and go back in. But he sat there looking at his hands, not at her, and waited, and it was the waiting that did it. Everyone else on the team finished your sentences for you.

"There's a carrier," she said. "On the district node. Injected at 14:18:40. It ran for thirty-eight minutes, under the fact stream, to every interface in range."

He went very still. Not the stillness of someone surprised. The stillness of someone who has been carrying something heavy and has just felt it shift. She noticed it, and put it away, because she had no room for it.

"Seeding," he said quietly.

"You've read the article too."

"Everyone's read the article."

"There's a comment in the header." Her voice cracked on it, and that made her furious, so she said the rest faster. "A developer's comment. Lowercase Latin tag, a stupid pun. *Ut apes. Bee back in an hour.* And I know whose it is. I know exactly whose it is, because it was on our fridge. It was on our fridge every day until I was ten years old."

She heard herself say *our*. She heard him hear it.

"My name's Reeves," she said. "It's not a coincidence. It's not *a common name*. He's my father. The man in the article. He's my father, and he's alive, and he did this, and I've been sitting in that room for two weeks being *proud* of myself." She was crying now, and she hated it, and she went on anyway. "He killed her. He killed a Deputy Minister because she was going to close him down, and he made forty people watch somebody else do it, and he put it in the header, Pieter. He *signed* it. He always has to leave a note."

Pieter didn't say anything for a long time. She wiped her face and glared at the opposite wall and waited for him to say he was sorry, or any of the things people said.

He said, "May I see it?"

She held out her tablet. He took it and read the header the way she would have read it, field by field, with his lips pressed together. He read the comment twice.

"People don't leave comments in payloads," he said at last. Carefully, as if he were testing the weight of each word before he set it down. "Not in anything that's going to leave the building."

"He did. He always did. He left notes on the milk." She took the tablet back. "You don't know him."

"No," Pieter said. "I don't." He was quiet again. Then: "Who else knew the joke?"

She stared at him. "What?"

"The bees. The fridge. Who else would know it?"

"Nobody. Me. My mother." She laughed, and it came out wrong. "Anyone who ever stood in our kitchen, I suppose. He had colleagues round. He used to show off the notes like they were clever." She shook her head. "It doesn't matter. It's him. I'd know it anywhere."

Pieter nodded slowly, as though he were filing that, rather than agreeing with it. He looked at his hands again.

"What are you going to do?" he asked.

"I don't know." She pressed her palms against the cold wall behind her. "If I report it, I'm the daughter who turned him in. Or the daughter who was put here to find it. If I don't, I'm hiding it. For him." Her voice went hard. "I am not hiding anything for him. I'd rather die."

"Then don't decide today," Pieter said.

It was the only advice he gave her. He didn't tell her anything about himself. He just sat on the step, a dull man with a beard and glasses he didn't seem to need, who listened like someone who had once needed very badly to be listened to, and after a while he held out a paper napkin from his pocket, slightly greasy from the noodles.

She took it. She blew her nose. She hated him a little for it, and liked him more.

"Tell no one," she said.

"I won't."

She believed him. She would wonder later why she had been so sure.

---

She was back at her desk by 15:21. At 16:40 Wei came down the room.

He did it every afternoon, a slow circuit of the desks with a cup of tea, stopping at each one for a word. He knew everyone's name, and which of the imaging team had a sister in hospital. He never stood behind anyone for long. He said it made people type worse.

She had the fact stream up on her screen. The carrier was closed. Its packet ID was on a scrap of paper under her keyboard.

He stopped beside her desk and looked at her screen.

She would never be able to prove it was any longer than he looked at anyone's. But she timed things, and she felt it the way you feel a process hang: his eyes on the band of the maintenance channel, on the place where, if she scrolled down eleven lines, 14:18:40 would be. A fraction of a second too long.

"Anything?" he asked.

"Not yet."

He nodded. He looked at her then, not at the screen, with the same calm, courteous attention he gave to everyone, the attention that had made her proud to be on his team from the first afternoon.

"Take your time," Wei said, and walked on to the next desk.

She sat with her hands in her lap. Her heart was going very fast.

It was irrational. He had given her the drive himself; of course he wanted to know what was on it. And yet she had the sudden, unreasonable feeling that he already knew what she had found, and where, and whose it was, and that *take your time* was not permission. It was a kindness offered by someone who could afford to wait.

At 18:30 she logged off, said goodnight to Pieter, who said it back without looking up, and went home.

---

Her flat was two rooms on the sixth floor, with a window onto a courtyard where someone was always practising the same four bars of a tune. She didn't turn the lights on. She sat on the floor with her back to the sofa, the way she had sat in August, and opened a message account she had not touched in four years.

It still worked. At the top of an empty list was the last message she had ever sent him, a week before the dinner. *Fine. Thursday. Not the fish place.*

She typed: *I know it was you.*

She looked at it. Five words. She deleted them.

She sat for a while in the dark and listened to the four bars in the courtyard, over and over, stopping each time on the same wrong note.

She typed it again. *I know it was you.*

It was stupid. If the account was watched, she had just told someone that she knew something. She thought about that clearly, the way she would have thought about a packet with no owner. Then she thought about the yellow squares, and *they always find their way home*, and the thirty-eight minutes, climbing and levelling and holding.

She sent it at 21:12:06.

She had expected silence, probably. The same silence as the last four years. She watched the seconds in the corner of the screen, because that was what she did.

The reply came at 21:12:46.

Forty seconds. As if he had been sitting with the account open. As if he had been waiting four years for her to write.

*No, Maya. It wasn't. But I know who writes like me now.*
