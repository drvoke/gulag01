import sys, os, random, noise, time
from PIL import Image
from PIL import ImageDraw


class PerlinImage(object):
    def __init__(self, size, scale=1, **kwargs):
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.scale = scale
        self.image = Image.new("L", self.size)
        self.listRep = None
        self.keywords = kwargs

    def toRGB(self, value):
        return int(round(((value + 1) / 2) * 255))
        
    def generateRep(self):
        keywords = self.keywords
        scale = self.scale
        width = self.width
        height = self.height
        ratio = float(height) / width
        rep = genlist2d(height, width)
        for row in xrange(height):
            noisey = (float(row) / height) * (scale * ratio)
            for col in xrange(width):
                noisex = (float(col) / width) * scale
                rep[row][col] = self.toRGB(noise.snoise2(noisex, noisey, **keywords))
        return rep
    
    def getValueAt(self, x, y):
        return self.listRep[y][x]
    
    def getValueFrom(self, rep, x, y):
        return rep[y][x]
     
    def renderImage(self):
        if self.listRep is None:
            self.listRep = self.generateRep()
        rep = self.listRep
        width = self.width
        height = self.height
        impix = self.image.load()
        for row in xrange(height):
            for col in xrange(width):
                value = rep[row][col]
                impix[col,row] = (value)
        return self.image
        
    def saveImage(self, filename, mode=None):
        self.image.save(filename, mode)
        
    def printRep(self, sep):
        if self.listRep is None:
            self.listRep = self.generateRep()
        rep = self.listRep
        width = self.width
        height = self.height
        superset = []
        for row in (item for item in xrange(height) if item % sep == 0):
            subset = []
            for col in (item for item in xrange(width) if item % sep == 0):
                subset.append(self.getValueFrom(rep, col, row))
            superset.append(subset)
        topstr = '+---'*(width/sep)+'+'
        print(topstr)
        for row in superset:
            rowstr = ''
            for col in row:
                zero_padding_amt = 3 - len(str(col))
                rowstr+='|{}'.format('0'*zero_padding_amt + str(col))
            rowstr+='|'
            print(rowstr)
            print(topstr)
            
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

def outputTester(reps):
    for i in xrange(int(reps)):
        start = time.clock()
        pimg = PerlinImage((300,300), scale=1.0, octaves=4, persistence=0.6, lacunarity=2.0, base=random.random()*500.0)
        end = time.clock()
        print('300x300 PerlinImage object created in {} seconds.'.format(str(end - start)))
        start = time.clock()
        pimg.renderImage()
        end = time.clock()
        print('300x300 PerlinImage image rendered in {} seconds.'.format(str(end - start)))
        start = time.clock()
        pimg.saveImage('test{}.png'.format(str(i)))
        end = time.clock()
        print('300x300 PerlinImage image saved to disk in {} seconds.'.format(str(end - start)))

if __name__ == '__main__':
    outputTester(10)
    
    
    
