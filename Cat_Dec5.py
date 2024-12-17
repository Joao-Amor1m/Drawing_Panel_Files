import DrawingPanel


w = DrawingPanel.DrawingPanel(300,300)
#draw body/head
w.fill_oval(50,50,200,200,"grey")
#draw eyes
w.fill_oval(90,90,50,50,"white")
w.fill_oval(160,90,50,50,"white")
w.fill_oval(97,92,25,45, "blue") #iris
w.fill_oval(167,92,25,45, "blue")
w.fill_oval(95,95,20,40) #pupils
w.fill_oval(165,95,20,40)

#draw ears
w.fill_polygon(70,30,110,60,70,90,70,30, "grey") #outer
w.fill_polygon(230,30,190,60,230,90,230,30, "grey")
w.fill_polygon(80,30,100,60,80,90,70,30,"pink") #inner

#draw mouth/nose
w.draw_line(130,210,150,200)#mouth
w.draw_line(150,200,170,210)
w.draw_line(150,200,150,190)
w.fill_polygon(150,190,130,170,170,170,150,190,"pink")#nose
#whiskers
w.draw_line(110,190,30,170)#left
w.draw_line(110,200,30,200)
w.draw_line(110,210,30,230)
w.draw_line(190,190,270,170)#right
w.draw_line(190,200,270,200)
w.draw_line(190,210,270,230)
