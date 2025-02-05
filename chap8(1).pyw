import shelve
import sys
import pyperclip

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print(sys.argv[2] + ' saved successfully')

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
    print([sys.argv[2] + ' deleted'])

elif len(sys.argv) == 2 and sys.argv[1].lower() != 'delete_all':
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print('List of all keywords copied to clipboard')
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print(sys.argv[1] + ' loaded successfully')
    else:
        print('That keyword doesn\'t exist - so nothing'
              'has been loaded to the clipboard')
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete_all':
    mcb_shelf.clear()
    print('All keywords and associated contents have been deleted')

mcb_shelf.close()
