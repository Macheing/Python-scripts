#convert from fahreinheit scale to Celsius scale. 
def to_celsius(degree):
    return (degree-32)*5/9
#convert from Celsius scale to fahreinheit scale   
def to_fahrenheit(degree):
    return (degree*(9/5))+32

print('<= Fahrenheit to Celsius vs Celsius to Fahrenheit =>')
#convert Fahrenheit to Celsius, and Celsius to Fahrenheit.
for i in range(0,101,10):
    print("|{:>3} F  =  {:6.2F} C".format(i,to_celsius(i)), '     vs    ',
            "{:>3} C  =  {:6.2F} F".format(i,to_fahrenheit(i)),'|')
    

    
