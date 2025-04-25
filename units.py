# units.py
UNITS = {
    'Length': {
        'base': 'Meters',
        'units': {
            'Meters': 1,
            'Kilometers': 1000,
            'Centimeters': 0.01,
            'Millimeters': 0.001,
            'Feet': 0.3048,
            'Inches': 0.0254,
            'Miles': 1609.34
        }
    },
    'Weight': {
        'base': 'Grams',
        'units': {
            'Grams': 1,
            'Kilograms': 1000,
            'Pounds': 453.592,
            'Ounces': 28.3495
        }
    },
    'Volume': {
        'base': 'Liters',
        'units': {
            'Liters': 1,
            'Milliliters': 0.001,
            'Gallons': 3.78541,
            'Pints': 0.473176
        }
    },
    'Area': {
        'base': 'Square Meters',
        'units': {
            'Square Meters': 1,
            'Square Kilometers': 1_000_000,
            'Square Feet': 0.092903,
            'Acres': 4046.86
        }
    },
    'Speed': {
        'base': 'Meters per Second',
        'units': {
            'Meters per Second': 1,
            'Kilometers per Hour': 0.277778,  # 1000 m / 3600 s = 5/18
            'Miles per Hour': 0.44704         # 1609.34 m / 3600 s
        }
    },
    'Time': {
        'base': 'Seconds',
        'units': {
            'Seconds': 1,
            'Minutes': 60,
            'Hours': 3600,
            'Days': 86400
        }
    }
}

def convert_temperature(value, from_unit, to_unit):
    """Handle temperature conversions with formulas involving offsets."""
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return value * 9/5 + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    raise ValueError(f"Unsupported temperature conversion from {from_unit} to {to_unit}")

def convert_value(value, from_unit, to_unit, category):
    """Convert value from one unit to another within a category."""
    if category == 'Temperature':
        return convert_temperature(value, from_unit, to_unit)
    else:
        if from_unit == to_unit:
            return value
        factor_from = UNITS[category]['units'][from_unit]
        factor_to = UNITS[category]['units'][to_unit]
        value_in_base = value * factor_from
        value_in_to = value_in_base / factor_to
        return value_in_to