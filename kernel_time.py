def ImportToKernel(k):
  sys=k.get("ti_system")
  lib={}
  timer_pc=None
  timers=[]
  k.lib["time"]=lib
  class timer:
    def __init__(self,time=1000):
      nonlocal timer_pc
      self.finished=k.lib["system"]["slot"](k)
      self._time=time+sys.get_time_ms()
      timers.append(self)
      if timer_pc==None:
        timer_pc=k.lib["system"]["process"](k,code=timer_server)
  lib["timer"]=timer
  def timer_server():
    nonlocal timer_pc
    time=sys.get_time_ms()
    for timer in timers:
      if timer._time<=time:
        timer.finished.run()
        timers.remove(timer)
        if timers==[]:
          timer_pc.delete()
          timer_pc=None
