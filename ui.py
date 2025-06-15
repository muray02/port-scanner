from tkinter import *
from scanner import scan

def scan_ports():
    ip = ip_entry.get()
    port_start = int(port_start_entry.get())
    port_end = int(port_end_entry.get())
    ports = range(port_start, port_end + 1)

    result = scan(ip, ports)  

    if result:
        output_label.config(text=f"Открытые порты: {', '.join(map(str, result))}")
    else:
        output_label.config(text="Открытых портов не найдено")

root = Tk()

root.title("PortScanner")
root.geometry("300x400")

# Press button
button = Button(root, text="Сканировать порты", font=30, command=scan_ports)
button.pack(side=BOTTOM, pady=40)

Label(root, text="IP-adress").pack()
ip_entry = Entry(root)
ip_entry.pack()

Label(root, text="Начальный порт").pack()
port_start_entry = Entry(root)
port_start_entry.pack()

Label(root, text="Конечный порт").pack()
port_end_entry = Entry(root)
port_end_entry.pack()

output_label = Label(root, text="")
output_label.pack()

root.mainloop()