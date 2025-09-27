# ex1_lists_to_dict.py
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

def lists_to_dict(keys, values):
    """Return a dictionary created by zipping keys and values."""
    return dict(zip(keys, values))

if __name__ == "__main__":
    d = lists_to_dict(keys, values)
    print(d)  # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
