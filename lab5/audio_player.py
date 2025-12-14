from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class AudioPlayer:
    """
    Класс-обёртка над QMediaPlayer для управления воспроизведением аудио.
    """

    def __init__(self) -> None:
        """
        Инициализация аудиоплеера.
        """
        self._player = QMediaPlayer()
        self._current_path: str | None = None

    def load(self, file_path: str) -> None:
        """
        Загружает аудиофайл в плеер.

        :param file_path: Путь к mp3 файлу.
        """
        self.stop()
        self._current_path = file_path
        media = QMediaContent(QUrl.fromLocalFile(file_path))
        self._player.setMedia(media)

    def play(self) -> None:
        """
        Запускает воспроизведение.
        """
        if self._current_path is not None:
            self._player.play()

    def pause(self) -> None:
        """
        Ставит воспроизведение на паузу.
        """
        self._player.pause()

    def stop(self) -> None:
        """
        Полностью останавливает воспроизведение.
        """
        self._player.stop()

    def is_playing(self) -> bool:
        """
        Проверяет, воспроизводится ли аудио.

        :return: True, если аудио воспроизводится.
        """
        return self._player.state() == QMediaPlayer.PlayingState
