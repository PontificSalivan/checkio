import collections

def flatten(d, parent_key='', sep='/'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
            
    return dict(items)

if __name__ == '__main__':
    test_input = {{"empty": {}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

