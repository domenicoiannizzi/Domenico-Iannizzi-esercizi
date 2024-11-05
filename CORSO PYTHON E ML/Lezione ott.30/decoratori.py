#Area triangolo calcolata con decoratore

def decoratore(calcola_area_triangolo):
    def wrapper(a,b):
        print("Area del triangolo : ")
        area=calcola_area_triangolo(a,b)
        return area
    return wrapper

@decoratore
def calcola_area_triangolo(a,b):
    return (a*b)/2

print(calcola_area_triangolo(4,5))
    
def area_rettangolo(b,h):
    return b*h

def area_quadrato(l):
    return l**2

print("Area rettangolo" , area_rettangolo(4,2))
print("Area quadrato", area_quadrato(5))