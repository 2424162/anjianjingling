from pynput.mouse import Button,Controller
from PIL import ImageGrab
from time import sleep
bbox = (180,185,710,730)
mouse = Controller()
sleep(0.5)
for j in range(336,550):
    for i in range(0,6):
        print(i)
        mouse.position = (1500, 200)
        mouse.press(Button.left)
        mouse.position = (1500, 212)
        mouse.position = (1500,300+40*i)
        img = ImageGrab.grab(bbox)
        img.save("C:\\Users\Lenovo\Desktop\img3\jietu%s%s.jpg" %(j,i))
    mouse.position = (1500,700)
    sleep(3)
    mouse.release(button=Button.left)
    #mouse.position = (550,280)
    #mouse.position = (630, 280)
    mouse.position = (655, 280)
    mouse.click(Button.left)
    sleep(2)
