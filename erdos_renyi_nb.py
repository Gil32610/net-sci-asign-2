import os
from datetime import datetime

import matplotlib.pyplot as plt
import networkx as nx


def create_erdos_renyi(n, k_avg, seed=None, save=True, outdir=".", show=True):
    """Build a G(N, p) network with p chosen so that <k> = p * (N - 1).

    Returns (G, fig). In a notebook the figure is displayed inline
    when show=True.
    """
    p = k_avg / (n - 1)
    if not 0 <= p <= 1:
        raise ValueError(f"<k>={k_avg} is impossible for N={n} (p={p:.3f}).")

    G = nx.gnp_random_graph(n, p, seed=seed)

    L = G.number_of_edges()
    k_real = 2 * L / n  # measured average degree of this realization

    now = datetime.now()
    name = f"erdos_renyi_network_N{n}_k{k_avg}"
    title = f"{now:%Y-%m-%d %H:%M:%S} - {name}"
    filename = f"{now:%Y%m%d_%H%M%S}_{name}.png"

    fig, ax = plt.subplots(figsize=(8, 8))
    pos = nx.spring_layout(G, seed=seed)
    nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.4)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=30)

    handles = [plt.Line2D([], [], linestyle="none") for _ in range(3)]
    labels = [f"N = {n}", f"L = {L}", f"<k> = {k_real:.2f}"]
    ax.legend(handles, labels, loc="upper right")

    ax.set_title(title)
    ax.axis("off")

    if save:
        os.makedirs(outdir, exist_ok=True)
        path = os.path.join(outdir, filename)
        fig.savefig(path, dpi=150, bbox_inches="tight")
        print(f"Saved {path}")

    if show:
        plt.show()
    else:
        plt.close(fig)

    return G, fig