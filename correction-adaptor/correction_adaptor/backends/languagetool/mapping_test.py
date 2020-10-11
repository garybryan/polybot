from ...models import CorrectedMessage, Correction, Message, Context, Rule, Suggestion
from .models import (
    LanguageToolCorrectedMessage,
    LanguageToolLanguage,
    LanguageToolMessage,
    LanguageToolRule,
    Match,
    Replacement,
    URL,
)
from .mapping import map_corrected_message, map_message


def test_map_message():
    kwargs = {
        "text": "test",
        "language": "fr",
    }
    message = Message(**kwargs, user_language="en-GB")
    assert map_message(message) == LanguageToolMessage(**kwargs, motherTongue="en-GB")


def test_map_corrected_message():
    language = "fr"
    text = "Ça vaa. Et toi ?"
    message = "Faute de frappe possible trouvée."
    short_message = "Faute de frappe"
    replacements = [
        Replacement(value="va"),
        Replacement(value="va a", shortDescription="Separate words"),
    ]
    offset = 3
    length = 3
    rule = LanguageToolRule(
        id="FR_SPELLING_RULE",
        description="Faute de frappe possible",
        issueType="misspelling",
        category={"id": "TYPOS", "name": "Faute de frappe possible"},
        urls=[URL(value="http://www.example.com")],
    )
    context = Context(
        text=text,
        offset=offset,
        length=length,
    )
    sentence = "Ça vaa."

    corrected_message = LanguageToolCorrectedMessage(
        language=LanguageToolLanguage(code=language),
        text=text,
        matches=[
            Match(
                message=message,
                shortMessage=short_message,
                replacements=replacements,
                offset=offset,
                length=length,
                context=context,
                rule=rule,
                sentence=sentence,
            )
        ],
    )

    expected = CorrectedMessage(
        language=language,
        corrections=[
            Correction(
                message=message,
                short_message=short_message,
                suggestions=[
                    Suggestion(value=r.value, short_description=r.shortDescription)
                    for r in replacements
                ],
                offset=offset,
                length=length,
                context=context,
                rule=Rule(
                    id=rule.id,
                    description=rule.description,
                    type=rule.issueType,
                    urls=[rule.urls[0].value],
                    category=rule.category,
                ),
                sentence=sentence,
            )
        ],
    )

    assert map_corrected_message(corrected_message) == expected
