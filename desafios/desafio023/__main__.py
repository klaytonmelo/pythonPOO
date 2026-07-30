from poligono import *
from rich import inspect, print
from rich.traceback import install

install()

def main():
    q = Quadrado(12)
    # inspect(p1, methods=True)

    print(f"[green]Um quadrado de lado [black]{q.lado}[/black] tem perímetro de [yellow]{q.perimetro()}cm[/][/]")
    print(f"[green]Um quadrado de lado [black]{q.lado}[/black] tem área de [yellow]{q.area()}cm²[/][/]")

    print("-" * 40)
    c = Circulo(12)
    print(f"[blue]Um circulo de raio [black]{c.raio}[/black] tem perímetro de [yellow]{c.perimetro():.1f}cm[/][/]")
    print(f"[blue]Um circulo de raio [black]{c.raio}[/black] tem área de [yellow]{c.area():.1f}cm²[/][/]")

if __name__ == "__main__":
    main()