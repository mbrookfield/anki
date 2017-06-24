import os
import random
import sys
sys.path.append('/usr/share/anki')
from anki import Collection  # noqa


def main():
    """
    Pick 5 random lapsed words from Vocabulary deck for review.
    """

    collection_path = '~/etc/anki/user/collection.anki2'
    col = Collection(os.path.expanduser(collection_path))
    cards = col.findCards('deck:Vocabulary')
    vocabulary = []
    for _id in cards:
        card = col.getCard(_id)
        if card.lapses != 0:
            note = col.getNote(card.nid)
            vocabulary.append(note.fields[0])
    col.close()
    selection = random.sample(vocabulary, k=5)
    print('\n'.join(selection))


if __name__ == "__main__":
    main()
