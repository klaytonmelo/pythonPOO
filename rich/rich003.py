from rich import print
from rich.table import Table

tabela = Table(title="tabela de preços")

tabela.add_column("Nome", justify="right", style="red")
tabela.add_column("preço", justify="center", style="blue")

tabela.add_row("Lapís", "R$1,50")
tabela.add_row("Borracha", "[green]R$5,00[/green]")
print(tabela)
