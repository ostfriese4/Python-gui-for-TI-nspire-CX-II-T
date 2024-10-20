def ImportToKernel(k):
  keys=k.get("extra_characters_database").list
  search_term=""
  k.get("_gui")
  inputer=None
  theme=k.lib["gui"]["enabled theme"]
  sys=k.get("ti_system")
  enabled=0
  enabled_all=0
  key_area=(2,20,300,160)
  search_area=(2,2,315,16)
  description_area=(2,182,315,28)
  upper_row=0
  upper_row_all=0
  search_input=k.get("input").input()
  search_input.disable()
  def draw():
    theme.get("draw extra characters background")()
    draw_search()
    draw_keys()
    draw_description()
  def draw_description():
    data=k.get("extra_characters_database")
    x,y,width,height=description_area
    description="No description provided"
    try:
      description=data.descriptions[keys[enabled]]
    except KeyError:
      pass
    sys.set_color(0,0,0)
    sys.fill_rect(x,y,width,height)
    sys.set_color(255,0,0)
    sys.draw_text(x+2,y+16,description)
  def draw_search():
    x,y,width,height=search_area
    theme.get("draw TextEdit bg")(x,y,width,height)
    sys.set_color(255,0,0)
    sys.draw_text(x+2,y+16,search_term)
  def draw_keys():
    x2,y2,width,height=key_area
    theme.get("draw extra characters key area bg")(x2,y2,width,height)
    pos=upper_row*int(width*0.05)
    shown_keys=keys[pos:]
    x=x2
    y=y2
    j=0
    for i in shown_keys:
      if y>y2+height-20:
        return
      if j==enabled-pos:
        theme.get("draw extra characters enabled key")(x,y,i)
      else:
        theme.get("draw extra characters key")(x,y,i)
      j+=1
      x+=20
      if x-x2>width-20:
        x=x2
        y+=20
  def click(x,y):
    ax,ay,awidth,aheight=key_area
    if x>=ax and y>=ay and x<=ax+awidth and y<=ay+aheight:
      click_keys(x,y)
  def click_keys(x,y):
    x2,y2,width2,height2=key_area
    width=int(width2*0.05)
    x-=x2
    y-=y2
    x*=0.05
    x=int(x)
    y*=0.05
    y=int(y)
    i=y*width+x
    i+=width*upper_row
    if i==enabled:
      key=keys[i]
      print("clicked and choosen",key)
      choose(key)
    else:
      print("cliked and marked",keys[i])
      set_enabled(i)
  def choose(key):
    nonlocal inputer
    search_input.disable()
    if inputer:
      inputer.enable()
    k.lib["input"]["simulate"](key)
    hide()
    if inputer:
      i=inputer
      def reenable():
        i.disabled.disconnect(reenable)
        i.enable()
      inputer.disabled.connect(reenable)
      inputer=None
  def enter():
    key=keys[enabled]
    choose(key)
  area=k.lib["gui"]["area"](x=0,y=0,width=318,height=212,draw=draw,click=click)
  def show():
    nonlocal inputer
    if area.isEnabled():
      hide()
    else:
      area.enable()
      inputer=k.lib["input"]["get inputer"]()
      if inputer and inputer!=search_input:
        inputer.disable()
      search_input.enable()
  def hide():
    nonlocal search_input
    search_input.disable()
    search_input.text=""
    search()
    area.hide()
  def search():
    nonlocal search_term
    nonlocal keys
    nonlocal enabled
    nonlocal enabled_all
    nonlocal upper_row
    nonlocal upper_row_all
    data=k.get("extra_characters_database")
    if keys==data.list:
      enabled_all=enabled
      upper_row_all=upper_row
    search_term=search_input.text
    enabled=0
    upper_row=0
    if search_term=="":
      keys=data.list
      enabled=enabled_all
      upper_row=upper_row_all
    else:
      keys=[]
      terms=search_term.split(" ")
      for term in terms:
        for i in data.descriptions:
          if term.lower() in data.descriptions[i].lower():
            if not i in keys:
              keys.append(i)
    area.update()
  search_input.textChanged.connect(search)
  k.get("input").key("cat").pressed.connect(show)
  hide()
  def left():
    i=enabled-1
    if i==-1:
      i=len(keys)-1
    set_enabled(i)
  area.key("left").connect(left)
  def right():
    i=enabled+1
    if i==len(keys):
      i=0
    set_enabled(i)
  area.key("right").connect(right)
  def up():
    x,y,width,height=key_area
    width=int(width*0.05)
    x2=enabled-int(enabled/width)*width
    i=enabled-width
    if i<0:
      i=len(keys)+i
      x3=i-int(i/width)*width
      i+=x2-x3
      print(x2,x3)
      if i >= len(keys):
        i-=width
    set_enabled(i)
  area.key("up").connect(up)
  def down():
    x,y,width,height=key_area
    width=int(width*0.05)
    i=enabled+width
    x2=(i-int(i/width)*width)
    if i>=len(keys):
      i-=len(keys)
      x3=(i-int(i/width)*width)
      i+=x2-x3
    set_enabled(i)
  area.key("down").connect(down)
  area.key("enter").connect(enter)
  def draw_key(id):
    e=(id==enabled)
    x2,y2,width2,height2=key_area
    key=keys[id]
    width=int(width2*0.05)
    id-=width*upper_row
    y=y2+int(id/width)*20
    x=x2+(id-int(id/width)*width)*20
    theme.get("draw extra characters erase key")(x,y)
    if e:
      theme.get("draw extra characters enabled key")(x,y,key)
    else:
      theme.get("draw extra characters key")(x,y,key)
  def set_enabled(new):
    nonlocal enabled
    nonlocal upper_row
    x,y,width,height=key_area
    width=int(width*0.05)
    height=int(height*0.05)
    top=upper_row*width
    bottom=top+(width*height)
    bottom-=1
    draw=True
    while new<top or new>bottom:
      draw=False
      if new<top:
        upper_row-=1
        area.update()
      if new>bottom:
        upper_row+=1
        area.update()
      top=upper_row*width
      bottom=top+(width*height)
      bottom-=1
    old=enabled
    enabled=new
    if draw:
      draw_key(old)
      draw_key(new)
      draw_description()
      sys.paint_buffer()
  k.get("input").key("pi").pressed.connect(lambda:k.get("input").simulate("π"))
  return show
