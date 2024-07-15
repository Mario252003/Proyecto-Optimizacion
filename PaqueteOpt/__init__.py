#Parcial1
from .Parcial1.Ejercicio_Caja import calcular_punto
from .Parcial1.Ejercicio_Cerca import CalculoCerca
from .Parcial1.Ejercicio_Lata import calcular_area_superficie
from .Parcial1.Ejercicio_Lata2 import calcular_lata

#              Metodos Para Funciones De Una Variable               #
#Metodos De Eliminacion De Regiones
from .MetodosParaFuncionesDeUnaVariable.MetodosDeEliminacionDeRegiones.Metodo_Division_Intervalos import division_por_intervalos
from .MetodosParaFuncionesDeUnaVariable.MetodosDeEliminacionDeRegiones.Busqueda_Fibonacci import busqueda_fibonacci
from .MetodosParaFuncionesDeUnaVariable.MetodosDeEliminacionDeRegiones.Metodo_Seccion_Dorada import busqueda_seccion_dorada

#Metodos Basados En La Derivada
from .MetodosParaFuncionesDeUnaVariable.MetodosBasadosEnLaDerivada.Metodo_Newton_Raphson import metodo_newton_raphson
from .MetodosParaFuncionesDeUnaVariable.MetodosBasadosEnLaDerivada.Metodo_Biseccion import encontrar_raiz
from .MetodosParaFuncionesDeUnaVariable.MetodosBasadosEnLaDerivada.Metodo_Secante import met_secante

#               Metodos Para Funciones Multivariadas             #
#Metodos De Gradiente
from .MetodoParaFuncionesMultivariadas.MetodosDeGradiente.Gradiente_Conjugado import metodo_gradiente_conjugado
from .MetodoParaFuncionesMultivariadas.MetodosDeGradiente.Metodo_Cauchy import cauchy
from .MetodoParaFuncionesMultivariadas.MetodosDeGradiente.Metodo_Fletcher_Reeves import metodo_fletcher_reeves
from .MetodoParaFuncionesMultivariadas.MetodosDeGradiente.Metodo_Newton import newton

#Metodos Directos
from .MetodoParaFuncionesMultivariadas.MetodosDirectos.Algoritmos_con_restricciones import rosenbrock_cubica_linea, mishra_pajaro_restringida, rosenbrock_disco, simionescu, townsend, gomez_levy
from .MetodoParaFuncionesMultivariadas.MetodosDirectos.Algoritmos_sin_restricciones import ackley, beale, bukin_n6, cabina, camello_tres_jorobas, cruce_bandeja, easom, esfera, goldstein_price, himmelblau, holder, levi_n13, matyas, mccormick, rosenbrock, rastrigin, portahuevos, schaffer_n4, schaffer_n2, shekel, styblinski_tang
from .MetodoParaFuncionesMultivariadas.MetodosDirectos.BusquedaUnidireccional import next_point, objective_function

#Metodos Directos Multivariadas
from .MetodoParaFuncionesMultivariadas.MetodosDirectosMultivariadas.Caminata_Aleatoria import random_walk
from .MetodoParaFuncionesMultivariadas.MetodosDirectosMultivariadas.Hooke_Jeeves import hooke_jeeves
from .MetodoParaFuncionesMultivariadas.MetodosDirectosMultivariadas.Nelder_mead import nelder_mead
