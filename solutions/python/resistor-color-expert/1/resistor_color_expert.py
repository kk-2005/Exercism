color_dict = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}

tolerance_dict = {
    'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
    'brown': 1, 'red': 2, 'gold': 5, 'silver': 10
}

def resistor_label(colors):
    # Handle the special 1-band resistor edge case
    if len(colors) == 1:
        return f"{color_dict[colors[0]]} ohms"
        
    # 1. Parse base value and multiplier based on band counts
    if len(colors) == 4:
        digits = color_dict[colors[0]] * 10 + color_dict[colors[1]]
        value = digits * (10 ** color_dict[colors[2]])
        tolerance = tolerance_dict[colors[3]]
    else:  # len(colors) == 5
        digits = color_dict[colors[0]] * 100 + color_dict[colors[1]] * 10 + color_dict[colors[2]]
        value = digits * (10 ** color_dict[colors[3]])
        tolerance = tolerance_dict[colors[4]]

    # 2. Format tolerance string nicely without unnecessary .0 decimals
    tol_val = int(tolerance) if isinstance(tolerance, (int, float)) and tolerance.is_integer() else tolerance
    tolerance_str = f" ±{tol_val}%"

    # 3. Handle metric prefixes (ohms, kiloohms, megaohms, gigaohms) cleanly
    if value < 1000:
        val_str = str(int(value) if value.is_integer() else value)
        return f"{val_str} ohms{tolerance_str}"
    elif value < 1000000:
        val = value / 1000
        val_str = str(int(val) if val.is_integer() else val)
        return f"{val_str} kiloohms{tolerance_str}"
    elif value < 1000000000:
        val = value / 1000000
        val_str = str(int(val) if val.is_integer() else val)
        return f"{val_str} megaohms{tolerance_str}"
    else:
        val = value / 1000000000
        val_str = str(int(val) if val.is_integer() else val)
        return f"{val_str} gigaohms{tolerance_str}"


