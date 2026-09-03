import pandas

dataframe_vendas = pandas.read_csv("./vendas_tech.csv", low_memory=False)
dataframe_vendas = dataframe_vendas.rename(columns={"Qtd": "Quantidade"})
dataframe_vendas = dataframe_vendas[["Loja", "Produto", "Preco_Unitario", "Quantidade"]]
dataframe_vendas["Loja"] = dataframe_vendas["Loja"].fillna("Online")
dataframe_vendas = dataframe_vendas[dataframe_vendas["Loja"] == "Online"]
dataframe_vendas["Produto"] = dataframe_vendas["Produto"].str.strip().str.title()
dataframe_vendas["Faturamento"] = (
    dataframe_vendas["Quantidade"] * dataframe_vendas["Preco_Unitario"]
)
dataframe_vendas = dataframe_vendas[["Produto", "Faturamento"]]
dataframe_vendas = dataframe_vendas.groupby("Produto").sum()
dataframe_vendas = dataframe_vendas.sort_values(by="Faturamento", ascending=False)
dataframe_vendas = dataframe_vendas.reset_index()

dataframe_vendas["Faturamento"] = dataframe_vendas["Faturamento"].map(
    "R$ {:,.2f}".format
)
dataframe_vendas.to_csv("desafios/produtos_maior_faturamento.csv")

print(dataframe_vendas.head(n=10))

