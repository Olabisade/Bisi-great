import tkinter as tk

def ShowChoice():
    print(var.get())

root = tk.Tk()

var = tk.StringVar()
var.set("Lion")
label1 = tk.Label(root, text="Pick your favorite animal")
label1.pack()
radio1 = tk.Radiobutton(
    root, text="Lion", variable=var, value="Lion", command=ShowChoice
)
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(root, text="Elephant", variable=var, value="Elephant", command=ShowChoice)
radio2.pack(anchor="w")
radio3 = tk.Radiobutton(root, text="Donkey", variable=var, value="Donkey", command=ShowChoice)
radio3.pack(anchor="w")
radio4 = tk.Radiobutton(root, text="Lizard", variable=var, value="Lizard", command=ShowChoice)
radio4.pack(anchor="w")
radio5 = tk.Radiobutton(root, text="Monkey", variable=var, value="Monkey", command=ShowChoice)
radio5.pack(anchor="w")
radio6 = tk.Radiobutton(root, text="Antelope", variable=var, value="Antelope", command=ShowChoice)
radio6.pack(anchor="w")

root.mainloop()
