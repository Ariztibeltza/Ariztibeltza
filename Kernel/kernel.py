""" Backendaren Kernela

    Script honen bidez webapp-ean implementatuta dagoen frontend-etik jasotzen diren komandoen tratamendua egingo da, hortaz, app.py
    dokumentuan importatu egiten da eta ondoren definituta dauden funtzio guztiak honetan erabiliko dira. Beraz, fitxategi hau
    modulu bat bezala importatuta egoteko pentsatu da.

    Fitxategi honetan definituta dauden komando guztien informazioa batzen duen hiztegi bat daukagu, honako formatoarekin:
            cmd_dict = { 'cmd_name' : [ arg_number , 'cmd description' ]}
    
    Frontendetik, lehenengo unean, cmd_char_set karaktereen kate bat jasoko dugu, honako formatoa daukana:
            cmd_char_list = ['c','m','d','_','n','a','m','e','(','a','r','g','1',',',...,'a','r','g','n',')']

    Hortaz, nahitaezko egingo zaigu, ondoren intuitiboagoak diren komandoaren identifikadorea 
    debug(cmd_char_list) funtzioaren bidez karaktereen lista honetatik 'cmd_name' komandoaren identifikadorea eta 'arg_list' argumentuen
    lista erabiliko ditugu. 
"""

## ~~ CMD DICTIONARY ~~ #####################################################################################################################
"""Important note

    The import under this documentation is done in a way Flask recognizes it, as the structure inside the file system is the following:

    Software
        |-  Kernel
            |-  kernel.py
            |-  functionset.py
        |-  app.py
    
    Thus, from the 'POV' of app.py we need to import functionset form Kernel, but for kernel we only need functioonset. Juts to be clear.
"""
#   import functionset  #-> Testetan erabiltzeko
from Kernel import functionset

cmd_dict = {'HELP' : [0, 'All data will be printed on Terminal'] ,
            'test' : [2,'This is a test function'],
            'startBroker':[3,'Starts the EMQX broker'] , 
            'finishBroker':[0,'Kills the EMQX broker'],
            'brokerStatus':[1,"Gives info about the status of the broker's status"],
            'showContainers':[1,"Gives info about the Active/Resting+Active containers"]}

## ~~ FUNCTIONS ~~ ##########################################################################################################################

def debug(cmd_char_list):
    """cmd_char_list hartzen du eta komandoaren izena, argumentuak, errorea eta definizioa bueltatzen ditu

    Args:
        cmd_char_list (char list): Webapparen Frontend-etik, app.py dokumentuan definituta dagoenez, jasotzen dugun karaktereen lista iteragarria
                                    komando baten izena eta argumentuak dauzkana.

    Returns:
        cmd_id (str): komandoaren izena (ere deitu genezake cmd_name), giltz bezala erabiltzen duguna cmd_dict hiztegian.
        cmd_args (str list): komando honek dauzkan argumentuak jasotzen dituen lista.
        error (str): errore bat egotekotan komandoaren idazkerari buruz (izena ala argumentuen zenbakia ezegokia bada) honen bidez adieraziko dugu,
                     GEHIAGO GARATZEAN beste motako erroreak ere maneiatu ahalko ditugu.
        cmd_data (str): Frontend-ean exekuttu den komandoari buruzko informazio baliagarria erakusteko erabiltzen da.
    """
    error = None
    [cmd,arg_list] = parser(cmd_char_list)
    
    cmd_id = str()
    cmd_args = list()
    cmd_data = str()
    message = str()
    
    try:           
        
        cmd_dict[cmd]
        
        if len(arg_list)!=cmd_dict[cmd][0]:
            cmd_id = cmd
            cmd_args = None
            cmd_data = None
            message = None
            error = f'Incorrect number of argument for "{cmd}", {cmd_dict[cmd][0]} arguments where spected {len(arg_list)} were given'
            return cmd_id,cmd_args,error,cmd_data,message
        else:
            cmd_id = cmd
            cmd_args = arg_list
            cmd_data = cmd_dict[cmd][1]
            error = None
            message = execute(cmd_id,cmd_args)
            return cmd_id,cmd_args,error,cmd_data,message
    except:
        error = f'Command "{cmd}" is not defined, if you need help please type HELP'
        cmd_id = None
        cmd_args = None
        cmd_data = None
        return cmd_id,cmd_args,error,cmd_data,message

def execute(cmd_id, cmd_args):

    #functionset.update_container_data()

    if cmd_id == 'test':
        return functionset.test(cmd_args[0],cmd_args[1])
    elif cmd_id == 'HELP':
        return functionset.help()
    elif cmd_id == 'startBroker':
        return functionset.startBroker(cmd_args[0],cmd_args[1],cmd_args[2])
    elif cmd_id == 'brokerStatus':
        message= functionset.brokerStatus(cmd_args[0])
        return message
    elif cmd_id == 'showContainers':
        message= functionset.showContainers(cmd_args[0])
        return message

## ~~ AUXILIARY FUNCTIONS ~~ ################################################################################################################

def parser(cmd_char_list):
    """cmd_char_list hartu eta hemendik komandoaren izena eta argumentuen lista bueltatzen du

    Args:
        cmd_char_list (char list): Webapparen Frontend-etik, app.py dokumentuan definituta dagoenez, jasotzen dugun karaktereen lista iteragarria
                                    komando baten izena eta argumentuak dauzkana.
    Returns:
        cmd (str): komandoaren izena (ere deitu genezake cmd_name eta debug(cmd_char_list)-en cmd_id deitzen dena).
        arg_list (str list): komando honek dauzkan argumentuak jasotzen dituen lista.
    """
    #Kontutan eduki beahr dugu cmd_char_list honako formatoa daukagula:
    #           cmd_char_list = ['c','m','d','_','n','a','m','e','(',...,')']
    bracket = False
    cmd = str()
    arg_str = str()
    arg_list = list()

    for i in range(0,len(cmd_char_list)):
        if cmd_char_list[i]== '(':
            bracket = True
        elif bracket != True:
            cmd+=cmd_char_list[i]
        elif (bracket == True) and (cmd_char_list[i] !=',') and (cmd_char_list[i] != ')'):
            arg_str+=cmd_char_list[i]
        else:
            if arg_str !='':
                arg_list.append(arg_str)
                arg_str = str()
    return cmd,arg_list

## ~~ VALUABLE PIECES ~~ ####################################################################################################################

#1. #import os

    #os.system('docker run emqx/emqx:4.3.5º')
    #input()

##  ~~ TEST MAIN ~~ #########################################################################################################################

#cmd_char_list1 = ['c','m','d','_','n','a','m','e','(','a','b',',','c',')']
#cmd_char_list2 = ['c','m','d','_','n','a','m','e']
#cmd_char_list = ['t','e','s','t','(','a',',','b',')']
#debug(cmd_char_list)