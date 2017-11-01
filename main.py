#!/usr/bin/env python
import sys, os, random
import sentgen
from PIL import ImageStat
from PIL import ImageFilter
from pimage import PerlinImage
from clamour import threshold
from clamour import rorschach
from clamour import camo
from clamour import ribbons
from clamour import verse


pleasantries = ['Hail Eris...',
    '23',
    'Got any Slack?',
    'Don\'t fnordget yourself.',
    'It never gets any easier.  Or harder.',
    'X Day Approaches.',
    'Fought any interdimensional sex jellies recently?',
    'I wouldn\'t put that there if I were you.',
    'I can hear what you\'re thinking.',
    'Do you really think you can get away with this?',
    'Never submit.',
    'That will be $110 NuBux please.',
    'This bill is never due.',
    'This bill is always due.',
    'I feel weird.']


def chant():
    s = ''
    return s
    
def lowMurmur():
    s = ''
    return s
    
def ecstaticRoar():
    s = ''
    return s
    
def bodilySacrifice():
    s = ''
    return s
    
def spiritualSacrifice():
    s = ''
    return s

def introspect():
    pass
    
def generateOaths():
    s = ''
    return s
    
def generateGestrures():
    s = ''
    return s

sacrificial_corpus = pleasantries[random.choice(range(len(pleasantries)))]

sacred_energy = introspect()

if __name__ == '__main__':
    #pimage = PerlinImage((300,500), scale=1.5, octaves=4, base=random.random()*500).renderImage()
    #pimage.save('intermediate.png')
    #timage = threshold(pimage, 128)
    #timage.save('testthresh.png')
#    csum = 0.0
#    for item in xrange(10):
        #rimage = rorschach((250,250), threshlevel=random.randint(108,128), symmetry='b', scale=.75, octaves=5, base=random.random()*500)
#        rimage = rorschach((250,250), threshlevel=random.randint(108,128), symmetry='b', scale=1, octaves=2, base=random.random()*500)
#        rimage.save('testschach{}.png'.format(str(item)))
        #print(rimage.histogram())
#        imagemean = ImageStat.Stat(rimage).mean[0] / 255
#        print(imagemean)
#        csum += imagemean
#    print(csum / 10)
#    goop = goop()
#    goop.save('goop.png')
    #camofimg = camo((600,600), scale=2.0)
    #camofimg.save('camo.png')
    #pimage = PerlinImage((600,600), scale=1.5, octaves=1, base=random.random()*500).renderImage()
    #pimage.save('perlin.png')
    #rimage = ribbons(pimage, color='#90EE90', bg='#ffffff00', stops=(128,129))
    #rimage.save('ribbons.png')
    for i in xrange(5):
        vimg = verse((300,300), 'Moon Flower Bold.ttf')
        vimg.save('vimg{}.png'.format(i))

# generate a palette
# generate some text


