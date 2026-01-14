import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from scipy import stats

def permutation_test_assortativity(G, attribute, n_permutations=1000, method='pearson'):
    """
    Test assortativity significance via attribute randomization.
    
    The null model: random assignment of attributes to nodes.
    If observed > null, nodes with similar attributes are clustering.
    
    Args:
        G: NetworkX graph
        attribute: node attribute name (string)
        n_permutations: number of randomizations
        method: 'pearson' or 'nx' (NetworkX numeric_assortativity_coefficient)
    
    Returns:
        dict with observed, null distribution, p-value, effect size
    """
    
    # Extract attribute values (handle missing data)
    valid_nodes = [n for n, d in G.nodes(data=True) if attribute in d]
    H = G.subgraph(valid_nodes).copy()
    
    if H.number_of_edges() == 0:
        return {
            'method': method,
            'observed': np.nan,
            'null_mean': np.nan,
            'null_std': np.nan,
            'p_value': np.nan,
            'effect_size': np.nan,
            'n_nodes': len(valid_nodes),
            'n_edges': 0,
            'error': 'No edges in subgraph'
        }
    
    # Calculate observed assortativity
    attr_values = [H.nodes[n][attribute] for n in H.nodes()]
    
    if method == 'nx':
        try:
            observed = nx.numeric_assortativity_coefficient(H, attribute)
            if pd.isna(observed):
                observed = np.nan
        except:
            observed = np.nan
    elif method == 'pearson':
        edge_grades_source = [H.nodes[u][attribute] for u, v in H.edges()]
        edge_grades_target = [H.nodes[v][attribute] for u, v in H.edges()]
        observed = pd.Series(edge_grades_source).corr(pd.Series(edge_grades_target))
    
    # Permutation testing
    null_distribution = []
    
    for i in range(n_permutations):
        # Shuffle attribute values across nodes
        shuffled_values = np.random.permutation(attr_values)
        
        # Create copy of H with shuffled attributes
        H_shuffled = H.copy()
        for j, node in enumerate(H.nodes()):
            H_shuffled.nodes[node][f'{attribute}_shuffled'] = shuffled_values[j]
        
        # Calculate assortativity on shuffled version
        if method == 'nx':
            try:
                assort_perm = nx.numeric_assortativity_coefficient(H_shuffled, f'{attribute}_shuffled')
                if not pd.isna(assort_perm):
                    null_distribution.append(assort_perm)
            except:
                pass
        elif method == 'pearson':
            edge_vals_source = [H_shuffled.nodes[u][f'{attribute}_shuffled'] for u, v in H_shuffled.edges()]
            edge_vals_target = [H_shuffled.nodes[v][f'{attribute}_shuffled'] for u, v in H_shuffled.edges()]
            assort_perm = pd.Series(edge_vals_source).corr(pd.Series(edge_vals_target))
            if not pd.isna(assort_perm):
                null_distribution.append(assort_perm)
    
    null_dist = np.array(null_distribution)
    
    # Calculate p-value (two-tailed)
    if len(null_dist) > 0:
        p_value = np.mean(np.abs(null_dist - np.mean(null_dist)) >= np.abs(observed - np.mean(null_dist)))
        # One-tailed alternatives:
        # p_greater = np.mean(null_dist >= observed)  # observed > null
        # p_less = np.mean(null_dist <= observed)     # observed < null
        
        effect_size = (observed - np.mean(null_dist)) / (np.std(null_dist) + 1e-10)  # Cohen's d
    else:
        p_value = np.nan
        effect_size = np.nan
    
    return {
        'method': method,
        'observed': observed,
        'null_mean': np.mean(null_dist) if len(null_dist) > 0 else np.nan,
        'null_std': np.std(null_dist) if len(null_dist) > 0 else np.nan,
        'p_value': p_value,
        'effect_size': effect_size,
        'n_nodes': len(valid_nodes),
        'n_edges': H.number_of_edges(),
        'null_distribution': null_dist,
        'n_permutations': len(null_dist)
    }


def visualize_permutation_test(result, attribute_name='Grade'):
    """Visualize null distribution vs observed assortativity."""
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    null_dist = result['null_distribution']
    observed = result['observed']
    
    # Histogram of null distribution
    ax.hist(null_dist, bins=40, alpha=0.7, color='steelblue', edgecolor='black', label='Null distribution')
    ax.axvline(np.mean(null_dist), color='steelblue', linestyle='--', linewidth=2, label=f"Null mean: {np.mean(null_dist):.4f}")
    
    # Observed value
    ax.axvline(observed, color='crimson', linestyle='-', linewidth=3, label=f"Observed: {observed:.4f}")
    
    # Formatting
    ax.set_xlabel('Assortativity Coefficient', fontsize=11)
    ax.set_ylabel('Frequency', fontsize=11)
    ax.set_title(f'Permutation Test: {attribute_name} Assortativity\n({result["method"].upper()}, n={result["n_permutations"]} permutations)', 
                 fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)
    
    # Add p-value and effect size to plot
    textstr = f"p-value: {result['p_value']:.4f}\nEffect size (Cohen's d): {result['effect_size']:.4f}\nn_nodes: {result['n_nodes']}, n_edges: {result['n_edges']}"
    ax.text(0.98, 0.97, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    return fig


# ============================================================================
# INTEGRATION WITH YOUR EXISTING CODE
# ============================================================================

def run_assortativity_with_permutation_test(networks, attribute='Grade_Mock', n_permutations=1000):
    """
    Run assortativity analysis with permutation testing for multiple networks.
    """
    
    results_list = []
    figures = {}
    
    for network_name, G in networks.items():
        print(f"\n{'='*60}")
        print(f"{network_name} Network - Assortativity Permutation Test")
        print(f"{'='*60}")
        print(f"Total nodes: {G.number_of_nodes()}")
        print(f"Total edges: {G.number_of_edges()}")
        
        # Filter to nodes with attribute
        valid_nodes = [n for n, d in G.nodes(data=True) if attribute in d]
        H = G.subgraph(valid_nodes).copy()
        
        print(f"Nodes with {attribute}: {len(valid_nodes)}")
        print(f"Edges in filtered subgraph: {H.number_of_edges()}")
        
        if H.number_of_edges() == 0:
            print("⚠ No edges - skipping")
            results_list.append({
                'network': network_name,
                'method': 'both',
                'n_nodes': len(valid_nodes),
                'n_edges': 0,
                'error': 'No edges'
            })
            continue
        
        # Check attribute distribution
        attr_vals = [d for n, d in H.nodes(data=attribute)]
        print(f"\nAttribute '{attribute}' distribution:")
        print(f"  Unique values: {len(set(attr_vals))}")
        print(f"  Range: [{min(attr_vals):.2f}, {max(attr_vals):.2f}]")
        print(f"  Mean: {np.mean(attr_vals):.4f}")
        print(f"  Std: {np.std(attr_vals):.4f}")
        
        # Test both methods
        for method in ['pearson', 'nx']:
            print(f"\n--- Method: {method.upper()} ---")
            
            result = permutation_test_assortativity(H, attribute, n_permutations=n_permutations, method=method)
            
            print(f"Observed assortativity: {result['observed']:.6f}")
            print(f"Null mean: {result['null_mean']:.6f}")
            print(f"Null std: {result['null_std']:.6f}")
            print(f"P-value (two-tailed): {result['p_value']:.6f}")
            print(f"Effect size (Cohen's d): {result['effect_size']:.4f}")
            print(f"Permutations completed: {result['n_permutations']}/{n_permutations}")
            
            # Interpretation
            if result['p_value'] < 0.05:
                print(f"✓ SIGNIFICANT: Pattern stronger than random (p < 0.05)")
            else:
                print(f"✗ NOT SIGNIFICANT: Pattern could be due to chance (p ≥ 0.05)")
            
            result['network'] = network_name
            results_list.append(result)
            
            # Visualize
            fig = visualize_permutation_test(result, attribute_name=attribute)
            figures[f"{network_name}_{method}"] = fig
    
    return pd.DataFrame(results_list), figures


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Assume you have networks dict already defined:
    # networks = {'Acquaintance': G_acquaintance, ...}
    
    # Run analysis
    # df_results, figs = run_assortativity_with_permutation_test(networks, n_permutations=1000)
    # print("\n" + "="*60)
    # print("SUMMARY TABLE")
    # print("="*60)
    # print(df_results.to_string())
    
    pass