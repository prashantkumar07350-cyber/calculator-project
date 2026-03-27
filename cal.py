import tkinter as tk 

#function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

#main window
root = tk.Tk()
root.title("calculator")
root.geometry("300x400")
root.minsize(350, 500)

#stringVar for Display
screen = tk.StringVar()

#display Entry
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=8, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

#Button Layout
buttons = [
    ["0", "C", "=", "+"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"]
   
]

#Create buttons
for i, row in enumerate(buttons):
    for j, val in enumerate(row):
        #different colors for buttons
        if val in "+-*/=":
            bg_color = "orange"
            fg_color = "white"
        elif val == "=":
            bg_color = "green"
            fg_color = "white"
        elif val == "C":
            bg_color = "red"
            fg_color = "white"
        else:
            bg_color = "lightblue"
            fg_color = "black"
        btn = tk.Button(root, text=val, font="Arial 16", bg=bg_color, fg=fg_color)
        btn.grid(row=i+1, column=j, sticky="nsew", padx=2, pady=2)
        btn.bind("<Button-1>",click)

#Make grid responsive
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_rowconfigure(j, weight=1)

#run app
root.mainloop()
