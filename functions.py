def developer_info(*args, **kwargs):
    print(args)
    print(kwargs)

developer_info('Python', 'Java', 'C++', name='John', age=23)