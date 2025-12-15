from presidio_anonymizer.operators import (
    Redact,
    Replace,
    Mask,
    Initial,
    # ...other operators
)

OPERATORS = {
    "redact": Redact,
    "replace": Replace,
    "mask": Mask,
    "initial": Initial,
    # ...other operators
}
