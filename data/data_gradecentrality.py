import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import networkx as nx
    import ast
    import seaborn as sns
    import numpy as np
    import matplotlib.pyplot as plt
    from assortativity_permutation_test import run_assortativity_with_permutation_test
    return ast, np, nx, pd, plt, run_assortativity_with_permutation_test, sns


@app.cell
def _(mo):
    mo.md(r"""
    ***
    ## Edges
    """)
    return


@app.cell
def _(ast, pd):
    df_edges = pd.read_csv("/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/data/W2/data_edges.csv")

    for col in df_edges.columns[1:]:
        df_edges[col] = df_edges[col].apply(ast.literal_eval)
    return (df_edges,)


@app.cell
def _(df_edges, nx):
    def network_loom(df_edge, col_relation, col_weights=None, attr_dict=None):
        edge_list = []
        for _, row in df_edge.iterrows():
            source = row['Label']
            targets = row[col_relation]

            for target in targets:
                if col_weights:
                    # col_weights has (target, weight) tuples - use directly
                    target_weights = row[col_weights]
                    for (target, weight) in target_weights:
                        edge_list.append((source, target, {'weight': weight}))
                else:
                    # Fallback: unweighted from aquaintance
                    edge_list.append((source, target))

        G = nx.DiGraph()
        G.add_edges_from(edge_list)
        G.remove_edges_from(nx.selfloop_edges(G))

        if attr_dict:
            for attr_name, attr_values in attr_dict.items():
                nx.set_node_attributes(G, attr_values, name=attr_name)

        return G

    G_acquaintance = network_loom(df_edges, 'Aquaintance', col_weights="Grade")
    #G_friend = network_loom(df_edges, 'Friend', col_weights="Grade")

    # # Check weights now
    # for u, v, data in list(G_friend.edges(data=True))[:5]:
    #     print(f"{u} -> {v}: weight={data['weight']}")
    return (G_acquaintance,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Attributes
    """)
    return


@app.cell
def _(pd):
    df_nodes = pd.read_csv("W2/data_filtered.csv")
    df_mock = pd.read_csv("Tutorial_Exam/mockexam_fix.csv")
    return df_mock, df_nodes


@app.cell
def _(G_acquaintance, df_mock, df_nodes, nx):
    attrs = {
        'Grade_Self': dict(zip(df_nodes['participant.label'], df_nodes["app_studium.1.player.grade"])),
        'Grade_Mock': dict(zip(df_mock['Code'], df_mock["GradeMock"])),
    }

    for attr_name, attr_values in attrs.items():
        # Filter: only keep non-zero values
        filtered_values = {k: v for k, v in attr_values.items() if v != 0}

        nx.set_node_attributes(G_acquaintance, filtered_values, name=attr_name)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ***
    """)
    return


@app.cell
def _(G_acquaintance, df_mock, df_nodes, np, nx, pd):
    def aggregate_peer_effects(G):
        """
        Extract peer effect proxies for each node from incoming edges
        """
        peer_stats = {}

        # Centrality measures (computed once for all nodes)
        betweenness = nx.betweenness_centrality(G, weight=None, normalized=False)
        closeness = nx.closeness_centrality(G, distance=None)
        pagerank = nx.pagerank(G, weight=None)
        katz = nx.katz_centrality(G, normalized=False)

        # Assign to graph
        nx.set_node_attributes(G, betweenness, 'betweenness')
        nx.set_node_attributes(G, closeness, 'closeness')
        nx.set_node_attributes(G, pagerank, 'pagerank')
        nx.set_node_attributes(G, katz, 'katz')

        for node in G.nodes():
            incoming_weights = [G[source][node]['weight'] 
                               for source in G.predecessors(node) 
                               if G[source][node]['weight'] != 0]
            outgoing_weights = [G[node][target]['weight'] 
                               for target in G.successors(node) 
                               if G[node][target]['weight'] != 0]

            # Build stats dict with both peer effects and centrality
            if incoming_weights:
                peer_stats[node] = {
                    # 'peer_median': np.median(incoming_weights),
                    # 'peer_std': np.std(incoming_weights),

                    'Grade_median_in': np.median(incoming_weights)if incoming_weights else np.nan,
                    'Grade_median_out': np.median(outgoing_weights) if outgoing_weights else np.nan,

                    'Grade_mean_in': np.mean(incoming_weights) if incoming_weights else np.nan,
                    'Grade_mean_out': np.mean(outgoing_weights) if outgoing_weights else np.nan,

                    'count_in': len(incoming_weights),
                    'count_out': len(incoming_weights),

                    'betweenness': betweenness.get(node, 0),
                    'closeness': closeness.get(node, 0),
                    'pagerank': pagerank.get(node, 0),
                    'katz': katz.get(node, 0),
                }
            else:
                peer_stats[node] = {
                    'Grade_median_in': np.nan,
                    'Grade_median_out': np.nan,

                    'Grade_mean_in': np.nan,
                    'Grade_mean_out': np.nan,

                    'count_in': np.nan,
                    'count_out': np.nan,

                    'betweenness': betweenness.get(node, 0),
                    'closeness': closeness.get(node, 0),
                    'pagerank': pagerank.get(node, 0),
                    'katz': katz.get(node, 0),
                }

        return pd.DataFrame(peer_stats).T

    # Use it
    peer_effects_acq = aggregate_peer_effects(G_acquaintance)
    #peer_effects_study = aggregate_peer_effects(G_friend)

    # Merge with your outcome
    results = df_mock[['Code', 'GradeMock']].set_index('Code')
    results = results.join(df_nodes[['participant.label', "app_studium.1.player.grade"]].set_index('participant.label'), how='left')
    results = results.join(peer_effects_acq, how='left', rsuffix='_acquaintance')
    #results = results.join(peer_effects_study, how='left', rsuffix='_friend')
    return (results,)


@app.cell
def _():
    results = results[results["app_studium.1.player.grade"] != 0 & 
                      (results["app_studium.1.player.grade"].notna())]
    results = results[(results["Grade_mean_in"].notna())]
    return (results,)


@app.cell
def _(results, sns):
    # Rename for readability
    cols_to_plot = results[['pagerank', 'katz', 'closeness', 'betweenness']]

    cols_to_plot = cols_to_plot.rename(columns={
        'pagerank': 'Pagerank',
        'katz': 'Katz',
        'closeness': 'Closeness',
        'betweenness': 'Betweenness',
    })

    sns.heatmap(cols_to_plot.corr(), annot=True, fmt='.2f', cmap='coolwarm', 
                cbar_kws={'label': 'Correlation'}, vmin=-1, vmax=1)
    return


@app.cell
def _(results, sns):
    # Rename for readability
    cols_to_plot = results[['GradeMock', "app_studium.1.player.grade", 
                            'Grade_mean_in','Grade_median_in', 
                            'Grade_mean_out', 'Grade_median_out', 'pagerank', 'katz', 'closeness', 'betweenness']]

    cols_to_plot = cols_to_plot.rename(columns={
        'GradeMock': 'Mock Grade',
        'app_studium.1.player.grade': 'Self Grade',
        'Grade_mean_in': 'Peer Grade Mean (In)',
        'Grade_median_in': 'Peer Grade Median (In)',
        'Grade_mean_out': 'Peer Grade Mean (Out)',
        'Grade_median_out': 'Peer Grade Median (Out)',
        'pagerank': 'Pagerank',
        'katz': 'Katz',
        'closeness': 'Closeness',
        'betweenness': 'Betweenness',
    })

    sns.heatmap(cols_to_plot.corr(), annot=True, fmt='.2f', cmap='coolwarm', 
                cbar_kws={'label': 'Correlation'}, vmin=-1, vmax=1)
    return


@app.cell
def _(G_acquaintance, run_assortativity_with_permutation_test):
    # Your existing networks dict
    networks = {
        'Acquaintance': G_acquaintance,
        #'Friend': G_friend,
    }

    # Run with permutation test
    df_results, figs = run_assortativity_with_permutation_test(
        networks, 
        attribute='Grade_Self', 
        n_permutations=1000  # Adjust for speed/precision tradeoff
    )

    print(df_results)
    return


@app.cell
def _(G_acquaintance, run_assortativity_with_permutation_test):
    # Your existing networks dict
    networks = {
        'Acquaintance': G_acquaintance,
        #'Friend': G_friend,
    }

    # Run with permutation test
    df_results, figs = run_assortativity_with_permutation_test(
        networks, 
        attribute='Grade_Mock', 
        n_permutations=1000  # Adjust for speed/precision tradeoff
    )

    print(df_results)
    return


@app.cell
def _(G_acquaintance, nx, results):
    attrs = {
        'Grade_Received': dict(zip(results.index, results["Grade_mean_in"])),
        'Grade_Given': dict(zip(results.index, results["Grade_mean_out"])),
    }

    for attr_name, attr_values in attrs.items():
        nx.set_node_attributes(G_acquaintance, attr_values, name=attr_name)
    return


@app.cell
def _(G_acquaintance, plt):
    from explore_grade_discrepancy import analyze_grade_discrepancy, visualize_grade_discrepancy, check_data_quality_issues

    df_grades, stats = analyze_grade_discrepancy(G_acquaintance, 
                                                 mock_attr='Grade_Mock',
                                                 self_attr='Grade_Self',
                                                 network_name='Acquaintance')

    check_data_quality_issues(df_grades)

    fig = visualize_grade_discrepancy(df_grades, self_attr='Grade_Self',)
    plt.show()
    return (
        analyze_grade_discrepancy,
        check_data_quality_issues,
        stats,
        visualize_grade_discrepancy,
    )


@app.cell
def _(
    G_acquaintance,
    analyze_grade_discrepancy,
    check_data_quality_issues,
    plt,
    visualize_grade_discrepancy,
):
    df_grades, stats = analyze_grade_discrepancy(G_acquaintance, 
                                                 mock_attr='Grade_Mock',
                                                 self_attr='Grade_Received',
                                                 network_name='Acquaintance Network')

    check_data_quality_issues(df_grades)

    fig = visualize_grade_discrepancy(df_grades, self_attr='Grade_Received',)
    plt.show()
    return (stats,)


@app.cell
def _(mo):
    mo.md(r"""
    ***
    ## Edge Based
    """)
    return


@app.cell
def _():
    from sklearn.preprocessing import StandardScaler
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    import scipy.stats as stats
    from statsmodels.formula.api import mixedlm
    return StandardScaler, mixedlm, ols, stats


@app.cell
def _(G_acquaintance, StandardScaler, np, pd):
    def edge_level_analysis(G):
        """
        Convert network to edge-level dataset for analysis
        Each row = one assessment edge
        """
        edge_data = []

        for u, v, data in G.edges(data=True):
            target_grade_mock = G.nodes[v].get('Grade_Mock', np.nan)
            target_grade_self = G.nodes[v].get('Grade_Self', np.nan)

            target_pagerank = G.nodes[v].get('pagerank', np.nan)
            target_closeness = G.nodes[v].get('closeness', np.nan)
            target_betweenness = G.nodes[v].get('betweenness', np.nan)
            target_katz = G.nodes[v].get('katz', np.nan)

            assessment = data['weight']

            edge_data.append({
                'source': u,
                'target': v,

                'Grade_Received': assessment,
                'Grade_Mock': target_grade_mock,
                'Grade_Self': target_grade_self,

                'pagerank': target_pagerank,
                'closeness': target_closeness,
                'betweenness': target_betweenness,
                'katz': target_katz,

                #'diff_ReceivedMock': assessment - target_grade_mock,  # How far off was the assessment?
                #'diff_ReceivedSelf': assessment - target_grade_self,  # How far off was the assessment?
                #'diff_SelfMock': target_grade_self - target_grade_mock,  # How far off was the assessment?
            })

        edge_df = pd.DataFrame(edge_data)

        edge_df = edge_df[(edge_df["Grade_Received"].notna())]
        edge_df = edge_df[(edge_df["Grade_Mock"].notna())]
        edge_df = edge_df[(edge_df["Grade_Self"].notna())]
        edge_df = edge_df[edge_df["Grade_Received"] != 0]
        edge_df = edge_df[edge_df["Grade_Mock"] != 0]
        edge_df = edge_df[edge_df["Grade_Self"] != 0]


        return edge_df

    # Build edge-level datasets
    edges_acq = edge_level_analysis(G_acquaintance)                   

    # Correlation at edge level
    print("Acquaintance network:")
    print(edges_acq[['Grade_Received', 'Grade_Mock']].corr())
    print(f"N edges: {len(edges_acq)}")

    scaler = StandardScaler()
    edges_acq['pagerank_std'] = scaler.fit_transform(edges_acq[['pagerank']])
    edges_acq['closeness_std'] = scaler.fit_transform(edges_acq[['closeness']])
    edges_acq['betweenness_std'] = scaler.fit_transform(edges_acq[['betweenness']])
    edges_acq['katz_std'] = scaler.fit_transform(edges_acq[['katz']])
    return (edges_acq,)


@app.cell
def _(edges_acq):
    import numpy as np
    from scipy import stats
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    centralities = ['pagerank_std', 'katz_std', 'betweenness_std', 'closeness_std']
    titles = ['PageRank', 'Katz', 'Betweenness', 'Closeness']

    for ax, cent, title in zip(axes, centralities, titles):
        ax.scatter(edges_acq['Grade_Self'], edges_acq[cent], alpha=0.5)

        # Linear regression
        slope, intercept, r_value, p_value, std_err = stats.linregress(edges_acq['Grade_Self'], edges_acq[cent])
        line_x = np.array([edges_acq['Grade_Self'].min(), edges_acq['Grade_Self'].max()])
        line_y = slope * line_x + intercept
        ax.plot(line_x, line_y, 'r-', linewidth=2)

        # Regression info box
        info_text = f'y = {slope:.4f}x + {intercept:.4f}\nR² = {r_value**2:.4f}\np = {p_value:.2e}\nStd Err = {std_err:.4f}'
        ax.text(0.05, 0.95, info_text, transform=ax.transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                fontsize=8, family='monospace')

        ax.set_xlabel('Self Grade')
        ax.set_ylabel(f'{title} (z-score)')
        ax.set_title(title)

    plt.tight_layout()
    plt.show()
    return np, plt, stats


@app.cell
def _(edges_acq):
    edges_acq
    return


@app.cell
def _(edges_acq):
    # What differs by pagerank?
    by_pagerank = edges_acq.groupby('target').agg({
        'katz_std': 'mean',
        'betweenness_std': 'mean',
        'closeness_std': 'mean',
        'pagerank_std': 'mean',
        'Grade_Self': 'mean',
        'Grade_Mock': 'mean',
        'Grade_Received': 'mean'
    }).corr()
    print(by_pagerank)
    return


@app.cell
def _(edges_acq, ols):
    model_base = ols(
        'Grade_Mock ~ Grade_Received + Grade_Self + pagerank_std',
        data=edges_acq
    ).fit()
    print(model_base.summary())
    return


@app.cell
def _(edges_acq, ols):
    model_base_fixed = ols(
        'Grade_Mock ~ C(target) + Grade_Received + Grade_Self + pagerank_std',
        data=edges_acq
    ).fit()
    print(model_base_fixed.summary())
    return


@app.cell
def _(edges_acq, mixedlm):
    model_simple = mixedlm(
        'Grade_Mock ~ Grade_Received + Grade_Self + pagerank_std',
        data=edges_acq,
        groups=edges_acq['target']
    ).fit()
    print(model_simple.summary())

    # Compare coefficients
    print(f"With slopes: Grade_Self = {model_simple.fe_params['Grade_Self']:.4f}")
    print(f"Simple: Grade_Self = {model_simple.fe_params['Grade_Self']:.4f}")
    return


@app.cell
def _(edges_acq, mixedlm):
    # Refit
    model_central = mixedlm(
        'Grade_Mock ~ Grade_Received + Grade_Self + pagerank_std',
        data=edges_acq,
        groups=edges_acq['target'],
        re_formula='~Grade_Self'
    ).fit()
    print(model_central.summary())
    return (model_central,)


@app.cell
def _(model_central):
    # Then extract: which students are well-calibrated vs. delusional?
    random_effects_slopes = model_central.random_effects
    for target_id, effects in list(random_effects_slopes.items())[:15]:
        intercept = effects['Group']
        slope = effects['Grade_Self']
        print(f"{target_id}: intercept={intercept:.3f}, Grade_Self_slope={slope:.3f}")
    return (random_effects_slopes,)


@app.cell
def _(edges_acq, mixedlm):
    model_slopes = mixedlm(
        'Grade_Mock ~ Grade_Received + Grade_Self + pagerank_std',
        data=edges_acq,
        groups=edges_acq['target'],
        re_formula='~Grade_Self + pagerank_std' 
    ).fit()
    print(model_slopes.summary())
    return


@app.cell
def _(edges_acq, pd, random_effects_slopes, stats):
    # Test the interaction implicitly
    # Does pagerank predict the random slope?
    slopes_df = pd.DataFrame([
        {'target': t, 'slope': e['Grade_Self']} 
        for t, e in random_effects_slopes.items()  # from slopes model
    ])

    target_pagerank = edges_acq.groupby('target')['pagerank_std'].first().reset_index()
    slopes_with_pr = slopes_df.merge(target_pagerank, on='target')


    corr, p = stats.pearsonr(slopes_with_pr['slope'], slopes_with_pr['pagerank_std'])
    print(f"Slope-PageRank correlation: r={corr:.3f}, p={p:.4f}")
    return


@app.cell
def _(edges_acq, model_central, pd):
    # Extract random slopes
    random_effects_slopes = model_central.random_effects
    slopes_df = pd.DataFrame([
        {'target': t, 'slope': e['Grade_Self']} 
        for t, e in random_effects_slopes.items()
    ])

    # What student-level attributes correlate with calibration?
    # (Do you have GPA, demographic data, survey responses?)
    target_outcomes = edges_acq.groupby('target').agg({
        'Grade_Mock': 'mean',
        'Grade_Self': 'mean',
        'Grade_Received': 'mean',
        'pagerank_std': 'first',
    }).reset_index()

    slopes_with_outcomes = slopes_df.merge(target_outcomes, on='target')

    # Who's well-calibrated?
    print(slopes_with_outcomes.sort_values('slope', ascending=False).head(10))
    print("\n" + "="*50)
    print(slopes_with_outcomes.sort_values('slope', ascending=True).head(10))
    return (random_effects_slopes,)


if __name__ == "__main__":
    app.run()
