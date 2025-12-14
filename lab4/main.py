import argparse
import os
from data_processing import create_dataframe
from df_operations import sort_by_ratio, filter_by_ratio
from plotting import plot_histogram


def main() -> None:
    """
    Точка входа для лабораторной работы №4.
    """
    parser = argparse.ArgumentParser(description="Анализ аудиофайлов через pandas")

    parser.add_argument(
        "-f", "--folder",
        required=True,
        help="Папка с mp3 файлами"
    )

    parser.add_argument(
        "-t", "--threshold",
        type=float,
        required=True,
        help="Порог амплитуды (0.0–1.0)"
    )

    args = parser.parse_args()

    df = create_dataframe(args.folder, args.threshold)

    os.makedirs("results", exist_ok=True)

    df_sorted = sort_by_ratio(df)

    csv_path = "results/data.csv"
    df_sorted.to_csv(csv_path, index=False)
    print(f"DataFrame сохранён в {csv_path}")

    plot_histogram(df_sorted, "results/hist.png")
    print("Гистограмма сохранена в results/hist.png")


if __name__ == "__main__":
    main()
