import re

def strip(text, remove=''):
    if remove == '':
        space_regex = re.compile(r'^(\s*)(\S*)(\s)*$')
        trimmed = space_regex.search(text)
        return trimmed.group(2)
    else:
        remove_start = re.compile(r'^([%s]+)' % remove)
        remove_end = re.compile(r'([%s]+)$' % remove)
        start = remove_start.search(text)
        end = remove_end.search(text)
        try:
            return text[len(start.group()):len(text) - len(end.group())]
        except AttributeError:
            error_avoid = remove + text + remove
            return strip(error_avoid, remove)
user_text = input('Enter the text you would like stripped here: ')
user_remove = input('Enter the character you want stripped here'
                    ' (Removes Space as Default): ')

print(strip(user_text, user_remove))
