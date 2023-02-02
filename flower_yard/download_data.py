import json
import os
from inspect import getmembers, isclass
from typing import List

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_yard.settings')
django.setup()
from flower import models
from flower.models import (
    Category, Badge,
    Product, Characteristic, ProductCharacteristic
    # FlowerCharacteristic
)


def drop_data():
    for i in (i for i in getmembers(models) if
              isclass(i[1]) and "flower.models" in i[1].__module__):
        i[1].objects.all().delete()


def open_file_json(file: str) -> List[dict]:
    path = os.path.join('data/', file + '.json')
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'Файла с путем {path} не существует!')


def main():
    data_files = [
        'categories',
        'badges',
        'products',
        'characteristics',
        'product_characteristic'
    ]
    data_models = [
        Category,
        Badge,
        Product,
        Characteristic,
        ProductCharacteristic
    ]
    try:
        for num in range(len(data_models)):
            data_models[num].objects.bulk_create([
                data_models[num](**data) for data in open_file_json(
                    data_files[num]
                )
            ])
            print(f'Данные для модели {data_models[num].__name__} - загрузились!')
    except Exception as err:
        drop_data()
        print(f'Возникла ошибка: {err}')


if __name__ == '__main__':
    main()