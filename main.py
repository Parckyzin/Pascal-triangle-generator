def pascal_triangle(n: int) -> None:
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    max_num = max(max(row) for row in triangle)
    max_width = len(str(max_num))

    for i in range(n):
        print(" " * (n - i - 1) * max_width, end="")
        for j in range(i + 1):
            print(f"{triangle[i][j]:{max_width}}", end=" " * max_width)
        print()


if __name__ == "__main__":
    int_input = int(input("Type an integer number: "))
    pascal_triangle(int_input)


 
