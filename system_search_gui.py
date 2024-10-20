def ImportToKernel(k):
  k.get("basic_search_modules")
  backend=k.get("system_search")
  k.get("_gui")
  sys=k.get("ti_system")
  input=k.get("input")
  theme=k.lib["gui"]["enabled theme"]
  inputer=input.input(text="")
  inputer.disable()
  items=[]
  enabled=0
  def search():
    nonlocal items
    nonlocal enabled
    enabled=0
    term=inputer.text
    if term=="":
      items=[]
      area.resize(218,20)
    else:
      items=backend.search(term)
      area.resize(218,20+20*len(items))
  def draw():
    x,y=area.get_position()
    width,height=area.get_size()
    theme.get("draw search bg")(x,y,width,height)
    theme.get("draw search input")(x,y,width,20,inputer.text)
    x=51
    y=21
    i=0
    for item in items:
      if i==enabled:
        theme.get("draw search enabled item")(x,y,width,20,item)
      else:
        theme.get("draw search item")(x,y,width,20,item)
      y+=20
      i+=1
  def click(x,y):
    i=int(y*0.05)
    i-=1
    item=items[i]
    k.run_code(item.code)
    disable()
  def enable():
    nonlocal enabled
    enabled=0
    inputer.enable()
    area.enable()
  def disable():
    inputer.disable()
    area.hide()
  def button():
    if area.isEnabled():
      disable()
    else:
      enable()
  def up():
    nonlocal enabled
    enabled-=1
    if enabled==-1:
      enabled=len(items)-1
    area.update()
  def down():
    nonlocal enabled
    enabled+=1
    if enabled==len(items):
      enabled=0
    area.update()
  def enter():
    k.run_code(items[enabled].code)
    disable()

  area=k.lib["gui"]["area"](50,0,218,20,draw=draw,click=click)
  area.hide()
  inputer.updated.connect(area.update)
  inputer.textChanged.connect(search)
  input.key("doc").pressed.connect(button)
  area.not_clicked.connect(disable)
  area.key("up").connect(up)
  area.key("down").connect(down)
  area.key("enter").connect(enter)
