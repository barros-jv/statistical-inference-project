import os
import matplotlib.pyplot as plt

def savefig(FIG_DIR, name, dpi=600):
    """
    Salva a figura Matplotlib atualmente ativa (plt.gcf()) em um arquivo.

    Esta função utiliza a API pyplot (plt.savefig) para salvar o gráfico
    que foi criado mais recentemente ou o gráfico definido como ativo.

    Parameters
    ----------
    FIG_DIR : str
        Caminho do diretório onde a figura será salva.
    name : str
        Nome do arquivo da figura, incluindo a extensão (ex: 'histograma.png').
    dpi : int, default=600
        Resolução (Dots Per Inch) da imagem salva. Valores mais altos resultam
        em maior qualidade e tamanho de arquivo.

    Returns
    -------
    None
        A função não retorna nada, mas imprime a confirmação no console.

    Raises
    ------
    FileNotFoundError
        Se o diretório especificado em `FIG_DIR` não existir.

    Notes
    -----
    Para garantir que o gráfico correto seja salvo, esta função DEVE ser
    chamada ANTES de `plt.show()` ou `plt.close()`.
    O parâmetro `bbox_inches='tight'` é usado para cortar o espaço em branco
    excessivo ao redor do gráfico.
    """
    path = os.path.join(FIG_DIR, name)
    plt.savefig(path, dpi=dpi, bbox_inches='tight')
    print(f"Figura salva: {path}")