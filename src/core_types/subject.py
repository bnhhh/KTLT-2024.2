# subject.py
class Subject:
    def __init__(self, subject_code, subject_name, credits):
        self.subject_code = subject_code
        self.subject_name = subject_name
        self.credits = int(credits)

    def to_dict(self):
        return {
            'subject_code': self.subject_code,
            'subject_name': self.subject_name,
            'credits': self.credits
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['subject_code'], data['subject_name'], data['credits'])