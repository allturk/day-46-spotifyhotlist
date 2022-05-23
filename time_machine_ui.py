import tkinter as tk
import os

import messagebox
from billboard_list import Billboard

class TimeMachineUI:
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.config_windows()
        self.canvas = tk.Canvas(height=450, width=500, background="#5EE6EB", )
        self.canvas.grid(row=0, column=0)
        self.id_text = tk.Entry(self.canvas, width=35)
        self.sec_text = tk.Entry(self.canvas, width=35)
        self.date_entry = tk.Entry(self.canvas, width=32)
        self.clid_get_btn = tk.Button(text="ID Get")
        self.clid_ent_btn = tk.Button(text="ID Enter")
        self.clsec_get_btn = tk.Button(text="Sec Get")
        self.clsec_ent_btn = tk.Button(text="Sec Enter")
        self.billboard_btn = tk.Button(text="Billboard List")
        self.create_labels()
        self.config_entries()
        self.config_buttons()
        self.billb=Billboard()


    def id_get(self, btn):
        if btn:
            text = self.id_text.get()
            cl_id = os.getenv(text)
            # self.clid=client_id

            if cl_id != None:
                self.clid_get_btn.config(state="disabled")
                self.clid_ent_btn.config(state="disabled")
                # self.spfy.client_id=cl_id
                # print(self.spfy.client_id)

        else:
            text = self.sec_text.get()
            client_sec = os.getenv(text)
            if client_sec != None:
                self.clsec_get_btn.config(state="disabled")
                self.clsec_ent_btn.config(state="disabled")
                self.playlist_id=client_sec
            print(client_sec)


    def id_enter(self, btn):

        if messagebox.askokcancel(title="Sure", message="Is your entry True?"):
            if btn:
                text = self.id_text.get()
                print(text)
                return text
            else:
                text = self.sec_text.get()
                print(text)
                return text
        else:
            messagebox.showinfo(title="Info", message="Please reenter your entry.")

    def config_windows(self):

        self.window.title("Time Machine")
        self.window.config(padx=20, pady=20, bg="#5EE6EB")
        self.window.tk.call("wm", "iconphoto", self.window, tk.PhotoImage(file="images/computer.png"))

    def create_labels(self):
        # labels
        id_label = tk.Label(self.canvas, text="Client_ID   :", bg="#5EE6EB")
        id_label.config(justify="left")
        self.canvas.create_window(50, 30, window=id_label)
        sec_label = tk.Label(self.canvas, text="Client_Sec : ", bg="#5EE6EB")
        self.canvas.create_window(50, 70, window=sec_label)

        date_lbl = tk.Label(self.canvas, text="Hot List Date :", bg="#5EE6EB")
        date_lbl.config(justify="left")
        self.canvas.create_window(55, 110, window=date_lbl)

    def config_entries(self):
        self.id_text.insert(tk.END, "Enter Client_id or Env variable name")
        self.id_text.bind("<FocusIn>", lambda x: self.id_text.selection_range(0, tk.END))
        self.canvas.create_window(190, 30, window=self.id_text)

        self.sec_text.insert(tk.END, "Enter Client_Sec or Env variable name")
        self.sec_text.bind("<FocusIn>", lambda x: self.sec_text.selection_range(0, tk.END))
        self.canvas.create_window(190, 70, window=self.sec_text)

        self.date_entry.insert(tk.END, "Date format YYYY-MM-DD")
        self.date_entry.bind("<FocusIn>", lambda x: self.date_entry.selection_range(0, tk.END))
        self.canvas.create_window(200, 110, window=self.date_entry)

    def config_buttons(self):
        # Buttons

        self.clid_get_btn.config(command=lambda m=True: self.id_get(m), width=10)

        self.canvas.create_window(350, 30, window=self.clid_get_btn)

        self.clid_ent_btn.config(command=lambda m=True: self.id_enter(m), width=10)
        self.canvas.create_window(440, 30, window=self.clid_ent_btn)

        self.clsec_get_btn.config(command=lambda m=False: self.id_get(m), width=10)
        self.canvas.create_window(350, 70, window=self.clsec_get_btn)

        self.clsec_ent_btn.config(command=lambda m=False: self.id_enter(m), width=10)
        self.canvas.create_window(440, 70, window=self.clsec_ent_btn)

        self.billboard_btn.config(width=23, command=self.bilboard_list)
        self.canvas.create_window(395, 110, window=self.billboard_btn)

    def bilboard_list(self):
        self.billb.list_date = self.date_entry.get()
        self.billb.search_hotlist()
