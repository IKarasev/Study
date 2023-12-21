"""
Кодирование и декодирование методом перестановки
Варинат 4
Таблица 3, задание 2
"""

import argparse


class CypherTransposition:
    """
    Предоставляет методы кодирования и декодирования
    """

    # block = [0, 1, 2, 3, 4]
    _trans = [4, 3, 0, 1, 2]
    _block_len = 5

    @classmethod
    def _pad_text(cls, text: str) -> str:
        """Если длинна текста не кратна _block_len,
        то добавляет необходимое колличество пробелов,
        что бы строка была кратной
        """

        pad = cls._block_len - len(text) % cls._block_len
        text = text if pad == 5 else text + " " * pad
        return text

    @classmethod
    def encode(cls, text: str) -> str:
        """Закодирование текста"""

        text = cls._pad_text(text)
        encripted = ""
        for i in range(0, len(text), cls._block_len):
            for j in range(0, cls._block_len):
                encripted += text[i + cls._trans[j]]
        return encripted.rstrip()

    @classmethod
    def decode(cls, text: str) -> str:
        """Декодирование текста"""

        text = cls._pad_text(text)
        decripted = ""
        for i in range(0, len(text), cls._block_len):
            block = [""] * 5
            for j in range(0, cls._block_len):
                block[cls._trans[j]] = text[i + j]
            decripted += "".join(block)
        return decripted.rstrip()


parser = argparse.ArgumentParser(
    prog="Кодировани и декодирование методом подстановки",
    description="По умолчанию кодирует заданный текст, для декодирования используйте ключ [-d]",
)
parser.add_argument(
    "text",
    type=str,
    help="Входной текст",
)

parser.add_argument(
    "-d",
    "--decrypt",
    action="store_true",
    default=False,
    help="Декодировать текст",
)

args = parser.parse_args()

if args.decrypt:
    print(f'"{CypherTransposition.decode(args.text)}"')
else:
    print(f'"{CypherTransposition.encode(args.text)}"')

# Пример ввода: Hello World:
# encripted:
#   "olHellr Wo  d"
# decripted:
#   "Hello World"

