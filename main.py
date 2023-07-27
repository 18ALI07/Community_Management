import conn
import otp_send as ot
import tkinter as tk
from tkinter import ttk
import dashboard as dd




def get_otp():
    # Replace this function with the logic to generate and handle OTP
    # For now, we'll just print the OTP to the console as a placeholder
    # generated_otp = "123456"
    # print("Generated OTP:", generated_otp)
    connection=conn.connect_db()
    cursor=connection.cursor()
    cursor.execute("select email,password from tbl_user")
    rows=cursor.fetchall()
    connection.close()

    if(email_entry.get()=='' and password_entry.get()==''):
        msg.set("Please Enter Both The details")
        return
    if (email_entry.get() == ''):
        msg.set("Please Enter The Email Adress")
        return
    if (password_entry.get() == ''):
        msg.set("Please Enter The Password")
        return
    # Get user input from email and password entries
    user_email = email_entry.get()
    user_password = password_entry.get()

    # Check if the user input matches the data from rows
    if str(rows[0][0]) == str(user_email) and str(rows[0][1]) == str(user_password):
        generated_otp=ot.generate_otp()
        ot.send_otp_email(user_email,generated_otp)
        open_otp_window(generated_otp)
    else:
        msg.set("Please Enter The Correct details")





def open_otp_window(otp):
    otp_window = tk.Toplevel(root)
    otp_window.title("OTP Verification")
    otp_window.geometry("300x150")

    # Calculate the center position of the screen for the OTP window
    screen_width = otp_window.winfo_screenwidth()
    screen_height = otp_window.winfo_screenheight()
    otp_width = 300
    otp_height = 150
    otp_x = (screen_width - otp_width) // 2
    otp_y = (screen_height - otp_height) // 2

    otp_window.geometry(f"{otp_width}x{otp_height}+{otp_x}+{otp_y}")

    # Set the background color to gray
    otp_window.configure(bg="lightgray")

    # OTP Label and Entry

    mesg = tk.StringVar()
    # mesg.set('')

    otp_label = ttk.Label(otp_window, text="Enter the OTP:", font=("Helvetica", 16), background="lightgray")
    otp_label.pack(pady=(10, 0))
    otp_label = ttk.Label(otp_window, textvariable=mesg, font=("Helvetica", 12), background="lightgray",
                          foreground="red")
    otp_label.pack(pady=(0, 10))
    otp_entry = tk.Entry(otp_window, font=("Helvetica", 14))
    otp_entry.pack(pady=(0, 5))


    cont = tk.IntVar()
    cont.set(3)
    # Login button
    def login():

        if (cont.get() == 1):
            otp_window.destroy()
        else:
            entered_otp = otp_entry.get()
            if entered_otp == otp:
                print("Login Successful!")
                otp_window.destroy()
                root.destroy()
                dd.dashboard()

            else:
                cont.set(cont.get() - 1)

                mesg.set(f'Attempt left: {cont.get()}')

                print("Invalid OTP. Try again.")
                # You can add code here to show an error message to the user

    login_button = tk.Button(otp_window, text="Login", width=8, font=("Judons bold", 12), bg="white", fg="black", bd=1,
                             relief="solid", command=lambda: login())
    login_button.pack(pady=10)


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Login Page")

    # Calculate the center position of the screen for the logo
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    logo_width = 150  # Set the desired logo width
    logo_x = (screen_width - logo_width) // 2

    root.geometry(f"{screen_width}x{screen_height}")

    # Set the background color to gray
    root.configure(bg="lightgray")

    # Logo
    # Replace 'assets/logo.png' with the path to your logo image file
    logo_image = tk.PhotoImage(file="assets/logo.png").subsample(2)  # Reduce the size of the logo
    logo_label = tk.Label(root, image=logo_image, background="lightgray")
    logo_label.place(x=logo_x + 30, y=50)  # Adjust the y value as needed
    c_label = ttk.Label(root, text="MidLead Technovation Software", font=("Judson", 20), background="lightgray")
    c_label.place(x=logo_x - 80, y=230)  # Adjust the y value as needed
    # StringVar to store the message
    msg = tk.StringVar()
    msg.set('')
    msg_label = ttk.Label(root, textvariable=msg, font=("Judson", 12), background="lightgray", foreground="red")
    msg_label.place(x=logo_x - 50, y=260)
    # Email
    email_label = ttk.Label(root, text="E-Mail:", font=("Judson", 16), background="lightgray")
    email_label.place(x=logo_x - 50, y=290)  # Adjust the y value as needed
    email_entry = ttk.Entry(root, font=("Helvetica", 16), width=25)
    email_entry.place(x=logo_x - 50, y=330)  # Adjust the y value as needed

    # Password
    password_label = ttk.Label(root, text="Password:", font=("Judson", 16), background="lightgray")
    password_label.place(x=logo_x - 50, y=380)  # Adjust the y value as needed
    password_entry = ttk.Entry(root, show="*", font=("Helvetica", 16), width=25)
    password_entry.place(x=logo_x - 50, y=420)  # Adjust the y value as needed

    # Get OTP button
    otp_button = tk.Button(root, text="Get OTP", width=10, font=("Judons bold", 14), bg="white", fg="black", bd=1,
                           relief="solid", command=get_otp)
    otp_button.place(x=logo_x + 130, y=500)  # Adjust the y value as needed
    # Define a custom style for the button with a black border
    custom_style = ttk.Style()
    custom_style.configure("Custom.TButton", borderwidth=10, relief="solid", background="black", foreground="black")
    root.mainloop()


