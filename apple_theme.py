def ImportToKernel(k):
  sys=k.get("ti_system")
  theme=k.lib["gui"]["theme"]("Apple")
  theme2=k.lib["gui"]["theme"]("Apple dark")
  colors={}
  colors2={}
  def dc(color):
    return k.lib["gui"]["enabled theme"].get("colors")[color]

  def drawButtonBg(x,y,width,height,color):
    if color is None:
      color=dc("button background")
    sys.set_color(color)
    fillRoundedRect(x,y,width,height)

  def drawTextEditBg(x,y,width,height):
    sys.set_color(0,0,0)
    drawRoundedRect(x,y,width,height)

  def drawTaskTitle(x,y,width,height,title):
    x+=2
    width-=4
    sys.set_color(dc("task title"))
    drawRoundedRect(x,y,width,height)
    k.lib["gui"]["draw title"](x+2,y+14,width-4,title)

  def drawTaskBackground():
    sys.set_color(dc("task bg"))
    fillRoundedRect(10,190,298,17)
    sys.set_color(0,0,0)
    drawRoundedRect(10,190,298,17)
    sys.set_color(255,0,0)
    sys.plot_xy(16,195,8)
    sys.set_color(0,255,0)
    sys.plot_xy(16,203,8)
    sys.set_color(0,0,255)
    sys.plot_xy(24,195,8)
    sys.set_color(255,255,0)
    sys.plot_xy(24,203,8)

  def drawMenuItem(x,y,text):
    sys.set_color(dc("menu text"))
    k.lib["gui"]["draw title"](x+2,y+19,96,text)

  def drawMenuCascadeItem(x,y,text):
    sys.set_color(dc("menu text"))
    k.lib["gui"]["draw title"](x+2,y+19,90,text)
    sys.draw_text(x+92,y+19,">")

  def drawActiveMenuItem(x,y,text):
    sys.set_color(0,0,255)
    fillRoundedRect(x+1,y+1,99,19)
    sys.set_color(dc("menu text"))
    k.lib["gui"]["draw title"](x+2,y+19,96,text)

  def drawActiveMenuCascadeItem(x,y,text):
    sys.set_color(0,0,255)
    fillRoundedRect(x+1,y+1,99,19)
    sys.set_color(dc("menu text"))
    k.lib["gui"]["draw title"](x+2,y+19,90,text)
    sys.draw_text(x+92,y+19,">")

  def drawMenuBackground(x,y,width,height):
      sys.set_color(dc("menu bg"))
      fillRoundedRect(x,y,width,height)
      sys.set_color(0,0,0)
      drawRoundedRect(x,y,width,height)

  def drawApple(x,y,width,height):
    sys.fill_circle(x+width*0.25,y+height*0.25,width*0.75)
    sys.set_color(255,255,255)
    sys.fill_arc(x+width*0.5,y,width*0.125,height*0.25,120,360)

  def fillRoundedRect(x,y,width,height):
    sys.fill_rect(x,y+5,width,height-10)
    sys.fill_rect(x+5,y,width-10,height)
    sys.fill_circle(x+5,y+5,5)
    sys.fill_circle(x+5,y+height-5,5)
    sys.fill_circle(x+width-5,y+5,5)
    sys.fill_circle(x+width-5,y+height-5,5)

  def drawRoundedRect(x,y,width,height):
    sys.draw_line(x+5,y,x+width-5,y)
    sys.draw_line(x+5,y+height,x+width-5,y+height)
    sys.draw_line(x,y+5,x,y+height-5)
    sys.draw_line(x+width,y+5,x+width,y+height-5)
    sys.draw_arc(x,y,10,10,90,90)
    sys.draw_arc(x+width-10,y,10,10,0,90)
    sys.draw_arc(x,y+height-10,10,10,180,90)
    sys.draw_arc(x+width-10,y+height-10,10,10,270,90)

  def drawBg():
    sys.set_color(dc("bg"))
    sys.fill_rect(0,0,318,212)
    sys.set_color(0,0,0)
    drawApple(109,56,100,100)

  def drawWindowBg(x,y,width,height,title,window):
    sys.set_color(dc("window bg"))
    fillRoundedRect(x,y,width,height)
    sys.set_color(dc("window title"))
    sys.draw_line(x,y+15,x+width,y+15)
    drawRoundedRect(x,y,width,height)
    k.lib["gui"]["draw title"](x+48,y+14,width-50,title)
    sys.set_color(255,0,0)
    sys.fill_circle(x+8,y+8,6)
    sys.set_color(255,255,0)
    sys.fill_circle(x+24,y+8,6)
    sys.set_color(0,220,0)
    sys.fill_circle(x+40,y+8,6)

  def drawNotification(x,y,width,height,text,app):
    sys.set_color(255,255,255)
    fillRoundedRect(x,y,width,height)
    sys.set_color(0,0,0)
    drawRoundedRect(x,y,width,height)
    k.lib["gui"]["draw title"](x+2,y+14,width-4,app)
    y2=y+15
    for line in text:
      y2+=15
      if y2>y+height:
        return
      sys.draw_text(x+2,y2,line)

  theme.set("draw window background",drawWindowBg)
  theme.set("draw bg",drawBg)
  theme.set("resize button right",[-1,0,0,-1])
  theme.set("resize button bottom",[0,-1,-1,0])
  theme.set("resize button top",[0,0,-1,0])
  theme.set("resize button left",[0,0,0,-1])
  theme.set("move button area",[46,1,-1,15])
  theme.set("close button area",[2,2,12,12])
  theme.set("maximize button area",[34,2,12,12])
  theme.set("minimize button area",[18,2,12,12])
  theme.set("window widgets area",[3,19,-7,-23])
  theme.set("maximized window data",[-1,-1,320,214])
  colors["window bg"]=(255,255,255)
  colors2["window bg"]=(55,55,55)
  colors["window title"]=(0,0,0)
  colors2["window title"]=(200,200,200)

  theme.set("draw notification",drawNotification)
  theme.set("notification position size",[163,110,150,75])

  theme.set("draw menu background",drawMenuBackground)
  theme.set("draw menu item",drawMenuItem)
  theme.set("draw menu cascade item",drawMenuCascadeItem)
  theme.set("draw active menu item",drawActiveMenuItem)
  theme.set("draw active menu cascade item",drawActiveMenuCascadeItem)
  colors["menu text"]=(0,0,0)
  colors["menu bg"]=(255,255,255)
  colors2["menu text"]=(230,230,230)
  colors2["menu bg"]=(0,0,0)

  theme.set("task title area position",[28,192,280,13])
  theme.set("app menu area position",[10,190,18,18])
  theme.set("task position",[10,190,298,18])
  theme.set("app menu position",[10,180])
  theme.set("draw task title",drawTaskTitle)
  theme.set("floating panel",True)
  theme.set("draw task background",drawTaskBackground)
  colors["task bg"]=(255,255,255)
  colors["task title"]=(0,0,0)
  colors2["task bg"]=(50,50,50)
  colors2["task title"]=(230,230,230)

  theme.set("label button text color",(0,0,0))
  theme.set("draw button bg",drawButtonBg)
  theme.set("draw TextEdit bg",drawTextEditBg)
  colors["button background"]=(200,200,200)
  colors2["button background"]=(0,0,0)
  theme.set("colors",colors)


  def drawSearchInput(x,y,width,height,inputer):
    sys.set_color(dc("window bg"))
    fillRoundedRect(x,y,width,height)
    sys.set_color(dc("window title"))
    drawRoundedRect(x,y,width,height)
    sys.draw_text(x+3,y+17,inputer)
  def drawSearchBg(x,y,width,height):
    sys.set_color(dc("window bg"))
    fillRoundedRect(x,y,width,height)
    sys.set_color(dc("window title"))
    drawRoundedRect(x,y,width,height)
  def drawSearchItem(x,y,width,height,item):
    sys.set_color(dc("window title"))
    sys.draw_text(x+1,y+16,item.name)
  def drawSearchEnabledItem(x,y,width,height,item):
    sys.set_color(0,0,255)
    fillRoundedRect(x,y,width-1,height-1)
    sys.set_color(dc("window title"))
    sys.draw_text(x+1,y+16,item.name)
  theme.set("draw search enabled item",drawSearchEnabledItem)
  theme.set("draw search bg",drawSearchBg)
  theme.set("draw search input",drawSearchInput)
  theme.set("draw search item",drawSearchItem)

  def drawExtraKeysBg():
    sys.set_color(dc("window bg"))
    x,y,width,height=(0,0,318,212)
    sys.fill_rect(x,y,width,height)
    sys.set_color(dc("window title"))
    drawRoundedRect(x,y,width,height)
  def drawExtraKeysKey(x,y,i):
      sys.set_color(dc("window title"))
      width2,height2=sys.string_size(i)
      sys.draw_text(x+(10-width2/2),y+height2,i)
  def drawExtraKeysEnabledKey(x,y,i):
      sys.set_color(0,0,255)
      sys.fill_rect(x+1,y+1,19,19)
      sys.set_color(dc("window title"))
      width2,height2=sys.string_size(i)
      sys.draw_text(x+(10-width2/2),y+height2,i)
  def drawExtraKeysEraseKey(x,y):
    sys.set_color(dc("window bg"))
    sys.fill_rect(x+1,y+1,19,19)
  def drawExtraKeysKeysBg(x,y,width,height):
    sys.set_color(dc("window title"))
    drawRoundedRect(x,y,width,height)
    x2=x+20
    while x2 < x+width:
      sys.draw_line(x2,y,x2,y+height)
      x2+=20
    y2=y+20
    while y2 < y+height:
      sys.draw_line(x,y2,x+width,y2)
      y2+=20
  theme.set("draw extra characters key area bg",drawExtraKeysKeysBg)
  theme.set("draw extra characters erase key", drawExtraKeysEraseKey)
  theme.set("draw extra characters enabled key", drawExtraKeysEnabledKey)
  theme.set("draw extra characters key", drawExtraKeysKey)
  theme.set("draw extra characters background", drawExtraKeysBg)
  theme.set("extra characters dialog position size",(5,5,308,202))

  colors["bg"]=(255,255,0)
  colors2["bg"]=(0,100,0)

  theme2.data=theme.data.copy()
  theme2.set("label button text color",(255,255,255))
  theme2.set("colors",colors2)
