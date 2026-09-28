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
}


def select_books(argv):
    """Books named on the command line (e.g. `05`), or all of them."""
    keys = [a for a in argv if a in BOOKS]
    unknown = [a for a in argv if a not in BOOKS]
    if unknown:
        raise SystemExit(f"Unknown book(s): {', '.join(unknown)}. Choose from: {', '.join(BOOKS)}")
    return keys or list(BOOKS)
