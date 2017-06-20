from collections import OrderedDict
import json
import os
import sys
sys.path.append('/usr/share/anki')
from anki import Collection  # noqa


def main():
    """
    Build a list of common words from jmdict-simplified that match the
    following conditions:

    * must contain kanji
    * only have known kanji (data/kanji.txt)
    * does not already exist in anki deck 'Vocabulary'
    * not in blacklist (data/blacklist.txt)

    https://github.com/scriptin/jmdict-simplified
    """

    collection_path = '~/etc/anki/user/collection.anki2'
    col = Collection(os.path.expanduser(collection_path))
    notes = col.findNotes('deck:Vocabulary')
    existing = []
    for _id in notes:
        note = col.getNote(_id)
        existing.append(note.fields[0])
    col.close()

    valid = ''.join([chr(i) for i in range(12352, 12543)])
    vocabulary = []

    with open('data/blacklist.txt', 'r') as f:
        blacklist = f.read().split()
    with open('data/kanji.txt', 'r') as f:
        known = [char for char in f.read()]
    with open('data/jmdict_eng_common.json', 'r') as f:
        jmdict = json.load(f)

    for word in jmdict['words']:
        for kanji in word['kanji']:
            if kanji['common'] is True:
                readable = True
                for char in kanji['text']:
                    if (char not in known) and (char not in valid):
                        readable = False
                if readable and (kanji['text'] not in existing):
                    if kanji['text'] not in blacklist:
                        vocabulary.append(kanji['text'])
    vocabulary = list(OrderedDict.fromkeys(vocabulary))

    print('words found: ' + str(len(vocabulary)))
    with open('data/words.txt', 'w') as f:
        f.write('\n'.join(vocabulary))


if __name__ == "__main__":
    main()
