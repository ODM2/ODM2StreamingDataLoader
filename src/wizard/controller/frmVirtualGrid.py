import wx
import wx.grid as Grid

class GridBase(Grid.PyGridTableBase):
    def __init__(self, data, columns):
        super(GridBase, self).__init__()
        self._data = data
        self._columns = columns 
        self._rows = len(data)
        self._cols = len(data[0])
        self.attr = Grid.GridCellAttr()
        self.attr.SetReadOnly(True)

    def GetNumberRows(self):
        return self._rows

    def GetNumberCols(self):
        return self._cols

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return unicode(self._data[row][col])    

    def SetValue(self, row, col, value):
        pass
    
    def GetColLabelValue(self, col):
        return unicode(self._columns[col])

    def GetAttr(self, row, col, kind):
        attr = self.attr
        attr.IncRef()
        return attr

class VirtualGrid(Grid.Grid):
    def __init__(self, parent, **kwargs):
        super(VirtualGrid, self).__init__(parent, **kwargs)

    def setTable(self, table):
        self.SetTable(table, True)
        #self.SetColSizes(200)

    def Reset(self):
        self._table.ResetView(self)
