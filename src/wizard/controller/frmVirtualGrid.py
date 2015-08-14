import wx
import wx.grid as Grid

class GridBase(Grid.PyGridTableBase):
    def __init__(self, data, columns):
        super(GridBase, self).__init__()
        print columns
        print data
        self._data = data
        self._rows = 0
        self._cols = 0
    
    def setData(self, data):
        self._data = data

    def GetNumberRows(self):
        return 10

    def GetNumberCols(self):
        return 10

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return unicode(self._data[row][col])    

    def SetValue(self, row, col, value):
        pass

class VirtualGrid(Grid.Grid):
    def __init__(self, parent, **kwargs):
        super(VirtualGrid, self).__init__(parent, **kwargs)
    
    def setTable(self, table):
        self._table = table
        self.SetTable(self._table)

    def Reset(self):
        self._table.ResetView(self)
