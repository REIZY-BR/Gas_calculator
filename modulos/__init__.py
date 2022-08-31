import datetime


def menu():
    """
    :return: A formated menu for User.
    """
    print('-=' * 30)
    print("""
    1. Register new Data.
    2. Show all before registers.
    3. Show previous compare registers.
    4. Save and exit.
    """)
    print('-=' * 30)


def valid_menu_option():
    """
    :return: A valid decision in between 1 and 4.
    """
    # Creating a while to catch for sure a valid decision.
    while True:
        try:
            decision = int(input("Your Choice: "))
            if decision != 1 and decision != 2 and decision != 3 and decision != 4:
                raise
            else:
                break
        except KeyboardInterrupt:
            print('Interrupted program!')
        except:
            print("Invalid choice, please try again! [1/2/3/4]")
    return decision


def valid_date():
    """
    :return: A valid date object variable.
    """
    # Creating a while to catch for sure a valid date object.
    while True:
        try:
            day = int(input("Choice your day date: "))
            month = int(input("Choice your month date: "))
            date = datetime.date(int(datetime.date.today().year), month, day)
        except KeyboardInterrupt:
            print('Interrupted program!')
        except ValueError:
            print("Invalid date! please try again")
        else:
            return date


def valid_value():
    """
    :return: Value of kilometers in int type.
    """
    # Creating a while to catch for sure a valid int number.
    while True:
        try:
            value = int(input("kilometers traveled: "))
        except KeyboardInterrupt:
            print('Interrupted program!')
        except:
            print("invalid number!, please try again")
        else:
            return value


def register():
    """
    :return: A formated string with valid values to manipulate and added to file txt.
    """
    # Creating a while for User choose your day.
    while True:
        try:
            registerToday = str(input("save today's date? [S/N]: ")).strip().upper()
            if registerToday != 'S' and registerToday != 'N':
                raise
            else:
                break
        except KeyboardInterrupt:
            print('Interrupted program!')
        except:
            print("invalid choice!, please try again")
    # Cath today date to facilitate a user if want.
    if registerToday == 'S':
        date = datetime.date.today()
    # Call a function to catch a valid day if User want customize it.
    else:
        date = valid_date()
    # Creating a while to catch a valid int number to assign in a variable
    while True:
        try:
            gas_liter = int(input("how many liters? "))
        except KeyboardInterrupt:
            print('Interrupted program!')
        except:
            print("invalid number!, please try again")
        else:
            break
    # Creating a variable to assign every value and add attributes to easy manipulate in future.
    token = f'\n{date}={valid_value()}={gas_liter}'
    return token


def array_creator(txtFile):
    """
    :param txtFile: A file .txt with datas.
    :return: Array with dicionarys and txtFile data's.
    """
    array = list()
    temporary_dict = dict()
    for item in txtFile:
        date, kilometer, gas_liters = item.split('=')
        temporary_dict["date"] = date
        temporary_dict["km"] = kilometer
        temporary_dict["liter"] = gas_liters.replace('\n', '')
        array.append(temporary_dict.copy())
        temporary_dict.clear()
    return array


def poli_array(txtFile):
    """
    :param txtFile: A file .txt with datas.
    :return: Array with dicionarys and formated txtFile data's.
    """
    # Using the inter function to complemented.
    raw_array = array_creator(txtFile)
    temporary_dict = dict()
    final_array = list()
    for ind, item in enumerate(raw_array):
        date, kilometer, gas_liters = item.values()
        # The first line in file .txt is empty.
        if ind == 0:
            pass
        else:
            temporary_dict["start_date"] = raw_array[ind -1]["date"]
            temporary_dict["end_date"] = date
            temporary_dict["percorred_km"] = int(kilometer) - int(raw_array[ind-1]["km"])
            temporary_dict["km_for_liter"] = int(temporary_dict["percorred_km"]) / float(gas_liters)
            final_array.append(temporary_dict.copy())
            temporary_dict.clear()
    return final_array


def calc_percent(current_value, previous_value):
    """
    :param current_value: The current value.
    :param previous_value: The previus value.
    :return: The percentage ratio between current_value and previus_value.
    """
    # Checking if current value is less than previus value.
    if current_value < previous_value:
        percent = ((previous_value / current_value) - 1) * 100
        percent = percent * -1
        return round(percent, 2)
    else:
        percent = ((current_value / previous_value) - 1) * 100
        return round(percent, 2)