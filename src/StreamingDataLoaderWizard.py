import os
import sys

import ObjectListView
import pyodbc
import pymysql
import sqlite3
sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
from src.wizard.controller.frmMain import MainController
import wx
if __name__ == '__main__':
    app = wx.App()
    frame = MainController(None)
    frame.CenterOnScreen()
    frame.Show()
    app.MainLoop()

