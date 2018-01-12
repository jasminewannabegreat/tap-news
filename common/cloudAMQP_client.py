import json
import pika

#send message:transfer json to string and use pika to send to cloundAMQP
#receive message:

class CloudAMQPClient:
    def __init__(self, cloud_amqp_url, queue_name):
        self.cloud_amqp_url = cloud_amqp_url
        self.queue_name = queue_name
        self.params = pika.URLParameters(cloud_amqp_url)
        self.params.socket_time_timeout = 3
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
   
    def sendMessage(self, message):
        self.channel.basic_publish(exchange='',routing_key=self.queue_name, body=json.dumps(message))
        print "[x] sent message to %s: %s" %(self.queue_name,message)

    # get a message
    def getMessage(self):
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            print "[x] Received message from %s: %s" % (self.queue_name, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return json.loads(body)
        else:
            print 'No message returned.'
            return None
    # blocking connection.sleep is a safer way to sleep than time.sleep() 
    # heart-beat mechaism
    def sleep(self,seconds):
		    self.connection.sleep(seconds)
	

