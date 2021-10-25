from PIL import Image
import tkinter as tk
from tkinter import ttk


def main():
    global root
    global dir_label
    global dir_Entry
    global name_Entry
    global converted_name_Entry
    global width_Entry
    global height_Entry
    global drop

    root = tk.Tk()
    root.geometry('600x500')
    root.title('Image resizer')
    root.configure(bg='white')

    tk.Label(root, text='Image Resizer', font=('times new roman', 20, 'bold'), bg='white', fg='green').place(x=200, y=20)

    dir_label = tk.Label(text='Enter the directory of Image:', font=('Lato', 12), bg='white')
    dir_label.place(x=50, y=70)

    dir_Entry = tk.Entry(width=50, font=('Arial', 10))
    dir_Entry.place(x=70, y=100)
    dir_Entry.insert(0, 'eg. C:\Lenovo\\')

    tk.Label(root, text='Enter the name of file:', font=('Lato', 12), bg='white').place(x=50, y=130)
    name_Entry = tk.Entry(root, width=30, font=('Arial', 10), bg='white')
    name_Entry.place(x=70, y=160)
    name_Entry.insert(0, 'eg. image.png')

    tk.Label(text="Dimensions:", font=('Lato', 12), bg='white').place(x=50, y=190)

    tk.Label(text="Width", font=('Lato', 12), bg='white').place(x=60, y=220)
    width_Entry = tk.Entry(width=5, font=('Arial', 10))
    width_Entry.place(x=110, y=220)

    tk.Label(text="Height", font=('Lato', 12), bg='white').place(x=180, y=220)
    height_Entry = tk.Entry(width=5, font=('Arial', 10))
    height_Entry.place(x=240, y=220)

    tk.Label(root, text='Enter the name of converted file:', font=('Lato', 12), bg='white').place(x=50, y=250)
    converted_name_Entry = tk.Entry(root, width=30, font=('Arial', 10), bg='white')
    converted_name_Entry.place(x=70, y=280)

    tk.Label(text="Choose the format of resized image:", font=('Lato', 12), bg='white').place(x=50, y=310)
    drop = ttk.Combobox(root, width=5, state='readonly')
    drop['values'] = ('JPG', 'JPEG', 'PNG')
    drop.place(x=70, y=340)

    tk.Button(text='Resize', font=('Lato', 12, 'bold'), bg='black', fg='white', command=resize).place(x=200, y=380)
    tk.Button(text='Cancel', font=('Lato', 12, 'bold'), bg='black', fg='white', command=root.destroy).place(x=270,
                                                                                                            y=380)
    root.mainloop()


def resize():
    try:
        directory = dir_Entry.get()
        path = directory + name_Entry.get()
        img = Image.open(path)
        width = int(width_Entry.get())
        height = int(height_Entry.get())
        resized_img = img.resize((width, height))

        converted = directory + converted_name_Entry.get()
        resized_img.save(converted, drop.get())
        tk.Label(root,
                 text='Resized/Converted successfully.. Find your image file in the \nsame directory as entered above',
                 font=('Calibri', 12, 'bold'),
                 fg='green', bg='white').place(x=60, y=420)

    except FileNotFoundError:
        tk.Label(root, text='Wrong directory or file name entered, try again...', font=('Calibri', 12, 'bold'),
                 fg='red', bg='white').place(x=60, y=420)

    except OSError:
        tk.Label(root, text='Wrong directory or file name entered, try again...', font=('Calibri', 12, 'bold'),
                 fg='red', bg='white').place(x=60, y=420)

    except:
        tk.Label(root, text='Something went wrong, try again...', font=('Calibri', 12, 'bold'), fg='red',
                 bg='white').place(x=60, y=420)


if __name__ == '__main__':
    main()
