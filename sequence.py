def sequence(n):
    """Програма, которая выводит n первых элементов
        последовательности 122333444455555…
        (число повторяется столько раз, чему оно равно).
    """
    title = []
    for num in range(1, int(n + 1)):
        for _ in range(num):  # повторяем num раз
            title.append(num)
    return title


print(sequence(5))
