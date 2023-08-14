def get_val(collection, key, default='git'):
    """
    :param collection: словарь
    :param key:ключ словаря
    :param default:'git'
    :return:значение из словаря по переданному ключу, если ключ существует.Иначе значение
default
    """
    dict_key = key.strip()
    return collection.get(dict_key, default)
