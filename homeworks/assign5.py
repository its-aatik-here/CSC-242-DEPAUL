class excessiveBrushworkException(Exception):
    def __init__(self, message ,num_strokes):
        self.message = message
        self.num_strokes = num_strokes
        self.args = (f"{message} {num_strokes}",)

class poorCompositionException(Exception):
    def __init__(self, message, follows_rule_of_thirds):
        self.message = message
        self.follows_rule_of_thirds = follows_rule_of_thirds
        self.args = (f"{message} {follows_rule_of_thirds}",)

class UnderwhelmingSubjectException(Exception):
    def __init__(self, message, subjects):
        self.message = message
        self.subjects = subjects
        self.args = (f"{message} {', '.join(subjects)}",)


class BrushStrokeChecker():
    def __init__(self,threshold):
        self.threshold = threshold
    def check_brushstrokes(self,painting_name,num_strokes):
        if num_strokes > self.threshold:
            raise excessiveBrushworkException('The number of brushstrokes is ', num_strokes)
        else:
            return f"The painting {painting_name} has an acceptable number of brushstrokes."
        

def silly(n):
    if n == 0:
        return
    else:
        print("*", end=" ")
        silly(n-1)
        print("!", end=" ")


def tough(indent, num_stars):
    if num_stars == 0:
        return
    else:
        print(" " * indent + "*" * num_stars)
        tough(indent + 1, num_stars // 2)
        tough(indent, num_stars)