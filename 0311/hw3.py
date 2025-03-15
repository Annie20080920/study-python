var = "Hello" 

def update_var():
    var = var + " World"
    print(var)

update_var()
print(var)

실행 결과:
UnboundLocal Error
fixed:
var = "Hello" 

def update_var():
  global var  
  var = var + " World"
  print(var)

update_var()
print(var)

실행결과
Hello World
Hello World