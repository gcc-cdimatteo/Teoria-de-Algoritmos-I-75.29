$$T(n)=A*T \left(\frac{n}{B}\right)+O(n^C)$$
$A \in$ cantidad de llamados recursivos
$B \in$ proporción del tamaño original con el que llamamos recursivamente
$O(n^C) \in$ costo de partir y juntar (todo lo que no son llamados recursivos)
Si
- $\log_{B}{(A)} < C \implies T(n)=O(n^C)$
- $\log_{B}{A} = C \implies T(n)=O(n^C)* \log_{B}{n} = O(n^C \log{n})$
- $\log_{B}{(A)} > C \implies T(n)=O(n^{\log_{B}{A}})$
