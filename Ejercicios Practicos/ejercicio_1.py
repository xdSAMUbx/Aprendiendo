#Promedio duracion

curso_min = 2.5
curso_max = 7
promedio_cursos = 4
curso_tomado = 1.5

#Diferencias de duracion

diferencia_min = 100 - (curso_tomado / curso_min * 100)
diferencia_max = 100 - (curso_tomado * 1000 // curso_max / 10)
diferencia_promedio = 100 - (curso_tomado / promedio_cursos * 100)

print('------------------------')
print(f'El curso tomado tarda {diferencia_min}% menos que el más rapido')
print(f'El curso tomado tarda {diferencia_max}% menos que el más lento')
print(f'El curso tomado tarda {diferencia_promedio}% menos que el más promedio')


#Material Inservible

crudo_curso_tomado = 3.5
crudo_promedio_cursos = 5

#Porcentaje material inservible reducido

material_reducido = 100 - (promedio_cursos / crudo_promedio_cursos * 100)
material_reducido_tomado = 100 - (curso_tomado * 1000 // crudo_curso_tomado / 10)

print('------------------------')
print(f'El material inservible promedio reducido es de {material_reducido}%')
print(f'El material inservible promedio reducido en el curso tomado es de {material_reducido_tomado}%')
print('------------------------')

#Ver 10 horas curso

print(f'Ver 10 horas de este curso equivale a ver {promedio_cursos * 100 // curso_tomado / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {curso_tomado * 100 // promedio_cursos / 10} horas de este curso')
print('------------------------')

