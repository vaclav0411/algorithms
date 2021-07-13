def flatten(d: dict, new_d, path=''):
    for key, value in d.items():
        if not isinstance(value, dict):
            new_d[path + key] = value
        else:
            path += f'{key}.'
            return flatten(d[key], new_d, path=path)
    return new_d


if __name__ == "__main__":
    d = {"foo": 42,
         "bar": "qwe",
         "buz": {
             "one": 1,
             "two": 2,
             "nested": {
                 "deep": "blue",
                 "deeper": {
                     "song": "my heart",
                 }
             }
         }
    }
    print(flatten(d, {}))
