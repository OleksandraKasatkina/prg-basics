def time_string(hours, minutes, time_format):
    minute_str = f"{minutes:02}"

    if time_format == '24':
        hour_str = f"{hours:02}"
        return f"{hour_str}:{minute_str}"
    elif time_format == '12':
        if hours == 0:
            return f"12:{minute_str}am"  
        elif hours < 12:
            return f"{hours}:{minute_str}am"  
        elif hours == 12:
            return f"12:{minute_str}pm"  
        else:
            return f"{hours - 12}:{minute_str}pm"  
    else:
        return "Invalid format"

print(time_string(15, 38, '24'))  
print(time_string(8, 3, '24'))    
print(time_string(0, 5, '24'))    
print(time_string(11, 15, '12'))  
print(time_string(0, 7, '12'))   
print(time_string(7, 30, '12'))   
print(time_string(12, 46, '12'))  
print(time_string(13, 10, '12'))  
print(time_string(19, 2, '12'))  