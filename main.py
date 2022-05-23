from tkinter import *
import requests


def get_quote():
    kanye_data = requests.get(url="https://api.kanye.rest")
    kanye_data.raise_for_status()
    kanye_quote = kanye_data.json()["quote"]

    canvas.itemconfig(quote_text, text=kanye_quote)

BACKGROUND_COLOR = "white"

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=300, height=414, bg=BACKGROUND_COLOR, highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.config(bg=BACKGROUND_COLOR)
kanye_button.grid(row=1, column=0)

initial_quote = get_quote()

window.mainloop()