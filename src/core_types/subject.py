class Subject:
    def __init__(self, subject_code, subject_name, credits):
        if not subject_code or not subject_code.strip():
            raise ValueError("Mã môn học không được để trống")
        if not subject_name or not subject_name.strip():
            raise ValueError("Tên môn học không được để trống")
        try:
            credits = int(credits)
            if credits <= 0:
                raise ValueError("Số tín chỉ phải là số nguyên dương")
        except ValueError as e:
            if "số nguyên dương" in str(e):
                raise e
            raise ValueError("Số tín chỉ phải là số nguyên")
            
        self.subject_code = subject_code.strip()
        self.subject_name = subject_name.strip()
        self.credits = credits

    def to_dict(self):
        return {
            'subject_code': self.subject_code,
            'subject_name': self.subject_name,
            'credits': self.credits
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['subject_code'], data['subject_name'], data['credits'])