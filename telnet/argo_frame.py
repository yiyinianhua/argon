# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from chaofeng import Frame,static
from libtelnet import zh_format
import chaofeng.ascii as ac
import config

from datetime import datetime

class ArgoBaseFrame(Frame):

    shortcuts = config.default_shortcuts
    
    '''
    全部类的基类。
    '''

    def cls(self):
        self.write(ac.clear)
        
    def render_background(self,*args,**kwargs):
        self.write(self.background % kwargs)

class ArgoStatusFrame(ArgoBaseFrame):

    top_txt = static['top']
    bottom_txt = static['bottom']

    def top_bar(self,left=u'',mid=u'逸仙时空 Yat-Sen Channel'):
        self.write( zh_format(self.top_txt,
                              left, mid, '007') )

    def bottom_bar(self,repos=False,close=False):
        if close : self.write(ac.save)
        if repos : self.write(ac.move2(24,0))
        self.write( zh_format(self.bottom_txt,
                              datetime.now().ctime(),
                              0,
                              0,
                              self.session.userid))
        if close : self.write(ac.restore)
        
