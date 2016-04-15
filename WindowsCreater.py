from tkinter import*
import time
count=-1
canvasarray=[]
animation=Tk()
photoarray=[]
def createNewCanvas(width1,height1):
        global count
        count=count+1
        global animation
        canvas=Canvas(animation,width=width1,height=height1)
        canvasarray.append(canvas)
def createRectangle(x0,y0,x1,y1,color):
    if(count == -1):
        print("A frame has not been create")
    else:
        canvas=canvasarray[count]
        canvas.create_rectangle(x0,y0,x1,y1,fill=color)


def createCircle(x0,y0,radius,color):
    if(count == -1):
        print("A frame has not been create")
    else:
        canvas=canvasarray[count]
        canvas.create_oval(x0-radius,y0-radius,x0+radius,y0+radius,fill=color)
        canvas.update()

def createTriangle(x0,y0,x1,y1,x2,y2,color):
    if(count == -1):
        print("A frame has not been create")
    else:
        canvas=canvasarray[count]
        canvas.create_polygon(x0,y0,x1,y1,x2,y2,fill=color)

def loadimage(image,x0,y0):
        global animation
        originalPath = image + ".gif"
        canvas = canvasarray[count]
        photo = PhotoImage(file=originalPath)
        photoarray.append(photo)
        canvas.create_image(x0,y0,image=photo)
        #label = Label(animation, image=photo)
        #label.pack()
    
def run(deltaX,deltaY,iterations,delay):
    if(count == -1):
        print("A frame has not been create")
    else:
        canvas=canvasarray[count]
        canvas.pack()
        global animation
        for i in range(0, iterations):
                animation.update()
                canvas.move(ALL,deltaX,deltaY)
                time.sleep(delay/1000)
                animation.update()        
        print("Done");