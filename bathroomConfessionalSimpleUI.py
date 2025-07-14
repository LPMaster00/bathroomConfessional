import tkinter as tk

def display_text(filepath):
    with open(filepath, "r") as file:
        content = file.read()

    root = tk.Tk()
    root.title("Confession Booth")
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    label = tk.Label(root, text=content,
                     fg='white', bg='black',
                     font=('Helvetica', 36), wraplength=1000,
                     justify='center')
    label.pack(expand=True)

    # Auto close after 10 seconds or when user presses a key
    root.after(10000, root.destroy)
    root.bind("<Escape>", lambda e: root.destroy())  # ESC to quit
    root.mainloop()

display_text("introductionText.txt")