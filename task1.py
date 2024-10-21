import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізуємо мін-купу з довжинами кабелів
    heapq.heapify(cables)
    total_cost = 0

    # Поки в купі більше ніж один кабель
    while len(cables) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Витрати на з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо з'єднаний кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Тестуємо функцію
cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print(f"Мінімальні витрати на з'єднання кабелів: {result}")
