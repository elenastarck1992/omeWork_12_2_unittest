def get_val(collection, key, default='git'):
    """
    :param collection: словарь
    :param key:ключ словаря
    :param default:'git'
    :return:значение из словаря по переданному ключу, если ключ существует.Иначе значение
default
    """
    dict_key = key.strip()
    if collection.get(dict_key) is not None:
        return collection.get(dict_key)
    else:
        return default
