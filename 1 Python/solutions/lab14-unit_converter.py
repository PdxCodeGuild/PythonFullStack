


# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m
# 1 yard is 0.9144 m
# 1 inch is 0.0254 m


def clean_units(units):
    units = units.lower().strip()

    # unit_groups = [
    #     ['ft', 'feet'],
    #     ['mi', 'miles', 'mile'],
    #     ['m', 'meters', 'meter']
    # ]
    # for unit_group in unit_groups:
    #     if units in unit_group:
    #         return unit_group[0]

    if units in ['feet', 'ft']:
        return 'ft'
    if units in ['mi', 'miles', 'mile']:
        return 'mi'
    if units in ['m', 'meters', 'meter']:
        return 'm'
    if units in ['km', 'kilometers', 'kilometer']:
        return 'km'
    if units in ['yd', 'yards', 'yard']:
        return 'yd'
    if units in ['in', 'inches', 'inch']:
        return 'in'
    return None


conversion_factors = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

while True:
    try:
        distance = float(input('what is the distance? '))
        break
    except ValueError:
        print('enter a valid floating-point number')

while True:
    input_units = clean_units(input('what are the input units? '))
    if input_units is None:
        print('invalid units')
    else:
        break

while True:
    output_units = clean_units(input('what are the output units? '))
    if output_units is None:
        print('invalid units')
    else:
        break

distance_output = distance*conversion_factors[input_units]/conversion_factors[output_units]
distance_output = round(distance_output, 2)
print(distance, input_units, 'is', distance_output, output_units)


