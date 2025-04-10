class BaseStrategy:
    def __init__(self, df):
        self.df = df

    def verificar_entrada(self):
        raise NotImplementedError("Você precisa implementar a lógica de entrada.")
