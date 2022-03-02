from dbmanager import get_meaning

from sys import argv

meanings = get_meaning(argv[1], argv[2], json_out=True)
print(meanings)
meanings = get_meaning(argv[1], argv[2], json_out=False)

for entry in meanings:
    print('«' + entry['word'] + '» یعنی «' + entry['definition'] + '»')
