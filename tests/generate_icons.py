#!/Users/paulrentschler/Documents/projects/printablesocial/bin/python

import os, sys
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, parent)

from printablesocial import PrintableSocial


if __name__ == '__main__':
    p_social = PrintableSocial()

    img = p_social.create('facebook', 'paul.rentschler')
    img.save('tmp/facebook.png')

    img = p_social.create('twitter', 'paulrentschler')
    img.save('tmp/twitter.png')

    img = p_social.create('youtube')
    img.save('tmp/youtube.png')
