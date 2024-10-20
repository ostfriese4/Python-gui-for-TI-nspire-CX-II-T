def ImportToKernel(k):
  lib={}
  sys=k.get("ti_system")
  k.get("input")
  empty=k.lib["system"]["empty"]
  movepc=[]

  updated=[]
  areas=[]

  class mouse:
    def __init__(self):
      self.position=sys.get_mouse()
      self.moved=k.lib["system"]["slot"](k)
      self.moved.connect(self._moveHandle)
      self.clicked=k.lib["system"]["slot"](k)
      k.lib["input"]["key"]("center").pressed.connect(self.clicked.run)
    def _moveHandle(self):
      for i in range(len(areas)):
        area=areas[len(areas)-1-i]
        area.mouseMoved.run()
  mouse=mouse()

  class area:
    def __init__(self,x,y,width,height,click=empty,draw=empty,clickable=True,backgroundVisible=False):
      self.__x=x
      self.__y=y
      self.__width=width
      self.__height=height
      self.__clickable=clickable
      self.__keys={}
      self.enabled=k.lib["system"]["slot"](k)
      self.disabled=k.lib["system"]["slot"](k)
      self.enabled.connect(self._enableKeys)
      self.disabled.connect(self._disableKeys)
      self.mouseMoved=k.lib["system"]["slot"](k)
      self.__backgroundVisible=backgroundVisible
      self.setClick(click)
      self.setDraw(draw)
      self.show()
      self.clicked=k.lib["system"]["slot"](k)
      self.not_clicked=k.lib["system"]["slot"](k)
    def key(self,key):
      if key in self.__keys:
        return self.__keys[key]
      connection=k.lib["system"]["slot"](k)
      if self.isEnabled():
        k.lib["input"]["key"](key).pressed.connect(connection.run)
      self.__keys[key]=connection
      return connection
    def _enableKeys(self):
      keys=list(self.__keys.keys())
      for key in keys:
        k.lib["input"]["key"](key).pressed.connect(self.__keys[key].run)
    def _disableKeys(self):
      keys=list(self.__keys.keys())
      for key in keys:
        k.lib["input"]["key"](key).pressed.disconnect(self.__keys[key].run)
    def update(self,changed=True):
      if not self in updated:
        updated.append(self)
        if changed:
          self.update_foreground()
          if self.__backgroundVisible:
            self.update_background()
    def show(self):
      try:
        areas[len(areas)-1].disabled.run()
      except IndexError: #no element in background
        pass
      if not self in areas:
        areas.append(self)
        self.update()
      self.enabled.run()
    def isEnabled(self):
      if self in areas:
        return areas[len(areas)-1]==self
      return False
    def get_size(self):
      return self.__width,self.__height
    def get_position(self):
      return self.__x,self.__y
    def hide(self):
      if self in areas:
        areas.remove(self)
        self.disabled.run()
        areas[len(areas)-1].enabled.run()
        self.update_all()
    def move(self,x,y):
      if x==self.__x:
        if y==self.__y:
          return
      self.__x=x
      self.__y=y
      self.update_all()
    def resize(self,width,height):
      if width==self.__width:
        if height==self.__height:
          return
      if width>=self.__width and height>=self.__height:
        self.update_foreground()
      else:
        self.update_all()
      self.update(False)
      self.__width=width
      self.__height=height
    def update_all(self):
      for area in areas:
        area.update(False)
    def update_background(self):
      if self in areas:
        index=areas.index(self)
        background=areas[:index]
        for area in background:
          area.update(False)
    def update_foreground(self):
      if self in areas:
        index=areas.index(self)
        foreground=areas[index:]
        for area in foreground:
          area.update(False)
    def enable(self):
      if self in areas:
        areas.remove(self)
      self.show()
    def setClick(self,action):
      self._click=action
    def click(self,x,y):
      if x>=self.__x and y>=self.__y and x<=self.__x+self.__width and y<=self.__y+self.__height:
        k.run_code(lambda:self._click(x,y))
        self.clicked.run()
        return True
      self.not_clicked.run()
      return False
    def setDraw(self,action):
      self.draw=action
    def delete(self):
      self.hide()
      if self in updated:
        updated.remove(self)
  themes=[]
  change_actions=[]
  provided={}

  def getThemeByName(name):
    for theme in themes:
      if theme.name==name:
        return theme

  class enabled_theme:
    def __init__(self):
      self.theme=None
    def set(self,theme):
      self.theme=theme
    def get(self,name):
      return self.theme.get(name)
  enabled_theme=enabled_theme()

  class theme:
    def __init__(self,name):
      self.data={}
      self.name=name
      if enabled_theme.theme is None:
        self.enable()
      themes.append(self)
    def set(self,name,func):
      self.data[name]=func
      try:
        provided[name]
      except:
        provided[name]=func
    def get(self,name):
      if name in self.data:
        return self.data[name]
      elif name in provided:
        return provided[name]
      else:
        return
    def enable(self):
      enabled_theme.set(self)
      lib["theme changed"].run()

  def server():
    nonlocal updated
    if updated!=[]:
      for area in areas:
        if area in updated:
          k.run_code(area.draw)
      updated=[]
      sys.paint_buffer()
    if mouse.position!=sys.get_mouse():
      mouse.position=sys.get_mouse()
      mouse.moved.run()

  click_finished=k.lib["system"]["slot"](k)
  def clicker():
    if movepc!=[]:
      for pc in movepc:
        pc.delete()
      movepc.clear()
      click_finished.run()
      return
    xm,ym=mouse.position
    mode="test"
    for i in range(len(areas)):
      area=areas[len(areas)-1-i]
      if mode=="set":
        area.not_clicked.run()
      elif mode=="test" and area.__clickable:
        if area.click(xm,ym):
          mode="set"
    click_finished.run()

  def create_movepc(code):
    pc=k.lib["system"]["process"](k,code=code,name="move-process "+str(len(movepc)+1))
    movepc.append(pc)
    return pc

  pc=None
  cl=None
  def redraw():
    for area in areas:
      updated.append(area)
  def restart():
    start()
    k.lib["input"]["simulate"]("None")
    redraw()
  lib["stopping"]=k.lib["system"]["slot"](k)
  lib["starting"]=k.lib["system"]["slot"](k)
  def isRunning():
    if pc==None:
      return False
    return True
  def start():
    nonlocal pc
    sys.use_buffer()
    if pc==None:
      if areas!=[]:
        areas[0].update_all()
      k.lib["input"]["key"](key="center").pressed.connect(clicker)
      pc=k.lib["system"]["process"](k,code=server,name="gui")
      lib["starting"].run()
      k.starting.connect(restart)
  def stop():
    nonlocal pc
    pc.delete()
    k.lib["input"]["key"](key="center").pressed.disconnect(clicker)
    pc=None
    lib["stopping"].run()
    k.starting.disconnect(restart)

  k.lib["gui"]=lib

  lib["get theme by name"]=getThemeByName
  lib["mouse"]=mouse
  lib["stop"]=stop
  lib["running"]=isRunning
  lib["start"]=start
  lib["area"]=area
  lib["themes"]=themes
  lib["theme"]=theme
  lib["enabled theme"]=enabled_theme
  lib["move process"]=create_movepc
  lib["theme changed"]=k.lib["system"]["slot"](k)
  lib["click finished"]=click_finished

  k.get("default_theme")
