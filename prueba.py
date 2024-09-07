from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar

# Mode Historical = 1
# Mode Schedule = 2

def format_dates(mode,input_date):
    
    input_date = input_date.strip()

    output_dates = []

    inner_dates = {}

    fecha_actual = datetime.strptime(input_date, "%Y-%m-%d")

    if mode == 1:

        # Restar 2 años
        two_years_ago = fecha_actual - relativedelta(years=2)

        ultimo_dia_numero = calendar.monthrange(two_years_ago.year, two_years_ago.month)[1]

        # Si el día no es el de fin de mes, acomienza en el siguiente mes ya restado
        if two_years_ago.day != ultimo_dia_numero :

            print("NOT Last day of month")

            fecha_actual2 = two_years_ago + relativedelta(months=1)
            fecha_actual2 = fecha_actual2.replace(day=1)

            inner_dates['start_date'] = fecha_actual2.strftime("%Y-%m-%d")
            start_date = fecha_actual2

            fecha_actual_menos1 = fecha_actual - relativedelta(months=1)
            ultimo_dia_numero = calendar.monthrange(fecha_actual_menos1.year, fecha_actual_menos1.month)[1]

            inner_dates['end_date'] = fecha_actual_menos1.replace(day=ultimo_dia_numero).strftime("%Y-%m-%d")
            end_date = fecha_actual_menos1.replace(day=ultimo_dia_numero)
            
            while start_date <= end_date:

                # Crear un diccionario para almacenar las fechas
                inner_dates = {}

                # Obtener el primer día del mes (que ya es current_date)
                inner_dates['start_date'] = start_date.strftime("%Y-%m-%d")
                
                # Obtener el último día del mes actual
                ultimo_dia_numero = calendar.monthrange(start_date.year, start_date.month)[1]
                end_of_month = start_date.replace(day=ultimo_dia_numero)
                inner_dates['end_date'] = end_of_month.strftime("%Y-%m-%d")
                
                # Añadir el diccionario a la lista
                output_dates.append(inner_dates)
                
                # Avanzar al primer día del siguiente mes
                start_date = start_date + relativedelta(months=1)
                
        # Si el día es el de fin de mes, comienza con 1 del mes :
        else:
            print("Last day of month")

            fecha_actual2 = two_years_ago.replace(day=1)
            inner_dates['start_date'] = fecha_actual2.strftime("%Y-%m-%d")
            start_date = fecha_actual2

            fecha_actual_menos1 = fecha_actual - relativedelta(months=1)
            ultimo_dia_numero = calendar.monthrange(fecha_actual_menos1.year, fecha_actual_menos1.month)[1]

            inner_dates['end_date'] = fecha_actual_menos1.replace(day=ultimo_dia_numero).strftime("%Y-%m-%d")
            end_date = fecha_actual_menos1.replace(day=ultimo_dia_numero)

            while start_date <= end_date:

                # Crear un diccionario para almacenar las fechas
                inner_dates = {}

                # Obtener el primer día del mes (que ya es current_date)
                inner_dates['start_date'] = start_date.strftime("%Y-%m-%d")
                
                # Obtener el último día del mes actual
                ultimo_dia_numero = calendar.monthrange(start_date.year, start_date.month)[1]
                end_of_month = start_date.replace(day=ultimo_dia_numero)
                inner_dates['end_date'] = end_of_month.strftime("%Y-%m-%d")
                
                # Añadir el diccionario a la lista
                output_dates.append(inner_dates)
                
                # Avanzar al primer día del siguiente mes
                start_date = start_date + relativedelta(months=1)

    elif mode == 2:

        # Restar un mes para obtener el mes anterior
        fecha_mes_anterior = fecha_actual - relativedelta(months=1)

        # Obtener el primer día del mes anterior
        primer_dia = fecha_mes_anterior.replace(day=1)

        # Obtener el último día del mes anterior
        ultimo_dia_numero = calendar.monthrange(fecha_mes_anterior.year, fecha_mes_anterior.month)[1]
        ultimo_dia = fecha_mes_anterior.replace(day=ultimo_dia_numero)

        inner_dates['start_date'] = primer_dia.strftime("%Y-%m-%d")
        inner_dates['end_date'] = ultimo_dia.strftime("%Y-%m-%d")

        output_dates.append(inner_dates)

    return output_dates

user_mode = int(input('Introduce un modo (1 para Historico, 2 para Programado): '))
user_date = input('Introduce la fecha con formato YYYY-mm-dd: ').strip()

print(format_dates(user_mode,user_date))
