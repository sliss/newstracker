#!/usr/bin/python

# capitals.py
from NewsTracker import get_Links
import wx

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(1600,500), style=wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

        hbox  = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.GridSizer(2,2,0,0)
        vbox4 = wx.BoxSizer(wx.VERTICAL)
        vbox5 = wx.BoxSizer(wx.VERTICAL) #
        pnl1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        pnl2 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        #pnl3 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.lc.InsertColumn(0, 'Headline')
        self.lc.InsertColumn(1, 'Link')
        self.lc.SetColumnWidth(0, 600)
        self.lc.SetColumnWidth(1, 600)
        vbox1.Add(pnl1, 1, wx.EXPAND | wx.ALL, 3)
        vbox1.Add(pnl2, 1, wx.EXPAND | wx.ALL, 3)
        vbox2.Add(self.lc, 1, wx.EXPAND | wx.ALL, 3)
        self.tc1 = wx.TextCtrl(pnl1, -1)
        self.tc2 = wx.TextCtrl(pnl1, -1)
        vbox3.AddMany([ (wx.StaticText(pnl1, -1, 'Keyword'),0, wx.ALIGN_CENTER),
                        (self.tc1, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL),
                        (wx.StaticText(pnl1, -1, 'Extra'),0, wx.ALIGN_CENTER_HORIZONTAL),
                        (self.tc2,0)])
        pnl1.SetSizer(vbox3)
        vbox4.Add(wx.Button(pnl2, 10, 'Run'),   0, wx.ALIGN_CENTER| wx.TOP, 45)
        vbox4.Add(wx.Button(pnl2, 11, 'Remove'), 0, wx.ALIGN_CENTER|wx.TOP, 15)
        vbox4.Add(wx.Button(pnl2, 12, 'Clear'), 0, wx.ALIGN_CENTER| wx.TOP, 15)
        vbox4.Add(wx.Button(pnl2, 13, 'Close'), 0, wx.ALIGN_CENTER| wx.TOP, 15)
        pnl2.SetSizer(vbox4)
        self.Bind (wx.EVT_BUTTON, self.OnRun, id=10)
        self.Bind (wx.EVT_BUTTON, self.OnRemove, id=11)
        self.Bind (wx.EVT_BUTTON, self.OnClear, id=12)
        self.Bind (wx.EVT_BUTTON, self.OnClose, id=13)
        
        #vbox5.Add(wx.Button(pnl2, 14, 'New'),   0, wx.ALIGN_CENTER| wx.TOP, 45)
        hbox.Add(vbox1, 1, wx.EXPAND)
        hbox.Add(vbox2, 3, wx.EXPAND)
        self.SetSizer(hbox)

    def OnRun(self, event):
    	results = get_Links()
        #if not self.tc1.GetValue() or not self.tc2.GetValue():
         #   return
        
        for r in results: 
			num_items = self.lc.GetItemCount()
			self.lc.InsertStringItem(num_items, r.headline)
			self.lc.SetStringItem(num_items, 1, r.url)
			self.tc1.Clear()
			self.tc2.Clear()

    def OnRemove(self, event):
        index = self.lc.GetFocusedItem()
        self.lc.DeleteItem(index)

    def OnClose(self, event):
        self.Close()

    def OnClear(self, event):
        self.lc.DeleteAllItems()

class MyApp(wx.App):
    def OnInit(self):
        dia = MyDialog(None, -1, 'HF News Tracker')
        dia.ShowModal()
        dia.Destroy()
        return True

app = MyApp(0)
app.MainLoop()