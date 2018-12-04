from kandinsky import*

def carre(x1,y1,x2,y2):
    for i in range(100): 
        set_pixel(x1, i, color(0,0,0))
    for i in range(100):
        set_pixel(x2, i, color(0,0,0))
    for i in range(100):
        set_pixel(i, y1, color(0,0,0))
    for i in range(100):
        set_pixel(i, y2, color(0,0,0))
        
input()
