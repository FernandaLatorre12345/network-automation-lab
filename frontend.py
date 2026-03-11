import tkinter as tk
from tkinter import messagebox
from switch_config import configure_switch


def run_config():

    host = host_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    hostname = hostname_entry.get()
    vlan_id = vlan_entry.get()
    vlan_name = name_entry.get()

    try:

        backup = configure_switch(
            host,
            username,
            password,
            vlan_id,
            vlan_name,
            hostname
        )

        messagebox.showinfo(
            "Success",
            f"Configuration applied.\nBackup file: {backup}"
        )

    except Exception as e:

        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Network Automation Tool")


tk.Label(root, text="Device IP").grid(row=0, column=0)
host_entry = tk.Entry(root)
host_entry.grid(row=0, column=1)


tk.Label(root, text="Username").grid(row=1, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1)


tk.Label(root, text="Password").grid(row=2, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1)


tk.Label(root, text="New Hostname").grid(row=3, column=0)
hostname_entry = tk.Entry(root)
hostname_entry.grid(row=3, column=1)


tk.Label(root, text="VLAN ID").grid(row=4, column=0)
vlan_entry = tk.Entry(root)
vlan_entry.grid(row=4, column=1)


tk.Label(root, text="VLAN Name").grid(row=5, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=5, column=1)


tk.Button(root, text="Configure Switch", command=run_config).grid(row=6, column=1)

root.mainloop()
