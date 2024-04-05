def solution(n, works):
    if sum(works) <= n:
        return 0

    works.sort(reverse=True)

    while n > 0:
        max_work = works[0]
        if max_work == 0:
            break
        for index in range(len(works)):
            if works[index] < max_work:
                break
            works[index] -= 1
            n -= 1
            if n == 0:
                break

    return sum(work**2 for work in works)
