#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import pandas as pd


def main():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    df = pd.DataFrame(data['data'])
    df.to_excel('data.xlsx', index=False)


if __name__ == '__main__':
    main()
