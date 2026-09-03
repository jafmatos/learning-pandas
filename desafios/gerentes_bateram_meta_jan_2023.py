import pandas
import numpy

dataframe_vendas = pandas.read_csv("./vendas_tech.csv", low_memory=False)
dataframe_gerentes = pandas.read_excel("./gerentes_lojas.xlsx")

dataframe_vendas = dataframe_vendas.rename(columns={"Qtd": "Quantidade"})
dataframe_vendas = dataframe_vendas.drop_duplicates(subset=["ID_Pedido"])
dataframe_vendas = dataframe_vendas[["Data", "Loja", "Preco_Unitario", "Quantidade"]]
dataframe_vendas["Loja"] = dataframe_vendas["Loja"].fillna("Online")
dataframe_vendas["Loja"] = dataframe_vendas["Loja"].str.strip().str.title()

dataframe_vendas["Data"] = pandas.to_datetime(
    dataframe_vendas["Data"], format="%Y-%m-%d"
)
dataframe_vendas = dataframe_vendas[
    (dataframe_vendas["Data"].dt.year == 2023) & (dataframe_vendas["Data"].dt.month == 1)
]

dataframe_vendas["Faturamento"] = (
    dataframe_vendas["Quantidade"] * dataframe_vendas["Preco_Unitario"]
)

dataframe_faturamento = dataframe_vendas[["Loja", "Faturamento"]]
dataframe_faturamento = dataframe_faturamento.groupby("Loja").sum()
dataframe_faturamento = dataframe_faturamento.reset_index()

dataframe_gerentes["Loja"] = dataframe_gerentes["Loja"].str.strip().str.title()
dataframe_gerentes["Gerente"] = dataframe_gerentes["Gerente"].str.strip().str.title()

dataframe_faturamento_metas_gerentes = pandas.merge(
    dataframe_faturamento, dataframe_gerentes, on="Loja", how="left"
)
dataframe_faturamento_metas_gerentes["Meta_Atingida"] = numpy.where(
    dataframe_faturamento_metas_gerentes["Faturamento"]
    >= dataframe_faturamento_metas_gerentes["Meta_Mensal"],
    "Sim",
    "Não",
)

dataframe_faturamento_metas_gerentes.to_csv("desafios/gerentes_bateram_meta_jan_2023.csv")

print(dataframe_faturamento_metas_gerentes.head(n=10))
