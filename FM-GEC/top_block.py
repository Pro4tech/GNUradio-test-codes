#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov 12 11:02:52 2019
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.center_freq = center_freq = 88e6
        self.volume_slider = volume_slider = 5
        self.samp_rate = samp_rate = 2.5e6
        self.channel_width = channel_width = 200e3
        self.channel_slider = channel_slider = center_freq

        ##################################################
        # Blocks
        ##################################################
        _channel_slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_slider_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_slider_sizer,
        	value=self.channel_slider,
        	callback=self.set_channel_slider,
        	label='channel_slider',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_slider_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_slider_sizer,
        	value=self.channel_slider,
        	callback=self.set_channel_slider,
        	minimum=center_freq-samp_rate/2+channel_width/2,
        	maximum=center_freq+samp_rate/2-channel_width/2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_channel_slider_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=channel_slider,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        _volume_slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_slider_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_slider_sizer,
        	value=self.volume_slider,
        	callback=self.set_volume_slider,
        	label='volume_slider',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_slider_sizer,
        	value=self.volume_slider,
        	callback=self.set_volume_slider,
        	minimum=0,
        	maximum=10,
        	num_steps=20,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_volume_slider_sizer)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'rtl_tcp=192.168.43.42:1234' )
        self.rtlsdr_source_0.set_sample_rate(2e6)
        self.rtlsdr_source_0.set_center_freq(88e6, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(40, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)




        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_fftsink2_0, 0))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.set_channel_slider(self.center_freq)

    def get_volume_slider(self):
        return self.volume_slider

    def set_volume_slider(self, volume_slider):
        self.volume_slider = volume_slider
        self._volume_slider_slider.set_value(self.volume_slider)
        self._volume_slider_text_box.set_value(self.volume_slider)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width

    def get_channel_slider(self):
        return self.channel_slider

    def set_channel_slider(self, channel_slider):
        self.channel_slider = channel_slider
        self._channel_slider_slider.set_value(self.channel_slider)
        self._channel_slider_text_box.set_value(self.channel_slider)
        self.wxgui_fftsink2_0.set_baseband_freq(self.channel_slider)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
