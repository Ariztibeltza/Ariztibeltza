#   import paho.mqtt.client as mqtt

# Informazio gehiago lortzeko honakoa daukagu
#   ->  https://pypi.org/project/paho-mqtt/
#       https://docs.emqx.io/en/broker/v4.3/development/python.html#paho-python-usage-example
#       http://www.steves-internet-guide.com/publishing-messages-mqtt-client/

#   def on_connect(client, userdata, flags, result):
    #   print('Connected with result code '+str(result))
    #client.subscribe('testtopic/#')

#   def on_message(client, userdata, client_msg):
    #   print(client_msg.topic+' '+str(client_msg.payload))

## ~~ TEST MAIN ~~ ##########################################################################################################################

#   client = mqtt.Client()

# Funtzioak berridatzi egiten ditugu, gutxi gora behera
#   client.on_connect = on_connect
#   client.on_message = on_message

# Adierazi beahr dugu zein den gure brokerra, honetara konektatuz
#client.connect('broker.emqx.io', 1883,10)
# Mensaje bat publikatzeko
#client.publish('emqtt', payload = 'Hello World', qos=0)

#client.loop_forever()