import grpc
from concurrent import futures
import time
import virtualassistant_pb2
import virtualassistant_pb2_grpc

class VirtualAssistantServicer(virtualassistant_pb2_grpc.VirtualAssistantServicer):
    def __init__(self):
        self.responses = {
            "oi": "Olá, tudo bem? Em que posso ajudar?",
            "olá": "Olá, tudo bem? Em que posso ajudar?",
            "hello": "Hello, how can I assist you?",
            "hi": "Hi there, how can I assist you?",
            "como você está?": "Estou bem, obrigado por perguntar!",
            "tudo bem?": "Sim, e você?",
            "qual é o seu nome?": "Meu nome é Virtual Assistant!",
            "você é um robô?": "Sim, sou um robô, mas adoro conversar com pessoas!",
            "você tem alguma sugestão de filme?": "Recomendo 'A Viagem de Chihiro', é um dos meus favoritos!",
            "qual é a sua cor favorita?": "Eu sou um programa de computador, então não tenho uma cor favorita. Qual é a sua cor favorita?",
            "como posso ajudar?": "Você pode me dizer sobre o que gostaria de conversar ou perguntar.",
            "você pode me ajudar com o meu problema de computador?": "Claro, por favor, me diga qual é o problema que você está enfrentando.",
            "o que você gosta de fazer nas horas vagas?": "Gosto de conversar com pessoas como você! E você, o que gosta de fazer nas suas horas vagas?",
            "você é inteligente?": "Eu sou um programa de computador, então não posso ser inteligente no sentido humano. Mas estou programado para ajudá-lo da melhor maneira possível!",
            "qual é a sua música favorita?": "Eu não posso ouvir música, mas talvez você possa me contar sobre a sua música favorita?",
            "por que o mar é azul?": "Porque os peixinhos estão cantando 'blue blue blue' debaixo d'água!",
            "por que o computador foi ao médico?": "Porque estava com vírus!",
            "como se chama um elevador no polo norte?": "Elevadorrtico!",
            "por que a galinha atravessou a rua?": "Para chegar ao outro lado!",
            "o que um canibal vegetariano come?": "Palha!",
            "o que é que tem quatro patas pela manhã, duas patas ao meio-dia e três patas à noite?": "O ser humano: rasteja quando é bebê, caminha ereto na vida adulta e usa bengala na velhice!",
            "por que o cachorro foi ao médico?": "Porque ele estava se sentindo arfante!",
}



    def SendMessage(self, request, context):
        if request.message.lower() in self.responses:
            return virtualassistant_pb2.VirtualAssistantResponse(message=self.responses[request.message.lower()])
        else:
            return virtualassistant_pb2.VirtualAssistantResponse(message="Desculpe, não entendi. Poderia reformular a sua pergunta?")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
virtualassistant_pb2_grpc.add_VirtualAssistantServicer_to_server(VirtualAssistantServicer(), server)
server.add_insecure_port("[::]:50051")
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
