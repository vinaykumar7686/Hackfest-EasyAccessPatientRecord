from cProfile import label
from matplotlib import pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)

    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    buffer.close()
    return graph


def get_plot(x, y, xaxis, yaxis, title, sizex = 4, sizey = 3):
    plt.switch_backend('AGG')
    plt.figure(figsize=(sizex, sizey))
    plt.title(title)
    for i in range(min(len(x),len(y))):
        plt.plot(x[i], y[i])
    plt.xticks(rotation = 0)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.tight_layout()
    graph = get_graph()
    return graph
