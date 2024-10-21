def ImportToKernel(k):
  search=k.get("system_search")
  _ = k.get("translations.py").translate
  runner=search.modul("Time")
  def runner_search(term):
    dateTerm = _("week") + _("day") + _("date") + _("weekday") #This are the keywords for showing a result
    term=term.lower()
    dateTerm = dateTerm.lower()
    if term in dateTerm:
      time=k.get("time").localtime()
      month=[_("January"),_("February"),_("March"),_("April"),_("May"),_("June"),_("July"),_("August"),_("September"),_("October"),_("November"),_("December")][time[1]-1]
      day=[_("Monday"),_("Tuesday"),_("Wednesday"),_("Thursday"),_("Friday"),_("Saturday"),_("Sunday")][time[6]]
      text = _("{day} the {monthday}. {month} {year}")
      text=text.replace("{day}", day)
      text=text.replace("{monthday}", str(time[2])
      text=text.replace("{month}",month)
      text=text.replace("{year}", str(time[0]))
      return [search.item(text,_("Date"),clock)]
    if term in "zeitimeclockuhr":
      time=k.get("time").localtime()
      text=_("The time is {h}:{m}")
      text=text.replace("{h}",time[3])
      text=text.replace("{m}",time[4])
      text=text.replace("{s}",time[5])
      return [search.item(text,_("Time"),clock)]
    return []
  runner.search=runner_search
  def clock():
    time=k.get("time")
    gui=k.get("gui")
    days=[_("January"),_("February"),_("March"),_("April"),_("May"),_("June"),_("July"),_("August"),_("September"),_("October"),_("November"),_("December")]
    def update():
      year,month,day,hour,minute,second,weekday,yearday,summertime=time.localtime()
      text=_("Date") + ": " +  _("{day} the {monthday}.{month}.{year}") + _("Time") + ": {h}{m}{s}"
      text=text.replace("{day}", days[weekday])
      text=text.replace("{monthday}", str(day)
      text=text.replace("{month}",month)
      text=text.replace("{year}", str(year))
      text=text.replace("{h}", str(hour))
      text=text.replace("{m}", str(minute))
      text=text.replace("{s}", str(second))
      l.set_text(text)
    w=gui.window(title=_("Clock"))
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
    w=gui.window(title=_("Stopwatch"))
    l=widgets.Label(w,height=0.5,text="0")
    start=widgets.Button(w,y=0.55,height=0.45,width=0.48,text=_("Start"),text_align="center")
    stop=widgets.Button(w,y=0.55,height=0.45,x=0.52,width=0.48,text=_("Stop"),text_align="center")
    start.clicked.connect(starter)
    stop.clicked.connect(stopper)
    w.closed.connect(stopper)
  def timer():
    sys=k.get("ti_system")
    gui=k.get("gui")
    widgets=k.get("widgets")
    w=gui.window(title=_("Timer"))
    time=widgets.NumberChoose(w,height=0.5,suffix=" sek",value=60)
  app=k.get("apps")
  app(name="Timer",categories=["Utilities/Time"],startcode=timer)
  app(name="Stopwatch",categories=["Utilities/Time"],startcode=stopwatch)
  app(name="Clock",categories=["Utilities/Time"],startcode=clock)
