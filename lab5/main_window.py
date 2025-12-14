import os

from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog
)

from audio_iterator import AudioIterator
from audio_player import AudioPlayer


class MainWindow(QMainWindow):
    """
    Главное окно приложения для просмотра аудиодатасета.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Audio Dataset Viewer")
        self.setGeometry(300, 200, 500, 300)

        self.iterator: AudioIterator | None = None
        self.player = AudioPlayer()

        self._setup_ui()
        self._apply_styles()

        self.player._player.durationChanged.connect(self._update_duration)

    def _setup_ui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.track_label = QLabel("Трек не выбран")
        self.duration_label = QLabel("Длительность: --:--")

        self.play_button = QPushButton("▶ Воспроизведение")
        self.next_button = QPushButton("⏭ Следующий")
        self.folder_button = QPushButton("📂 Выбрать папку")

        self.play_button.clicked.connect(self.toggle_play)
        self.next_button.clicked.connect(self.next_track)
        self.folder_button.clicked.connect(self.select_folder)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.play_button)
        buttons_layout.addWidget(self.next_button)

        layout = QVBoxLayout()
        layout.addWidget(self.track_label)
        layout.addWidget(self.duration_label)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.folder_button)

        central_widget.setLayout(layout)

    def _apply_styles(self) -> None:
        self.setStyleSheet("""
            QMainWindow { background-color: #2b1b3d; }
            QLabel { color: #e6d9ff; font-size: 14px; }
            QPushButton {
                background-color: #6a0dad;
                color: white;
                border-radius: 6px;
                padding: 8px;
            }
        """)

    def select_folder(self) -> None:
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку с аудио")
        if not folder:
            return

        self.iterator = AudioIterator(folder)
        self.next_track()

    def next_track(self) -> None:
        if self.iterator is None:
            return

        self.player.stop()

        path = self.iterator.next()
        if path is None:
            self.track_label.setText("Конец датасета")
            return

        self.player.load(path)
        self.player.play()

        self.track_label.setText(f"Трек: {os.path.basename(path)}")
        self.duration_label.setText("Длительность: загружается...")
        self.play_button.setText("⏸ Пауза")

    def toggle_play(self) -> None:
        if self.player.is_playing():
            self.player.stop()
            self.play_button.setText("▶ Воспроизведение")
        else:
            self.player.play()
            self.play_button.setText("⏸ Пауза")

    def _update_duration(self, duration_ms: int) -> None:
        minutes = duration_ms // 60000
        seconds = (duration_ms // 1000) % 60
        self.duration_label.setText(f"Длительность: {minutes:02d}:{seconds:02d}")
