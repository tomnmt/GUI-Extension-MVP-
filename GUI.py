import tkinter as tk
import dict_methods as dm

cart = {"Orange": 1, "Raspberry": 1, "Blueberries": 1}
cart_str = str(cart)

root = tk.Tk()
root.title("Fruit and Veg Shopping")
root.geometry("400x400")

cart_txt = tk.StringVar()
cart_txt.set("Cart Contents Displayed Here")

apple_btn = tk.Button(root, text="Add Apple to cart", command=lambda: dm.add_item(cart, "Apple"))
banana_btn = tk.Button(root, text="Add Banana to cart", command=lambda: dm.add_item(cart, "Banana"))
orange_btn = tk.Button(root, text="Add Orange to cart", command=lambda: dm.add_item(cart, "Orange"))
raspberry_btn = tk.Button(root, text="Add Raspberry to cart", command=lambda: dm.add_item(cart, "Raspberry"))
blueberry_btn = tk.Button(root, text="Add Blueberry to cart", command=lambda: dm.add_item(cart, "Blueberry"))
broccoli_btn = tk.Button(root, text="Add Broccoli to cart", command=lambda: dm.add_item(cart, "Broccoli"))
kiwi_btn = tk.Button(root, text="Add Kiwi to cart", command=lambda: dm.add_item(cart, "Kiwi"))
melon_btn = tk.Button(root, text="Add Melon to cart", command=lambda: dm.add_item(cart, "Melon"))

def update_cart_display():
    dm.sort_entries(cart)
    cart_str = str(cart)
    cart_txt.set("Current Cart: " + cart_str)


cart_btn = tk.Button(root, text="Click to view updated cart", command=update_cart_display)
cart_lbl = tk.Label(root, textvariable=cart_txt)

apple_btn.pack()
banana_btn.pack()
orange_btn.pack()
raspberry_btn.pack()
blueberry_btn.pack()
broccoli_btn.pack()
kiwi_btn.pack()
melon_btn.pack()

cart_lbl.pack()
cart_btn.pack()

root.mainloop()
