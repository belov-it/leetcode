
def solutionBook(n, target, lst):
    l = 0
    r = 0  # указатели в начале
    count = 0  # здесь будет ответ
    curSum = 0  # текущая сумма

    for r in range(n):
        curSum += lst[r]
        while (curSum > target):
            # пока отрезок "плохой"
            curSum -= lst[l]  # вычитаем крайний левый из отрезка
            l += 1  # передвигаем левый указатель
        # теперь когда отрезок хороший, обновляем ответ
        count = max(count, r - l + 1)
    return count


n, t = map(int, input().split())

a = []
for i in list(input().split()):
    a.append(int(i))

print(solutionBook(n, t, a))


def cefa_and_company(n, d, arr):
    l = 0
    r = 0
    curSum = 0
    for r in range(n):
        curSum += arr[r, 0]
        while (arr[r, 1] - arr[l, 1] > d):
            curSum -= arr[l, 1]
            l += 1
