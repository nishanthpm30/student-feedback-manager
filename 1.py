def collect_feedback():
    feedback = input("Enter your feedback: ")
    score = int(input("Rate us (1 to 10): "))
    return {"feedback": feedback, "score": score}

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)