import tkinter as tk
from gpiozero import PWMLED
from time import sleep

led = PWMLED(18)

def update_brightness(value):
    brightness = int(value) / 100 
    led.value = brightness

root = tk.Tk()
root.title("LED Brightness Control")

tk.Label(root, text="Adjust LED Brightness:").pack(pady=10)

brightness_slider = tk.Scale(root, from_=0, to=100, orient='horizontal', command=update_brightness)
brightness_slider.pack(pady=20)

tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

root.mainloop()
