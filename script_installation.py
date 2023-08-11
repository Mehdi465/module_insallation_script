import pip
import re

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


if __name__ == '__main__':

    with open("modules.txt","r+") as text_file:
        text = text_file.read()
        for module in text.split("\n"):
            print(module)
            install(module)


    """ res = ""
    with open("modules.txt",'r+') as text_file:
        res = text_file.read()

        print(res)

        res = res.split("\n")
        
        print(res)

        list_f = []

        for module in res:
            module = module.split(" ")
            print(module)
            while("" in module):
                module.remove("")
            list_f.append(module)    

        res_f = []

        for k in list_f:
            res_f.append(f"{k[0]}=={k[1]}")

        print(res_f)    
            

    
    with open("modules.txt",'w+') as text_file:
        for res1 in res_f:
            text_file.write(res1+"\n") """
 