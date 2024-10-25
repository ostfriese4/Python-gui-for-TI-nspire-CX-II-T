def ImportToKernel(k):
  sys=k.get("ti_system")
  lib=k.lib["gui"]
  widget=lib["widget"]
  crop=lib["crop text"]
  output=k.lib["system"]["lib"]()

  class Label(widget):
    def __init__(self, window, x=0, y=0, width=1, height=1, text="text", color=None, text_align="left", crop=True):
      super().__init__(window,x,y,width,height)
      sefl._crop = crop
      self._text=text
      self._cropped=None
      self._cropped_width=None
      self._cropped_text=None
      self.text_align=text_align
      self.text_updated=k.lib["system"]["slot"](k)
      self.set_color(color)
    def set_text(self,text):
      if self._text!=text:
        self._text=text
        self.update()
        self.text_updated.run()
    def get_text(self):
      return self._text
    def set_color(self,color):
      self._color=color
      self.update()
    def draw(self,x,y,width,height):
      align=self.text_align
      color=self._color
      if color==None:
        color=self._window.__theme.get("label button text color")
      sys.set_color(color)
      h=0
      if self._crop:
        if width!=self._cropped_width or self._text!=self._cropped_text:
          self._cropped_width=width
          self._cropped_text=self._text
          self._cropped=crop(self._text,width)
      else:
        self._cropped = self._crop.split("\n")
      for line in self._cropped:
        h+=20
        if h>height:
          return
        rwidth,rheight=sys.string_size(line)
        x2=width-rwidth
        if align=="left":
          x2=0
        if align=="right":
          pass
        if align=="center":
          x2*=0.5
        sys.draw_text(x+x2,y+19,line)
        y+=20
  lib["Label"]=Label
  output.Label=Label

  class Button(Label):
    def __init__(self,window,x=0,y=0,width=1,height=1,text="text",color=None,text_align="left",action=None,bg_color=None, crop=True):
      super().__init__(window,x,y,width,height,text,color,text_align,crop)
      if action!=None:self.clicked.connect(action)
      self._bgcolor=bg_color
    def draw(self,x,y,width,height):
      self._window.__theme.get("draw button bg")(x,y,width,height,self._bgcolor)
      super().draw(x,y,width,height)
  lib["Button"]=Button
  output.Button=Button

  class TextEdit(Label):
    def __init__(self,window,x=0,y=0,width=1,height=1,text="text",color=None,text_align="left"):
      super().__init__(window,x,y,width,height,text,color,text_align)
      self.input=k.lib["input"]["input"](text)
      self.input.updated.connect(self._updated)
      self.updated=self.input.textChanged
      self.not_clicked.connect(self.disable)
      self._window.not_clicked.connect(self.disable)
      self.enabled.connect(self.click)
    def draw(self,x,y,width,height):
      self._window.__theme.get("draw TextEdit bg")(x,y,width,height)
      super().draw(x,y,width,height)
      if self.input.isEnabled():
        pos=self.input.position
        txt=self.input.text
        yc=0
        if pos>len(txt):
          pos=-1
          self.input.position=-1
        if pos==-1:
          pos=len(txt)
        txt=txt[:pos]
        pos-=txt.count("\n")
        for line in self._cropped:
          if pos<=len(line):
            xc,y2=sys.string_size(line[:pos])
            xc+=x
            yc+=y
            if txt.endswith("\n"):
              xc=x
              yc+=20
            sys.set_color(10,255,50)
            sys.draw_line(xc,yc+2,xc,yc+16)
            return
          yc+=20
          pos-=len(line)
    def disable(self):
      self.input.disable()
      self.update()
    def click(self):
      self.input.enable()
      self.update()
    def _updated(self,info):
      self.set_text(self.input.text)
      self.update()
      self.updated.run()
  lib["TextEdit"]=TextEdit
  output.TextEdit=TextEdit

  class ComboBox(Button):
    def __init__(self,window,x=0,y=0,width=1,height=1,options=[]):
      super().__init__(window,x=x,y=y,width=width,height=height,text=options[0])
      self.clicked.connect(self.choose)
      self.options=options
    def set_var(self,var=None,info={}):
      if var is None:
        var=info["item"]
      self.set_text(var)
    def get_var(self):
      return self.get_text()
    def choose(self):
      items={}
      for item in self.options:
        items[item]=self.set_var
      m=k.lib["gui"]["Menu"]()
      m.items=items
      m.show(100,100)
  output.ComboBox=ComboBox

  class NumberChoose(widget):
    def __init__(self,window,x=0,y=0,width=1,height=1,suffix="",value=10):
      self.setSuffix(suffix)
      self.setValue(value)
      super().__init__(window,x=x,y=y,width=width,height=height)
    def setSuffix(self,suffix):
      self._suffix=suffix
    def setValue(self,value):
      self._value=value
    def draw(self,x,y,width,height):
      text=str(self._value)+self._suffix
      self._window.__theme.get("draw numberchoose")(x,y,width,height,text)
  output.NumberChoose=NumberChoose

  return output
