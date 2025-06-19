def calculate_ald(lectures): # Average Lecture Duration
    total_duration = sum(duration for _, duration in lectures)
    return total_duration / len(lectures) if lectures else 0