def decor(comprimi_stringa):
    def wrapper(*args, **kwargs):
        new_stringa= comprimi_stringa(*args, **kwargs)
        return new_stringa
    return wrapper
    
@decor 
def comprimi_stringa(stringa):
    count=1
    new_stringa= ""
    for i in range(len(stringa)+1):
     if stringa[i] == stringa[i - 1]:
          count += 1 
    else:
        new_stringa += stringa[i - 1] + str(count)
        count = 1
    
    new_stringa += stringa[-1] + str(count)
    return new_stringa if len(new_stringa) < len(stringa) else stringa
        
print(comprimi_stringa("mamma"))

            
    
            