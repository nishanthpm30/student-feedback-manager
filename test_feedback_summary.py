import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from feedback_summary import summarize_feedback

def test_summarize_feedback():
    sample_data = [
        {"name": "A", "subject": "Math", "score": 90, "grade": "A"},
        {"name": "B", "subject": "Eng", "score": 85, "grade": "B"},
        {"name": "C", "subject": "Sci", "score": 95, "grade": "A"},
        {"name": "D", "subject": "Hist", "score": 75, "grade": "C"},
        {"name": "E", "subject": "Math", "score": 88, "grade": "B"}
    ]

    result = summarize_feedback(sample_data)
    assert len(result["top_scores"]) == 3
    assert result["grade_counts"]["A"] == 2
    assert result["grade_counts"]["B"] == 2
    assert result["grade_counts"]["C"] == 1
