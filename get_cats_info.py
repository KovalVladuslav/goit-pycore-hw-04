def get_cats_info(path):
    try:
      with open(path) as cats_list:
        result = []

        list = cats_list.readlines()

        for cat in list:
           id, name, age = cat.split(',')
           
           result.append({
              "id": id,
              "name": name,
              "age": age.strip()
           })
           
        return result

    except FileNotFoundError:
       print(f"Файл {path} не знайдено.")


cats_info = get_cats_info("cats_file.txt")

print(cats_info)
