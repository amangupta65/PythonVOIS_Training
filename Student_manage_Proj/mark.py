
marks_data = {}

def add_marks(roll, marks):
    marks_data[roll] = marks

def calculate_average(roll):
    m = marks_data.get(roll, [])
    if m:
        return sum(m) / len(m)
    return 0

