import tkinter as tk
import random
import tkinter.messagebox as tm

l = ['NATHAN IS DONKEY', 'ur mum', 'DEMONISDONKEY', 'ur donkey']
rd = random.choice(l)
window = tk.Tk()
window.title("WHO IS DONKEY????")
frame = tk.Frame()

frame2 = tk.Frame()
frame3 = tk.Frame()
label = tk.Label(text="Donkey Game")
label.pack()
entry = tk.Entry(fg="yellow", bg="blue", width=100)
entry.pack()
def helloCallBack():
   entry.delete(0)
   entry.insert(0, rd)
   tm.showinfo("so the donkey is", rd)
   print(rd)

B = tk.Button(window, text = "who is donkey???", command = helloCallBack)

B.pack()



window.mainloop()