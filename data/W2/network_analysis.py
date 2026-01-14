import marimo

__generated_with = "0.17.0"
app = marimo.App()


@app.cell
def _():
    import networkx as nx
    import matplotlib.pyplot as plt
    import random
    import numpy as np
    import pandas as pd
    import ast
    return ast, np, nx, pd, plt


@app.cell
def _(df_edges):
    df_edges
    return


@app.cell
def _(ast, nx, pd):
    df_edges = pd.read_csv('data_edges.csv')

    df_edges["Friend"] = df_edges["Friend"].apply(ast.literal_eval)
    df_edges["Aquaintance"] = df_edges["Aquaintance"].apply(ast.literal_eval)
    df_edges["Study"] = df_edges["Study"].apply(ast.literal_eval)
    df_edges["Politics"] = df_edges["Politics"].apply(ast.literal_eval)
    df_edges["Support"] = df_edges["Support"].apply(ast.literal_eval)

    columns = ["Aquaintance", "Friend", "Study", "Poltics", "Support"]

    def network_loom(column):
        edge_list = []
        for index, row in df_edges.iterrows():
            source = row['Label']

            for target in row[column]:
                edge_list.append((source, target))

        G = nx.DiGraph()
        G.add_edges_from(edge_list)
        G.remove_edges_from(nx.selfloop_edges(G))

        return G

    G_aquaintance = network_loom("Aquaintance")
    G_friend = network_loom("Friend")
    G_poltics = network_loom("Study")
    G_study = network_loom("Politics")
    G_support = network_loom("Support")
    return G_aquaintance, G_friend, G_study, G_support, df_edges


@app.cell
def _(G_study, nx):
    nx.reciprocity(G_study)
    return


@app.cell
def _(G_support, np, nx, plt):
    _CLIQUE_MIN = 1
    _CLIQUE_MAX = 5
    _G_undirected = G_support.to_undirected(reciprocal=False)
    _isolated_nodes = list(nx.isolates(_G_undirected))
    _G_undirected.remove_nodes_from(_isolated_nodes)
    components = sorted(nx.connected_components(_G_undirected), key=len, reverse=True)
    two_largest = components[0] | components[1]
    _G_undirected = _G_undirected.subgraph(two_largest).copy()
    _G_sub = _G_undirected.copy()
    cliques = list(nx.find_cliques(_G_sub))
    _clique_sizes = {}
    for _node in _G_sub.nodes():
        _max_size = 0
        for _clique in cliques:
            if _node in _clique:
                _max_size = max(_max_size, len(_clique))
        _clique_sizes[_node] = _max_size
    _node_colors = [_clique_sizes[_node] for _node in _G_sub.nodes()]
    plt.figure(figsize=(24, 16))
    from networkx.drawing.nx_agraph import graphviz_layout
    _pos = graphviz_layout(_G_sub, prog='sfdp')
    _nodes = nx.draw_networkx_nodes(_G_sub, _pos, node_size=200, node_color=_node_colors, cmap='gist_heat', alpha=0.7, linewidths=0.5, edgecolors='black', vmin=_CLIQUE_MIN, vmax=_CLIQUE_MAX)
    nx.draw_networkx_edges(_G_sub, _pos, edge_color='gray', alpha=0.5, width=1)
    _cbar = plt.colorbar(_nodes, label='Largest Fully Connected Clique Size', shrink=0.8)
    _cbar.set_ticks(range(_CLIQUE_MIN, _CLIQUE_MAX + 1))
    _actual_max = max(_node_colors) if _node_colors else 0
    plt.style.use('dark_background')
    plt.title(f'Fully-Connected Cliques of Reciprocal Friendship Network\n({len(_G_sub.nodes())} nodes, {len(_G_sub.edges())} edges, {len(cliques)} cliques, max={_actual_max})', fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    print(f'\nClique analysis:')
    print(f'Total maximal cliques: {len(cliques)}')
    _clique_sizes_list = [len(c) for c in cliques]
    print(f'Largest clique size: {max(_clique_sizes_list)}')
    print(f'Average clique size: {np.mean(_clique_sizes_list):.2f}')
    print(f'Color scale: {_CLIQUE_MIN} to {_CLIQUE_MAX}')
    return (graphviz_layout,)


@app.cell
def _(G_aquaintance, graphviz_layout, np, nx, plt):
    _CLIQUE_MIN = 1
    _CLIQUE_MAX = 6
    _G_undirected = G_aquaintance.to_undirected(reciprocal=True)
    _isolated_nodes = list(nx.isolates(_G_undirected))
    _G_undirected.remove_nodes_from(_isolated_nodes)
    _largest_cc = max(nx.connected_components(_G_undirected), key=len)
    _G_undirected = _G_undirected.subgraph(_largest_cc).copy()
    _G_sub = _G_undirected.copy()
    cliques_1 = list(nx.find_cliques(_G_sub))
    _clique_sizes = {}
    for _node in _G_sub.nodes():
        _max_size = 0
        for _clique in cliques_1:
            if _node in _clique:
                _max_size = max(_max_size, len(_clique))
        _clique_sizes[_node] = _max_size
    _node_colors = [_clique_sizes[_node] for _node in _G_sub.nodes()]
    plt.figure(figsize=(24, 16))
    _pos = graphviz_layout(_G_sub, prog='sfdp')
    _nodes = nx.draw_networkx_nodes(_G_sub, _pos, node_size=200, node_color=_node_colors, cmap='gist_heat', alpha=0.7, linewidths=0.5, edgecolors='black', vmin=_CLIQUE_MIN, vmax=_CLIQUE_MAX)
    nx.draw_networkx_edges(_G_sub, _pos, edge_color='gray', alpha=0.5, width=1)
    _cbar = plt.colorbar(_nodes, label='Largest Fully Connected Clique Size', shrink=0.8)
    _cbar.set_ticks(range(_CLIQUE_MIN, _CLIQUE_MAX + 1))
    plt.style.use('dark_background')
    _actual_max = max(_node_colors) if _node_colors else 0
    plt.title(f'Fully-Connected Cliques of Reciprocal Aquaintance Network\n({len(_G_sub.nodes())} nodes, {len(_G_sub.edges())} edges, {len(cliques_1)} cliques, max={_actual_max})', fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    print(f'\nClique analysis:')
    print(f'Total maximal cliques: {len(cliques_1)}')
    _clique_sizes_list = [len(c) for c in cliques_1]
    print(f'Largest clique size: {max(_clique_sizes_list)}')
    print(f'Average clique size: {np.mean(_clique_sizes_list):.2f}')
    print(f'Color scale: {_CLIQUE_MIN} to {_CLIQUE_MAX}')
    return (cliques_1,)


@app.cell
def _(cliques_1):
    cliques_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    We have a ground truth of the frindship network and its groups, we can now compare this to the perception of people of said group in their network. 

    Find out if there is a difference between perceived groups and "ground-truth" / construct for friendship groups. 

    What is the distribution of deviation in perceptions from the metric obtained by the network. 

    Interesting is that each group is viewed from a multitude of viewpoints from members of said group.

    Q: Do people correlate more with reciprocal or one way groups.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _(G_aquaintance, G_friend, graphviz_layout, nx, plt):
    _G_friend_undirected = G_friend.to_undirected(reciprocal=True)
    _isolated_nodes = list(nx.isolates(_G_friend_undirected))
    _G_friend_undirected.remove_nodes_from(_isolated_nodes)
    friend_components = sorted(nx.connected_components(_G_friend_undirected), key=len, reverse=True)
    component_map = {}
    for _i, component in enumerate(friend_components):
        for _node in component:
            component_map[_node] = _i
    print(f'\nFriend graph components:')
    for _i, comp in enumerate(friend_components[:5]):
        print(f'  Component {_i}: {len(comp)} nodes')
    _G_undirected = G_aquaintance.to_undirected(reciprocal=False)
    _isolated_nodes = list(nx.isolates(_G_undirected))
    _G_undirected.remove_nodes_from(_isolated_nodes)
    _largest_cc = max(nx.connected_components(_G_undirected), key=len)
    _G_sub = _G_undirected.subgraph(_largest_cc).copy()
    nx.set_node_attributes(_G_sub, -1, 'friend_component')
    for _node in _G_sub.nodes():
        if _node in component_map:
            _G_sub.nodes[_node]['friend_component'] = component_map[_node]
    _pos = graphviz_layout(_G_sub, prog='sfdp')
    friend_edges = []
    acquaintance_only_edges = []
    for _edge in _G_sub.edges():
        if _G_friend_undirected.has_edge(_edge[0], _edge[1]):
            friend_edges.append(_edge)
        else:
            acquaintance_only_edges.append(_edge)
    print(f'\nEdge breakdown:')
    print(f'  Friendship edges: {len(friend_edges)}')
    print(f'  Acquaintance-only edges: {len(acquaintance_only_edges)}')
    print(f'  Total edges: {len(_G_sub.edges())}')
    plt.figure(figsize=(24, 20))
    component_colors = [_G_sub.nodes[_node]['friend_component'] for _node in _G_sub.nodes()]
    nx.draw_networkx_edges(_G_sub, _pos, edgelist=acquaintance_only_edges, edge_color='gray', alpha=0.5, width=1.0)
    nx.draw_networkx_edges(_G_sub, _pos, edgelist=friend_edges, edge_color='cyan', alpha=0.7, width=2.0)
    _nodes = nx.draw_networkx_nodes(_G_sub, _pos, node_size=200, node_color=component_colors, cmap='tab20', alpha=0.8, linewidths=0.5, edgecolors='black')
    plt.style.use('dark_background')
    visible_components = len(set(component_colors))
    plt.title(f'Acquaintance and Friendship Network\n({len(_G_sub.nodes())} nodes, {len(_G_sub.edges())} edges, {visible_components} friend components visible)\nCyan = Friendship edges, Gray = Acquaintance-only', fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    nodes_with_friend_component = sum((1 for c in component_colors if c >= 0))
    print(f'\nVisualization stats:')
    print(f'Nodes in acquaintance graph: {len(_G_sub.nodes())}')
    print(f'Nodes that exist in friend graph: {nodes_with_friend_component}')
    print(f'Nodes only in acquaintance graph: {len(_G_sub.nodes()) - nodes_with_friend_component}')
    print(f'Friend components represented: {visible_components}')
    return


@app.cell
def _(G_aquaintance, np, nx, plt):
    from sklearn.manifold import MDS
    _G_friend_undirected = G_aquaintance.to_undirected(reciprocal=False)
    _largest_cc = max(nx.connected_components(_G_friend_undirected), key=len)
    _G_largest = _G_friend_undirected.subgraph(_largest_cc).copy()
    _nodes = list(_G_largest.nodes())
    n = len(_nodes)
    dist_matrix = np.zeros((n, n))
    for _i, node_i in enumerate(_nodes):
        for j, node_j in enumerate(_nodes):
            if _i != j:
                dist_matrix[_i][j] = nx.shortest_path_length(_G_largest, node_i, node_j)
    dist_matrix = (dist_matrix + dist_matrix.T) / 2
    mds = MDS(n_components=2, dissimilarity='precomputed', metric=False, random_state=42)
    coords_mds = mds.fit_transform(dist_matrix)
    r_mds = np.sqrt(coords_mds[:, 0] ** 2 + coords_mds[:, 1] ** 2)
    theta_mds = np.arctan2(coords_mds[:, 1], coords_mds[:, 0])
    ssa = MDS(n_components=2, dissimilarity='precomputed', metric=True, random_state=42, max_iter=1000, eps=1e-09)
    coords_ssa = ssa.fit_transform(dist_matrix)
    r_ssa = np.sqrt(coords_ssa[:, 0] ** 2 + coords_ssa[:, 1] ** 2)
    theta_ssa = np.arctan2(coords_ssa[:, 1], coords_ssa[:, 0])
    fitted_dists_ssa = np.sqrt(((coords_ssa[:, np.newaxis, :] - coords_ssa[np.newaxis, :, :]) ** 2).sum(axis=2))
    original_dists = dist_matrix.copy()
    np.fill_diagonal(original_dists, 0)
    np.fill_diagonal(fitted_dists_ssa, 0)
    mask = original_dists > 0
    alienation = np.sqrt(np.sum((original_dists[mask] - fitted_dists_ssa[mask]) ** 2) / np.sum(original_dists[mask] ** 2))
    _fig = plt.figure(figsize=(27, 12))
    ax1 = _fig.add_subplot(121, projection='polar')
    ax2 = _fig.add_subplot(122, projection='polar')
    for _edge in _G_largest.edges():
        _i = _nodes.index(_edge[0])
        j = _nodes.index(_edge[1])
        ax1.plot([theta_mds[_i], theta_mds[j]], [r_mds[_i], r_mds[j]], 'gray', alpha=0.2, linewidth=0.5)
    ax1.scatter(theta_mds, r_mds, s=500, c='lightblue', edgecolors='black', linewidth=2, alpha=0.8)
    for _i, _node in enumerate(_nodes):
        ax1.text(theta_mds[_i], r_mds[_i], str(_node), ha='center', va='center', fontsize=8, weight='bold')
    ax1.set_title(f'MDS (Non-Metric) Polar\nStress: {mds.stress_:.2f}', fontsize=14, weight='bold', pad=20)
    for _edge in _G_largest.edges():
        _i = _nodes.index(_edge[0])
        j = _nodes.index(_edge[1])
        ax2.plot([theta_ssa[_i], theta_ssa[j]], [r_ssa[_i], r_ssa[j]], 'gray', alpha=0.2, linewidth=0.5)
    ax2.scatter(theta_ssa, r_ssa, s=500, c='lightcoral', edgecolors='black', linewidth=2, alpha=0.8)
    for _i, _node in enumerate(_nodes):
        ax2.text(theta_ssa[_i], r_ssa[_i], str(_node), ha='center', va='center', fontsize=8, weight='bold')
    ax2.set_title(f'SSA (Metric) Polar\nAlienation: {alienation:.4f}', fontsize=14, weight='bold', pad=20)
    plt.tight_layout()
    plt.show()
    print(f'Nodes: {n}')
    print(f'\nMDS Stress: {mds.stress_:.2f}')
    print(f'SSA Alienation: {alienation:.4f} (< 0.15 = excellent, < 0.20 = good, < 0.25 = acceptable)')
    return


@app.cell
def _(G_friend, G_study, np, nx, plt):
    from scipy.linalg import fractional_matrix_power
    from scipy.sparse.linalg import eigsh
    _G_friend_undirected = G_study.to_undirected(reciprocal=False)
    _largest_cc = max(nx.connected_components(_G_friend_undirected), key=len)
    _G_largest = _G_friend_undirected.subgraph(_largest_cc).copy()
    A = nx.to_numpy_array(G_friend)
    np.fill_diagonal(A, 0)
    D = np.diag(A.sum(axis=1))
    L = D - A
    D_inv_sqrt = fractional_matrix_power(D, -0.5)
    L_norm = D_inv_sqrt @ L @ D_inv_sqrt
    k = 2
    eigvals, eigvecs = eigsh(L_norm, k=k + 1, which='SM')
    embedding_orig = eigvecs[:, 1:k + 1]
    _fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    axes[0].scatter(embedding_orig[:, 0], embedding_orig[:, 1], s=150, c='tomato')
    for _i, (x, y) in enumerate(embedding_orig):
        axes[0].text(x, y, str(_i), fontsize=9, ha='center', va='center', color='white', weight='bold')
    axes[0].set_title('Original Graph Embedding')
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
