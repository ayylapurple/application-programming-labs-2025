import os
import matplotlib.pyplot as plt
import pandas as pd


def plot_histogram(df: pd.DataFrame, output_path: str) -> None:
    """
    Строит гистограмму значений amplitude_ratio и сохраняет в файл.

    :param df: DataFrame со значениями.
    :param output_path: Путь для сохранения изображения.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.hist(df["amplitude_ratio"], bins=10, edgecolor='black')

    plt.title("Гистограмма распределения amplitude_ratio")
    plt.xlabel("amplitude_ratio")
    plt.ylabel("Количество файлов")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
