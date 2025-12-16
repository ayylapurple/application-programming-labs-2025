import os

import pandas as pd
import numpy as np
import soundfile as sf

from typing import List, Tuple


def get_file_paths(folder: str) -> List[Tuple[str, str]]:
    """
    Получает абсолютные и относительные пути ко всем MP3-файлам в папке.

    :param folder: Папка с аудиофайлами.
    :return: Список кортежей (absolute_path, relative_path).
    """
    paths = []
    for file in os.listdir(folder):
        if file.lower().endswith(".mp3"):
            rel = os.path.join(folder, file)
            abs_path = os.path.abspath(rel)
            paths.append((abs_path, rel))
    return paths


def read_audio_mono(path: str) -> np.ndarray:
    """
    Считывает аудио и приводит к моно.

    :param path: Путь к аудиофайлу.
    :return: Моно-аудио в виде массива numpy.
    """
    audio, _ = sf.read(path)

    if audio.ndim == 2:
        audio = audio.mean(axis=1)

    return audio


def compute_amplitude_ratio(audio: np.ndarray, threshold: float) -> float:
    """
    Считает отношение количества сэмплов с амплитудой > threshold
    к общему количеству.

    :param audio: Массив аудиосэмплов.
    :param threshold: Порог амплитуды (0.0–1.0).
    :return: Значение отношения.
    """
    if len(audio) == 0:
        return 0.0

    count_high = np.sum(np.abs(audio) > threshold)
    return count_high / len(audio)


def create_dataframe(folder: str, threshold: float) -> pd.DataFrame:
    """
    Формирует DataFrame со столбцами:
    - absolute_path
    - relative_path
    - amplitude_ratio

    :param folder: Папка с mp3 файлами.
    :param threshold: Порог амплитуды.
    :return: Готовый DataFrame.
    """
    records = []

    for abs_path, rel_path in get_file_paths(folder):
        try:
            audio = read_audio_mono(abs_path)
            ratio = compute_amplitude_ratio(audio, threshold)
        except Exception as exc:
            print(f"Ошибка чтения файла {abs_path}: {exc}")
            ratio = None

        records.append({
            "absolute_path": abs_path,
            "relative_path": rel_path,
            "amplitude_ratio": ratio
        })

    return pd.DataFrame(records)
