# Project Euler: https://projecteuler.net/problem=11


def read_grid_from_file(file_path: str) -> list[list[int]]:
    """
    Lê um arquivo de texto contendo uma matriz de números inteiros
    separados por espaço e retorna uma lista de listas de inteiros.
    """
    grid: list[list[int]] = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            grid.append([int(number) for number in line.split()])

    return grid


def largest_product_in_grid(grid: list[list[int]], sequence_length: int = 4) -> int:
    """
    Retorna o maior produto de 'sequence_length' números adjacentes
    na mesma direção (horizontal, vertical ou diagonal) dentro da matriz.
    """
    total_rows: int = len(grid)
    total_columns: int = len(grid[0])
    max_product: int = 0

    for row_index in range(total_rows):
        for column_index in range(total_columns):

            # Horizontal →
            if column_index + sequence_length <= total_columns:
                product = 1
                for offset in range(sequence_length):
                    product *= grid[row_index][column_index + offset]
                max_product = max(max_product, product)

            # Vertical ↓
            if row_index + sequence_length <= total_rows:
                product = 1
                for offset in range(sequence_length):
                    product *= grid[row_index + offset][column_index]
                max_product = max(max_product, product)

            # Diagonal ↘
            if (
                row_index + sequence_length <= total_rows
                and column_index + sequence_length <= total_columns
            ):
                product = 1
                for offset in range(sequence_length):
                    product *= grid[row_index + offset][column_index + offset]
                max_product = max(max_product, product)

            # Diagonal ↙
            if (
                row_index + sequence_length <= total_rows
                and column_index - sequence_length + 1 >= 0
            ):
                product = 1
                for offset in range(sequence_length):
                    product *= grid[row_index + offset][column_index - offset]
                max_product = max(max_product, product)

    return max_product