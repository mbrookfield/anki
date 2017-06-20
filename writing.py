import os
import random
import sys
sys.path.append('/usr/share/anki')
from anki import Collection  # noqa


def main():
    """
    Pick 10 random words from Vocabulary deck for handwriting practice.

    * don't select unseen or learning cards
    * longer than 1 character
    """

    collection_path = '~/etc/anki/user/collection.anki2'
    col = Collection(os.path.expanduser(collection_path))
    cards = col.findCards('deck:Vocabulary')
    vocabulary = []
    for _id in cards:
        card = col.getCard(_id)
        if card.type == 2:
            note = col.getNote(card.nid)
            if len(note.fields[0]) > 1:
                vocabulary.append(note.fields[0])
    col.close()
    selection = random.choices(vocabulary, k=10)
    print('\n'.join(selection))


if __name__ == "__main__":
    main()
