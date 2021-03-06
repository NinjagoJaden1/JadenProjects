def convert_celcius_to_farenheit(temp_in_celcius) :
    temp_in_farenheit=32+9/5*temp_in_celcius
    return temp_in_farenheit

def convert_farenheit_to_celcius(temp_in_farenheit) :
    temp_in_celcius=5/9*(temp_in_farenheit-32)
    return temp_in_celcius

x = convert_celcius_to_farenheit(5)
print(x)
y=convert_farenheit_to_celcius(41)
print(y)