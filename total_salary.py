def total_salary(path):
    try:
      with open(path) as salary_list:
        total = 0

        list = salary_list.readlines()

        for worker in list:
           name, salary = worker.split(',')
           total += int(salary)
           
        return (total, total / len(list))
    except FileNotFoundError:
       print(f"Файл {path} не знайдено.")


total, average = total_salary("salary_file.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
