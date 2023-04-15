import grpc
import virtualassistant_pb2
import virtualassistant_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = virtualassistant_pb2_grpc.VirtualAssistantStub(channel)

while True:
    message_text = input("Digite a sua mensagem: ")
    message = virtualassistant_pb2.VirtualAssistantRequest(message=message_text)
    response = stub.SendMessage(message)
    print(response.message)
