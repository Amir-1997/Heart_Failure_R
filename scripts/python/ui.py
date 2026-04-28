import tkinter as tk
from pydantic import BaseModel, Field

# CONSTANTS
CANVAS_WIDTH = 625
CANVAS_HEIGHT = 250
BG_GRAY = "#486581"


class UX(tk.TK):
    def __init__(self):
        super().__init__()
        self.title("Heart Failure Predictor")
        self.minsize(width=750, height=600)
        self.config(padx=25, pady=25, bg=BG_GRAY)
        self.input_lbl = {}
        self.inputs = {}

    # Label - Title
        self.label_title = tk.Label(bg=BG_GRAY, fg="white", text="Heart Failure Predictor", font=("Helvetica", 20, "bold"))
        self.label_title.grid(row=0, columnspan=4, sticky="w", padx=80, pady=10)

    # Canvas
        self.canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BG_GRAY, highlightthickness=0)
        self.ecg_png = tk.PhotoImage(file="ecg.png")
        self.canvas.create_image(350, 125, image=ecg_png)
        self.canvas.grid(row=1, columnspan=4)
        self.set_inputs()
        self.get_vals()
        self.feat = None

    # Button
        self.predict_button = tk.Button(self, text="Predict", command=lambda: self.get_vals)

        fields = [("age", "Age (1-100):", 3, 0),
                  ("sex", "Sex (0=F,1=M):", 3, 2),
                  ("cp", "Chest Pain (0-3):", 4, 0),
                  ("trestbps", "Resting BP:", 4, 2),
                  ("fbs", "Fasting BS (0/1):", 5, 0),
                  ("restecg", "Resting ECG (0-2):", 5, 2),
                  ("thalach", "Max Heart Rate:", 6, 0),
                  ("exang", "Exercise Angina (0/1):", 6, 2),
                  ("oldpeak", "ST Depression:", 7, 0)]

# --------- Inputs --------- #
    def set_inputs(self):
        for var_name, txt, row_n, col_n in fields:
            lbl= tk.Label(self, text=f"{txt}", bg=BG_GRAY, fg="white", font=("Helvetica", 12))
            lbl.grid(row=row_n, column=col_n, sticky="e", pady=10, padx=(20, 10))

            inp = tk.Entry(window, width=15, bg=BG_GRAY, fg="white", font=("Helvetica", 12))
            inp.grid(row=row_n, column=col_n + 1, sticky="w", pady=10, padx=(0, 40))

            self.input_lbl[var_name] = lbl
            self.inputs[var_name] = inp


    def get_vals(self):
        for key, value in self.inputs.items():
            val = value.get()
            self.feat[key] = val
            value.delete(0, tk.END)
            


