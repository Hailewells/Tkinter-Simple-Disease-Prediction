from tkinter import *

# Define a list of diseases and their corresponding symptoms
diseases = [
    {'disease': 'Influenza', 'symptoms': ['fever', 'cough', 'sore throat', 'body aches']},
    {'disease': 'COVID-19', 'symptoms': ['fever', 'cough', 'shortness of breath', 'loss of taste or smell']},
    {'disease': 'Allergic rhinitis', 'symptoms': ['sneezing', 'runny nose', 'itchy eyes']},
    {'disease': 'Bronchitis', 'symptoms': ['cough', 'mucus', 'chest discomfort']},
    {'disease': 'Pneumonia', 'symptoms': ['fever', 'cough', 'shortness of breath', 'chest pain']},
]

# Define the symptoms
symptoms = ['fever', 'cough', 'sore throat', 'shortness of breath', 'loss of taste or smell', 'sneezing', 'runny nose', 'itchy eyes', 'mucus', 'chest discomfort', 'chest pain']

# Create the main window
window = Tk()
window.title("Disease Predictor")

# Create a frame for the selector buttons
frame = Frame(window)
frame.pack()

# Create the selector buttons
selector_buttons = []
for symptom in symptoms:
    selector_button = Button(frame, text=symptom, bg='cyan', activebackground='green', activeforeground='black', width=15, height=10)
    selector_button.pack(side=LEFT)
    selector_buttons.append(selector_button)

# Create a button to predict the disease
def predict_disease():
    # Get the selected symptoms
    selected_symptoms = [selector_button.cget('text') for selector_button in selector_buttons if selector_button['bg'] == 'green']

    # Predict the disease
    predicted_disease = None
    for disease in diseases:
        if all(symptom in disease['symptoms'] for symptom in selected_symptoms):
            predicted_disease = disease['disease']
            break

    # Print the predicted disease
    if predicted_disease is not None:
        print(f"Based on the selected symptoms, the predicted disease is: {predicted_disease}")
    else:
        print("No disease was found that matches all of the selected symptoms.")

# Toggle the selector buttons when clicked
def toggle_selector_button(button):
    if button['bg'] == 'green':
        button.config(bg='green')
    else:
        button.config(bg='green')

for selector_button in selector_buttons:
    selector_button.config(command=lambda b=selector_button: toggle_selector_button(b))

button = Button(window, text="Predict Disease", command=predict_disease)
button.pack()

# Run the main loop
window.mainloop()
