def ImportToKernel(k):
  lib={}
  sys=k.get("ti_system")
  k.get("input")
  empty=k.lib["system"]["empty"]
  movepc=[]
  host = None



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
    def __init__(self, x, y, width, height, click=empty, draw=empty, clickable=True, backgroundVisible=False, parent=None):
      nonlocal host
      self.__x=x
      self.__y=y
      self.__width=width
      self.__height=height
      self.__clickable=clickable
      self.__keys={}
      if host == None:
        host = self
      else:
        parent = host
        parent.addChild(self)
      self._parent = parent
      self._updatedChilds = []
      self.enabled=k.lib["system"]["slot"](k)
      self.disabled=k.lib["system"]["slot"](k)
      self.enabled.connect(self._enableKeys)
      self.disabled.connect(self._disableKeys)
      self.mouseMoved=k.lib["system"]["slot"](k)
      self._childs = []
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
      if not self in self._parent._updatedChilds:
        self._parent._updatedChilds.append(self)
        if self._parent is not None:
          self._parent.update()
        if changed:
          self.update_foreground()
          if self.__backgroundVisible:
            self.update_background()
    def show(self):
      areas = self._parent._childs
      try:
        areas[len(areas)-1].disabled.run()
      except IndexError: #no element in background
        pass
      if not self in areas:
        areas.append(self)
        self.update()
      self.enabled.run()
    def isEnabled(self):
      areas = self._parent._childs
      if self in areas:
        return areas[len(areas)-1]==self
      return False
    def get_size(self):
      return self.__width,self.__height
    def get_position(self):
      return self.__x,self.__y
    def hide(self):
      areas = self._parent._childs
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
      areas = self._parent._childs
      for area in areas:
        area.update(False)
    def update_background(self):
      areas = self._parent._childs
      if self in areas:
        index=areas.index(self)
        background=areas[:index]
        for area in background:
          area.update(False)
    def update_foreground(self):
      areas = self._parent._childs
      if self in areas:
        index=areas.index(self)
        foreground=areas[index:]
        for area in foreground:
          area.update(False)
    def enable(self):
      areas = self._parent._childs
      if self in areas:
        areas.remove(self)
      self.show()
    def setClick(self,action):
      self._click=action
    def click(self, xm, ym):
      x, y = self.get_position()
      xm -= x
      ym -= y

      k.run_code(lambda:self._click(x,y))
      self.clicked.run()
      self.not_clicked.run()


      areas = self._childs
      mode="test"
      for i in range(len(areas)):
        area=areas[len(areas)-1-i]
        if mode=="test":
          x, y = area.get_position()
          width, height = area.get_size()

          if x >= xm and y >= ym and area.__clickable:
            if width < 0:
              width = rwidth + 1 - width
            if height < 0:
              height = rheight + 1 - height
            if width <= xm + rwidth and height <= ym + rheight:
              area.click(xm, ym)
              mode = "set"
        elif mode=="set":
          area.not_clicked.run()
    def setDraw(self,action):
      self._draw=action
    def draw(self):
      for area in self._updatedChilds:
        k.run_code(area.draw)
    def delete(self):
      updated = self._parent._updatedChilds
      self.hide()
      if self in updated:
        updated.remove(self)
  host = area(0, 0, 318, 212)




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
    if updated:
      k.run_code(host.draw)
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
    host.click(xm, ym)
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

  k.lib["gui"] = lib

  lib["get theme by name"] = getThemeByName
  lib["mouse"] = mouse
  lib["stop"] = stop
  lib["running"] = isRunning
  lib["start"] = start
  lib["area"] = area
  lib["themes"] = themes
  lib["theme"] = theme
  lib["enabled theme"] = enabled_theme
  lib["move process"] = create_movepc
  lib["theme changed"] = k.lib["system"]["slot"](k)
  lib["click finished"] = click_finished
  lib["update all"] = updateAll

  k.get("default_theme")
