# import tkinter as tk
# from tkinter import messagebox
# import qrcode

# stations = {
#     "Majestic": 0,
#     "Rajajinagar": 5,
#     "Yeshwanthpur": 10,
#     "Jalahalli": 15,
#     "Peenya": 20,
#     "Nagasandra": 25,
#     "Yelahanka": 30
# }
# fare_per_km = 2

# def calculate_fare(source, destination):
#     distance = abs(stations[destination] - stations[source])
#     fare = distance * fare_per_km
#     return distance, fare

# def generate_ticket():
#     name = name_entry.get().strip().title()
#     source = source_entry.get().strip().title()
#     destination = dest_entry.get().strip().title()

#     if source not in stations or destination not in stations:
#         messagebox.showerror("Error", "Invalid station name.")
#         return
#     if source == destination:
#         messagebox.showwarning("Warning", "Source and destination cannot be the same.")
#         return

#     distance, fare = calculate_fare(source, destination)
#     ticket = (
#         f"🎫 Metro Ticket\n"
#         f"Name: {name}\nFrom: {source}\nTo: {destination}\n"
#         f"Distance: {distance} km\nFare: ₹{fare}"
#     )
#     result_label.config(text=ticket)

#     qr_data = f"{name},{source},{destination},{distance} km,₹{fare}"
#     qr = qrcode.make(qr_data)
#     qr.save("metro_ticket_qr.png")
#     messagebox.showinfo("QR Code", "QR Code saved as metro_ticket_qr.png")

# # GUI setup
# root = tk.Tk()
# root.title("Metro Ticket Booking")

# tk.Label(root, text="Name").pack()
# name_entry = tk.Entry(root)
# name_entry.pack()

# tk.Label(root, text="Source Station").pack()
# source_entry = tk.Entry(root)
# source_entry.pack()

# tk.Label(root, text="Destination Station").pack()
# dest_entry = tk.Entry(root)
# dest_entry.pack()

# tk.Button(root, text="Generate Ticket", command=generate_ticket).pack()
# result_label = tk.Label(root, text="", justify="left")
# result_label.pack()

# root.mainloop()
# import tkinter as tk
# import qrcode

# print("✅ tkinter and qrcode are working!")
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import qrcode
import os

stations = {
    "Majestic": 0,
    "Rajajinagar": 5,
    "Yeshwanthpur": 10,
    "Jalahalli": 15,
    "Peenya": 20,
    "Nagasandra": 25,
    "Yelahanka": 30
}
fare_per_km = 2

def calculate_fare(source, destination):
    distance = abs(stations[destination] - stations[source])
    fare = distance * fare_per_km
    return distance, fare

def generate_ticket():
    name = name_entry.get().strip().title()
    source = source_var.get()
    destination = dest_var.get()

    if source == destination:
        messagebox.showwarning("Warning", "Source and destination cannot be the same.")
        return

    distance, fare = calculate_fare(source, destination)
    ticket_text = (
        f"🎫 Metro Ticket\n"
        f"Name: {name}\nFrom: {source}\nTo: {destination}\n"
        f"Distance: {distance} km\nFare: ₹{fare}"
    )
    result_label.config(text=ticket_text)

    qr_data = f"{name},{source},{destination},{distance} km,₹{fare}"
    qr = qrcode.make(qr_data)
    qr_path = "metro_ticket_qr.png"
    qr.save(qr_path)

    # Show QR code in app
    qr_img = Image.open(qr_path)
    qr_img = qr_img.resize((150, 150))
    qr_photo = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    # Save ticket to file
    with open("ticket_history.txt", "a") as file:
        file.write(ticket_text + "\n\n")

    messagebox.showinfo("Success", "Ticket generated and QR code saved!")

def clear_fields():
    name_entry.delete(0, tk.END)
    source_var.set(station_list[0])
    dest_var.set(station_list[1])
    result_label.config(text="")
    qr_label.config(image="")

# GUI setup
root = tk.Tk()
root.title("Metro Ticket Booking App")
root.geometry("400x600")

station_list = list(stations.keys())

tk.Label(root, text="Passenger Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Source Station").pack()
source_var = tk.StringVar(value=station_list[0])
source_menu = tk.OptionMenu(root, source_var, *station_list)
source_menu.pack()

tk.Label(root, text="Destination Station").pack()
dest_var = tk.StringVar(value=station_list[1])
dest_menu = tk.OptionMenu(root, dest_var, *station_list)
dest_menu.pack()

tk.Button(root, text="Generate Ticket", command=generate_ticket).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields).pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()