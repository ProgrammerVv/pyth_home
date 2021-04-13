import data
import random
from collections import Counter


def CmdLine():
    """
    Comand Line Logic
    """
    user_cmd = (input("Get the command: "))
    if (user_cmd == "h"):
        ComandHelper()
    elif (user_cmd == "p"):
        DocOwner(data.documents)
    elif (user_cmd == "add"):
        DocAdd()
    elif (user_cmd == "exit"):
        Exit()
    elif (user_cmd == "show d"):
        ShowDiraddectories()
    elif (user_cmd == "show doc"):
        ShowDocs()
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

        if user_cmd == "Y":
            continue
        else:
            break

    print(type(new_info))
    Addnewinfotodocs(new_info)
    CmdLine()
    return new_info

def Addnewinfotodocs(new_info):
    """
        Add new information to data.documentation
    """

    data.documents.append(new_info)
    #print(data.documents[-1])
    CheckDocsKey(data.documents[-1])

def CheckDocsKey(doc_for_check):
    """
    Check any docs in dictionary documents and if value with key 'number' in documents it append to derictories
    """

    if 'number' in doc_for_check.keys():
        item_num_saver = doc_for_check['number']
        print([item_num_saver])
        new_dict_for_number = {}
        i = 0
        counter = 0
        while i < 1:
            #key = 'new' # Сделать динамический ключ!!!!!!!! Чтобы значения сохранялись
            # Читать значение ключа и прибавлять единицу
            key = random.randrange(0, 101, 2)
            value = [item_num_saver]
            new_dict_for_number[key] = value
            i +=1
        #print(new_dict_for_number)
        data.directories.update(new_dict_for_number)
        print('RESULTS',data.directories)


def ComandHelper():
    """
    Comand Helper
    """
    print(" p - comand for find the owner of d")
    print(" add - use for add new informations")
    print(" show doc - watch document")
    print(" shwo d - watch directorias")
    print(" q - exit from add")
    CmdLine()


def DocOwner(dictionaryForFind):
    """
    Find the docs owner
    """
    Doc_number = (input("Input the doc number without s : "))
    print ('perehod was')

    finded  = next(item for item in dictionaryForFind if item["number"] == Doc_number)
    if finded == None:
        print("No founded")
    else:
        print('Owner doc name: ',finded['name'])

    CmdLine()

def Exit():
    print('Have a nice day!')

def ShowDiraddectories():
    """
       Show dir
       """
    print(data.directories)
    CmdLine()

def ShowDocs():
    print(data.documents)
    CmdLine()

def counter(i):
    """
    key generators
    """
    i + 1
    return i
