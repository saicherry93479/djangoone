from channels.consumer import SyncConsumer

class ChatConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.send({
            "type":"websocket.accept"
        })
    def websocket_receive(self,event):
        print("received message")
    def websocket_disconnect(self,event):
        print("disconnected")