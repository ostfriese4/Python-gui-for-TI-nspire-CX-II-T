def ImportToKernel(k):
  def start():
    base=k.get("game_platform")
    sys=k.get("ti_system")
    k.get("gui")
    gui=k.lib["gui"]
    w=gui["window"](title="TicTacToe")
    sign="[X]"
    count=0
    looser=base.user1
    gui["notification"]("TicTacToe",base.user1.name+" starts")
    def reset():
      nonlocal count
      nonlocal sign
      sign="[X]"
      count=0
      gui["notification"]("TicTacToe",looser.name+" starts")
      for row in range(3):
        for column in range(3):
          space[row][column].set_text("[  ]")
    def get(x,y):
      return space[y][x].get_text()
    def check():
      nonlocal looser
      result=analyze()
      if result=="[]":result=""
      if result=="[X]":result="X"
      if result!=False:
        if result=="X":
          user=looser
        else:
          if looser == base.user1:
            user=base.user2
          else:
            user=base.user1
        user.score+=1
        if user==base.user1:
          looser=base.user2
        else:
          looser=base.user1
        gui["notification"]("TicTacToe",user.name+" won").timeout.connect(reset)
      elif count==9:
        gui["notification"]("TicTacToe","Tie").timeout.connect(reset)
    def analyze():
      for row in range(3):
        if get(0,row)==get(1,row)==get(2,row) and get(0,row)!="[  ]":
          return get(0,row)
      for column in range(3):
        if get(column,0)==get(column,1)==get(column,2) and get(column,0)!="[  ]":
          return get(column,0)
      if get(0,0)==get(1,1)==get(2,2) and get(1,1)!="[  ]":
        return get(1,1)
      if get(2,0)==get(1,1)==get(0,2) and get(1,1)!="[  ]":
        return get(1,1)
      return False
    def click(info):
      nonlocal count
      nonlocal sign
      widget=info["widget"]
      if widget.get_text()=="[  ]":
        widget.set_text(sign)
        if sign=="[X]":
          sign="[]"
        else:
          sign="[X]"
        count+=1
        check()
    row=0
    column=0
    space=[[]]
    for i in range(9):
      b=gui["Button"](w,x=0.333*column,y=0.333*row,width=0.3,height=0.3,text="[  ]",text_align="center")
      b.clicked.connect(click)
      space[row].append(b)
      column+=1
      if column==3:
        column=0
        row+=1
        space.append([])
  def init():
    k.get("game_platform").init(start)
  k.get("apps")(name="TicTacToe",categories=["Games"],startcode=init)
