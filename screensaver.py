def ImportToKernel(k):
  settings=k.get("settings")()
  k.get("input")
  process=k.lib["system"]["process"]
  get_mouse=k.get("ti_system").get_mouse
  get_time_ms=k.get("ti_system").get_time_ms
  randint=k.get("random").randint
  draw=k.get("ti_system")
  lib={}
  k.lib["screensaver"]=lib
  mode="testing"
  last=0
  settings.set("Screensaver_timeout",15000,True)
  mouse=(0,0)
  step=0
  bals=[]
  r=0
  g=0
  b=0
  rn=randint(0,255)
  gn=randint(0,255)
  bn=randint(0,255)
  x_fade=0
  y_fade=0
  class bal:
    def __init__(self):
      bals.append(self)
      self.x=randint(0,318)
      self.y=randint(0,212)
      self.xs=randint(-5,5)*0.5
      self.ys=randint(-5,5)*0.5
      self.r=randint(0,255)
      self.g=randint(0,255)
      self.b=randint(0,255)
      self.rn=randint(0,255)
      self.gn=randint(0,255)
      self.bn=randint(0,255)
    def move(self):
      self.x+=self.xs
      self.y+=self.ys
      if self.x<=10:
        if self.xs<0:
          self.xs*=-1
      if self.y<=10:
        if self.ys<0:
          self.ys*=-1
      if self.x>=308:
        if self.xs>0:
          self.xs*=-1
      if self.y>=202:
        if self.ys>0:
          self.ys*=-1
    def test_bals(self):
      for bal in bals:
        if bal==self:return
        if (self.x-bal.x)**2+(self.y-bal.y)**2<=400:
          dx=self.x-bal.x
          dy=self.y-bal.y
          distance=((dx**2)+(dy**2))**0.5
          nx=dx/distance
          ny=dy/distance
          tx=-ny
          ty=nx
          dpTan1=self.xs*tx+self.ys*ty
          dpTan2=bal.xs*tx+bal.ys*ty
          dpNorm1=self.xs*nx+self.ys*ny
          dpNorm2=bal.xs*nx+bal.ys*ny
          m1=dpNorm2
          m2=dpNorm1
          self.xs=tx*dpTan1+nx*m1
          self.ys=ty*dpTan1+ny*m1
          bal.xs=tx*dpTan2+nx*m2
          bal.ys=ty*dpTan2+ny*m2
    def color(self):
      self.r+=(self.rn-self.r)*0.02
      self.g+=(self.gn-self.g)*0.02
      self.b+=(self.bn-self.b)*0.02
    def Show(self):
      rand=randint(0,50)
      if rand==0:
        self.rn=randint(0,255)
        self.gn=randint(0,255)
        self.bn=randint(0,255)
      self.color()
      self.move()
      self.test_bals()
      draw.set_color(int(self.r),int(self.g),int(self.b))
      draw.fill_circle(self.x,self.y,10)
    def delete(self):
      bals.remove(self)
  def tester():
    nonlocal last
    nonlocal mouse
    time=get_time_ms()
    if get_mouse() != mouse:
      last=time
      mouse=get_mouse()
    if k.lib["input"]["last"]()>last:
      last=k.lib["input"]["last"]()
    if time-last>settings.get("Screensaver_timeout"):
      return True
    return False
  def color_changer():
    nonlocal r
    nonlocal g
    nonlocal b
    r+=(rn-r)*0.02
    g+=(gn-g)*0.02
    b+=(bn-b)*0.02
  def starter():
    nonlocal step
    nonlocal mode
    step+=1
    draw.set_color(int(r),int(g),int(b))
    for i in range(16):
      draw.draw_circle(x_fade,y_fade,400-step*2+i*0.125)
    draw.paint_buffer()
    if step==200 or not tester():
      step=0
      mode="running"
      k.log("The Screesaver is started now")
  def show():
    nonlocal mode
    nonlocal bals
    color_changer()
    draw.set_color(int(r),int(g),int(b))
    draw.fill_rect(0,0,318,212)
    for Bal in bals:
      Bal.Show()
    draw.paint_buffer()
    rand=randint(0,500)
    if rand==0:
      bal()
    elif rand==2 or rand==3 or rand==4:
      nonlocal rn,gn,bn
      rn=randint(0,255)
      gn=randint(0,255)
      bn=randint(0,255)
    elif rand==1 and len(bals)>5:
      try:
        bals[randint(0,len(bals)-1)].delete()
      except:pass
    if not tester():
      mode="stopping"
  def runner():
    nonlocal mode
    nonlocal stoppable
    nonlocal x_fade
    nonlocal y_fade
    if mode=="testing":
      if tester():
        k.log("Starting Screensaver")
        mode="starting"
        draw.use_buffer()
        draw.set_color(0,0,0)
        stoppable=False
        k.lib["gui"]["stop"]()
        stoppable=True
        x_fade,y_fade=get_mouse()
    elif mode=="starting":
      starter()
    elif mode=="running":
      show()
    elif mode=="stopping":
      k.lib["gui"]["start"]()
      mode="testing"
      k.log("Stopping screensaver")
  pc=0
  stoppable=True
  def start():
    nonlocal pc
    nonlocal last
    nonlocal mode
    last=get_time_ms()
    mode="testing"
    if pc==0:
      pc=process(k,name="screensaver",code=runner)
  def stop():
    nonlocal pc
    if stoppable:
      pc.delete()
      pc=0
  lib["start"]=start
  lib["stop"]=stop
  k.lib["gui"]["starting"].connect(start)
  k.lib["gui"]["stopping"].connect(stop)
  if k.lib["gui"]["running"]():
      start()
