from core.data_handler import get_data
from core.trade_executor import execute_trade
from strategies.cruzamento_medias import CruzamentoMedias
from core.risk_management import definir_risco
import yaml

if __name__ == "__main__":
    with open("config/settings.yaml", "r") as f:
        config = yaml.safe_load(f)

    df = get_data(
        simbolo=config["ativo"], 
        timeframe=config["timeframe"], 
        num_candles=500
    )

    estrategia = CruzamentoMedias(
        df,
        periodo_curto=config["periodo_movel_curto"],
        periodo_longo=config["periodo_movel_longo"]
    )

    sinal = estrategia.verificar_entrada()

    if sinal:
        stop, alvo = definir_risco(df, sinal, config)
        execute_trade(sinal, stop, alvo)
