from rich import print
from rich.panel import Panel

caixa = Panel("[white]Esse aqui é um painel de exemplo[/white]:+1:", title="caixa", style="red", width=35)
caixa2 = Panel("Olá, prazer em te conhecer!! :+1:",title="caixa 2", style="blue", width=35)

print(caixa)
print(caixa2)