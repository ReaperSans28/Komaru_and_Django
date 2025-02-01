from django.core.exceptions import ValidationError
from config.settings import INVALID_WORDS


def validate_disallowed_words(value):
    if any(disallowed_word in value.lower() for disallowed_word in INVALID_WORDS):
        raise ValidationError("ОСУЖДАЮ.")
