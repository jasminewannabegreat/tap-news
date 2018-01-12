from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://gnjkwrcm:wuIt26fgg3yjHAipAm7vV--KmcHV9ArE@donkey.rmq.cloudamqp.com/gnjkwrcm"

TEST_QUEUE_NAME = "TEST"

def test_basic():
    client= CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)
    sentMsg = {"test":"test"}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg
    print "test passedd"

if __name__ == "__main__":
    test_basic()
