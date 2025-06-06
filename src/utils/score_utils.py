def validate_score(score_str):
    """Kiểm tra tính hợp lệ của điểm số"""
    if not score_str or not score_str.strip():
        return False, "Điểm không được để trống"
    try:
        score = float(score_str)
        if score < 0 or score > 10:
            return False, "Điểm phải từ 0 đến 10"
        return True, ""
    except ValueError:
        return False, "Điểm phải là số"

def calculate_final_score(attendance, midterm, final):
    """Tính điểm tổng kết dựa trên các thành phần điểm
    Công thức: (Điểm chuyên cần * 0.4 + Điểm giữa kỳ * 0.6) * 0.5 + Điểm cuối kỳ * 0.5
    """
    return (attendance * 0.4 + midterm * 0.6) * 0.5 + final * 0.5

def get_grade(score):
    """Xác định xếp loại dựa trên điểm số"""
    if score >= 9.5:
        return "A+"
    elif score >= 8.5:
        return "A"
    elif score >= 8.0:
        return "B+"
    elif score >= 7.0:
        return "B"
    elif score >= 6.5:
        return "C+"
    elif score >= 5.5:
        return "C"
    elif score >= 5.0:
        return "D+"
    elif score >= 4.0:
        return "D"
    else:
        return "F"

def calculate_gpa(scores, subject_credits):
    """Tính điểm trung bình tích lũy dựa trên điểm số và số tín chỉ"""
    total_points = 0
    total_credits = 0
    
    for subject_code, score in scores.items():
        if subject_code in subject_credits:
            credits = subject_credits[subject_code]
            total_points += score * credits
            total_credits += credits
            
    return total_points / total_credits if total_credits > 0 else 0 