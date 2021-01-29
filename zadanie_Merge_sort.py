# Необходимо:
# Разработать алгоритм функции Merge(A,p,q,r) на любом удобном вам языке,
# с использованием дополнительной памяти или без нее, как вам будет быстрее или удобнее в реализации.

# Задача
# Функция сортирующая массив элементов A:


a = (5,2,4,6,1,3,2,6)

def merge_mas(a):
    """
    merge_sort sorts by merge sort
    :param a:  container of elements to be sorted
    :return: container sorted in ascending order
    """

    n = len(a)
    if n < 2:
        return a

    p = merge_mas(a[:n//2])
    q = merge_mas(a[n//2:n])

    i = j = 0
    res = []
    while i < len(p) or j < len(q):
        if not i < len(p):
            res.append(q[j])
            j += 1
        elif not j < len(q):
            res.append(p[i])
            i += 1
        elif p[i] < q[j]:
            res.append(p[i])
            i += 1
        else:
            res.append(q[j])
            j += 1

    return res


if __name__ == '__main__':
    a = (5, 2, 4, 6, 1, 3, 2, 6)
    a = merge_mas(a)
    print(a)

