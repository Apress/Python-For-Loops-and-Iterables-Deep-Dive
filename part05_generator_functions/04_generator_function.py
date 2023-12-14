sales_data = [('banana,', 'Q3', 155), ('cherry,', 'Q1', 235), ('cherry,', 'Q3', 220),
    ('cherry,', 'Q4', 150), ('date', 'Q4', 180), ('banana,', 'Q4', 175),
    ('date', 'Q3', 170), ('apple,', 'Q2', 170), ('date', 'Q1', 175),
    ('date', 'Q2', 230), ('cherry,', 'Q2', 250), ('apple,', 'Q3', 235),
    ('banana,', 'Q2', 185), ('banana,', 'Q1', 240), ('apple,', 'Q4', 150),
    ('apple,', 'Q1', 235)]

def grouped_by_fruit(sales_data):
    sorted_data = sorted(sales_data)
    previous_fruit = None
    grouped_data = []
    for fruit, month, amount in sorted_data:
        if fruit != previous_fruit and grouped_data:
            yield previous_fruit, grouped_data
            grouped_data = []
        grouped_data.append((month, amount))
        previous_fruit = fruit

    if grouped_data:
        yield fruit, grouped_data

for fruit, grouped_data in grouped_by_fruit(sales_data):
    print(fruit, grouped_data)
