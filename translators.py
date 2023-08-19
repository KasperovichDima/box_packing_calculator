from project_typing import Language, Position


class BaseTranslator:

    _dictionary: dict[str, str]

    def __call__(self, position: Position) -> str:
        try:
            english_name = position.name.replace('_', ' ')
            words = english_name.split()
            return f'{self._dictionary[words[0]]} '\
                   f'{self._dictionary[words[1]]}'
        except AttributeError:
            return english_name


class RU_Translator(BaseTranslator):

    _dictionary: dict[str, str] = dict(
        EDGE='БОКОМ',
        FLAT='ЛЕЖА',
        UP='СТОЯ',
        ACROSS='ПОПЕРЕК',
        ALONG='ВДОЛЬ',
    )


translators: dict[Language, BaseTranslator] = {
    Language.en: BaseTranslator(),
    Language.ru: RU_Translator(),
}
