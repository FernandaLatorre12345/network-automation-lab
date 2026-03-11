import tkinter as tk
from tkinter import messagebox
from switch_config import configure_switch


def run_automation():

    host = entry_host.get()
    username = entry_user.get()
    password = entry_pass.get()
    new_hostname = entry_hostname.get()
    vlan_id = entry_vlan.get()
    vlan_name = entry_vlan_name.get()

    if not host or not username or not password:
        messagebox.showerror("Input Error", "Please fill all required fields.")
        return

    try:
        backup = configure_switch(
            host,
            username,
            password,
            vlan_id,
            vlan_name,
            new_hostname
        )

        if backup:
            messagebox.showinfo(
                "Automation Successful",
                f"Configuration applied successfully.\n\nBackup created:\n{backup}"
            )
        else:
            messagebox.showerror(
                "Automation Failed",
                "Automation failed.\nCheck device connectivity or credentials."
            )

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Network Automation Tool")
root.geometry("420x360")


tk.Label(root, text="Device IP / Hostname").pack()
entry_host = tk.Entry(root)
entry_host.pack()

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Label(root, text="New Hostname").pack()
entry_hostname = tk.Entry(root)
entry_hostname.pack()

tk.Label(root, text="VLAN ID").pack()
entry_vlan = tk.Entry(root)
entry_vlan.pack()

tk.Label(root, text="VLAN Name").pack()
entry_vlan_name = tk.Entry(root)
entry_vlan_name.pack()


tk.Button(
    root,
    text="Run Automation",
    command=run_automation,
    bg="lightblue"
).pack(pady=20)


root.mainloop()
