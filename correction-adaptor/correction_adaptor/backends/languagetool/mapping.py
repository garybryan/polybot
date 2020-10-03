from ...models import CorrectedMessage, Correction, Message, Rule
from .models import LanguageToolCorrectedMessage, LanguageToolMessage


def map_message(message: Message) -> LanguageToolMessage:
    return LanguageToolMessage(
        text=message.text,
        language=message.language,
        motherTongue=message.user_language,
    )


def map_corrected_message(
    cm: LanguageToolCorrectedMessage,
) -> CorrectedMessage:
    return CorrectedMessage(
        text=cm.text,
        language=cm.language,
        corrections=[
            Correction(
                message=m.message,
                short_message=m.shortMessage,
                suggestions=m.replacements,
                offset=m.offset,
                length=m.length,
                context=m.context,
                rule=Rule(
                    id=m.rule.id,
                    description=m.rule.description,
                    type=m.rule.issueType,
                    urls=m.rule.urls,
                    category=m.rule.category,
                ),
                sentence=m.sentence,
            )
            for m in cm.matches
        ],
    )
