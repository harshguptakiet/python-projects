import tkinter as tk
from tkinter import messagebox, simpledialog, font

class RestaurantManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Management System")
        self.master.geometry("500x400")
        self.master.configure(bg="#F0F0F0")  # Light gray background

        self.menu = {}
        self.orders = []

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        title = tk.Label(self.master, text="Gourmet Haven", font=title_font, bg="#F0F0F0", fg="#333333")
        title.pack(pady=20)

        # Main frame
        main_frame = tk.Frame(self.master, bg="#FFFFFF", bd=2, relief=tk.RAISED)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Button style
        button_style = {
            "font": ("Helvetica", 12),
            "bg": "#4CAF50",  # Green
            "fg": "white",
            "activebackground": "#45a049",  # Darker green for active state
            "activeforeground": "white",
            "relief": tk.RAISED,
            "bd": 0,
            "padx": 20,
            "pady": 10,
            "width": 15
        }

        # Buttons
        tk.Button(main_frame, text="Add Menu Item", command=self.add_menu_item, **button_style).pack(pady=10)
        tk.Button(main_frame, text="View Menu", command=self.view_menu, **button_style).pack(pady=10)
        tk.Button(main_frame, text="Place Order", command=self.place_order, **button_style).pack(pady=10)
        tk.Button(main_frame, text="View Orders", command=self.view_orders, **button_style).pack(pady=10)

        # Footer
        footer = tk.Label(self.master, text="© 2024 CSIT SEC-B ", font=("Helvetica", 10), bg="#F0F0F0", fg="#666666")
        footer.pack(side=tk.BOTTOM, pady=10)

    def add_menu_item(self):
        name = simpledialog.askstring("Add Menu Item", "Enter item name:")
        if name:
            price = simpledialog.askfloat("Add Menu Item", f"Enter price for {name}:")
            if price is not None:
                self.menu[name] = price
                messagebox.showinfo("Success", f"{name} added to the menu.")

    def view_menu(self):
        if not self.menu:
            messagebox.showinfo("Menu", "The menu is empty.")
        else:
            menu_str = "\n".join([f"{item}: ${price:.2f}" for item, price in self.menu.items()])
            self.show_scrollable_message("Menu", menu_str)

    def place_order(self):
        if not self.menu:
            messagebox.showerror("Error", "The menu is empty. Please add items first.")
            return

        order = {}
        while True:
            item = simpledialog.askstring("Place Order", "Enter item name (or 'done' to finish):")
            if item == 'done':
                break
            if item in self.menu:
                quantity = simpledialog.askinteger("Place Order", f"Enter quantity for {item}:")
                if quantity:
                    order[item] = quantity
            else:
                messagebox.showerror("Error", f"{item} is not in the menu.")

        if order:
            self.orders.append(order)
            messagebox.showinfo("Success", "Order placed successfully.")

    def view_orders(self):
        if not self.orders:
            messagebox.showinfo("Orders", "No orders placed yet.")
        else:
            orders_str = ""
            for i, order in enumerate(self.orders, 1):
                orders_str += f"Order {i}:\n"
                for item, quantity in order.items():
                    orders_str += f"  {item}: {quantity}\n"
                orders_str += "\n"
            self.show_scrollable_message("Orders", orders_str)

    def show_scrollable_message(self, title, message):
        top = tk.Toplevel(self.master)
        top.title(title)
        top.geometry("300x400")

        frame = tk.Frame(top)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = tk.Text(frame, yscrollcommand=scrollbar.set, wrap=tk.WORD)
        text_widget.insert(tk.END, message)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=text_widget.yview)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    root.mainloop()