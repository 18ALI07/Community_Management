import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import addnew as an
def addnewm():
    an.addnewmember()
def create_subbox(frame, row, column, image_path, label_text,root):
    # sub_frame = ttk.Frame(frame, style='SubBox.TFrame')
    if(label_text=='admin-panel'):
        sub_frame = ttk.Frame(frame,style='SubBox1.TFrame')
        sub_frame.grid(row=row, column=column, padx=50, pady=10)
    elif(label_text=='Customers'):
        sub_frame = ttk.Button(frame, style='SubBox.TFrame', command=lambda:open_member_window(root))
        sub_frame.grid(row=row, column=column)
    elif (label_text == 'Accounts'):
        sub_frame = ttk.Button(frame, style='SubBox.TFrame', command=lambda:open_account_window(root))
        sub_frame.grid(row=row, column=column)
    elif (label_text == 'Certificates'):
        sub_frame = ttk.Button(frame, style='SubBox.TFrame')
        sub_frame.grid(row=row, column=column)



    # Load the image and resize it to fit the sub-box
    img = Image.open(image_path)
    img = img.resize((100, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    # Create a label to display the image
    if (label_text == 'admin-panel'):

        label = ttk.Label(sub_frame, image=photo,background="lightgray")
        label.photo = photo  # Keep a reference to the image to avoid garbage collection
        label.pack(pady=5)

        # Create a label to display the text
        text_label = ttk.Label(sub_frame, text=label_text,font=('Judons',12),background="lightgray")
        text_label.pack(pady=3)
    else:
        label = ttk.Label(sub_frame, image=photo)
        label.photo = photo  # Keep a reference to the image to avoid garbage collection
        label.pack(side="left",padx=10, pady=15)

        # Create a label to display the text
        text_label = ttk.Label(sub_frame, text=label_text,font=('Judons',14))
        text_label.pack(side="left",padx=10, pady=15)
def open_member_window(root):
    custom_style=ttk.Style()
    def go_back():
        other_window.destroy()

    # Create and configure the other window
    other_window = tk.Toplevel(root)
    other_window.title("Customers")
    other_window.geometry("1000x1200")

    # # Create menubar with a light gray background
    # menubar = tk.Menu(other_window, background="lightgray")
    # other_window.config(menu=menubar)
    frame=ttk.Frame(other_window,style="menu.TFrame")
    frame.pack(side="top",fill="x")
    custom_style.configure("menu.TFrame",background="lightgray")
    # Add "Members" label on the left side
    members_label = tk.Label(frame, text="Customers", font=("Arial ", 14,), padx=10,background="lightgray")
    members_label.pack(side="left",padx=30)

    # Add "Back" button on the right side
    back_button = tk.Button(frame, text="Back",width=15 ,font=("Judons bold",16) ,bg="white", fg="black", bd=1, relief="solid", command=go_back)
    back_button.pack(side="right",padx=20)
    frame1 = ttk.Frame(other_window)
    frame1.pack(side="top", fill="x",pady=30)
    add_button = tk.Button(frame1, text="Add New", width=12,height=2, font=("Judons bold", 14), bg="white", fg="black", bd=1,
                            relief="solid",command=addnewm)
    add_button.grid(row=0,column=0, padx=20)
    subframe1=ttk.Frame(frame1,style="Tsframe.TFrame")
    subframe1.grid(row=0,column=1,padx=20)
    custom_style.configure("Tsframe.TFrame",background="white",width=25, borderwidth=10, relief="solid")
    label1=ttk.Label(subframe1,text="Total Customers",font=("Judons",14),background="white")
    label1.pack(side="top",padx=10,pady=10)
    label2 = ttk.Label(subframe1, text="30", font=("Judons", 14), background="white")
    label2.pack(side="top",padx=10,pady=5)
    subframe2 = ttk.Frame(frame1, style="Tsframe2.TFrame")
    subframe2.grid(row=0, column=2, padx=20)
    custom_style.configure("Tsframe2.TFrame", background="#0FFF52",width=25, borderwidth=10, relief="solid")
    label1 = ttk.Label(subframe2, text="Active", font=("Judons", 14), background="#0FFF52")
    label1.pack(side="top", padx=30, pady=10)
    label2 = ttk.Label(subframe2, text="20", font=("Judons", 14),background="#0FFF52")
    label2.pack(side="top", padx=30, pady=5)
    subframe3 = ttk.Frame(frame1, style="Tsframe3.TFrame")
    subframe3.grid(row=0, column=3, padx=20)
    custom_style.configure("Tsframe3.TFrame", background="#FFF507",width=25, borderwidth=10, relief="solid")
    label1 = ttk.Label(subframe3, text="InActive", font=("Judons", 14), background="#FFF507")
    label1.pack(side="top", padx=25, pady=10)
    label2 = ttk.Label(subframe3, text="5", font=("Judons", 14), background="#FFF507")
    label2.pack(side="top", padx=25, pady=5)
    subframe4 = ttk.Frame(frame1, style="Tsframe4.TFrame")
    subframe4.grid(row=0, column=4, padx=20)
    custom_style.configure("Tsframe4.TFrame", background="red",width=25, borderwidth=10, relief="solid")
    label1 = ttk.Label(subframe4, text="Expired", font=("Judons", 14), background="red")
    label1.pack(side="top", padx=27, pady=10)
    label2 = ttk.Label(subframe4, text="30", font=("Judons", 14), background="red")
    label2.pack(side="top", padx=27, pady=5)
    frame1.columnconfigure((1,2,3,4),weight=1)
    # Create a frame to hold widgets
    frame2 = ttk.Frame(other_window)
    frame2.pack(side="top", fill="x", pady=20)

    subfrm1 = ttk.Frame(frame2)
    subfrm1.grid(row=0,column=0)
    imgfrm1 = ttk.Frame(subfrm1)
    imgfrm1.pack(side="top")
    # Create an image button
    img = Image.open("assets/search.png")
    img = img.resize((33, 33), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    img1 = ttk.Label(imgfrm1, image=photo, anchor="w")  # Set anchor to "w" (west) for left alignment
    img1.image = photo
    img1.pack(side="left", padx=5, pady=5)

    # Create a label
    lbl1 = ttk.Label(imgfrm1, text="Search", font=("Arial", 14))
    lbl1.pack(side="left", padx=5, pady=5)
    # Create a separate frame with a rounded border for the entry
    entry_frame = ttk.Frame(subfrm1, style="Entry.TFrame")
    entry_frame.pack(side="top", pady=1)

    # Create an entry
    ent1 = ttk.Entry(entry_frame, font=("Judons 12"),width=30, style="Entry.TEntry")  # Use "Entry.TEntry" for the custom style
    ent1.pack(padx=1, pady=1)

    custom_style.layout("Entry.TFrame",
                        [("Entry.TFrame", {"sticky": "nswe"})])  # Set sticky property for rounded border
    custom_style.configure("Entry.TFrame", background="black", borderwidth=10, relief="solid", bordercolor="black")
    custom_style.configure("Entry.TEntry", foreground="black", background="white")
    #subframe2
    subfrm2 = ttk.Frame(frame2)
    subfrm2.grid(row=0,column=1)
    # Create a label
    lbl1 = ttk.Label(subfrm2, text="Filter by status", font=("Arial", 14))
    lbl1.pack(side="top", padx=5, pady=9)
    # Create a separate frame with a rounded border for the entry
    entry_frame = ttk.Frame(subfrm2, style="Entry.TFrame")
    entry_frame.pack(side="top", pady=1)

    # Create an entry
    ent1 = ttk.Entry(entry_frame, font=("Judons 12"), width=30,
                     style="Entry.TEntry")  # Use "Entry.TEntry" for the custom style
    ent1.pack(padx=1, pady=1)

    custom_style.layout("Entry.TFrame",
                        [("Entry.TFrame", {"sticky": "nswe"})])  # Set sticky property for rounded border
    custom_style.configure("Entry.TFrame", background="black", borderwidth=10, relief="solid", bordercolor="black")
    custom_style.configure("Entry.TEntry", foreground="black", background="white")

#subframe3
    subfrm3 = ttk.Frame(frame2)
    subfrm3.grid(row=0,column=2)
    # Create a label
    lbl1 = ttk.Label(subfrm3, text="Sort Table", font=("Arial", 14))
    lbl1.pack(side="top", padx=5, pady=9)
    # Create a separate frame with a rounded border for the entry
    entry_frame = ttk.Frame(subfrm3, style="Entry.TFrame")
    entry_frame.pack(side="top", pady=1)

    # Create an entry
    ent1 = ttk.Entry(entry_frame, font=("Judons 12"), width=30,
                     style="Entry.TEntry")  # Use "Entry.TEntry" for the custom style
    ent1.pack(padx=1, pady=1)

    custom_style.layout("Entry.TFrame",
                        [("Entry.TFrame", {"sticky": "nswe"})])  # Set sticky property for rounded border
    custom_style.configure("Entry.TFrame", background="black", borderwidth=10, relief="solid", bordercolor="black")
    custom_style.configure("Entry.TEntry", foreground="black", background="white")
    frame2.columnconfigure((0,1,2),weight=1)
    custom_style.configure("frame4.TFrame", borderwidth=20, relief="solid", foreground="black")
    custom_style.configure("frame4m.TFrame", borderwidth=20, relief="solid", foreground="black", background="lightgray")
    # Create frame4 for the header row
    frame4 = ttk.Frame(other_window, style="frame4m.TFrame")
    frame4.pack(side="top", fill="x")

    # Create headings using ttk.Label widgets within the frame4
    headings = ["Profile", "Status", "Name", "Email", "ID", "Joined Date", "Action"]
    column_widths = [10, 8, 20, 10, 8, 12, 6]
    for col, (heading_text, width) in enumerate(zip(headings, column_widths)):
        lab1 = ttk.Label(frame4, text=heading_text, font=("Inter", 13), anchor="center", background="lightgray",
                         width=width)
        lab1.grid(row=0, column=col, pady=5, sticky="nsew")

    # Sample data rows
    data_rows = [
        ["Profile 1", "Active", "John DoeJohn Doe", "johndoe123@gmail.com", "12345", "2023-07-31"],
        ["Profile 2", "Inactive", "Jane SmithJane Smith", "janesmith123456@gmail.com", "67890", "2023-08-15"],
        # Add more data rows as needed
    ]

    # Create individual frames for each data row and fill them with ttk.Label widgets
    for row, data in enumerate(data_rows, start=1):
        data_frame = ttk.Frame(other_window, style="frame4.TFrame", relief="groove", borderwidth=2)
        data_frame.pack(side="top", fill="x")
        for col, (value, width) in enumerate(zip(data, column_widths)):
            lab1 = ttk.Label(data_frame, text=value, font=("Inter", 12), anchor="center", width=width)
            lab1.grid(row=0, column=col, pady=5, sticky="nsew")

        # Leave some space for the "Edit" button
        btn = tk.Button(data_frame, text="Edit", font="Judons 12", width=4, height=1, bg="#4ADDFD", bd=0,
                        relief=tk.FLAT)
        btn.grid(row=0, column=len(data), pady=5, sticky="nsew", padx=(0, 10))

        # Make all columns in each data frame resizable
        data_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    # Make all columns in the header frame resizable
    frame4.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    # Make data rows resizable as the window is resized
    for row in range(1, len(data_rows) + 1):
        other_window.grid_rowconfigure(row, weight=1)


def open_account_window(root):
    custom_style=ttk.Style()
    def go_back():
        other_window.destroy()

    # Create and configure the other window
    other_window = tk.Toplevel(root)
    other_window.title("Accounts")
    other_window.geometry("1000x1200")

    # # Create menubar with a light gray background
    # menubar = tk.Menu(other_window, background="lightgray")
    # other_window.config(menu=menubar)
    frame=ttk.Frame(other_window,style="menu.TFrame")
    frame.pack(side="top",fill="x")
    custom_style.configure("menu.TFrame",background="lightgray")
    # Add "Members" label on the left side
    members_label = tk.Label(frame, text="Accounts", font=("Arial ", 14,), padx=10,background="lightgray")
    members_label.pack(side="left",padx=30)

    # Add "Back" button on the right side
    back_button = tk.Button(frame, text="Back",width=15 ,font=("Judons bold",16) ,bg="white", fg="black", bd=1, relief="solid", command=go_back)
    back_button.pack(side="right",padx=20)
    frame1 = ttk.Frame(other_window)
    frame1.pack(side="top", fill="x",pady=30)
    add_button = tk.Button(frame1, text="Add Fund", width=12,height=2, font=("Judons bold", 14), bg="white", fg="black", bd=4,
                            relief="solid")
    add_button.grid(row=0,column=4, padx=20)
    subframe1=ttk.Frame(frame1,style="Tsframe.TFrame")
    subframe1.grid(row=0,column=1,padx=20)
    custom_style.configure("Tsframe.TFrame",background="white",width=25, borderwidth=10, relief="solid")
    label1=ttk.Label(subframe1,text="Total Funds",font=("Judons",14),background="white")
    label1.pack(side="top",padx=10,pady=10)
    label2 = ttk.Label(subframe1, text="300000", font=("Judons", 14), background="white")
    label2.pack(side="top",padx=10,pady=5)
    subframe2 = ttk.Frame(frame1, style="Tsframe2.TFrame")
    subframe2.grid(row=0, column=2, padx=20)
    custom_style.configure("Tsframe2.TFrame", background="#0FFF52",width=25, borderwidth=10, relief="solid")
    label1 = ttk.Label(subframe2, text="Income", font=("Judons", 14), background="#0FFF52"
)
    label1.pack(side="top", padx=30, pady=10)
    label2 = ttk.Label(subframe2, text="20000", font=("Judons", 14),background="#0FFF52"
)
    label2.pack(side="top", padx=30, pady=5)
    subframe3 = ttk.Frame(frame1, style="Tsframe3.TFrame")
    subframe3.grid(row=0, column=3, padx=20)
    custom_style.configure("Tsframe3.TFrame", background="#FFF507",width=25, borderwidth=10, relief="solid")
    label1 = ttk.Label(subframe3, text="Expenditure", font=("Judons", 14), background="#FFF507")
    label1.pack(side="top", padx=25, pady=10)
    label2 = ttk.Label(subframe3, text="50000", font=("Judons", 14), background="#FFF507")
    label2.pack(side="top", padx=25, pady=5)
    # subframe4 = ttk.Frame(frame1, style="Tsframe4.TFrame")
    # subframe4.grid(row=0, column=4, padx=20)
    # custom_style.configure("Tsframe4.TFrame", background="red",width=25, borderwidth=10, relief="solid")
    # label1 = ttk.Label(subframe4, text="Expired", font=("Judons", 14), background="red")
    # label1.pack(side="top", padx=27, pady=10)
    # label2 = ttk.Label(subframe4, text="30", font=("Judons", 14), background="red")
    # label2.pack(side="top", padx=27, pady=5)
    frame1.columnconfigure((1,2,3,4),weight=1)
    # Create a frame to hold widgets
    frame2 = ttk.Frame(other_window)
    frame2.pack(side="top", fill="x", pady=20)

    subfrm1 = ttk.Frame(frame2)
    subfrm1.grid(row=0,column=0)
    imgfrm1 = ttk.Frame(subfrm1)
    imgfrm1.pack(side="top")
    # Create an image button
    img = Image.open("assets/search.png")
    img = img.resize((33, 33), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    img1 = ttk.Label(imgfrm1, image=photo, anchor="w")  # Set anchor to "w" (west) for left alignment
    img1.image = photo
    img1.pack(side="left", padx=5, pady=5)

    # Create a label
    lbl1 = ttk.Label(imgfrm1, text="Search", font=("Arial", 14))
    lbl1.pack(side="left", padx=5, pady=5)
    # Create a separate frame with a rounded border for the entry
    entry_frame = ttk.Frame(subfrm1, style="Entry.TFrame")
    entry_frame.pack(side="top", pady=1)

    # Create an entry
    ent1 = ttk.Entry(entry_frame, font=("Judons 12"),width=30, style="Entry.TEntry")  # Use "Entry.TEntry" for the custom style
    ent1.pack(padx=1, pady=1)

    custom_style.layout("Entry.TFrame",
                        [("Entry.TFrame", {"sticky": "nswe"})])  # Set sticky property for rounded border
    custom_style.configure("Entry.TFrame", background="black", borderwidth=10, relief="solid", bordercolor="black")
    custom_style.configure("Entry.TEntry", foreground="black", background="white")
    #subframe2
    subfrm2 = ttk.Frame(frame2)
    subfrm2.grid(row=0,column=1)
    # Create a label
    lbl1 = ttk.Label(subfrm2, text="Filter by status", font=("Arial", 14))
    lbl1.pack(side="top", padx=5, pady=9)
    # Create a separate frame with a rounded border for the entry
    entry_frame = ttk.Frame(subfrm2, style="Entry.TFrame")
    entry_frame.pack(side="top", pady=1)

    # Create an entry
    ent1 = ttk.Entry(entry_frame, font=("Judons 12"), width=30,
                     style="Entry.TEntry")  # Use "Entry.TEntry" for the custom style
    ent1.pack(padx=1, pady=1)

    custom_style.layout("Entry.TFrame",
                        [("Entry.TFrame", {"sticky": "nswe"})])  # Set sticky property for rounded border
    custom_style.configure("Entry.TFrame", background="black", borderwidth=10, relief="solid", bordercolor="black")
    custom_style.configure("Entry.TEntry", foreground="black", background="white")

#subframe3
    subfrm3 = ttk.Frame(frame2)
    subfrm3.grid(row=0,column=2)
    # Create a label
    lbl1 = ttk.Label(subfrm3, text="Sort Table", font=("Arial", 14))
    lbl1.pack(side="top", padx=5, pady=9)
    # Create a separate frame with a rounded border for the entry
    entry_frame = ttk.Frame(subfrm3, style="Entry.TFrame")
    entry_frame.pack(side="top", pady=1)

    # Create an entry
    ent1 = ttk.Entry(entry_frame, font=("Judons 12"), width=30,
                     style="Entry.TEntry")  # Use "Entry.TEntry" for the custom style
    ent1.pack(padx=1, pady=1)

    custom_style.layout("Entry.TFrame",
                        [("Entry.TFrame", {"sticky": "nswe"})])  # Set sticky property for rounded border
    custom_style.configure("Entry.TFrame", background="black", borderwidth=10, relief="solid", bordercolor="black")
    custom_style.configure("Entry.TEntry", foreground="black", background="white")
    frame2.columnconfigure((0,1,2),weight=1)

    # Create a custom style for the frames
    custom_style = ttk.Style()
    custom_style.configure("frame4.TFrame", borderwidth=20, relief="solid", foreground="black")
    custom_style.configure("frame4m.TFrame", borderwidth=20, relief="solid", foreground="black", background="lightgray")
    # Create frame4 for the header row
    frame4 = ttk.Frame(other_window, style="frame4m.TFrame")
    frame4.pack(side="top", fill="x")

    # Create headings using ttk.Label widgets within the frame4
    headings = ["Profile", "Status", "Name", "Amount", "ID", "Due Date", "Action"]
    column_widths = [10, 8, 20, 10, 8, 12, 6]
    for col, (heading_text, width) in enumerate(zip(headings, column_widths)):
        lab1 = ttk.Label(frame4, text=heading_text, font=("Inter", 13), anchor="center", background="lightgray",
                         width=width)
        lab1.grid(row=0, column=col, pady=5, sticky="nsew")

    # Sample data rows
    data_rows = [
        ["Profile 1", "Active", "John DoeJohn Doe", "₹10000", "12345", "2023-07-31"],
        ["Profile 2", "Inactive", "Jane SmithJane Smith", "₹5000", "67890", "2023-08-15"],
        # Add more data rows as needed
    ]

    # Create individual frames for each data row and fill them with ttk.Label widgets
    for row, data in enumerate(data_rows, start=1):
        data_frame = ttk.Frame(other_window, style="frame4.TFrame", relief="groove", borderwidth=2)
        data_frame.pack(side="top", fill="x")
        for col, (value, width) in enumerate(zip(data, column_widths)):
            lab1 = ttk.Label(data_frame, text=value, font=("Inter", 12), anchor="center", width=width)
            lab1.grid(row=0, column=col, pady=5, sticky="nsew")

        # Leave some space for the "Edit" button
        btn = tk.Button(data_frame, text="Edit", font="Judons 12", width=4, height=1, bg="#4ADDFD", bd=0,
                        relief=tk.FLAT)
        btn.grid(row=0, column=len(data), pady=5, sticky="nsew", padx=(0, 10))

        # Make all columns in each data frame resizable
        data_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    # Make all columns in the header frame resizable
    frame4.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    # Make data rows resizable as the window is resized
    for row in range(1, len(data_rows) + 1):
        other_window.grid_rowconfigure(row, weight=1)


def create_button(parent, text,row):
    if(text=="Add New"):
        button = tk.Button(parent, text=text, width=15, font=("Judons", 14), bg="white", fg="black", bd=1,
                           relief="solid", padx=10, pady=5,command=addnewm)
        button.grid(row=row, column=0, padx=10, pady=20)
    else:
        button = tk.Button(parent, text=text, width=15, font=("Judons", 14), bg="white", fg="black", bd=1,
                           relief="solid", padx=10, pady=5)
        button.grid(row=row, column=0, padx=10, pady=20)

    return button
# Create the main window
def dashboard():
    root = tk.Tk()
    root.title("Dashboard")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    # Set the background color to gray
    root.configure(bg="lightgray")

    # Create a frame for the sub-boxes
    frame = ttk.Frame(root, style="Main.TFrame")  # Use "Main.TFrame" for the main frame
    frame.pack(side="top", fill='x', expand=True, padx=20)

    # Define a custom style for the main frame with a white background
    custom_style = ttk.Style()
    custom_style.configure("Main.TFrame", background="lightgray", borderwidth=20, relief="solid", foreground="black")

    # Define a custom style for the sub-boxes with a white background
    custom_style.configure("SubBox.TFrame", background="white", borderwidth=2, relief="solid")
    custom_style.configure("SubBox1.TFrame", background="lightgray")
    # Create the sub-boxes
    create_subbox(frame, 0, 0, "assets/logo.png", "admin-panel",root)
    create_subbox(frame, 0, 1, "assets/member.png", "Customers",root)
    create_subbox(frame, 0, 2, "assets/account.png", "Accounts",root)
    create_subbox(frame, 0, 3, "assets/certificate.png", "Certificates",root)

    # Configure the columns to have equal weight, so they are equally spaced
    frame.columnconfigure((1, 2, 3), weight=1)
    frame1 = ttk.Frame(root, style="Fram1.TFrame")  # Use "Main.TFrame" for the main frame
    frame1.pack(side="left", fill="y", padx=20, pady=20)
    custom_style.configure("Fram1.TFrame", background="lightgray")
    buttons_text = ["Add New", "Add Funds", "Settings", "Database", "Logout"]
    i = 1
    buttons = []
    for text in buttons_text:
        buttons.append(create_button(frame1, text, i))
        i += 1
    frame2 = ttk.Frame(root, style="Main2.TFrame")  # Use "Main.TFrame" for the main frame
    frame2.pack(side="right", fill="both", expand=True, padx=20, pady=20)
    custom_style.configure("Main2.TFrame", background="lightgray", borderwidth=4, relief="solid")
    root.mainloop()
