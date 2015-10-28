
from src.common.functions import searchDict

class Mapping:
    def __init__(self, tup):
        self.up(tup)
        
    def asTuple(self):
        return tuple(self.tup)
    
    def up(self, tup):
        self.tup = tup
        try:
            self.id = tup[0]
            self.server = searchDict(tup[1], 'Address')
            self.db = searchDict(tup[1], 'DatabaseName')
            self.path = searchDict(tup[1], 'FileLocation')
            self.update = searchDict(tup[1], 'LastUpdate')
            self.begin = searchDict(tup[1], 'Beginning')
            self.period = u'%s %s' % (searchDict(tup[1], 'Time'),
                searchDict(tup[1], 'Frequency'))
        except KeyError as e:
            print e
    
    def getId(self):
        return self.id

    def __unicode__(self):
        return unicode(self).encode('utf-8')

