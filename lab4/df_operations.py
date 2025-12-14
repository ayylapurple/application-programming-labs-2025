import pandas as pd


def sort_by_ratio(df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
    """
    Сортирует датафрейм по колонке amplitude_ratio.

    :param df: Исходный DataFrame.
    :param ascending: True — по возрастанию, False — по убыванию.
    :return: Отсортированный DataFrame.
    """
    return df.sort_values(by="amplitude_ratio", ascending=ascending)


def filter_by_ratio(df: pd.DataFrame, min_val: float, max_val: float) -> pd.DataFrame:
    """
    Фильтрует строки по диапазону значения amplitude_ratio.

    :param df: Исходный DataFrame.
    :param min_val: Нижняя граница.
    :param max_val: Верхняя граница.
    :return: Отфильтрованный DataFrame.
    """
    return df[(df["amplitude_ratio"] >= min_val) & (df["amplitude_ratio"] <= max_val)]
