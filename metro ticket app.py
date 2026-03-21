# # # # Simple Metro Train Ticket App
# # # from tkinter import *
# # # from PIL import Image, ImageTk

# # # root = Tk()
# # # root.title("Metro Ticket App")

# # # # Load Image
# # # img = Image.open("met.jpg")   # keep image in same folder
# # # img = img.resize((500, 200))    # adjust size
# # # photo = ImageTk.PhotoImage(img)

# # # # Add to Label
# # # image_label = Label(root, image=photo)
# # # image_label.pack()

# # # root.mainloop()

# # # stations = {
# # #     "Majestic": 0,
# # #     "Rajajinagar": 5,
# # #     "Yeshwanthpur": 10,
# # #     "Jalahalli": 15,
# # #     "Peenya": 20,
# # #     "Nagasandra": 25,
# # #     "Yelahanka": 30
# # # }

# # # fare_per_km = 2  # ₹2 per km

# # # def display_stations():
# # #     print("\nAvailable Metro Stations:")
# # #     for station in stations:
# # #         print(f"- {station}")

# # # def calculate_fare(source, destination):
# # #     distance = abs(stations[destination] - stations[source])
# # #     return distance * fare_per_km

# # # def calculate_fare(source, destination):
# # #     distance = abs(stations[destination] - stations[source])
# # #     fare = distance * fare_per_km
# # #     return  fare


# # # def generate_ticket(name, source, destination, fare):
# # #     print("\n🎫 Metro Train Ticket")
# # #     print("----------------------------")
# # #     print(f"Passenger Name : {name}")
# # #     print(f"From           : {source}")
# # #     print(f"To             : {destination}")
# # #     print(f"Fare           : ₹{fare}")
# # #     print(f"distance       :{abs(stations[destination]- stations[source])} km")
# # #     print("----------------------------")
# # #     print("Thank you for using Metro Services!")

# # #     #Generate qr code  
    

# # # def main():
# # #     print("🚇 Welcome to Metro Ticket Booking App 🚇")
# # #     name = input("Enter your name: ")

# # #     display_stations()
# # #     source = input("\nEnter source station: ")
# # #     destination = input("Enter destination station: ")

# # #     if source not in stations or destination not in stations:
# # #         print("❌ Invalid station name. Please try again.")
# # #         return
# # #     if source == destination:
# # #         print("⚠️ Source and destination cannot be the same.")
# # #         return
    
    
# # #     fare = calculate_fare(source, destination)
# # #     generate_ticket(name, source, destination, fare)

# # #     # distance = abs(stations[destination] - stations[source])
# # #     # fare = calculate_fare(source, destination)
# # #     # generate_ticket(name, source, destination, distance, fare)



# # # if __name__ == "__main__":
# # #     main()
# # from tkinter import *
# # from tkinter import ttk
# # from PIL import Image, ImageTk
# # import qrcode

# # root = Tk()
# # root.title("Namma Metro Ticket System")
# # root.geometry("520x700")
# # root.config(bg="#f5f5f5")

# # # ===== Image =====
# # img = Image.open("met.jpg")
# # img = img.resize((520, 180))
# # photo = ImageTk.PhotoImage(img)
# # Label(root, image=photo).pack()

# # # ===== Metro Lines =====
# # purple_line = [
# #     "Challaghatta", "Kengeri", "Vijayanagar", "Magadi Road",
# #     "Majestic", "Cubbon Park", "Indiranagar", "Baiyappanahalli", "Whitefield"
# # ]

# # green_line = [
# #     "Nagasandra", "Peenya", "Jalahalli", "Yeshwanthpur",
# #     "Majestic", "KR Market", "Jayanagar", "Banashankari", "Silk Institute"
# # ]

# # # Distance per station (approx)
# # DISTANCE_PER_STOP = 2  # km

# # # ===== Fare Logic =====
# # def calculate_fare(distance):
# #     if distance <= 2:
# #         return 10
# #     elif distance <= 5:
# #         return 20
# #     elif distance <= 10:
# #         return 30
# #     elif distance <= 15:
# #         return 40
# #     elif distance <= 20:
# #         return 50
# #     else:
# #         return 60

# # # ===== Time =====
# # def calculate_time(distance):
# #     return int((distance / 40) * 60)

# # # ===== Find Route =====
# # def find_route(source, dest):
# #     if source in purple_line and dest in purple_line:
# #         line = "Purple Line"
# #         stops = abs(purple_line.index(dest) - purple_line.index(source))
# #         color = "#800080"
# #     elif source in green_line and dest in green_line:
# #         line = "Green Line"
# #         stops = abs(green_line.index(dest) - green_line.index(source))
# #         color = "#008000"
# #     else:
# #         # Interchange at Majestic
# #         if source in purple_line:
# #             stops1 = abs(purple_line.index("Majestic") - purple_line.index(source))
# #         else:
# #             stops1 = abs(green_line.index("Majestic") - green_line.index(source))

# #         if dest in purple_line:
# #             stops2 = abs(purple_line.index(dest) - purple_line.index("Majestic"))
# #         else:
# #             stops2 = abs(green_line.index(dest) - green_line.index("Majestic"))

# #         stops = stops1 + stops2
# #         line = "Interchange (Purple ↔ Green)"
# #         color = "#444444"

# #     distance = stops * DISTANCE_PER_STOP
# #     return line, distance, color

# # #  qr code
# # def generate_ticket():
# #     name = name_entry.get()
# #     source = source_combo.get()
# #     dest = dest_combo.get()

# #     if not name or not source or not dest:
# #         result_label.config(text="❌ Fill all fields", fg="red")
# #         return

# #     if source == dest:
# #         result_label.config(text="⚠️ Same station selected", fg="orange")
# #         return

# #     line, distance, color = find_route(source, dest)
# #     fare = calculate_fare(distance)
# #     time = calculate_time(distance)

# #     # 🎫 Ticket Data
# #     ticket_data = f"""
# # Namma Metro Ticket
# # Name: {name}
# # From: {source}
# # To: {dest}
# # Route: {line}
# # Distance: {distance} km
# # Fare: ₹{fare}
# # Time: {time} min
# # """

# #     # ===== Generate QR =====
# #     import qrcode
# #     qr = qrcode.make(ticket_data)
# #     qr.save("ticket_qr.png")

# #     # ===== Show QR in UI =====
# #     from PIL import Image, ImageTk
# #     qr_img = Image.open("ticket_qr.png")
# #     qr_img = qr_img.resize((160, 160))
# #     qr_photo = ImageTk.PhotoImage(qr_img)

# #     qr_label.config(image=metro_ticket_qr.png)
# #     qr_label.image = metro_ticket_qr.png   # 🔥 IMPORTANT

# #     # ===== Show Ticket =====
# #     result = f"""
# # 🎫 METRO TICKET
# # -------------------------
# # Name: {name}
# # From: {source}
# # To: {dest}
# # -------------------------
# # Route: {line}
# # Distance: {distance} km
# # Fare: ₹{fare}
# # Time: {time} min
# # """
# #     result_label.config(text=result, fg=color)

# #     # ===== Show Ticket =====
# #     result = f"""
# # 🎫 METRO TICKET
# # -------------------------
# # Name: {name}
# # From: {source}
# # To: {dest}
# # -------------------------
# # Route: {line}
# # Distance: {distance} km
# # Fare: ₹{fare}
# # Time: {time} min
# # """
# #     result_label.config(text=result, fg=color)

# # # ===== UI Card =====
# # card = Frame(root, bg="white", bd=3, relief="ridge")
# # card.place(x=40, y=200, width=440, height=450)

# # Label(card, text="🚇 NAMMA METRO TICKET", bg="#222", fg="white",
# #       font=("Arial", 15, "bold"), pady=10).pack(fill=X)

# # # Inputs
# # Label(card, text="Name", bg="white").pack(pady=5)
# # name_entry = Entry(card)
# # name_entry.pack()

# # all_stations = list(set(purple_line + green_line))

# # Label(card, text="From", bg="white").pack(pady=5)
# # source_combo = ttk.Combobox(card, values=all_stations, state="readonly")
# # source_combo.pack()

# # Label(card, text="To", bg="white").pack(pady=5)
# # dest_combo = ttk.Combobox(card, values=all_stations, state="readonly")
# # dest_combo.pack()

# # result_label = Label(card, text="", bg="white", justify=LEFT, font=("Arial", 11))
# # result_label.pack(pady=15)

# # # ===== Generate Ticket =====
# # def generate_ticket():
# #     name = name_entry.get()
# #     source = source_combo.get()
# #     dest = dest_combo.get()

# #     if not name or not source or not dest:
# #         result_label.config(text="❌ Fill all fields", fg="red")
# #         return

# #     if source == dest:
# #         result_label.config(text="⚠️ Same station selected", fg="orange")
# #         return

# #     line, distance, color = find_route(source, dest)
# #     fare = calculate_fare(distance)
# #     time = calculate_time(distance)

# #     result = f"""
# # Name: {name}
# # From: {source}
# # To: {dest}

# # Route: {line}
# # Distance: {distance} km
# # Fare: ₹{fare}
# # Time: {time} min
# # """
# #     result_label.config(text=result, fg=color)

# # # Button
# # Button(card, text="Generate Ticket", bg="#0078D7", fg="white",
# #        font=("Arial", 12, "bold"), command=generate_ticket).pack(pady=10)

# # root.mainloop()
# import tkinter as tk
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk
# import qrcode
# from datetime import datetime

# class MetroApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("VISHWA SMART MERRO")
#         self.root.geometry("520x880")
#         self.root.config(bg="#f0f2f5")

#         # ===== STATIONS FROM YOUR DATA =====
#         self.green_line = [
#             "Madavara (BIEC)", "Nagasandra", "Peenya", "Yeshwanthpur", 
#             "Mantri Square Mall", "Nadaprabhu Kempegowda Station (Majestic)", 
#             "Chickpete", "KR Market", "National College", "Lalbagh", 
#             "South End Circle", "Jayanagar", "RV Road", "Banashankari", 
#             "JP Nagar", "Yelachenahalli", "Konanakunte Cross", 
#             "Doddakallasandra", "Vajarahalli", "Thalaghattapura", "Silk Institute"
#         ]

#         self.purple_line = [
#             "Whitefield (Kadugodi)", 
#             "KR Puram", "Swami Vivekananda Road", "Indiranagar", "Trinity", 
#             "Mahatma Gandhi (MG) Road", "Nadaprabhu Kempegowda Station (Majestic)", 
#             "Magadi Road", "Vijayanagar", "Hosahalli", "Mysore Road", 
#             "Kengeri", "Challaghatta"
#         ]

#         self.yellow_line = [
#             "RV Road", "Ragigudda", "Jayadeva Hospital", "BTM Layout", 
#             "Central Silk Board", "Bommanahalli", "Kudlu Gate", "Singasandra", 
#             "HSR Layout", "Electronic City", " Electronics city", "Bommasandra"
#         ]

#         self.all_stations = sorted(list(set(self.purple_line + self.green_line + self.yellow_line)))
#         self.setup_ui()

#     def setup_ui(self):
#         # Header with branding
#         try:
#             img = Image.open("met.jpg").resize((460, 170))
#             self.header_photo = ImageTk.PhotoImage(img)
#             tk.Label(self.root, image=self.header_photo, bg="#f0f2f5").pack()
#         except:
#             tk.Label(self.root, text="🚇 NAMMA METRO", font=("Helvetica", 24, "bold"), 
#                      bg="#2E3192", fg="white", height=4).pack(fill="x")

#         # Main Card UI
#         self.card = tk.Frame(self.root, bg="white", padx=30, pady=25, relief="flat")
#         self.card.place(relx=0.5, rely=0.6, anchor="center", width=460, height=650)

#         tk.Label(self.card, text="GENERATE DIGITAL TICKET", font=("Arial", 14, "bold"), bg="white", fg="#333").pack(pady=10)

#         # Form Fields
#         self.create_label("PASSENGER NAME")
#         self.name_entry = tk.Entry(self.card, font=("Arial", 12), bg="#f8f9fa", relief="flat", bd=8)
#         self.name_entry.pack(fill="x", pady=5)

#         self.create_label("NUMBER OF PASSENGERS")
#         self.pass_count = ttk.Spinbox(self.card, from_=1, to=10, font=("Arial", 11))
#         self.pass_count.set(1)
#         self.pass_count.pack(fill="x", pady=5)

#         self.create_label("FROM STATION")
#         self.src_cb = ttk.Combobox(self.card, values=self.all_stations, state="readonly", font=("Arial", 11))
#         self.src_cb.pack(fill="x", pady=5)

#         self.create_label("TO STATION")
#         self.dest_cb = ttk.Combobox(self.card, values=self.all_stations, state="readonly", font=("Arial", 11))
#         self.dest_cb.pack(fill="x", pady=5)

#         # Action Button
#         tk.Button(self.card, text="BOOK NOW", bg="#2E3192", fg="white", 
#                   font=("Arial", 12, "bold"), relief="flat", cursor="hand2", 
#                   command=self.generate_ticket).pack(fill="x", pady=25, ipady=10)

#         # Digital Ticket Result Area
#         self.ticket_display = tk.Frame(self.card, bg="#fffde7", bd=1, relief="solid")
#         self.qr_img_label = tk.Label(self.ticket_display, bg="#fffde7")
#         self.qr_img_label.pack(pady=10)
#         self.ticket_info = tk.Label(self.ticket_display, bg="#fffde7", font=("Courier", 9), justify="left")
#         self.ticket_info.pack(pady=5)

#     def create_label(self, text):
#         tk.Label(self.card, text=text, font=("Arial", 8, "bold"), bg="white", fg="#888").pack(anchor="w", pady=(5,0))

#     def generate_ticket(self):
#         name = self.name_entry.get().upper()
#         src = self.src_cb.get()
#         dest = self.dest_cb.get()
#         num_pass = self.pass_count.get()

#         if not name or not src or not dest:
#             messagebox.showwarning("Incomplete", "Please fill in all details!")
#             return

#         # Fare Logic (Simple calculation)
#         fare = 25 * int(num_pass) 
#         time_now = datetime.now().strftime("%Y-%m-%d %H:%M")

#         # --- THE SCANNER RECEIPT (THIS IS WHAT SHOWS UP ON THE PHONE) ---
#         qr_receipt = (
#             f"🎫 NAMMA METRO TICKET\n"
#             f"--------------------------\n"
#             f"PASSENGER: {name}\n"
#             f"PASSENGERS: {num_pass}\n"
#             f"FROM: {src}\n"
#             f"TO: {dest}\n"
#             f"TIME: {time_now}\n"
#             f"TOTAL FARE: ₹{fare}.00\n"
#             f"--------------------------\n"
#             f"Thank you for choosing \nNamma Metro!\n"
#             f"--------------------------"
#         )

#         # Generate QR
#         qr = qrcode.make(qr_receipt)
#         qr.save("ticket_output.png")

#         # Show Ticket in App UI
#         self.ticket_display.pack(fill="both", expand=True)
        
#         # Fixing the image bug: assign to 'self' to keep a reference
#         qr_raw = Image.open("ticket_output.png").resize((140, 140))
#         self.current_qr = ImageTk.PhotoImage(qr_raw)
        
#         self.qr_img_label.config(image=self.current_qr)
#         self.ticket_info.config(text=f"Ticket Issued for {name}\nTotal Fare: ₹{fare}")

#         messagebox.showinfo("Success", "Ticket Generated! Scan to see details.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MetroApp(root)
#     root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import qrcode
from datetime import datetime

class MetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VMETRO - powered by VISHWA")
        self.root.geometry("520x920")
        self.root.config(bg="#f0f2f5")

        # ===== OFFICIAL BMRCL DISTANCE DATA (KM from Line Start) =====
        # Distances are mapped to match official BMRCL route specifications
        self.purple_dist = {
            "Whitefield (Kadugodi)": 0.0, "KR Puram": 5.4, "Swami Vivekananda Road": 7.9, 
            "Indiranagar": 9.1, "Trinity": 11.2, "Mahatma Gandhi (MG) Road": 12.0, 
            "Nadaprabhu Kempegowda Station (Majestic)": 15.1, "Magadi Road": 17.4, 
            "Vijayanagar": 20.9, "Hosahalli": 22.1, "Mysore Road": 25.1, 
            "Kengeri": 32.6, "Challaghatta": 34.6
        }

        self.green_dist = {
            "Madavara (BIEC)": 0.0, "Nagasandra": 1.6, "Peenya": 4.8, "Yeshwanthpur": 7.3, 
            "Mantri Square Mall": 10.9, "Nadaprabhu Kempegowda Station (Majestic)": 12.0, 
            "Chickpete": 13.5, "KR Market": 14.7, "National College": 16.0, "Lalbagh": 17.2, 
            "South End Circle": 18.1, "Jayanagar": 19.3, "RV Road": 20.5, "Banashankari": 21.8, 
            "JP Nagar": 23.1, "Yelachenahalli": 25.3, "Konanakunte Cross": 26.5, 
            "Doddakallasandra": 27.8, "Vajarahalli": 28.9, "Thalaghattapura": 30.1, "Silk Institute": 31.2
        }

        self.yellow_dist = {
            "RV Road": 0.0, "Ragigudda": 1.4, "Jayadeva Hospital": 2.7, "BTM Layout": 3.9, 
            "Central Silk Board": 5.1, "Bommanahalli": 6.5, "Kudlu Gate": 9.4, "Singasandra": 10.7, 
            "HSR Layout": 12.1, "Electronic City": 15.2, "Electronics City": 16.5, "Bommasandra": 19.1
        }

        self.interchange_majestic = "Nadaprabhu Kempegowda Station (Majestic)"
        self.interchange_rvroad = "RV Road"
        
        self.all_stations = sorted(list(set(list(self.purple_dist.keys()) + 
                                           list(self.green_dist.keys()) + 
                                           list(self.yellow_dist.keys()))))
        self.setup_ui()

    def setup_ui(self):
        try:
            img = Image.open("met.jpg").resize((460, 170))
            self.header_photo = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.header_photo, bg="#f0f2f5").pack(pady=10)
        except:
            tk.Label(self.root, text="🚇 VMETRO SMART", font=("Helvetica", 24, "bold"), 
                     bg="#2E3192", fg="white", height=4).pack(fill="x")

        self.card = tk.Frame(self.root, bg="white", padx=30, pady=20, relief="flat")
        self.card.place(relx=0.5, rely=0.6, anchor="center", width=460, height=680)

        tk.Label(self.card, text="VMETRO DIGITAL TICKET", font=("Arial", 14, "bold"), bg="white", fg="#333").pack(pady=5)

        self.create_label("PASSENGER NAME")
        self.name_entry = tk.Entry(self.card, font=("Arial", 12), bg="#f8f9fa", relief="flat", bd=8)
        self.name_entry.pack(fill="x", pady=2)

        self.create_label("NUMBER OF PASSENGERS")
        self.pass_count = ttk.Spinbox(self.card, from_=1, to=10, font=("Arial", 11))
        self.pass_count.set(1)
        self.pass_count.pack(fill="x", pady=2)

        self.create_label("FROM STATION")
        self.src_cb = ttk.Combobox(self.card, values=self.all_stations, state="readonly", font=("Arial", 11))
        self.src_cb.pack(fill="x", pady=2)

        self.create_label("TO STATION")
        self.dest_cb = ttk.Combobox(self.card, values=self.all_stations, state="readonly", font=("Arial", 11))
        self.dest_cb.pack(fill="x", pady=2)

        tk.Button(self.card, text="GENERATE SMART TICKET", bg="#2E3192", fg="white", 
                  font=("Arial", 12, "bold"), relief="flat", cursor="hand2", 
                  command=self.generate_ticket).pack(fill="x", pady=15, ipady=10)

        self.ticket_display = tk.Frame(self.card, bg="white", bd=1, relief="solid")
        self.qr_img_label = tk.Label(self.ticket_display, bg="white")
        self.qr_img_label.pack(pady=5)
        self.ticket_info = tk.Label(self.ticket_display, bg="white", font=("Courier", 9), justify="left")
        self.ticket_info.pack(pady=5)

    def create_label(self, text):
        tk.Label(self.card, text=text, font=("Arial", 8, "bold"), bg="white", fg="#888").pack(anchor="w", pady=(5,0))

    def get_exact_dist(self, s, d):
        # 1. Same Line Logic
        if s in self.purple_dist and d in self.purple_dist:
            return abs(self.purple_dist[d] - self.purple_dist[s])
        if s in self.green_dist and d in self.green_dist:
            return abs(self.green_dist[d] - self.green_dist[s])
        if s in self.yellow_dist and d in self.yellow_dist:
            return abs(self.yellow_dist[d] - self.yellow_dist[s])

        # 2. Interchange Logic
        # Case A: Purple <-> Green (Via Majestic)
        if (s in self.purple_dist or d in self.purple_dist) and (s in self.green_dist or d in self.green_dist):
            d1 = abs(self.purple_dist.get(s, self.purple_dist.get(d)) - self.purple_dist[self.interchange_majestic])
            d2 = abs(self.green_dist.get(d, self.green_dist.get(s)) - self.green_dist[self.interchange_majestic])
            return d1 + d2
        
        # Case B: Green <-> Yellow (Via RV Road)
        if (s in self.green_dist or d in self.green_dist) and (s in self.yellow_dist or d in self.yellow_dist):
            d1 = abs(self.green_dist.get(s, self.green_dist.get(d)) - self.green_dist[self.interchange_rvroad])
            d2 = abs(self.yellow_dist.get(d, self.yellow_dist.get(s)) - self.yellow_dist[self.interchange_rvroad])
            return d1 + d2

        return 10.0 # Default fallback

    def calculate_real_fare(self, distance_km, passenger_count):
        # Official BMRCL Slab Logic
        if distance_km <= 2: base_fare = 10
        elif distance_km <= 4: base_fare = 20
        elif distance_km <= 6: base_fare = 30
        elif distance_km <= 10: base_fare = 45
        elif distance_km <= 15: base_fare = 60
        else: base_fare = 95 # Maximum Cap

        return base_fare * int(passenger_count)

    def generate_ticket(self):
        name = self.name_entry.get().upper()
        source = self.src_cb.get()
        dest = self.dest_cb.get()
        count = self.pass_count.get()

        if not name or not source or not dest:
            messagebox.showwarning("Incomplete", "Please fill in all details!")
            return
        
        if source == dest:
            messagebox.showwarning("Error", "Source and Destination cannot be same!")
            return

        exact_km = self.get_exact_dist(source, dest)
        total_fare = self.calculate_real_fare(exact_km, count)

        receipt_content = f"""
------------------------------
   VISHWA SMART METRO E-TICKET
------------------------------
PASSENGER : {name}
ADULTS    : {count}
FROM      : {source}
TO        : {dest}
DISTANCE  : {exact_km:.2f} KM
------------------------------
TOTAL FARE: RS {total_fare}
TIME      : {datetime.now().strftime('%H:%M:%S')}
DATE      : {datetime.now().strftime('%d-%b-%Y')}
------------------------------
THANK YOU FOR CHOOSING
VMETRO BENGALURU!
------------------------------
"""
        qr = qrcode.make(receipt_content)
        qr.save("ticket_output.png")

        self.ticket_display.pack(fill="both", expand=True, pady=10)
        qr_raw = Image.open("ticket_output.png").resize((150, 150))
        self.current_qr = ImageTk.PhotoImage(qr_raw)
        self.qr_img_label.config(image=self.current_qr)
        
        self.ticket_info.config(text=f"Confirmed: {name}\nFare: ₹{total_fare} |Tota Distance: {exact_km:.2f}km")
        messagebox.showinfo("Success", f"Ticket Generated!\nTotal Distance: {exact_km:.2f} km")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroApp(root)
    root.mainloop()