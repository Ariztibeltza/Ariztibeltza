import os
import subprocess
from MQTT import client

## ~~ STORED DATA ~~ ########################################################################################################################

#       container_data = {'container_id' : ['container_name', 'container_host', 'container_port]}
container_data = dict()

def test(a,b):
    message = str(a)+' '+str(b)
    return message

def help():
    message = 'Following this messsage : '
    return message

## ~~ BROKER MANAGEMENT THROUGH DOCKER ~~ ###################################################################################################
def startBroker(container_name, host_port, container_port):
    # Komando honen formatoa honakoa da beti
    #       docker run -d --name [container_name] -p [host port]:[container port] emqx/emqx:4.3.5

    # Defektuz guk maneiatuko dugu 1883:1883

    # HEEN MANEIATU BEHARKO DITUGU DATUAK, HEMENDIK JASOZ ETA ORDENATUZ DENA ONDO
    try:
        if (host_port != 'None'):
            if (container_port != 'None'):
                message_stream = os.popen(f'docker run -d --name {container_name} -p {host_port}:{container_port} emqx/emqx:4.3.5')
                container_data[container_name] = [message_stream.read().split()[0],host_port,container_port]
                message = f'An EMQX conatainer has been created with  name: {container_name } host port: {host_port} and container port: {container_port}'
                return message

            else:
                message_stream = os.popen(f'docker run -d --name {container_name} -p {host_port}:1883 emqx/emqx:4.3.5')
                container_data[container_name] = [message_stream.read().split()[0],host_port,'1883']
                message = f'An EMQX conatainer has been created with  name: {container_name } host port: {host_port} and container port: 1883'
                return message
        else:
            message_stream = os.popen(f'docker run -d --name {container_name} -p 1883:1883 emqx/emqx:4.3.5')
            container_data[container_name] = [message_stream.read().split()[0],'1883','1883']
            message = f'An EMQX container has been created with name: {container_name } host port: 1883 and container port: 1883'
            return message
    except:
        message = '''The continer could not be created or is already in use, might want to see which continers have been already created or are being used.
                     Type "showContainers(Active/All)" for a full list of containers'''
        return message

def brokerStatus(container_name):
    i = 0
    try:   
        for name in list(container_data.keys()):
            if container_name == name:   
                #ONDO JARRI DATUEN ESTRUKTURA 
                message = f'''The broker container is up, with ID: {container_data[container_name][0]}, 
                              Container's name is: {container_name}
                              Broker's host port: {container_data[container_name][1]}, 
                              Broker's container port: {container_data[container_name][2]}'''       # Honela lortzen dugu lista bat,  nahi ditugun elementuekin
            i+=1
        return message
    except:
        message = 'The broker is down, it has to be started.'
        return message

def finishBroker():
    message = 'Broker finished'
    return message

def startClient():
    #Hemen MQTT karpetan dagoen programa erabili beharko dugu
    message = 'Client goes here'
    return message
    
def executeCmd(str):
    message = os.popen(f'docker exec emqx {str}')
    return message

## ~~ DOCKER MANAGEMENT ~~ ##################################################################################################################
def showContainers(operation):
    if operation == 'Active':
        message_stream = os.popen('docker ps')
        message = message_stream.read()
        return message
    elif operation == 'All':
        message_stream = os.popen('docker ps -a')
        message = message_stream.read()
        return message
    else:
        message = 'Only "Active" or "All" are taken as arguments.'
        return message




## ~~ AUX FUNCTIONS ~~ ######################################################################################################################

## ~~ TEST MAIN ~~ ##########################################################################################################################

## ~~ BESTE APUNTEAK ~~ #####################################################################################################################

# Docker buruzko komando garrantzitsuak:
#       docker stop container_name
#       docker rm container_name        -> Honela gelditu eta hil egiten dugu kontainer bat