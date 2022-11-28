import os
import wx
import sys
import pcbnew

pcbnew.GetBoard()
from pcbnew import *

class SimplePlugin(pcbnew.ActionPlugin):
	def defaults(self):
		self.name                = "Track Length"
		self.category            = "Measure Track Length"
		self.description         = "Measure Track Length"
		self.show_toolbar_button = True
		self.icon_file_name      = os.path.join(os.path.dirname(__file__), 'track_length_plugin_icon.png')

	def Run(self):
		board            = GetBoard() # This is to load the board inside the kicad python console
		tracks           = board.GetTracks()
		total_length     = 0.0
		num_sections     = 0
		total_resistance = 0.0
		
		for track in board.GetTracks():
			if track.IsSelected():
				section_length   = track.GetLength()/1000000      # converted to mm
				total_length     = total_length + section_length
				num_sections     = num_sections + 1
				total_resistance = total_resistance + (section_length/(track.GetWidth()/1000000)) * 0.000486 # constant is for mm length, mm width, 1 Oz copper and 25C
		
		wx.MessageBox('Total Length =  %.4f' % total_length + ' mm\n\n' + str(num_sections) + ' Track(s) Measured'+'\n\n' + 'Total Resistance (1 Oz copper, 25C) = %.4f' % total_resistance + ' Ohm\n\n', 'Info',  wx.OK | wx.ICON_INFORMATION)

SimplePlugin().register()
