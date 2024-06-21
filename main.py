import defs_module as dm

word = dm.string_cleaner(input('Введите произвольную строку\n'))
print(dm.nato_code_maker(word))
