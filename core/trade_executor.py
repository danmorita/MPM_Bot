from core.broker_interface import enviar_ordem

def execute_trade(sinal, stop, alvo):
    enviar_ordem(sinal, stop, alvo)
