import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# ---------- Load the Trained Model ----------
model = pickle.load(open("cancer_mutation.pkl", "rb"))

# ---------- Prediction Function ----------
def predict_cancer():
    try:
        # Get input values from entry fields
        features = [float(entry.get()) for entry in entries]
        features = np.array(features).reshape(1, -1)

        # Predict using model
        prediction = model.predict(features)

        # Show result
        if prediction[0] == 1:
            messagebox.showinfo("Prediction Result", "⚠️ Cancer Detected")
        else:
            messagebox.showinfo("Prediction Result", "✅ No Cancer Detected")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# ---------- GUI Design ----------
root = tk.Tk()
root.title("Cancer Prediction System")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Labels for Features (Change according to your dataset)
feature_names = ["Mean Radius", "Mean Texture", "Mean Perimeter", "Mean Area", "Mean Smoothness"]

entries = []
for i, feature in enumerate(feature_names):
    label = tk.Label(root, text=feature, font=("Arial", 12), bg="#f0f0f0")
    label.pack(pady=5)
    
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entries.append(entry)

# Predict Button
predict_btn = tk.Button(root, text="Predict", command=predict_cancer, 
                        font=("Arial", 14), bg="#4CAF50", fg="white")
predict_btn.pack(pady=20)

root.mainloop()
