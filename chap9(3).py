import os
import re
import shutil

folder = input("Enter the absolute path of the folder you'd like to search: ")

prefix = input("Enter the prefix (up to the numbering) of the files whose"
               "numbering you'd like to check: ")

ordered_regex = re.compile(r'({0})(\d*)(.*)(\..*)'.format(prefix))

found = []
for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:

        if ordered_regex.search(filename) is not None:

            num_length = int(len(ordered_regex.search(filename).group(2)))

            extension = ordered_regex.search(filename).group(4)

            found.append(ordered_regex.search(filename).group(2))

    ordered = sorted([int(x) for x in found])

for number in range(1, len(found) + 1):

    zeroes = '0' * (num_length - len(str(number)))

    current_file = '{}/{}{}{}{}'.format(folder, prefix, zeroes,
                                        number, extension)

    if os.path.exists(current_file) is False:
        next_num = ordered[number - 1]
        next_zeroes = '0' * (num_length - len(str(next_num)))
        next_file = (folder + '/' + prefix + str(next_zeroes)
                     + str(next_num) + extension)

        shutil.move(next_file, current_file)

print('File numbering has been fixed.')