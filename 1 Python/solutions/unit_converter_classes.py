


class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'ft': 0.3048,
            'mi': 1609.34,
            'm': 1,
            'km': 1000,
            'yd': 0.9144,
            'in': 0.0254
        }
    
    def convert(self, input_distance, input_units, output_units):
        return input_distance*self.conversion_factors[input_units]/self.conversion_factors[output_units]


unit_converter = UnitConverter()
distance_meters = unit_converter.convert(5, 'mi', 'm')
print(distance_meters)





