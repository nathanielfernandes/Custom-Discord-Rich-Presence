# Nathaniel Fernandes
from pypresence import Presence
import tkinter as tk
import random
import time


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Custom Discord Presence")
        self.window.configure(bg="#2C2F33")
        self.window.resizable(width=False, height=False)
        self.frames = []

    def add_frame(self, row, col):
        frame = Frame(self.window, row, col)
        self.frames.append(frame)

    def add_field_entry(self, frame_n, name, row_start=0, col_start=0):
        field = self.frames[frame_n].add_field_entry(name, row_start, col_start)
        return field

    def add_field_dropdown(self, frame_n, name, options, row_start=0, col_start=0):
        field = self.frames[frame_n].add_field_dropdown(
            name, options, row_start, col_start
        )
        return field

    def add_field_slider(self, frame_n, name, ran, row_start=0, col_start=0):
        field = self.frames[frame_n].add_field_slider(name, ran, row_start, col_start)
        return field

    def start(self):
        self.window.mainloop()


class Frame:
    def __init__(self, window, row, col):
        self.row = row
        self.col = col
        self.frame = tk.Frame(master=window, bg="#2C2F33")
        self.fields = {}

    def add_field_entry(self, name, row_start=0, col_start=0):
        field = Entry_Field(self.frame, name, row_start, col_start)
        self.fields[name] = field
        self.frame.grid(row=self.row, column=self.col, padx=20, pady=20)
        return field

    def add_field_dropdown(self, name, options, row_start=0, col_start=0):
        field = Dropdown_Field(self.frame, name, options, row_start, col_start)
        self.fields[name] = field
        self.frame.grid(row=self.row, column=self.col, padx=20, pady=20)
        return field

    def add_field_slider(self, name, ran, row_start=0, col_start=0):
        field = Slider_Field(self.frame, name, ran, row_start, col_start)
        self.fields[name] = field
        self.frame.grid(row=self.row, column=self.col, padx=20, pady=20)
        return field


class Entry_Field:
    def __init__(self, frame, text, row_start, col_start):
        self.row_start = row_start
        self.col_start = col_start
        self.entry = tk.Entry(master=frame, width=10, bg="#2C2F33", fg="white")
        self.name = tk.Label(master=frame, text=text, bg="#2C2F33", fg="white")
        self.display = tk.Label(master=frame, text=None, fg="#7289DA", bg="#2C2F33")
        self.button = tk.Button(
            master=frame, text="Set", fg="green", command=self.on_click,
        )

        self.name.grid(row=self.row_start, column=self.col_start, sticky="w")
        self.entry.grid(row=self.row_start, column=self.col_start + 1, sticky="e")
        self.button.grid(row=self.row_start, column=self.col_start + 2, padx=5)

        self.value = None

    def on_click(self):
        text = self.entry.get()
        if (self.button["text"] == "Set") and (128 >= len(text) >= 2):
            self.display["text"] = text
            self.button["text"] = "Reset"
            self.button["fg"] = "black"
            self.entry.delete(0, tk.END)
            self.entry.grid_remove()
            self.display.grid(row=self.row_start, column=self.col_start + 1, sticky="w")
            self.value = text
        else:
            self.button["text"] = "Set"
            self.button["fg"] = "green"
            self.display.grid_remove()
            self.display["text"] = None
            self.entry.grid(row=self.row_start, column=self.col_start + 1, sticky="e")
            self.value = None

        update()


class Dropdown_Field:
    def __init__(self, frame, text, options, row_start, col_start):
        self.row_start = row_start
        self.col_start = col_start

        self.variable = tk.StringVar(frame)
        self.variable.set(options[0])  # default value

        self.entry = tk.OptionMenu(frame, self.variable, *options)
        self.name = tk.Label(master=frame, text=text, bg="#2C2F33", fg="white")
        self.display = tk.Label(master=frame, text=None, fg="#7289DA", bg="#2C2F33")
        self.button = tk.Button(
            master=frame, text="Set", fg="green", command=self.on_click,
        )

        self.name.grid(row=self.row_start, column=self.col_start, sticky="w")
        self.entry.grid(row=self.row_start, column=self.col_start + 1, sticky="e")
        self.button.grid(row=self.row_start, column=self.col_start + 2, padx=5)

        self.value = None

    def on_click(self):
        text = self.variable.get()
        if self.button["text"] == "Set":
            self.display["text"] = text
            self.button["text"] = "Reset"
            self.button["fg"] = "black"
            self.entry.grid_remove()
            self.display.grid(row=self.row_start, column=self.col_start + 1, sticky="w")
            self.value = text
        else:
            self.button["text"] = "Set"
            self.button["fg"] = "green"
            self.display.grid_remove()
            self.display["text"] = None
            self.entry.grid(row=self.row_start, column=self.col_start + 1, sticky="e")
            self.value = None

        update()


class Slider_Field:
    def __init__(self, frame, text, ran, row_start, col_start):
        self.row_start = row_start
        self.col_start = col_start

        self.entry = tk.Scale(
            master=frame, from_=ran[0], to=ran[1], orient=tk.HORIZONTAL
        )
        self.name = tk.Label(master=frame, text=text, bg="#2C2F33", fg="white")
        self.display = tk.Label(master=frame, text=None, fg="#7289DA", bg="#2C2F33")
        self.button = tk.Button(
            master=frame, text="Set", fg="green", command=self.on_click,
        )

        self.name.grid(row=self.row_start, column=self.col_start, sticky="w")
        self.entry.grid(row=self.row_start, column=self.col_start + 1, sticky="e")
        self.button.grid(row=self.row_start, column=self.col_start + 2, padx=5)

        self.value = None

    def on_click(self):
        text = self.entry.get()
        if self.button["text"] == "Set":
            self.display["text"] = time.strftime(
                "%H:%M:%S", time.gmtime(text - time.time())
            )
            self.entry["from_"] = time.time()
            self.button["text"] = "Reset"
            self.button["fg"] = "black"
            self.entry.grid_remove()
            self.display.grid(row=self.row_start, column=self.col_start + 1, sticky="w")
            self.value = text
        else:
            self.button["text"] = "Set"
            self.button["fg"] = "green"
            self.display.grid_remove()
            self.display["text"] = None
            self.entry.grid(row=self.row_start, column=self.col_start + 1, sticky="e")
            self.value = None

        update()


def update():
    join_button = bool(join.value) if join is not None else False
    RPC.update(
        details=details.value if details is not None else None,
        state=state.value if state is not None else None,
        small_image=small_image.value if small_image is not None else None,
        small_text=small_text.value if small_text is not None else None,
        large_image=large_image.value if large_image is not None else None,
        large_text=large_text.value if large_text is not None else None,
        join="test" if join_button else None,
        start=time.time(),
        end=time_left.value if time_left is not None else None,
        # party_size=[1, 4],
    )


def close():
    RPC.close()
    window.window.destroy()


if __name__ == "__main__":
    # you can replace this client_id with your own apps client_id and adjust the options accordingly
    client_id = "798338902389817345"
    options = [
        "doge",
        "otter",
        "cursed",
        "babyyoda",
        "confetti",
        "sovietdoge",
        "pupper",
        "highestintheroom",
        "splash",
        "water",
        "beans",
        "minecraft",
        "pigeon",
    ]
    random.shuffle(options)

    RPC = Presence(client_id, pipe=0)
    RPC.connect()
    RPC.update()

    window = Window()

    window.add_frame(0, 0)
    details = window.add_field_entry(0, "Details:", 0, 0)
    state = window.add_field_entry(0, "State:", 1, 0)
    join = window.add_field_dropdown(0, "Join Button:", ["True"], 0, 3)
    time_left = window.add_field_slider(
        0, "Time Left:", [time.time(), time.time() + 86400], 1, 3
    )

    window.add_frame(1, 0)
    large_image = window.add_field_dropdown(1, "Large Image:", options, 0, 0)
    large_text = window.add_field_entry(1, "Large Image Text:", 0, 3)

    small_image = window.add_field_dropdown(1, "Small Image:", options, 1, 0)
    small_text = window.add_field_entry(1, "Small Image Text:", 1, 3)

    window.window.protocol("WM_DELETE_WINDOW", close)
    window.start()

