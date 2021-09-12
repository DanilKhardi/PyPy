import os
import tempfile
import argparse
import json


def read_file(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r', encoding='utf-8') as fin:
        data = fin.read()
        if data:
            return json.loads(data)
        return {}


def add_data(storage_path, key, value):
    data = read_file(storage_path)
    data[key] = data.get(key, [])
    data[key].append(value)
    write_data(storage_path, data)


def write_data(storage_path, data):
    with open(storage_path, 'w', encoding='utf-8') as fout:
        fout.write(json.dumps(data))


def get_data(storge_path, key):
    data = read_file(storge_path)
    return data.get(key, [])


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Input key')
    parser.add_argument('--val', help='Input value')
    return parser.parse_args()


def main(storage_path):
    args = parse()
    if args.key and args.val:
        add_data(storage_path, args.key, args.val)
    elif args.key:
        print(*get_data(storage_path, args.key), sep=', ')
    else:
        print('Please input correct data')


if __name__ == "__main__":
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
