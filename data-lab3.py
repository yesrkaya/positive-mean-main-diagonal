def positive_mean(matrix):
    n = len(matrix)
    mean_list = []

    for column in range(n):
        positives = [matrix[i][column] for i in range(n) if matrix[i][column] > 0]
        if positives:
            mean = sum(positives) / len(positives)
            mean_list.append(mean)
        else:
            mean_list.append(0)

    return mean_list

def main():
    n = int(input("Enter the size of the matrix: "))

    matrix = []
    for _ in range(n):
        row = []
        for _ in range(n):
            element = float(input("Enter an element: "))
            row.append(element)
        matrix.append(row)

    mean_list = positive_mean(matrix)
    main_diagonal = [mean_list[i] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                print(main_diagonal[i], end=" ")
            else:
                print(matrix[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
