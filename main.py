import customtkinter
import math

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title("Bookings Helper")

def calculate_function():
    total_func = float(total.get())
    priceLimit_func = float(price_limit.get())
    qty = 0
    unitPrice = 9999
    answerFound = False
    smallestDiff = 9999
    while not answerFound and qty < 100000:
        qty += 1
        unitPrice = total_func / qty
        roundedUnitPrice = math.floor(unitPrice * 100) / 100.0
        if unitPrice < priceLimit_func:
            if (unitPrice - roundedUnitPrice) < smallestDiff:
                smallestDiff = unitPrice - roundedUnitPrice
                smallestDiffQty = qty
                smallestDiffUnitPrice = unitPrice

            if str(unitPrice)[::-1].find('.') < 3:
                answerFound = True
    if not answerFound:
        qty = smallestDiffQty
        unitPrice = round(smallestDiffUnitPrice, 2)
    quantity.configure(text=qty)
    price.configure(text=unitPrice)

def enter():
    print('enter')

total = customtkinter.CTkEntry(window, placeholder_text="Total Available")
total.grid(column=0, row=0, padx=20, pady=20)

price_limit = customtkinter.CTkEntry(window, placeholder_text="Price Limit")
price_limit.grid(column=1, row=0, columnspan=2, padx=20, pady=20)

calculate_button = customtkinter.CTkButton(master=window, text="Calculate", command=calculate_function)
calculate_button.grid(column=0, row=1, columnspan=3, padx=20, pady=20)

quantity_result_text = customtkinter.CTkLabel(window, text="Quantity", fg_color="transparent")
quantity_result_text.grid(column=0, row=3, padx=20, pady=20)

price_result_text = customtkinter.CTkLabel(window, text="Price", fg_color="transparent")
price_result_text.grid(column=0, row=2, padx=20, pady=20)

quantity = customtkinter.CTkLabel(window, text="", fg_color="transparent")
quantity.grid(column=1, row=3, padx=20, pady=20)

price = customtkinter.CTkLabel(window, text="", fg_color="transparent")
price.grid(column=1, row=2, padx=20, pady=20)

window.mainloop()







