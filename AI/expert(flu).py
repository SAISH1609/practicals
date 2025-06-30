def ask_flu_symptoms():
    symptoms = []

    print("Welcome to the Flu Diagnosis Expert System!")
    print("Please answer the following questions to help identify your condition:\n")

    print("1. Do you have a fever? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Fever")
        print("   - Is it a mild or high fever? (mild/high)")
        fever_type = input().lower()
        if fever_type == "mild":
            symptoms.append("Mild fever")
        elif fever_type == "high":
            symptoms.append("High fever")

    print("2. Are you experiencing a cough? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Cough")
        print("   - Is it dry or with phlegm? (dry/wet)")
        cough_type = input().lower()
        if cough_type == "dry":
            symptoms.append("Dry cough")
        elif cough_type == "wet":
            symptoms.append("Wet cough")

    print("3. Do you have a sore throat? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Sore throat")

    print("4. Are you experiencing body aches or fatigue? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Body aches or fatigue")

    print("5. Do you have a runny or blocked nose? (yes/no)")
    answer = input().lower()
    if answer == "yes":
        symptoms.append("Nasal congestion")
        print("   - Is it mostly runny or blocked? (runny/blocked)")
        nose_type = input().lower()
        if nose_type == "runny":
            symptoms.append("Runny nose")
        elif nose_type == "blocked":
            symptoms.append("Blocked nose")

    return symptoms

def diagnose_flu_conditions(symptoms):
    remedies = []

    if "Fever" in symptoms:
        if "High fever" in symptoms:
            remedies.append("Take paracetamol and stay hydrated. Consult a doctor if fever persists for more than 3 days.")
        elif "Mild fever" in symptoms:
            remedies.append("Rest and drink warm fluids. Monitor temperature regularly.")

    if "Dry cough" in symptoms:
        remedies.append("Use a humidifier and take warm honey-lemon water to soothe the throat.")
    elif "Wet cough" in symptoms:
        remedies.append("Expectorants may help clear mucus. Avoid dairy and cold drinks.")

    if "Sore throat" in symptoms:
        remedies.append("Gargle with warm salt water and avoid spicy/acidic foods.")

    if "Body aches or fatigue" in symptoms:
        remedies.append("Take adequate rest and use over-the-counter pain relievers like ibuprofen if needed.")

    if "Runny nose" in symptoms:
        remedies.append("Use a saline nasal spray and antihistamines if caused by allergies.")
    elif "Blocked nose" in symptoms:
        remedies.append("Inhale steam twice daily and use decongestant drops if severe.")

    if len(remedies) == 0:
        remedies.append("No specific flu symptoms detected. If you're feeling unwell, consider consulting a healthcare provider.")

    return remedies

# Main execution
symptoms = ask_flu_symptoms()
remedies = diagnose_flu_conditions(symptoms)

print("\nPossible remedies and advice based on your symptoms:")
for remedy in remedies:
    print("-", remedy)