from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    def __init__(self):
        super().__init__()

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params: dict) -> None:
        """No special params needed for now."""
        pass

    def operate(self, text: str, params: dict = None) -> str:
        # Minimal implementation: just return the original text
        return text
