from collections import Counter
specializations = {
    "Artificial Intelligence": ["math", "logic", "interested in machines that learn"],
    "Cybersecurity": ["networking", "security", "problem-solving"],
    "Web Development": ["creative", "design", "frontend/backend"],
    "Embedded Systems": ["hardware", "electronics", "low-level programming"],
    "Networking": ["networking", "infrastructure", "communication systems"],
    "Data Science": ["math", "statistics", "data analysis"]
}
print("Welcome to the Career Selection Expert System")
print("You can answer freely (e.g., 'yes, I love it', 'a bit', 'not really', or describe your interest).")
questions = {
    "math": "Do you enjoy mathematics and logic?",
    "security": "Are you interested in cybersecurity or system protection?",
    "creative": "Do you enjoy designing websites or user interfaces?",
    "hardware": "Are you interested in working with electronics or hardware devices?",
    "networking": "Do you enjoy understanding how networks and the internet work?",
    "data": "Do you like working with data and statistics?",
    "ai": "Are you curious about machines that can learn or make decisions?"
}
keywords = {
    "math": ["math", "logic", "calculation", "algebra"],
    "security": ["security", "cyber", "hacking", "protection"],
    "creative": ["design", "creative", "interface", "frontend", "web"],
    "hardware": ["hardware", "electronics", "circuits", "devices"],
    "networking": ["network", "internet", "communication", "infrastructure"],
    "data": ["data", "statistics", "analysis", "numbers"],
    "ai": ["ai", "intelligence", "learn", "decision", "machine"]
}
traits = []
for trait_key, question in questions.items():
    response = input(question + " (yes/no) ").lower()
    if response.startswith("y"):  
        if trait_key == "math":
            traits.extend(["math", "logic"])
        elif trait_key == "security":
            traits.extend(["security", "problem-solving"])
        elif trait_key == "creative":
            traits.extend(["creative", "design", "frontend/backend"])
        elif trait_key == "hardware":
            traits.extend(["hardware", "electronics", "low-level programming"])
        elif trait_key == "networking":
            traits.extend(["networking", "infrastructure", "communication systems"])
        elif trait_key == "data":
            traits.extend(["statistics", "data analysis"])
        elif trait_key == "ai":
            traits.append("interested in machines that learn")
match_scores = {}
for field, field_traits in specializations.items():
    score = sum(1 for trait in field_traits if trait in traits)
    match_scores[field] = score

best_match = max(match_scores, key=match_scores.get)
if match_scores[best_match] > 0:
    print(f"\nBased on your interests, a good specialization is: {best_match}")
else:
    print("No perfect match found, but explore more based on your favorite subjects and projects.")

