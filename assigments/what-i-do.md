# QUE HAGO YO?

En los siguientes ejercicios usted debera crear una tabla en excel o cualquier otra herramienta que prefiera y hacerle
seguimiento a las variables de las funciones que se muestran en cada problema, con el proposito de entender que hace cada de ellas


1. Problema 1

```python
def what_i_do(x):
    result = []
    for i in range(1,x + 1):
        if x % i == 0:
            result.append(i)
    return result

print(what_i_do(12))
```

Para iniciar simplemente tome este codigo y ejecutelo, despues cree su tabla y haga el paso a paso del ciclo for como
se hizo en clase, repita este proceso con los demas problemas

2. Problema 2

```python
def what_i_do(x):
    result = []
    for i in range(x):
        result.append(2*i)
    return result

print(what_i_do(12))
```

2. Problema 3

```python
def what_i_do(x):
    n = len(x)
    result = x
    for i in range(n):
        if i % 2 == 0:
            result[i] = '1'
    return result

sample_list = ['0', '0', '0', '0','0', '0', '0', '0', '0', '0', '0', '0']

print(what_i_do(sample_list))
```

## NOTA
Recuerde que puede acceder al excel de la clase en el siguiente [link](https://docs.google.com/spreadsheets/d/1qUQllZLedjlD_1Kgyo74sHySd4FldeW3xDTq3EM_sLo), y el codigo de la clase [aqui](https://github.com/stivencardona/basic-programming/tree/main/clases/class-vi), para que los tome como ejemplos.