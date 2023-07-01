# В строке "Иван Иванов" поменяйте местами слова. Может быть представлена любая строка с именем и фамилией.
# Например: "Пётр Иванов" => "Иванов Пётр"

full_name = input("Введите имя и фамилию: ")
full_name = full_name.split(" ")
first_name = full_name[0]
lust_name = full_name[1]
full_name = lust_name + " " + first_name
print(full_name)
