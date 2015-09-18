
import datetime
import wx

def searchDict(obj, key, lvl=0):
    # Base case: key is in the first level of dictionary.
    if key in obj:
        return obj[key]
    # Key is not in the first level of the dictionary.
    # Loop through keys to find nested dictionaries.
    for k,v in obj.items():
        # Recurse if a dictionary is found.
        if isinstance(v, dict):
            item = searchDict(v, key, lvl+1)
            if item is not None:
                return item
    # If we're done looking and key still has not
    # been found, then raise a KeyError
    if lvl == 0:
        raise KeyError(key)

 
def pydate2wxdate(date):
     assert isinstance(date, (datetime.datetime, datetime.date))
     tt = date.timetuple()
     dmy = (tt[2], tt[1]-1, tt[0])
     return wx.DateTimeFromDMY(*dmy)

 
def wxdate2pydate(date):
     assert isinstance(date, wx.DateTime)
     if date.IsValid():
          ymd = map(int, date.FormatISODate().split('-'))
          return datetime.date(*ymd)
     else:
          return None
