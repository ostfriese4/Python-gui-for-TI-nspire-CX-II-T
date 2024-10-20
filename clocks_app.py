def ImportToKernel(k):
  search=k.get("system_search")
  runner=search.modul("Time")
  def runner_search(term):
    term=term.lower()
    if term in "datedaydatumwochentag":
      zeit=k.get("time").localtime()
      monat=["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"][zeit[1]-1]
      tag=["Montag","Dienstag","Mitwoch","Donnerstag","Freitag","Samstag","Sonntag"][zeit[6]]
      text=tag+" der "+str(zeit[2])+". "+monat+" "+str(zeit[0])
      return [search.item(text,"Datum",clock)]
    if term in "zeitimeclockuhr":
      zeit=k.get("time").localtime()
      text="Es ist jetzt "+str(zeit[3])+":"+str(zeit[4])
      return [search.item(text,"Uhrzeit",clock)]
    return []
  runner.search=runner_search
  def clock():
    time=k.get("time")
    gui=k.get("gui")
    tage=["Montag","Dienstag","Mitwoch","Donnerstag","Freitag","Samstag","Sonntag"]
    def update():
      jahr,monat,tag,stunde,minute,sekunde,wochentag,jahrestag,sommerzeit=time.localtime()
      text="Datum: "+tage[wochentag]+" der "+str(tag)+"."+str(monat)+"."+str(jahr)+"\n"
      text+="Zeit:     "+str(stunde)+":"+str(minute)+":"+str(sekunde)+"\n"
      l.set_text(text)
    w=gui.window(title="Uhr")
    l=k.get("widgets").Label(w,text="")
    pc=k.lib["system"]["process"](k,name="clock",code=update)
    w.closed.connect(pc.delete)
  def stopwatch():
    starttime=0
    pc=None
    def proc():
      dif=time()-starttime
      l.set_text(str(dif))
    def starter():
      nonlocal starttime
      nonlocal pc
      stopper()
      starttime=time()
      pc=k.lib["system"]["process"](k,name="stopwatch",code=proc)
    def stopper():
      nonlocal pc
      if pc is not None:
        pc.delete()
        pc=None
    gui=k.get("gui")
    time=k.get("ti_system").get_time_ms
    widgets=k.get("widgets")
    w=gui.window(title="Stopuhr")
    l=widgets.Label(w,height=0.5,text="0")
    start=widgets.Button(w,y=0.55,height=0.45,width=0.48,text="Start",text_align="center")
    stop=widgets.Button(w,y=0.55,height=0.45,x=0.52,width=0.48,text="Stop",text_align="center")
    start.clicked.connect(starter)
    stop.clicked.connect(stopper)
    w.closed.connect(stopper)
  def timer():
    sys=k.get("ti_system")
    gui=k.get("gui")
    widgets=k.get("widgets")
    w=gui.window(title="Timer")
    time=widgets.NumberChoose(w,height=0.5,suffix=" sek",value=60)
  app=k.get("apps")
  app(name="Timer",categories=["Zubehör/Zeit"],startcode=timer)
  app(name="Stopuhr",categories=["Zubehör/Zeit"],startcode=stopwatch)
  app(name="Uhr",categories=["Zubehör/Zeit"],startcode=clock)
