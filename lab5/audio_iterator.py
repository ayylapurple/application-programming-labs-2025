import os

from typing import List


class AudioIterator:
    """
    Итератор для перебора аудиофайлов (.mp3) в заданной папке.
    """

    def __init__(self, folder: str) -> None:
        """
        Инициализация итератора.

        :param folder: Путь к папке с аудиофайлами.
        :raises FileNotFoundError: если папка не существует.
        :raises ValueError: если в папке нет mp3 файлов.
        """
        if not os.path.isdir(folder):
            raise FileNotFoundError(f"Папка не найдена: {folder}")

        self._files: List[str] = self._scan_folder(folder)
        self._index: int = 0

        if not self._files:
            raise ValueError("В папке нет mp3 файлов")

    @staticmethod
    def _scan_folder(folder: str) -> List[str]:
        """
        Сканирует папку и возвращает список mp3 файлов.

        :param folder: Путь к папке.
        :return: Список путей к mp3 файлам.
        """
        files = [
            os.path.join(folder, f)
            for f in sorted(os.listdir(folder))
            if f.lower().endswith(".mp3")
        ]
        return files

    def next(self) -> str:
        """
        Возвращает путь к следующему аудиофайлу.

        При достижении конца списка начинает с начала.

        :return: Путь к mp3 файлу.
        """
        file_path = self._files[self._index]
        self._index = (self._index + 1) % len(self._files)
        return file_path

    def reset(self) -> None:
        """
        Сбрасывает итератор в начальное состояние.
        """
        self._index = 0

    def count(self) -> int:
        """
        Возвращает количество аудиофайлов.

        :return: Количество файлов.
        """
        return len(self._files)
    