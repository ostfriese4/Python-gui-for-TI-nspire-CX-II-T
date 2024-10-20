def ImportToKernel(k):
  k.get("_gui")
  mouse=k.lib["gui"]["mouse"]
  k.get("kernel_time")
  output=k.lib["system"]["lib"]()
  lib=k.lib["gui"]
  sys=k.get("ti_system")
  defaultTheme=lib["enabled theme"]
  areaClass=lib["area"]

  background=lib["area"](0,0,318,212,draw=lambda:defaultTheme.get("draw bg")())

  windows=[]

  class window(areaClass):
    def __init__(self,x=50,y=50,width=218,height=112,theme=defaultTheme,title="unnamed"):
      super().__init__(x,y,width,height,self.WindowClick,self.WindowDraw)
      self.__theme=theme
      self._enabledWidget=None
      self._title=title
      self._minimized=False
      self._old=(0,0,0,0)
      self._maximized=False
      self.closed=k.lib["system"]["slot"](k)
      windows.append(self)
      self.widgets=[]
      task.update()
      self.key("tab").connect(self._tabKey)
      self.key("enter").connect(self._enabledEnter)
      k.lib["gui"]["start"]()
    def _enabledEnter(self):
      if self._enabledWidget is None:
        i=-1
      else:
        self._enabledWidget.click()
    def _tabKey(self):
      if self._enabledWidget is None:
        i=-1
      else:
        i=self.widgets.index(self._enabledWidget)
        self._enabledWidget.disable()
      i+=1
      if i==len(self.widgets):
        i=0
      self._enabledWidget=self.widgets[i]
      self._enabledWidget.enable()
    def get_area(self,x,y,width,height):
      aw,ah=self.get_size()
      if width<0:
        width=aw+width+1
      if height<0:
        height=ah+height+1
      if x<0:
        x=aw+x+1
      if y<0:
        y=ah+y+1
      return x,y,width,height
    def area_clicked(self,x,y,width,height,xm,ym):
      x,y,width,height=self.get_area(x,y,width,height)
      return xm>=x and ym>=y and xm<=x+width and ym<=y+height
    def WindowClick(self,xm,ym):
      self.enable()
      x,y=self.get_position()
      xm-=x
      ym-=y

      x,y,width,height=self.__theme.get("move button area")
      if self.area_clicked(x,y,width,height,xm,ym):
        self._move(xm,ym)

      x,y,width,height=self.__theme.get("resize button right")
      if self.area_clicked(x,y,width,height,xm,ym):
        self._resizeRight(xm,ym)

      x,y,width,height=self.__theme.get("resize button bottom")
      if self.area_clicked(x,y,width,height,xm,ym):
        self._resizeBottom(xm,ym)

      x,y,width,height=self.__theme.get("resize button top")
      if self.area_clicked(x,y,width,height,xm,ym):
        self._resizeTop(xm,ym)

      x,y,width,height=self.__theme.get("resize button left")
      if self.area_clicked(x,y,width,height,xm,ym):
        self._resizeLeft(xm,ym)

      x,y,width,height=self.__theme.get("close button area")
      if self.area_clicked(x,y,width,height,xm,ym):
        self.close()

      x,y,width,height=self.__theme.get("minimize button area")
      if self.area_clicked(x,y,width,height,xm,ym):
        self.minimize()

      x,y,width,height=self.__theme.get("maximize button area")
      if self.area_clicked(x,y,width,height,xm,ym):
        if self.maximized():
          self.restore()
        else:
          self.maximize()

      x,y,width,height=self.__theme.get("window widgets area")
      x,y,width,height=self.get_area(x,y,width,height)
      if self.area_clicked(x,y,width,height,xm,ym):
        for widget in self.widgets:
          xw,yw,widthw,heightw=widget._x,widget._y,widget._width,widget._height
          xw=x+width*xw
          yw=y+height*yw
          widthw*=width
          heightw*=height
          if self.area_clicked(xw,yw,widthw,heightw,xm,ym):
            widget.click()
            widget.enable()
            widget.clicked.run()
          else:
            widget.disable()
            widget.not_clicked.run()
    def _move(self,x,y):
      if self.minimized():
        self.restore()
      xo,yo=self.get_position()
      def movepc():
        nonlocal xo,yo
        xm,ym=mouse.position
        if self.maximized() and not xm==-1:
          self.restore()
          xo,yo=self.get_position()
        elif xm==-1 and not self.maximized():
          self.move(xo,yo)
          self.maximize()
        if self.maximized():
          return
        xm-=x
        ym-=y
        self.move(xm,ym)
      k.lib["gui"]["move process"](movepc)

    def _resizeRight(self,xmo,ymo):
      xo,yo=self.get_position()
      xmo+=xo
      widtho,heighto=self.get_size()
      def resizepc():
        width,height=self.get_size()
        xm,ym=mouse.position
        width=widtho+(xm-xmo)
        self.resize(width,height)
      k.lib["gui"]["move process"](resizepc)

    def _resizeBottom(self,xmo,ymo):
      xo,yo=self.get_position()
      ymo+=yo
      widtho,heighto=self.get_size()
      def resizepc():
        width,height=self.get_size()
        xm,ym=mouse.position
        height=heighto+(ym-ymo)
        self.resize(width,height)
      k.lib["gui"]["move process"](resizepc)

    def _resizeTop(self,xmo,ymo):
      xo,yo=self.get_position()
      ymo+=yo
      widtho,heighto=self.get_size()
      def resizepc():
        width,height=self.get_size()
        x,y=self.get_position()
        xm,ym=mouse.position
        height=heighto-(ym-ymo)
        y=yo+(ym-ymo)
        self.resize(width,height)
        self.move(x,y)
      k.lib["gui"]["move process"](resizepc)

    def _resizeLeft(self,xmo,ymo):
      xo,yo=self.get_position()
      xmo+=xo
      widtho,heighto=self.get_size()
      def resizepc():
        width,height=self.get_size()
        x,y=self.get_position()
        xm,ym=mouse.position
        width=widtho-(xm-xmo)
        x=xo+(xm-xmo)
        self.resize(width,height)
        self.move(x,y)
      k.lib["gui"]["move process"](resizepc)
    def WindowDraw(self):
      width,height=self.get_size()
      x,y=self.get_position()
      self.__theme.get("draw window background")(x,y,width,height,self._title,self)
      x,y,width,height=self.__theme.get("window widgets area")
      x,y,width,height=self.get_area(x,y,width,height)
      xw,yw=self.get_position()
      x+=xw
      y+=yw
      for widget in self.widgets:
        xw,yw,widthw,heightw=widget._x,widget._y,widget._width,widget._height
        xw=x+width*xw
        yw=y+height*yw
        widthw*=width
        heightw*=height
        widget.draw(xw,yw,widthw,heightw)
    def delete(self):
      self.close()
    def close(self):
      while len(self.widgets)!=0:
        self.widgets[0].delete()
      super().delete()
      windows.remove(self)
      self.closed.run()
    def minimize(self):
      if not self._minimized:
        self._minimized=True
        self.hide()
    def minimized(self):
      return self._minimized
    def restore(self):
      if self._minimized:
        self.show()
        self._minimized=False
      elif self._maximized:
        x,y,width,height=self._old
        self.move(x,y)
        self.resize(width,height)
        self._maximized=False
    def maximized(self):
      return self._maximized
    def maximize(self):
      if not self._maximized:
        x,y=self.get_position()
        width,height=self.get_size()
        self._old=(x,y,width,height)
        x,y,width,height=defaultTheme.get("maximized window data")
        self.move(x,y)
        self.resize(width,height)
        self._maximized=True

  class widget:
    def __init__(self,window,x=0,y=0,width=1,height=1):
      self._window=window
      self._x=x
      self._y=y
      self._width=width
      self._height=height
      self._window.widgets.append(self)
      self._isEnabled=False
      self.clicked=k.lib["system"]["slot"](k)
      self.clicked.info["widget"]=self
      self.not_clicked=k.lib["system"]["slot"](k)
      self.enabled=k.lib["system"]["slot"](k)
      self.disabled=k.lib["system"]["slot"](k)
      self.update()
    def update(self):
      self._window.update()
    def draw(self,x,y,width,height):
      pass
    def click(self):
      pass
    def delete(self):
      self._window.widgets.remove(self)
      self._window.update()
    def enable(self):
      self.enabled.run()
      self._isEnabled=True
    def disable(self):
      self.disabled.run()
      self._isEnabled=False

  class frontLayer(areaClass):
    def __init__(self,draw):
      super().__init__(x=0,y=0,width=318,height=212,clickable=False,draw=draw,backgroundVisible=True)

  class notification:
    def __init__(self,app="unnamed",text=""):
      x,y,width,height=defaultTheme.get("notification position size")
      self._area=lib["area"](x,y,width,height,draw=self.draw)
      self.clicked=self._area.clicked
      self._text=lib["crop text"](text,width=width-4)
      self._app=app
      self._timer=k.lib["time"]["timer"](defaultTheme.get("notification time"))
      self._timer.finished.connect(self._area.delete)
      self.timeout=self._timer.finished
    def draw(self):
      x,y=self._area.get_position()
      width,height=self._area.get_size()
      defaultTheme.get("draw notification")(x,y,width,height,self._text,self._app)

  class Menu:
    def __init__(self,parent=[]):
      self.items={}
      self._areas=[]
      self._parent=parent
      self._close=None
      self._enabledItem=None
      k.lib["gui"]["click finished"].connect(self.finished_click)
    def _down(self):
      keys=list(self.items.keys())
      if self._enabledItem is None:
        i=-1
      else:
        i=keys.index(self._enabledItem)
      i+=1
      if i == len(keys):i=0
      self._enabledItem=keys[i]
      self._areas[0].update()
    def _up(self):
      keys=list(self.items.keys())
      if self._enabledItem is None:
        i=len(keys)
      else:
        i=keys.index(self._enabledItem)
      i-=1
      if i == -1:i=len(keys)-1
      self._enabledItem=keys[i]
      self._areas[0].update()
    def show(self,x=50,y=20):
      width=100
      height=len(self.items)*defaultTheme.get("menu item height")+defaultTheme.get("menu top height")+defaultTheme.get("menu bottom height")
      if y>=106:
        y-=height
      else:
        y-=defaultTheme.get("menu item height")
      area=lib["area"](x,y,width,height,click=self.click,draw=self.draw)
      area.key("up").connect(self._up)
      area.key("down").connect(self._down)
      area.key("left").connect(self.hide)
      area.key("right").connect(self._enabledClick)
      area.key("enter").connect(self._enabledClick)
      self._areas.append(area)
      for i in self._parent:
        i._areas.append(area)
        area.clicked.connect(i.clicked)
      area.clicked.connect(self.clicked)
      area.not_clicked.connect(self.not_clicked)
      self._enabledItem=list(self.items.keys())[-1]
    def _enabledClick(self):
      area = self._areas[0]
      x,y=area.get_position()
      item=list(self.items.keys()).index(self._enabledItem)
      y+=item*defaultTheme.get("menu item height")
      self.click(x,y)
    def click(self,x,y):
      self._areas[0].update()
      y-=self._areas[0].__y
      y-=defaultTheme.get("menu top height")
      i=int(y/defaultTheme.get("menu item height"))
      keys=list(self.items.keys())
      key=keys[i]
      code=self.items[key]
      self._enabledItem=key
      if type(code)==dict:
        parent=self._parent.copy()
        parent.append(self)
        submenu=Menu(parent=parent)
        submenu.items=code
        y2=i+1
        y2*=defaultTheme.get("menu item height")
        y2+=defaultTheme.get("menu top height")
        y2+=self._areas[0].__y
        x=self._areas[0].__x+100
        if x>218:
          x-=200
        submenu.show(x,y2)
      else:
        tmp=k.lib["system"]["slot"](k)
        tmp.info["item"]=key
        tmp.connect(code)
        tmp.run()
        if self._parent==[]:
          self.hide()
        else:
          self._parent[0].hide()
    def draw(self):
      area=self._areas[0]
      y=area.__y
      y+=defaultTheme.get("menu top height")
      x=area.__x
      width=area.__width
      height=area.__height
      defaultTheme.get("draw menu background")(x,y,width,height)
      items=list(self.items.keys())
      for item in items:
        code=self.items[item]
        if type(code)==dict:
          if self._enabledItem==item:
            defaultTheme.get("draw active menu cascade item")(x,y,str(item))
          else:
            defaultTheme.get("draw menu cascade item")(x,y,str(item))
        else:
          if self._enabledItem==item:
            defaultTheme.get("draw active menu item")(x,y,str(item))
          else:
            defaultTheme.get("draw menu item")(x,y,str(item))
        y+=defaultTheme.get("menu item height")
    def clicked(self,info):
      self._close=False
    def not_clicked(self,info):
      if self._close==None:
        self._close=True
    def finished_click(self,info):
      if self._close==True:
        self.hide()
      self._close=None
    def hide(self):
      for i in self._areas:
        i.delete()
      self._areas.clear()
    def visible(self):
      return not self._areas==[]

  task=None
  def panel():
    k.get("input")
    nonlocal task
    if "Appmenu" not in lib:
      menu=Menu()
      lib["Appmenu"]=menu
      menu.items["Shut down"]=k.stop
    def showMenu():
      menu=lib["Appmenu"]
      if menu.visible():
        menu.hide()
      else:
        task.enable()
        x,y=defaultTheme.get("app menu position")
        menu.show(x,y)
    def taskClick(xm,ym):
      x,y,width,height=defaultTheme.get("app menu area position")
      if xm>=x and ym>=y and ym<=y+height and xm<=x+width:
        showMenu()
      elif len(windows)!=0:
        x,y,width,height=defaultTheme.get("task title area position")
        width=width/len(windows)
        xm-=x
        i=int(xm/width)
        window=windows[i]
        if window.minimized():  window.restore()
        elif window.isEnabled():  window.minimize()
        else:                                  window.enable()
    def drawTask():
      defaultTheme.get("draw task background")()
      if len(windows)!=0:
        x,y,width,height=defaultTheme.get("task title area position")
        width=width/len(windows)
        for window in windows:
          defaultTheme.get("draw task title")(x,y,width,height,window._title)
          x+=width
    def update():
      task.delete()
      k.lib["gui"]["theme changed"].disconnect(update)
      try:
        mouse.moved.disconnect(mouse_moved)
      except:
        pass
      panel()
    if defaultTheme.get("floating panel")==True:
      def still():
        x,y=mouse.position
        border=defaultTheme.get("tab edge panel")
        if border=="bottom":
          if y==210:
            task.enable()
      def mouse_moved():
        x,y=mouse.position
        border=defaultTheme.get("tab edge panel")
        if border=="bottom":
          if y==210:
            k.get("kernel_time")
            k.lib["time"]["timer"](defaultTheme.get("tab time panel")).finished.connect(still)
      mouse.moved.connect(mouse_moved)
    x,y,width,height=defaultTheme.get("task position")
    task=k.lib["gui"]["area"](x,y,width,height,draw=drawTask,click=taskClick)
    k.lib["gui"]["theme changed"].connect(update)
    k.lib["input"]["key"]("home").pressed.connect(showMenu)
  panel()

  def remaximize():
    x,y,width,height=defaultTheme.get("maximized window data")
    for window in windows:
      if window.maximized():
        window.move(x,y)
        window.resize(width,height)
  lib["theme changed"].connect(remaximize)

  def draw_title(x,y,width,title):
    width2,height=sys.string_size(title)
    if width2>width:
      ok=False
      width-=12 # for "..."
      while not ok:
        title=title[:len(title)-1]
        width2,height=sys.string_size(title)
        if len(title)==1 and width2>width:
          return
        if width2<=width:ok=True
      title+="..."
    sys.draw_text(x,y,title)

  def crop_text(text,width=318):
    lines=text.split("\n")
    line=0
    if width<10:
      return
    while line<len(lines):
      width2,height2=sys.string_size(lines[line])
      if width2>width:
        text2=lines[line]
        i=0
        letters=len(text2)
        width2=500
        while width2>width:
          i+=1
          width2,height2=sys.string_size(text2[:letters-i])
        lines[line]=text2[:letters-i]
        lines.insert(line+1,text2[letters-i:])
      line+=1
    return lines

  lib["crop text"]=crop_text
  lib["notification"]=notification
  lib["window"]=window
  lib["widget"]=widget
  lib["draw title"]=draw_title
  lib["frontLayer"]=frontLayer
  lib["Menu"]=Menu
  k.get("widgets")

  output.notification=notification
  output.window=window
  output.Menu=Menu
  output.frontLayer=frontLayer
  output.start=lib["start"]
  return output
