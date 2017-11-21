def coordinate_pair(value):
    valid_pair = 'x' in value and 'y' in value \
                 and isinstance(value['x'], int) and isinstance(value['y'], int)
    if not valid_pair:
        raise ValueError("Invalid list of coordinates")
    return value
