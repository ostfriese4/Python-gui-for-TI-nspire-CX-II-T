def ImportToKernel(k):
  sys=k.get("ti_system")

  theme=k.lib["gui"]["theme"]("Default")

  def drawNumberChoose(x,y,width,height,text):
    sys.set_color(255,0,0)
    sys.draw_line(x+width-10,y,x+width-10,y+height)
    sys.draw_line(x+width-10,y+height*0.5,x+width,y+height*0.5)
    sys.draw_rect(x,y,width,height)
    sys.draw_text(x+2,y+height*0.5+7,text)

  def drawMenuItem(x,y,text):
    sys.set_color(0,255,0)
    k.lib["gui"]["draw title"](x+2,y+19,96,text)
    sys.set_color(255,0,0)
    sys.draw_line(x,y+20,x+100,y+20)

  def drawMenuCascadeItem(x,y,text):
    sys.set_color(0,255,0)
    k.lib["gui"]["draw title"](x+2,y+19,90,text)
    sys.draw_text(x+92,y+19,">")
    sys.set_color(255,0,0)
    sys.draw_line(x,y+20,x+100,y+20)

  def drawActiveMenuItem(x,y,text):
    sys.set_color(0,255,0)
    sys.fill_rect(x+1,y+1,99,19)
    sys.set_color(255,0,0)
    k.lib["gui"]["draw title"](x+2,y+19,96,text)
    sys.draw_line(x,y+20,x+100,y+20)

  def drawActiveMenuCascadeItem(x,y,text):
    sys.set_color(0,255,0)
    sys.fill_rect(x+1,y+1,99,19)
    sys.set_color(255,0,0)
    k.lib["gui"]["draw title"](x+2,y+19,90,text)
    sys.draw_text(x+92,y+19,">")
    sys.draw_line(x,y+20,x+100,y+20)

  def drawMenuBackground(x,y,width,height):
      sys.set_color(0,0,0)
      sys.fill_rect(x,y,width,height)
      sys.set_color(255,0,0)
      sys.draw_rect(x,y,width,height)

  def drawButtonBg(x,y,width,height,color):
    if color is None:
      color=(50,50,50)
    sys.set_color(color)
    sys.fill_rect(x,y,width,height)

  def drawTextEditBg(x,y,width,height):
    sys.set_color(255,50,50)
    sys.draw_rect(x,y,width,height)

  def drawTaskTitle(x,y,width,height,title):
    x+=2
    width-=4
    sys.set_color(200,0,0)
    sys.fill_rect(x,y,width,height)
    sys.set_color(0,255,0)
    sys.draw_rect(x,y,width,height)
    k.lib["gui"]["draw title"](x+1,y+16,width-2,title)

  def drawBg():
    sys.set_color(0,0,0)
    sys.fill_rect(0,0,318,212)

  def drawTaskBackground():
    sys.set_color(255,0,0)
    sys.fill_rect(0,192,318,20)
    sys.set_color(0,255,0)
    sys.draw_poly([2,10,18,2],[210,194,210,210])

  def drawWindowBg(x,y,width,height,title,window):
    sys.set_color(0,0,0)
    sys.fill_rect(x,y,width,height)
    sys.set_color(255,0,0)
    sys.draw_rect(x,y,width,height)
    sys.draw_line(x,y+20,x+width,y+20)
    sys.draw_text(x+width-15,y+19,"X")
    if window.maximized():
      sys.draw_rect(x+width-35,y+5,7,7)
      sys.draw_rect(x+width-38,y+8,7,7)
      sys.set_color(0,0,0)
      sys.fill_rect(x+width-34,y+7,5,5)
      sys.set_color(255,0,0)
    else:
      sys.draw_rect(x+width-35,y+5,10,10)
    sys.draw_line(x+width-55,y+10,x+width-45,y+10)
    k.lib["gui"]["draw title"](x+1,y+20,width-60,title)

  def drawNotification(x,y,width,height,text,app):
    sys.set_color(0,0,0)
    sys.fill_rect(x,y,width,height)
    sys.set_color(255,0,0)
    sys.draw_rect(x,y,width,height)
    k.lib["gui"]["draw title"](x+2,y+19,width-12,app)
    y2=y+19
    for line in text:
      y2+=17
      if y2>y+height:
        return
      sys.draw_text(x+2,y2,line)


  def drawSearchInput(x,y,width,height,inputer):
    sys.set_color(120,120,0)
    sys.fill_rect(x+1,y+1,width-3,height-3)
    sys.set_color(0,0,0)
    sys.draw_rect(x+1,y+1,width-3,height-3)
    sys.draw_text(x+3,y+17,inputer)
  def drawSearchBg(x,y,width,height):
    sys.set_color(150,150,0)
    sys.fill_rect(x,y,width,height)
  def drawSearchItem(x,y,width,height,item):
    sys.set_color(120,120,0)
    sys.fill_rect(x,y,width-3,height-3)
    sys.set_color(0,0,0)
    sys.draw_rect(x,y,width-3,height-3)
    sys.draw_text(x+1,y+16,item.name)
  def drawSearchEnabledItem(x,y,width,height,item):
    sys.set_color(200,200,0)
    sys.fill_rect(x,y,width-3,height-3)
    sys.set_color(0,0,0)
    sys.draw_rect(x,y,width-3,height-3)
    sys.draw_text(x+1,y+16,item.name)
    sys.draw_text(x+1,y+16,item.name)
  theme.set("draw search enabled item",drawSearchEnabledItem)
  theme.set("draw search bg",drawSearchBg)
  theme.set("draw search input",drawSearchInput)
  theme.set("draw search item",drawSearchItem)


  def drawExtraKeysBg():
    sys.set_color(0,0,0)
    x,y,width,height=(0,0,318,212)
    sys.fill_rect(x,y,width,height)
  def drawExtraKeysKeysBg(x,y,width,height):
    sys.set_color(255,0,0)
    sys.draw_rect(x,y,width,height)
    x2=22
    while x2 < x+width:
      sys.draw_line(x2,y,x2,y+height)
      x2+=20
    y2=20
    while y2 < y+height:
      sys.draw_line(x,y2,x+width,y2)
      y2+=20
  def drawExtraKeysKey(x,y,i):
      sys.set_color(255,0,0)
      width2,height2=sys.string_size(i)
      sys.draw_text(x+(10-width2/2),y+height2,i)
  def drawExtraKeysEnabledKey(x,y,i):
      sys.set_color(150,150,150)
      sys.fill_rect(x+1,y+1,19,19)
      sys.set_color(255,0,0)
      width2,height2=sys.string_size(i)
      sys.draw_text(x+(10-width2/2),y+height2,i)
  def drawExtraKeysEraseKey(x,y):
    sys.set_color(0,0,0)
    sys.fill_rect(x+1,y+1,19,19)
  theme.set("draw extra characters key area bg",drawExtraKeysKeysBg)
  theme.set("draw extra characters erase key", drawExtraKeysEraseKey)
  theme.set("draw extra characters enabled key", drawExtraKeysEnabledKey)
  theme.set("draw extra characters key", drawExtraKeysKey)
  theme.set("draw extra characters background", drawExtraKeysBg)

  theme.set("draw notification",drawNotification)
  theme.set("draw menu item",drawMenuItem)
  theme.set("draw menu cascade item",drawMenuCascadeItem)
  theme.set("draw active menu item",drawActiveMenuItem)
  theme.set("draw active menu cascade item",drawActiveMenuCascadeItem)
  theme.set("draw menu background",drawMenuBackground)
  theme.set("app menu position",[0,192])
  theme.set("window widgets area",[5,25,-11,-31])
  theme.set("maximized window data",[-1,-1,320,194])
  theme.set("task title area position",[20,194,298,16])
  theme.set("app menu area position",[0,192,20,20])
  theme.set("notification position size",[163,115,150,75])
  theme.set("task position",[0,192,318,20])
  theme.set("resize button right",[-1,0,0,-1])
  theme.set("resize button bottom",[0,-1,-1,0])
  theme.set("resize button top",[0,0,-1,0])
  theme.set("resize button left",[0,0,0,-1])
  theme.set("move button area",[1,1,-61,20])
  theme.set("close button area",[-21,0,20,20])
  theme.set("maximize button area",[-41,0,20,20])
  theme.set("minimize button area",[-61,0,20,20])
  theme.set("label button text color",(255,0,0))
  theme.set("menu item height",20)
  theme.set("menu top height",0)
  theme.set("menu bottom height",0)
  theme.set("draw task title",drawTaskTitle)
  theme.set("draw task background",drawTaskBackground)
  theme.set("draw bg",drawBg)
  theme.set("draw window background",drawWindowBg)
  theme.set("draw button bg",drawButtonBg)
  theme.set("draw TextEdit bg",drawTextEditBg)
  theme.set("notification time",5000)
  theme.set("floating panel",False)
  theme.set("tab edge panel","bottom")
  theme.set("tab time panel",500)
  theme.set("draw numberchoose",drawNumberChoose)

  return theme
