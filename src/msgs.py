from typing import Any, Protocol

from project_typing import Language

import translators as t


class _Response(Protocol):
    """Response protocol."""

    lng: Language
    optymal_position: str
    product_lwh: tuple[float, float, float]
    pcs_in_row: int
    rows_in_layer: int
    layesr_in_box: int

    @property
    def total_amount(self) -> int: ...


class MsgGenerator:
    """Generates response message according to specified language."""

    _response_msgs: dict[Language, str] = {
        Language.en: 'Optimal fit: {}. '
                     'Put {} pcs in a row across the box. '
                     'Put {} rows along the box. '
                     'Put {} layers to the height of the box. '
                     'Total box loading: {} psc.',

        Language.ru: 'Оптимальная укладка: {}. '
                     'Уложите {} единиц товара в ряд поперек коробки. '
                     'Уложите {} рядов вдоль коробки. '
                     'Уложите {} слоев в высоту коробки. '
                     'Общая загрузка коробки: {} штук.'
    }

    def __init__(self, response: _Response) -> None:
        self._response = response

    def __getattr__(self, __name: str) -> Any:
        return getattr(self._response, __name)

    def get_response_msg(self) -> str:
        return self._response_msgs[self.lng].format(
            self._translator(self.optymal_position),
            self.pcs_in_row,
            self.rows_in_layer,
            self.layesr_in_box,
            self.total_amount,
        )

    @property
    def _translator(self) -> t.BaseTranslator:
        return t.translators[self.lng]
