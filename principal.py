from modulos import *
from time import sleep

while True:
    sleep(2)
    menu()
    decision = valid_menu_option()
    # select new function after function valid_menu_option return a number between 1 and 4
    if decision == 1:
        token = register()
        date, kilometer, gas_liters = token.split('=')
        date = date.strip('\n')
        print(f"adding date: {date} Km's: {kilometer} liters: {gas_liters}")
        file = open('index.txt', 'a')
        file.write(token)
        file.close()

    elif decision == 2:
        file = open('index.txt', 'r')
        final_array = poli_array(file)
        # Show every register in the file .txt.
        for ind, item in enumerate(final_array):
            start_date, end_date, percorred_km, km_for_liter = item.values()
            print(f'in {end_date} you traveled km: {percorred_km} and maded {km_for_liter} kilometers for liter.')

    elif decision == 3:
        file = open('index.txt', 'r')
        final_array = poli_array(file)
        # Reverting array to catch the last two.
        final_array.reverse()
        current_km_for_liter = final_array[0]["km_for_liter"]
        previous_km_for_liter = final_array[1]["km_for_liter"]
        percent = calc_percent(current_km_for_liter, previous_km_for_liter)
        print("==" * 20)
        print(f"the previous time you vehicle maded {previous_km_for_liter}")
        print(f"the last time you vehicle maded {current_km_for_liter}")
        print(f"its {percent}% of diference")
        print("==" * 20)

    else:
        print('Finalized Program')
        break
