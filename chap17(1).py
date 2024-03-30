import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_im = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_im.size

os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
            or filename.lower().endswith('.gif') or filename.lower().endswith('bmp')) \
            or filename == LOGO_FILENAME:
        continue   
    im = Image.open(filename)
    width, height = im.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

    print('Resizing {}...'.format(filename))
    im = im.resize((width, height))

    width, height = im.size
    if width < logo_width * 2 or height < logo_height * 2:
        print("The logo wouldn't look good on an image this size so "
              "it is being skipped. The unadorned image will still be saved "
              "to the 'withLogo' directory.")
    else:
        print('Adding logo to {}...'.format(filename))
        im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)

    im.save(os.path.join('withLogo', filename))