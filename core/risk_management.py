def definir_risco(df, sinal, config):
    preco_entrada = df["close"].iloc[-1]
    if sinal == "compra":
        stop = preco_entrada - config["stop_pts"]
        alvo = preco_entrada + config["alvo_pts"]
    else:
        stop = preco_entrada + config["stop_pts"]
        alvo = preco_entrada - config["alvo_pts"]
    return stop, alvo
