def coordinate_pair(value):
    valid_pair = 'x' in value and 'y' in value \
                 and isinstance(value['x'], float) and isinstance(value['y'], float)
    if not valid_pair:
        raise ValueError("Invalid list of coordinates")
    return value
