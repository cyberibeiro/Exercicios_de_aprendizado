from exercicios_de_aprendizado.largest_productin_a_grid import (
    largest_product_in_grid,
    read_grid_from_file,
)


def test_read_grid_from_file() -> None:
    grid = read_grid_from_file("../grid.txt")

    assert len(grid) == 20
    assert len(grid[0]) == 20
    assert grid[0][0] == 8
    assert grid[6][8] == 26


def test_largest_product_in_grid() -> None:
    grid = read_grid_from_file("../grid.txt")
    result = largest_product_in_grid(grid)

    assert result == 70_600_674
