def ImportToKernel(kernel):
  def empty():
    pass
  lib=kernel.lib
  output=kernel.lib["system"]["lib"]()
  ti_system=kernel.get("ti_system")
  get_key=ti_system.get_key
  time=ti_system.get_time_ms
  log=kernel.log
  shorts={}
  last_time=0
  keys=[]
  container=[]
  inputer=False
  class input:
    def __init__(self,text="",position=-1):
      self.text=text
      self.disabled=kernel.lib["system"]["slot"](kernel)
      self.enabled=kernel.lib["system"]["slot"](kernel)
      self.position=position
      self.updated=kernel.lib["system"]["slot"](kernel)
      self.textChanged=kernel.lib["system"]["slot"](kernel)
    def write(self,key):
      position=self.position
      if position==-1:
        position=len(self.text)
      h1=self.text[:position]
      h2=self.text[position:]
      if key=="return":
        key="\n"
      if key=="del":
        if len(h1)!=0:
          h1=h1[:len(h1)-1]
          self.text=h1+h2
          position-=1
        self.updated.run()
        self.textChanged.run()
      elif len(key)==1:
        h1+=key
        self.text=h1+h2
        position+=1
        self.updated.run()
        self.textChanged.run()
      elif key=="left":
        position-=1
        if position==-1:
          position=0
        self.updated.run()
      elif key=="right":
        position+=1
        self.updated.run()
      else:
        return False
        if position>=len(self.text):
          position=-1
      self.position=position
    def enable(self):
      nonlocal inputer
      inputer=self
      self.enabled.run()
    def isEnabled(self):
      return inputer==self
    def disable(self):
      nonlocal inputer
      if inputer==self:
        inputer=False
      self.disabled.run()
    def delete(self):
      self.disable()
  class key:
    def __init__(self,key="esc",code=empty,do=True):
      self.key=key
      shorts[key]=self
      self.pressed=kernel.lib["system"]["slot"](kernel)
  def check_shorts(key):
    ok=False
    try:
      shorts[key].pressed.run()
    except:
      pass
    return ok
  def handle(key):
    nonlocal last_time
    last_time=time()
    if inputer!=False:
      if not inputer.write(key):
        check_shorts(key)
    else:
      check_shorts(key)
  def server():
    key=get_key(0)
    if key!="":
      handle(key)
      server()
  def last():
    return last_time
  def getin():
    return inputer
  pc=lib["system"]["process"](kernel,code=server,name="Input-server")
  libinput={}
  lib["input"]=libinput
  libinput["key"]=key
  libinput["input"]=input
  libinput["last"]=last
  libinput["get inputer"]=getin
  libinput["simulate"]=handle
  output.key=key
  output.input=input
  output.simulate=handle
  return output
