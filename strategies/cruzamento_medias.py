from strategies.base_strategy import BaseStrategy
import pandas as pd

class CruzamentoMedias(BaseStrategy):
    def __init__(self, df, periodo_curto=9, periodo_longo=21):
        super().__init__(df)
        self.periodo_curto = periodo_curto
        self.periodo_longo = periodo_longo

    def verificar_entrada(self):
        df = self.df.copy()
        df["sma_curta"] = df["close"].rolling(self.periodo_curto).mean()
        df["sma_longa"] = df["close"].rolling(self.periodo_longo).mean()

        if df["sma_curta"].iloc[-2] < df["sma_longa"].iloc[-2] and df["sma_curta"].iloc[-1] > df["sma_longa"].iloc[-1]:
            return "compra"
        elif df["sma_curta"].iloc[-2] > df["sma_longa"].iloc[-2] and df["sma_curta"].iloc[-1] < df["sma_longa"].iloc[-1]:
            return "venda"
        else:
            return None
