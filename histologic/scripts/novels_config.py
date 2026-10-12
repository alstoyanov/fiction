"""
Shared configuration for the novel build scripts
(create-novel-ebook.py and export-novel-html.py).

Add a book here to make both scripts build it. Each chapter entry is
(file, number, title, POV).
"""

from pathlib import Path

BOOKS = {
    "04": {
        "dir": Path("novels/04-the-correction"),
        "epub": "the-correction.epub",
        "title": "The Correction",
        "subtitle": "Novel 04 of the Histologic Series",
        "description": """Marcus Chen believed in Veridica with his whole heart, and he did everything the system asked of him. It sent him to Ashford anyway, to a silent wing of glass cells where a programme called Continuity takes the belief out of people and leaves them empty.

Seven prisoners have been chosen: a believer, an architect of the factorepo, three brothers who cannot be broken, a doctor, and a journalist. To survive they must learn to look erased while staying themselves, find each other without speaking, and escape a building that can read their minds, before the day they are due to be finished.""",
        "parts": [
    ('Prologue', [
        ('00-prologue.md', 'Prologue', 'The Conviction', 'Marcus'),
    ]),
    ('Part One: The Erasure', [
        ('01-cell-7h.md', 'Chapter 1', 'Cell 7-H', 'Marcus'),
        ('02-the-white-room.md', 'Chapter 2', 'The White Room', 'Marcus'),
        ('03-two-months.md', 'Chapter 3', 'Two Months', 'Marcus'),
        ('04-the-arrival.md', 'Chapter 4', 'The Arrival', 'Kira'),
        ('05-the-corrected.md', 'Chapter 5', 'The Corrected', 'Dmitri'),
        ('06-the-library.md', 'Chapter 6', 'The Library', 'Alexei'),
        ('07-the-observer.md', 'Chapter 7', 'The Observer', 'Tanaka'),
        ('08-the-pattern.md', 'Chapter 8', 'The Pattern', 'Isaiah'),
    ]),
    ('Part Two: The Connection', [
        ('09-the-recognition.md', 'Chapter 9', 'The Recognition', 'Marcus'),
        ('10-the-whisper.md', 'Chapter 10', 'The Whisper', 'Kira'),
        ('11-the-garden-meetings.md', 'Chapter 11', 'The Garden Meetings', 'Marcus'),
        ('12-the-discovery.md', 'Chapter 12', 'The Discovery', 'Nikolai'),
        ('13-the-revelation.md', 'Chapter 13', 'The Revelation', 'Dmitri'),
        ('14-the-message-system.md', 'Chapter 14', 'The Message System', 'Alexei'),
        ('15-the-triplet-story.md', 'Chapter 15', 'The Triplet Story', 'Nikolai'),
        ('16-the-conspiracy.md', 'Chapter 16', 'The Conspiracy', 'Marcus'),
        ('17-the-ally.md', 'Chapter 17', 'The Ally', 'Tanaka'),
    ]),
    ('Part Three: The Plan', [
        ('18-the-breaking-point.md', 'Chapter 18', 'The Breaking Point', 'Marcus'),
        ('19-the-alliance-forms.md', 'Chapter 19', 'The Alliance Forms', 'Kira'),
        ('20-the-impossible-plan.md', 'Chapter 20', 'The Impossible Plan', 'Dmitri'),
        ('21-the-single-node.md', 'Chapter 21', 'The Single Node', 'Nikolai'),
        ('22-the-sacrifice.md', 'Chapter 22', 'The Sacrifice', 'Isaiah'),
    ]),
    ('Part Four: The Storm', [
        ('23-the-fact-storm.md', 'Chapter 23', 'The Fact Storm', 'Marcus'),
        ('24-the-breakout.md', 'Chapter 24', 'The Breakout', 'Kira'),
        ('25-the-cost-of-freedom.md', 'Chapter 25', 'The Cost of Freedom', 'Dmitri'),
        ('26-the-pursuit.md', 'Chapter 26', 'The Pursuit', 'Alexei'),
    ]),
    ('Part Five: The Aftermath', [
        ('27-the-report.md', 'Chapter 27', 'The Report', 'Isaiah'),
        ('28-the-recovery.md', 'Chapter 28', 'The Recovery', 'Kira'),
        ('29-the-missions.md', 'Chapter 29', 'The Missions', 'Marcus'),
    ]),
    ('Epilogue', [
        ('30-epilogue.md', 'Epilogue', 'Seven Paths, One Truth', None),
    ]),
],
    },
    "05": {
        "dir": Path("novels/05-the-lost-hour"),
        "epub": "the-lost-hour.epub",
        "title": "The Lost Hour",
        "subtitle": "Novel 05 of the Histologic Series",
        "description": """On Monday, November 15, 2106, between two and three in the afternoon, an hour of Veridica's history disappears from every record at once. In that hour a Deputy Minister is murdered, and forty witnesses saw the killer walk into her office: Marcus Chen, a man the Registry lists as dead.

Marcus did not do it. But he was in the building, and so, for their own secret reasons, were all the people who escaped Ashford with him. To clear him they must prove that testimony can outweigh the record, in a country where the record is the truth. And the harder they fight, the more it looks as if the hour was not only erased. It was written.""",
        "parts": [
            ('Prologue', [
                ('00-prologue.md', 'Prologue', '13:59', 'Singh'),
            ]),
            ('Part One: The Missing Hour', [
                ('01-system-failure.md', 'Chapter 1', 'System Failure', 'Maya'),
                ('02-the-hearing-room.md', 'Chapter 2', 'The Hearing Room', 'Kovač'),
                ('03-the-upload.md', 'Chapter 3', 'The Upload', 'Marcus'),
                ('04-the-dead-man.md', 'Chapter 4', 'The Dead Man', 'Marcus'),
                ('05-the-coat.md', 'Chapter 5', 'The Coat', 'Isaiah'),
                ('06-the-crossing.md', 'Chapter 6', 'The Crossing', 'Tanaka'),
                ('07-the-ghosts.md', 'Chapter 7', 'The Ghosts', 'Alexei'),
                ('08-forty-witnesses.md', 'Chapter 8', 'Forty Witnesses', 'Kira'),
            ]),
            ('Part Two: The Witnesses', [
                ('09-recruitment.md', 'Chapter 9', 'Recruitment', 'Nikolai'),
                ('10-another-day-in-paradise.md', 'Chapter 10', 'Another Day in Paradise', 'Marcus'),
                ('11-erase-then-seed.md', 'Chapter 11', 'Erase, Then Seed', 'Tanaka'),
                ('12-the-singer.md', 'Chapter 12', 'The Singer', 'Old Songs'),
                ('13-the-only-clean-witness.md', 'Chapter 13', 'The Only Clean Witness', 'Dmitri'),
                ('14-the-carrier.md', 'Chapter 14', 'The Carrier', 'Maya'),
                ('15-the-doctrine.md', 'Chapter 15', 'The Doctrine', 'Kovač'),
                ('16-the-source.md', 'Chapter 16', 'The Source', 'Kira'),
                ('17-how-the-hour-was-written.md', 'Chapter 17', 'How the Hour Was Written', 'Isaiah'),
            ]),
            ('Part Three: The Source', [
                ('18-protective-custody.md', 'Chapter 18', 'Protective Custody', 'Marcus'),
                ('19-the-resurrection.md', 'Chapter 19', 'The Resurrection', 'Alexei'),
                ('20-confessions.md', 'Chapter 20', 'Confessions', 'Nikolai'),
                ('21-the-annex.md', 'Chapter 21', 'The Annex', 'Kira'),
                ('22-the-body.md', 'Chapter 22', 'The Body', 'Tanaka'),
                ('23-a-very-good-case.md', 'Chapter 23', 'A Very Good Case', 'Dmitri'),
                ('24-i-remember-doing-it.md', 'Chapter 24', 'I Remember Doing It', 'Marcus'),
            ]),
            ('Part Four: The Verdict', [
                ('25-the-hearing.md', 'Chapter 25', 'The Hearing', 'Kovač'),
                ('26-status-living.md', 'Chapter 26', 'Status: Living', 'Marcus'),
                ('27-the-editor.md', 'Chapter 27', 'The Editor', 'Isaiah'),
                ('28-the-signature.md', 'Chapter 28', 'The Signature', 'Kira'),
                ('29-desk-14-09.md', 'Chapter 29', 'Desk 14-09', 'Marcus'),
                ('30-the-dilemma.md', 'Chapter 30', 'The Dilemma', 'Old Songs'),
                ('31-the-commission.md', 'Chapter 31', 'The Commission', 'Marcus'),
            ]),
            ('Epilogue', [
                ('32-epilogue.md', 'Epilogue', 'One Year Later', None),
            ]),
        ],
    },
    "06": {
        "dir": Path("novels/06-the-distributed-truth"),
        "epub": "the-distributed-truth.epub",
        "title": "The Distributed Truth",
        "subtitle": "Novel 06 of the Histologic Series",
        "description": """Seventeen minutes vanish from the life-logs of Chronos, a nation that records every heartbeat, and the scar of the Lost Hour is in the wound. Two nations slide into a war of facts. Veridica asks its most trusted restorer, Marcus Chen, to end it by manufacturing the trust of Chronos's senior historian, a lonely man who admires him.

Marcus refuses, and publishes everything, by many hands, in three nations at once. The war stops. Then the government confesses first and offers the remedy the heroes always wanted: an index of every citizen's journal. The design has anticipated every reformer. Now it has to anticipate everyone.""",
        "parts": [
            ('Prologue', [
                ('00-prologue.md', 'Prologue', 'The Doubled Pier', 'Ruth'),
            ]),
            ('Part One: The War of Facts', [
                ('01-the-seventeen-minutes.md', 'Chapter 1', 'The Seventeen Minutes', 'Kira'),
                ('02-kindred.md', 'Chapter 2', 'KINDRED', 'Marcus'),
                ('03-the-sealed-ward.md', 'Chapter 3', 'The Sealed Ward', 'Tanaka'),
                ('04-the-kestrel-book.md', 'Chapter 4', 'The Kestrel Book', 'Ruth'),
                ('05-the-compilers-voice.md', 'Chapter 5', "The Compiler's Voice", 'Old Songs'),
                ('06-the-lakes-talks.md', 'Chapter 6', 'The Lakes Talks', 'Marcus'),
                ('07-aunt-helena.md', 'Chapter 7', 'Aunt Helena', 'Kovač'),
                ('08-meridian.md', 'Chapter 8', 'MERIDIAN', 'Marcus'),
            ]),
            ('Part Two: The Fragments', [
                ('09-the-true-source.md', 'Chapter 9', 'The True Source', 'Kira'),
                ('10-the-calibration-grounds.md', 'Chapter 10', 'The Calibration Grounds', 'Dmitri'),
                ('11-seventeen-minutes-asleep.md', 'Chapter 11', 'Seventeen Minutes Asleep', 'Julian'),
                ('12-the-third-fragment.md', 'Chapter 12', 'The Third Fragment', 'Isaiah'),
                ('13-the-table-of-contents.md', 'Chapter 13', 'The Table of Contents', 'Old Songs'),
                ('14-stabilisation.md', 'Chapter 14', 'Stabilisation', 'Tanaka'),
                ('15-the-warning.md', 'Chapter 15', 'The Warning', 'Marcus'),
                ('16-fourteen-hundred.md', 'Chapter 16', 'Fourteen Hundred', 'Ruth'),
            ]),
            ('Part Three: The Concordance', [
                ('17-the-remedy.md', 'Chapter 17', 'The Remedy', 'Marcus'),
                ('18-the-league-of-the-record.md', 'Chapter 18', 'The League of the Record', 'Nikolai'),
                ('19-the-false-entry.md', 'Chapter 19', 'The False Entry', 'Ruth'),
                ('20-the-crossing.md', 'Chapter 20', 'The Crossing', 'Alexei'),
                ('21-mrs-kerr.md', 'Chapter 21', 'Mrs. Kerr', 'Tanaka'),
                ('22-two-old-people.md', 'Chapter 22', 'Two Old People', 'Old Songs'),
                ('23-the-drafts.md', 'Chapter 23', 'The Drafts', 'Maya'),
                ('24-the-remedy-was-ready.md', 'Chapter 24', 'The Remedy Was Ready', 'Kira'),
            ]),
            ('Part Four: Many Hands', [
                ('25-0-58.md', 'Chapter 25', '0.58', 'Marcus'),
                ('26-the-night-of-copies.md', 'Chapter 26', 'The Night of Copies', 'Dmitri'),
                ('27-the-compilers-confession.md', 'Chapter 27', "The Compiler's Confession", 'Vance'),
                ('28-the-reply.md', 'Chapter 28', 'The Reply', 'Kira'),
                ('29-thank-you.md', 'Chapter 29', 'Thank You', 'Marcus'),
                ('30-two-hands.md', 'Chapter 30', 'Two Hands', 'Nikolai'),
            ]),
            ('Epilogue', [
                ('31-epilogue.md', 'Epilogue', 'The Round', None),
            ]),
        ],
    },
    "07": {
        "dir": Path("novels/07-battle-of-truths"),
        "epub": "battle-of-truths.epub",
        "title": "Battle of Truths",
        "subtitle": "Novel 07 of the Histologic Series",
        "description": """Two million journals are rewritten in a single night, and the countersignature belongs to the Chronos Archive key that Julian Kovač holds. Marcus Chen checks the record, and the record says what he fears. So he asks for the operation he once refused: to use the trust of the man he befriended, enter the Archive, and cut one hand out of Chronos's past.

It works far beyond its purpose. The two nations' records turn out to be one system, and Chronos wakes believing Veridica's history. Then the truth comes in, piece by piece, and none of it helps: Julian was innocent, a letter proves it, and someone in Veridica has been handing the enemy a war before it happened.""",
        "parts": [
            ('Prologue', [
                ('00-prologue.md', 'Prologue', 'The Rewriting', 'Ruth'),
            ]),
            ('Part One: The Rewriting', [
                ('01-two-million-journals.md', 'Chapter 1', 'Two Million Journals', 'Kira'),
                ('02-julian.md', 'Chapter 2', 'Julian?', 'Marcus'),
                ('03-gullhaven.md', 'Chapter 3', 'Gullhaven', 'Ruth'),
                ('04-chronos-believes.md', 'Chapter 4', 'Chronos Believes', 'Tanaka'),
                ('05-the-attache.md', 'Chapter 5', 'The Attaché', 'Isaiah'),
                ('06-i-cant-authorise-this.md', 'Chapter 6', "I Can't Authorise This", 'Marcus'),
                ('07-the-falling-phrase.md', 'Chapter 7', 'The Falling Phrase', 'Old Songs'),
                ('08-the-knife.md', 'Chapter 8', 'The Knife', 'Kira'),
            ]),
            ('Part Two: RESTORATION', [
                ('09-lessons.md', 'Chapter 9', 'Lessons', 'Marcus'),
                ('10-the-brother.md', 'Chapter 10', 'The Brother', 'Julian'),
                ('11-copy-vii.md', 'Chapter 11', 'Copy VII', 'Dmitri'),
                ('12-the-diplomats-page.md', 'Chapter 12', "The Diplomat's Page", 'Isaiah'),
                ('13-the-two-maps.md', 'Chapter 13', 'The Two Maps', 'Old Songs'),
                ('14-the-image.md', 'Chapter 14', 'The Image', 'Kira'),
                ('15-the-key.md', 'Chapter 15', 'The Key', 'Marcus'),
                ('16-one-source.md', 'Chapter 16', 'One Source', 'Kira'),
            ]),
            ('Part Three: The Awakening', [
                ('17-the-causeway.md', 'Chapter 17', 'The Causeway', 'Alexei'),
                ('18-the-awakening.md', 'Chapter 18', 'The Awakening', 'Tanaka'),
                ('19-they-wrote-us.md', 'Chapter 19', 'They Wrote Us', 'Aubry'),
                ('20-a-diplomatic-breakthrough.md', 'Chapter 20', 'A Diplomatic Breakthrough', 'Marcus'),
                ('21-maximum.md', 'Chapter 21', 'Maximum', 'Julian'),
                ('22-the-restorer.md', 'Chapter 22', 'The Restorer', 'Isaiah'),
                ('23-some-of-it.md', 'Chapter 23', 'Some of It', 'Elena'),
                ('24-the-folder.md', 'Chapter 24', 'The Folder', 'Kovač'),
            ]),
            ('Part Four: The Price', [
                ('25-no-remedy.md', 'Chapter 25', 'No Remedy', 'Marcus'),
                ('26-the-speech.md', 'Chapter 26', 'The Speech', 'Old Songs'),
                ('27-by-many-hands.md', 'Chapter 27', 'By Many Hands', 'Kira'),
                ('28-enemies-outside.md', 'Chapter 28', 'Enemies Outside', 'Isaiah'),
                ('29-colonel.md', 'Chapter 29', 'Colonel', 'Sokolov'),
                ('30-battle-of-truths.md', 'Chapter 30', 'Battle of Truths', 'Marcus'),
            ]),
            ('Epilogue', [
                ('31-epilogue.md', 'Epilogue', 'The Coast', None),
            ]),
        ],
    },
    "08": {
        "dir": Path("novels/08-battle-of-blood"),
        "epub": "battle-of-blood.epub",
        "title": "Battle of Blood",
        "subtitle": "Novel 08 of the Histologic Series",
        "description": """An SFW fleet lands on Veridica's Atlantic coast. Its soldiers have no interfaces, so no storm can turn them and no seeding can reach them, and every weapon Veridica spent forty years perfecting is useless. The Sovereignty has come for The Judge, which now holds the record of two nations, and the heroes fight a war they were never built for.

Then they learn who invited it. Behind the front, under cover of the invasion, a whole people is being corrected by broadcast, and the order quotes a principle written in 1966. At the end, with the enemy at the gates, the First Minister signs the machine away to save the city, and that act, not a bomb, ends The Judge, by its maker's hidden design. This time the heroes ask Chronos first.""",
        "parts": [
            ('Prologue', [
                ('00-prologue.md', 'Prologue', 'Landfall', 'Sokolov'),
            ]),
            ('Part One: Landfall', [
                ('01-questions-for-the-war.md', 'Chapter 1', 'Questions for the War', 'Marcus'),
                ('02-no-storm-will-turn-them.md', 'Chapter 2', 'No Storm Will Turn Them', 'Dmitri'),
                ('03-embedded.md', 'Chapter 3', 'Embedded', 'Isaiah'),
                ('04-the-names-longer.md', 'Chapter 4', 'The Names, Longer', 'Old Songs'),
                ('05-the-judge-at-war.md', 'Chapter 5', 'The Judge at War', 'Kira'),
                ('06-field-hospital.md', 'Chapter 6', 'Field Hospital', 'Tanaka'),
                ('07-behind-the-lines.md', 'Chapter 7', 'Behind the Lines', 'Elena'),
                ('08-who-is-invading-whom.md', 'Chapter 8', 'Who Is Invading Whom?', 'Marcus'),
            ]),
            ('Part Two: The Leak', [
                ('09-the-wine-was-open.md', 'Chapter 9', 'The Wine Was Open', 'Sokolov'),
                ('10-nora.md', 'Chapter 10', 'Nora', 'Isaiah'),
                ('11-two-nations-one-core.md', 'Chapter 11', 'Two Nations, One Core', 'Nikolai'),
                ('12-ashford.md', 'Chapter 12', 'Ashford', 'Kovač'),
                ('13-artillery.md', 'Chapter 13', 'Artillery', 'Alexei'),
                ('14-release.md', 'Chapter 14', 'Release', 'Maya'),
                ('15-siege.md', 'Chapter 15', 'Siege', 'Marcus'),
                ('16-not-before.md', 'Chapter 16', 'Not Before', 'Old Songs'),
            ]),
            ('Part Three: The Broadcast', [
                ('17-certainty-is-care.md', 'Chapter 17', 'Certainty Is Care', 'Tanaka'),
                ('18-read-your-own-book.md', 'Chapter 18', 'Read Your Own Book', 'Kira'),
                ('19-across-the-lines.md', 'Chapter 19', 'Across the Lines', 'Isaiah'),
                ('20-thirty-seconds.md', 'Chapter 20', 'Thirty Seconds', 'Dmitri'),
                ('21-the-sympathisers.md', 'Chapter 21', 'The Sympathisers', 'Marcus'),
                ('22-dad.md', 'Chapter 22', 'Dad', 'Maya'),
                ('23-silence.md', 'Chapter 23', 'Silence', 'Nikolai'),
            ]),
            ('Part Four: Seven', [
                ('24-terms.md', 'Chapter 24', 'Terms', 'Marcus'),
                ('25-the-page.md', 'Chapter 25', 'The Page', 'Kira'),
                ('26-consent.md', 'Chapter 26', 'Consent', 'Julian'),
                ('27-the-core.md', 'Chapter 27', 'The Core', 'Nora Chen'),
                ('28-truth-endures.md', 'Chapter 28', 'Truth Endures', 'Kira'),
                ('29-elise.md', 'Chapter 29', 'Elise', 'Old Songs'),
                ('30-it-moved.md', 'Chapter 30', 'It Moved', 'Marcus'),
            ]),
            ('Epilogue', [
                ('31-epilogue.md', 'Epilogue', 'The Names', None),
            ]),
        ],
    },
    "09": {
        "dir": Path("novels/09-architects-of-chaos"),
        "epub": "architects-of-chaos.epub",
        "title": "Architects of Chaos",
        "subtitle": "Novel 09 of the Histologic Series",
        "description": """Five years after both Judges died, the world is learning to live without a machine that decides. Then the dead come back: a Deputy Minister murdered in the Lost Hour walks out of a crowd, and an old archivist solves the riddle that leads to the Compiler's own copy of the manuscript, hidden for fifty years behind an unanswered letter. It names the twelve who designed the world, and almost every name is a family.

When the heroes move to publish the names by many hands, the designers disclose first, and offer the peace everyone wants: one record for every nation, restored from a single source. It is the last trap, and the man they prepared to keep it is the one who has spent his life refusing. The series ends where it began, with a stone, a song, and the choice between one record and many hands.""",
        "parts": [
            ('Prologue', [
                ('00-prologue.md', 'Prologue', 'The Fifteenth', 'Tanaka'),
            ]),
            ('Part One: The Riddle', [
                ('01-where-is-east.md', 'Chapter 1', 'Where Is East?', 'Marcus'),
                ('02-the-shelf-of-us.md', 'Chapter 2', 'The Shelf of Us', 'Old Songs'),
                ('03-the-third-site.md', 'Chapter 3', 'The Third Site', 'Kira'),
                ('04-carver-street.md', 'Chapter 4', 'Carver Street', 'Isaiah'),
                ('05-the-filed-woman.md', 'Chapter 5', 'The Filed Woman', 'Singh'),
                ('06-the-man-at-1421.md', 'Chapter 6', 'The Man at 14:21', 'Marcus'),
                ('07-ask-him-twice.md', 'Chapter 7', 'Ask Him Twice', 'Old Songs'),
                ('08-the-second-letter.md', 'Chapter 8', 'The Second Letter', 'Kovač'),
            ]),
            ('Part Two: The Register', [
                ('09-the-annex.md', 'Chapter 9', 'The Annex', 'Kira'),
                ('10-the-register.md', 'Chapter 10', 'The Register', 'Dmitri'),
                ('11-the-parlour.md', 'Chapter 11', 'The Parlour', 'Isaiah'),
                ('12-the-administrator.md', 'Chapter 12', 'The Administrator', 'Sokolov'),
                ('13-heirs.md', 'Chapter 13', 'Heirs', 'Tanaka'),
                ('14-uncle-tobias.md', 'Chapter 14', 'Uncle Tobias', 'Julian'),
                ('15-copy-x.md', 'Chapter 15', 'Copy X', 'Marcus'),
                ('16-ra-12.md', 'Chapter 16', 'RA·12', 'Nikolai'),
            ]),
            ('Part Three: The Disclosure', [
                ('17-many-hands-once-more.md', 'Chapter 17', 'Many Hands, Once More', 'Kira'),
                ('18-cast.md', 'Chapter 18', 'Cast', 'Martinez'),
                ('19-the-orchard.md', 'Chapter 19', 'The Orchard', 'Elena'),
                ('20-disclosed.md', 'Chapter 20', 'Disclosed', 'Isaiah'),
                ('21-the-peace-everyone-wants.md', 'Chapter 21', 'The Peace Everyone Wants', 'Marcus'),
                ('22-no-revenge.md', 'Chapter 22', 'No Revenge', 'Dmitri'),
                ('23-one-source-again.md', 'Chapter 23', 'One Source, Again', 'Kira'),
                ('24-the-heir.md', 'Chapter 24', 'The Heir', 'Marcus'),
            ]),
            ('Part Four: Many Hands', [
                ('25-on-keeping.md', 'Chapter 25', 'On Keeping', 'Old Songs'),
                ('26-refused.md', 'Chapter 26', 'Refused', 'Marcus'),
                ('27-the-checkpoint.md', 'Chapter 27', 'The Checkpoint', 'Sokolov'),
                ('28-a-better-enemy.md', 'Chapter 28', 'A Better Enemy', 'Isaiah'),
                ('29-containment.md', 'Chapter 29', 'Containment', 'Dmitri'),
                ('30-the-lakeshore-air.md', 'Chapter 30', 'The Lakeshore Air', 'Marcus'),
            ]),
            ('Epilogue', [
                ('31-epilogue.md', 'Epilogue', 'Twenty Years', None),
            ]),
        ],
    },
}


def select_books(argv):
    """Books named on the command line (e.g. `05`), or all of them."""
    keys = [a for a in argv if a in BOOKS]
    unknown = [a for a in argv if a not in BOOKS]
    if unknown:
        raise SystemExit(f"Unknown book(s): {', '.join(unknown)}. Choose from: {', '.join(BOOKS)}")
    return keys or list(BOOKS)
