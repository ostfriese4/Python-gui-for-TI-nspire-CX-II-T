current=None
def empty(a=0,b=0,c=0):
  pass
class slot:
  def __init__(self,kernel):
    self._actions=[]
    self.info={}
    self.kernel=kernel
  def run(self,info=True):
    actions=self._actions.copy()
    for action in actions:
      if info:
        try:
          action(info=self.info)
        except Exception as e:
          if type(e)==TypeError:
            if str(e.args)=="""("unexpected keyword argument 'info'",)""":
              self.run(False)
          else:
            self.kernel.log("<ERROR>")
            self.kernel.log(e)
            self.kernel.errors+=1
      else:
        self.kernel.run_code(action)
  def connect(self,action):
    self._actions.append(action)
  def disconnect(self,action):
    if action in self._actions:
      self._actions.remove(action)
class lib:
  pass
class kernel:
  def __init__(self,verbose=True):
    self.exec=[]
    self.running=False
    self.lib={}
    self.logfile=[]
    self.print=not verbose
    self.modules={}
    modul=lib()
    self.modules["kernel"]=modul
    modul.lib=lib
    modul.slot=slot
    modul.process=process
    modul.empty=empty
    self.starting=slot(self)
    self.stopping=slot(self)
    self.stopped=slot(self)
    self.errors=0
    system={}
    self.lm=False
    self.lib["system"]=system
    system["slot"]=slot
    system["kernel"]=kernel
    system["process"]=process
    system["empty"]=empty
    system["lib"]=lib
  def log(self,message):
    if self.print == True:
      if message=="<ERROR>":
        self.get("sys")
        self.lm=True
        self.logfile.append(message)
      elif self.lm:
        self.get("sys").print_exception(message)
        self.logfile.append(message)
        self.lm=False
      else:
        print(message)
    else:
      self.logfile.append(message)
  def run_code(self,code):
    try:
      return code()
    except Exception as e:
      self.log("<ERROR>")
      self.log(e)
      self.errors+=1
  def print_log(self,delete=False):
    i=0
    while i < len(self.logfile):
      log=self.logfile[i]
      if log=="<ERROR>":
        i+=1
        sys=self.get("sys")
        sys.print_exception(self.logfile[i])
      else:
        print(log)
      i+=1
    if delete:
      self.logfile=[]
  def get(self,name):
    try:
      return self.modules[name]
    except:
      try:
        modul=__import__(name)
      except:
        self.log("Failed to import "+name)
        return
      try:
        code=modul.ImportToKernel
        modul=self.run_code(lambda:code(self))
        self.log("Imported to kernel: "+name)
      except:
        pass
      self.modules[name]=modul
      self.log("Added to database: "+name)
      return modul
  def start(self):
    self.log("Starting kernel")
    if self.running:
      self.log("The kernel is already running")
      return
    self.running=True
    self.starting.run()
    while self.running:
      self.run()
    self.log("stopped kernel")
    self.stopped.run()
  def run(self):
    global current
    for process in self.exec:
      current=process
      self.run_code(process.run)
  def stop(self):
    self.stopping.run()
    self.log("Stopping kernel")
    self.running=False
    allowed=False
    while not allowed:
      allowed=True
      for proc in self.exec:
        if not proc.allowStopping:
          allowed=False
      if not allowed:
         self.run()
class process:
  def __init__(self,kernel,name="process",code=empty):
    self.code=code
    self.name=name
    self.allowStopping=True
    self._state="running"
    self.kernel=kernel
    self.deleting=slot(kernel)
    kernel.exec.append(self)
  def run(self):
    self.code()
  def halt(self):
    self._state="stopped"
    self.kernel.exec.remove(self)
  def restart(self):
    self._state="running"
    self.kernel.exec.append(self)
  def delete(self):
    self.deleting.run()
    self._state="deleted"
    if self in self.kernel.exec:
      self.kernel.exec.remove(self)
