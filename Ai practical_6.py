def evaluate_employee(attendance, tasks_completed, communication, teamwork):
    score = 0

    # Rule-based scoring
    if attendance >= 90:
        score += 25
    elif attendance >= 75:
        score += 15
    else:
        score += 5

    if tasks_completed >= 90:
        score += 25
    elif tasks_completed >= 75:
        score += 15
    else:
        score += 5

    if communication == "excellent":
        score += 20
    elif communication == "good":
        score += 10
    else:
        score += 5

    if teamwork == "excellent":
        score += 20
    elif teamwork == "good":
        score += 10
    else:
        score += 5

    # Final Evaluation
    if score >= 80:
        evaluation = "Outstanding"
    elif score >= 60:
        evaluation = "Good"
    elif score >= 40:
        evaluation = "Satisfactory"
    else:
        evaluation = "Needs Improvement"

    return score, evaluation


def main():
    print("Welcome to the Employee Performance Evaluation Expert System\n")

    name = input("Enter Employee Name: ")
    attendance = int(input("Enter attendance percentage (0-100): "))
    tasks_completed = int(input("Enter task completion percentage (0-100): "))
    communication = input("Communication skill (excellent/good/poor): ").lower()
    teamwork = input("Teamwork skill (excellent/good/poor): ").lower()

    score, evaluation = evaluate_employee(attendance, tasks_completed, communication, teamwork)

    print("\n--- Evaluation Report ---")
    print(f"Employee: {name}")
    print(f"Score: {score}/90")
    print(f"Performance Level: {evaluation}")


if __name__ == "__main__":
    main()