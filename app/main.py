
import tkinter as tk
import requests

def get_country():
    try:
        c = entry.get().strip()

        result_label.config(text=" Loading...")

        url = f"https://restcountries.com/v3.1/name/{c}"
        data = requests.get(url, timeout=5).json()[0]

        name = data["name"]["common"]
        capital = data["capital"][0]
        population = data["population"]
        flag = data["flag"]

        result_label.config(
            text=f"{flag} {name}\n Capital: {capital}\n Population: {population:,}"
        )

        entry.delete(0, tk.END)

    except:
        result_label.config(text="❌ Error or country not found")
        entry.delete(0, tk.END)

# ---------------- UI ----------------
app = tk.Tk()
app.title( "Country Info App")
app.geometry("500x400")
app.configure(bg="#0f172a")

title = tk.Label(
    app,
    text=" Country Info App",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#0f172a"
)
title.pack(pady=15)

entry = tk.Entry(app, font=("Arial", 12), width=30)
entry.pack(pady=10)

btn = tk.Button(
    app,
    text="Get Country Info",
    command=get_country,
    bg="#22c55e",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=5
)
btn.pack(pady=10)

result_label = tk.Label(
    app,
    text="Enter a country name above ",
    fg="white",
    bg="#1e293b",
    font=("Arial", 12),
    padx=15,
    pady=15,
    justify="left",
    wraplength=450
)
result_label.pack(pady=20)

app.mainloop()