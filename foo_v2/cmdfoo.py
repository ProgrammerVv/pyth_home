import data

def CmdLine():
    """
    Comand Line Logic
    """
    user_cmd = (input("Get the command: "))
    if (user_cmd == "h"):
        ComandHelper()
    if (user_cmd == "p"):
        DocOwner()
    if (user_cmd == "add"):
        DocAdd()
    if (user_cmd == "exit"):
        Exit()
    if (user_cmd == "show d"):
        ShowDiraddectories()
    else:
        print("Command not found, try again or use command h for help")
        CmdLine()


def DocAdd():
    """
    Add any information in documents
    """
    new_info = {}
    user_cmd = 0
    i = 0
    while i != 'q':
        AnyKey = input('Type of info: ')
        AnyValue = input('info: ')
        new_info[AnyKey] = AnyValue
        i += 1
        user_cmd = input("Continue? (Y/N)")
        data.documents.append(new_info)
        # print(documents) - check
        print(new_info)
        return new_info

        if user_cmd == "Y":
            continue
        else:
            break
        CmdLine()  # тут дописать выход в главную функцию
        CheckDocsKey(new_info)
        #CheckDocsKey(new_info)

        #print(new_info)
        return new_info



def CheckDocsKey(new_info):
    """
    Check any docs in dictionary docunents and if value with key 'number' in documents it append to derictories
    """
    # Write the foo
    if 'number' in data.documents:
        data.directories.update(new_info)
        print(data.directories)


def ComandHelper():
    """
    Comand Helper
    """
    print(" p - comand for find the owner of d")
    print(" add - use for add new informations")
    print(" q - exit from add")


def DocOwner():
    """
    Find the docs owner
    """
    Doc_number = (input("Input the doc number without s : "))
    print('finded')
    # Проверить наличие определенного ключа можно при помощи операции in. Для этого достаточно вывести результат ее выполнения для словаря по имени a.

    # a = {1: "one", 2: "two", 3: "three"}
    # print(2 in a)
    # print(4 in a)

    # True
    # False
    # https://all-python.ru/osnovy/slovari.html


def Exit():
    print('Have a nice day!')

def ShowDiraddectories():
    """
       Show dir
       """
    print(data.directories)
    CmdLine()