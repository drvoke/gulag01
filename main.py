import sys, os, random, noise
from PIL import Image
from PIL import ImageDraw

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

class PerlinImage(object):
    def __init__(self, size):
        self.size = size
        self.image = Image.new("RGB", self.size)
        self.listRep = genlist2d(self.size[0], self.size[1])

    def populateRep(self, **kwargs):
        for row in range(len(self.listRep)):
            for col in range(len(row)):
                print(str(row) + '= row\n' + str(col) + '= col')
                self.listRep[row][col] = noise.snoise2(float(col) / self.size[0], float(row) / self.size[1], **kwargs)
                
    def getValueAt(self, x, y):
        return self.listRep[y][x]
        
    def renderImage(self):
        width = self.size[0]
        height = self.size[1]
        imdraw = ImageDraw.Draw(self.image)
        for row in xrange(len(self.listRep)):
            for col in xrange(len(row)):
                value = ((getValueAt(col, row) + 1) / 2) * 255
                imdraw.point((col,row), (value, value, value))
        return self.image
        
    def saveImage(filename, mode=None):
        self.image.save(filename, mode)




class Coords2d(object):
    def __init__(self, x=None, y=None):
        if x:
            self._x = int(x)
        else:
            self._x = 0
        if y:
            self._y = int(y)
        else:
            self._y = 0
     
    @property
    def x(self):
        return self._x
     
    @x.setter
    def x(self, value):
        self._x = int(value)
         
    @x.deleter
    def x(self):
        pass
         
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = int(value)
        
    @y.deleter
    def y(self):
        pass
    
    
class Coords3d(object):
    def __init__(self, x=None, y=None, z=None):
        if x:
            self._x = x
        else:
            self._x = 0
        if y:
            self._y = y
        else:
            self._y = 0
        if z:
            self._z = z
        else:
            self._z = 0
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = int(value)
    
    @x.deleter
    def x(self):
        pass
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = int(value)
    
    @x.deleter
    def y(self):
        pass
    
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, value):
        self._z = int(value)
    
    @z.deleter
    def z(self):
        pass


def genlist2d(rows, cols):
    list2d = [[0 for col in range(cols)] for row in range(rows)]
    return list2d


if __name__ == '__main__':
    pimg = PerlinImage((300,300))
    pimg.populateRep()
    
    
