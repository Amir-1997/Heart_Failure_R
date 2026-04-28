IS_VALID = True
ERROR_LOG = []

raw_data = {
    "age": input_age.get(),
    "sex": input_sex.get(),
    "cp": input_cp.get(),
    "trestbps": input_trestbps.get(),
    "fbs": input_fbs.get(),
    "restecg": input_restecg.get(),
    "thalach": input_thalach.get(),
    "exang": input_exang.get(),
    "oldpeak": input_oldpeak.get()
}


class HeartData(BaseModel):
    age: int
    Field(ge=0, le=100)
    sex: int
    Field(ge=0, le=1)
    cp: int
    Field(ge=1, le=4)
    trestbps: int
    Field(ge=0, le=220)
    fbs: int
    Field(ge=0, le=1)
    restecg: int
    Field(ge=0, le=3)
    thalach: float
    exang: int
    Field(ge=0, le=1)
    oldpeak: float


try:
    preds = HeartData(**raw_data)

except ValidationError as e:


def check_valid(var, lb, ub):
    global IS_VALID, ERROR_LOG
    try:
        val = int(var.get())
        if val not in range(lb, ub):
            Error = f"{var}: Invalid Input\n"
            error_log.append(Error)
            is_valid = False
            return None
        else:
            print(f"{var}: Valid")
            return val
    except ValueError:
        Error = "Only numbers allowed\n"
        error_log.append(Error)
        is_valid = False
        return None


def get_values():
    age = check_valid(input_age, 0, 101)
    sex = check_valid(input_sex, 0, 2)
    (
        int(input_sex.get()))


if sex not in [0, 1]:
    Error = "Sex: only 0 and 1 are allowed.\n"
    errors.append(Error)
    is_valid = False

cp = int(input_cp.get())
if cp not in [1, 2, 3, 4]:
    Error = "CP: Invalid CP\n"
    errors.append(Error)
    is_valid = False

try:
    trestbps = int(input_trestbps.get())
    if trestbps <= 0 or trestbps >= 250:
        Error = "Trestbps: Extreme val Trestbps\n"
        errors.append(Error)
except ValueError:
    Error = "Trestbps: Invalid Trestbps\n"
    errors.append(Error)
    is_valid = False

fbs = input_fbs.get()
if fbs not in ["0", "1"]:
    Error = "FBS: Invalid FBS\n"
    errors.append(Error)
    is_valid = False

restecg = input_restecg.get()
if restecg not in ["0", "1", "2"]:
    Error = "Resting ECG: Invalid Resting ECG\n"
    errors.append(Error)

try:
    thalach = int(input_thalach.get())
    if thalach <= 40 or thalach >= 252:
        Error = "Thalach: Invalid Thalach\n"
        errors.append(Error)
except ValueError:
    Error = "Only numbers allowed\n"
    errors.append(Error)
    is_valid = False

exang = input_exang.get()
if exang not in ["0", "1"]:
    Error = "Exercise induced Angina: Invalid input only 0 or 1\n"
oldpeak = float(input_oldpeak.get())

predict_button = tk.Button(window, text="Predict", bg="blue", fg="white",
                           font=("Helvetica", 14, "bold"), width=20, command=get_values)

predict_button.grid(row=8, column=0, columnspan=4, pady=30)
window.mainloop()

# Save your history