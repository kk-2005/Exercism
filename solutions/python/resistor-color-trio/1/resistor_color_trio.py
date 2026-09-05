def label(colors):
    color_values={'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    band1=color_values[colors[0]]
    band2=color_values[colors[1]]
    band3=color_values[colors[2]]
    value=(10*band1+band2)*(10**band3)
    
    # Strip trailing '.0' from division by checking if it's a whole number
    if value<1000:
        return f"{value} ohms"
    elif value>=1000 and value<1000000:
        val = value/1000
        return f"{int(val) if val.is_integer() else val} kiloohms"
    elif value>=1000000 and value<1000000000: # Changed <= to < for consistency
        val = value/1000000
        return f"{int(val) if val.is_integer() else val} megaohms"
    else:
        val = value/1000000000
        return f"{int(val) if val.is_integer() else val} gigaohms"
