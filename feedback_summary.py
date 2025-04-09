def summarize_feedback(feedback_list):
    if not feedback_list:
        return {"top_scores": [], "grade_counts": {}}

    sorted_feedback = sorted(feedback_list, key=lambda x: x['score'], reverse=True)
    top_scores = sorted_feedback[:3]

    grade_counts = {}
    for entry in feedback_list:
        grade = entry.get('grade', 'Ungraded')
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    return {
        "top_scores": top_scores,
        "grade_counts": grade_counts
    }
