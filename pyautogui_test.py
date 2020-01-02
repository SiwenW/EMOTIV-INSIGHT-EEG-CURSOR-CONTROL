
import pyautogui

currX,currY=pyautogui.position()
maxX,maxY=pyautogui.size()
movX=float(input("Enter x position you want to move: "))
pyautogui.moveRel(movX,0,5)
movY=float(input("Enter y position you want to move: "))
pyautogui.moveRel(0,movY,1)

