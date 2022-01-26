from distutils import command
import tkinter as tk
window = tk.Tk()
counter = 0

#button = tk.Button(text='Click this button', bg="white", fg="black")
#print(button.configure().keys())
#button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
def buttonfunction():
    global window,counter
    if counter == 0:
        color = 'green'
        window.configure(bg=(color))
        print(f"The window color is now: {color}")
        counter += 1

    else:
        color = 'red'
        window.configure(bg=(color))
        print(f"The window color is now: {color}")
        counter -= 1
    return



button = tk.Button(text='Click here', bg="white", fg="black", command = buttonfunction)
button.pack(pady = 50, padx = 50)

# schijf hier tussen je code

window.mainloop()
