from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    def __init__(self):
        super().__init__()

    def operator_name(self):
        return "initial"

    def operator_type(self):
        return OperatorType.Anonymize

    def validate(self, params=None):
        # No parameters to validate
        return True

    def operate(self, text: str, params=None):
        # Transform "John Smith" -> "J. S."
        parts = text.split()
        initials = [p[0].upper() + "." for p in parts if p]
        return " ".join(initials)
