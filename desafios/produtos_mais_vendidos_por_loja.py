import pandas

dataframe_vendas = pandas.read_csv("./vendas_tech.csv", low_memory=False)
dataframe_vendas = dataframe_vendas.rename(columns={"Qtd": "Quantidade"})
dataframe_vendas = dataframe_vendas[["Loja", "Produto", "Quantidade"]]
dataframe_vendas["Loja"] = dataframe_vendas["Loja"].str.strip().str.title()
dataframe_vendas["Loja"] = dataframe_vendas["Loja"].fillna("Online")
dataframe_vendas["Produto"] = dataframe_vendas["Produto"].str.strip().str.title()
dataframe_vendas = dataframe_vendas.groupby(["Loja", "Produto"]).sum()
dataframe_vendas = dataframe_vendas.sort_values(by=["Loja", "Quantidade"], ascending=[True, False])
dataframe_vendas = dataframe_vendas.reset_index()

dataframe_vendas.to_csv("desafios/produtos_mais_vendidos_por_loja.csv")

print(dataframe_vendas.head(n=10))
