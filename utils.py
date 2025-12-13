
#Float validation
def valid_float(input_str, min_value=0, angle = None):
    try:
        num = float(input_str)
        if num < min_value:
            return False, num
        if angle is not None and (0 < angle or angle > 90):
            return False,angle
        return True, num
        
    except ValueError as vE:
        return False, vE

#Sorting a dictionary to semi pretty form ;D
def pretty_dict(d_i_c_t):
    data = d_i_c_t
    for k, v in data.items():
        print(f'{k}:{v}')