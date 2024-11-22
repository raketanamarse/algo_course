from datetime import datetime, timedelta
from collections import Counter

def find_busiest_day(visits):
    # Хранение посещений в формате Counter
    day_counts = Counter()
    
    # Проходим по каждому периоду посещения
    for start, end in visits:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
        
        # Увеличиваем счетчик для всех дней в периоде
        current_date = start_date
        while current_date <= end_date:
            day_counts[current_date] += 1
            current_date += timedelta(days=1)
    
    # Поиск дня с максимальным количеством гостей
    busiest_day = max(day_counts, key=day_counts.get)
    return busiest_day.strftime("%Y-%m-%d"), day_counts[busiest_day]


visits = [("2024-09-15", "2024-09-16"), ("2024-09-14", "2024-09-21"), ("2024-09-25", "2024-09-30"), ("2024-09-10", "2024-09-20")]


busiest_day, visitors = find_busiest_day(visits)
print(f"Самый загруженный день: {busiest_day}, количество посетителей: {visitors}")
