import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def analyze_grade_discrepancy(G, mock_attr='Grade_Mock', self_attr='Grade_Received', network_name='Network'):
    """
    Analyze the relationship between mock exam grades and self-attributed grades.
    Includes correlation, bias direction, and potential explanations.
    """
    
    # Extract nodes with both attributes
    valid_nodes = [n for n, d in G.nodes(data=True) 
                   if mock_attr in d and self_attr in d]
    
    if len(valid_nodes) == 0:
        print(f"No nodes with both {mock_attr} and {self_attr}")
        return None
    
    # Get the grades
    mock_grades = [G.nodes[n][mock_attr] for n in valid_nodes]
    self_grades = [G.nodes[n][self_attr] for n in valid_nodes]
    
    # Create DataFrame for easier analysis
    df_grades = pd.DataFrame({
        'mock': mock_grades,
        'self': self_grades,
        'node_id': valid_nodes
    })
    
    # Calculate discrepancy (self - mock)
    df_grades['discrepancy'] = df_grades['self'] - df_grades['mock']
    df_grades['abs_discrepancy'] = np.abs(df_grades['discrepancy'])
    
    print(f"\n{'='*70}")
    print(f"{network_name} - Grade Discrepancy Analysis")
    print(f"{'='*70}")
    print(f"N students with both grades: {len(valid_nodes)}")
    
    # Basic statistics
    print(f"\n--- {mock_attr} ---")
    print(f"  Mean: {df_grades['mock'].mean():.4f}")
    print(f"  Std:  {df_grades['mock'].std():.4f}")
    print(f"  Min/Max: [{df_grades['mock'].min():.2f}, {df_grades['mock'].max():.2f}]")

    print(f"\n--- {self_attr} ---")
    print(f"  Mean: {df_grades['self'].mean():.4f}")
    print(f"  Std:  {df_grades['self'].std():.4f}")
    print(f"  Min/Max: [{df_grades['self'].min():.2f}, {df_grades['self'].max():.2f}]")
    
    print(f"\n--- Discrepancy ({self_attr} - {mock_attr}) ---")
    print(f"  Mean: {df_grades['discrepancy'].mean():.4f}")
    print(f"  Std:  {df_grades['discrepancy'].std():.4f}")
    print(f"  Min/Max: [{df_grades['discrepancy'].min():.2f}, {df_grades['discrepancy'].max():.2f}]")
    
    # Count bias direction
    overestimate = (df_grades['discrepancy'] > 0).sum()
    underestimate = (df_grades['discrepancy'] < 0).sum()
    accurate = (df_grades['discrepancy'] == 0).sum()
    
    print(f"\n--- Bias Direction ---")
    print(f"  Overestimate {self_attr} ({self_attr} > {mock_attr}): {overestimate} ({100*overestimate/len(df_grades):.1f}%)")
    print(f"  Underestimate {self_attr} ({self_attr} < {mock_attr}): {underestimate} ({100*underestimate/len(df_grades):.1f}%)")
    print(f"  Accurate ({self_attr} ≈ {mock_attr}): {accurate}")
    
    # Correlation analysis
    corr_pearson, p_pearson = stats.pearsonr(df_grades['mock'], df_grades['self'])
    corr_spearman, p_spearman = stats.spearmanr(df_grades['mock'], df_grades['self'])
    
    print(f"\n--- Correlation: {mock_attr} vs {self_attr} ---")
    print(f"  Pearson r: {corr_pearson:.6f} (p={p_pearson:.6f})")
    print(f"  Spearman ρ: {corr_spearman:.6f} (p={p_spearman:.6f})")
    
    if corr_pearson < 0:
        print(f"  ⚠ NEGATIVE correlation detected!")
        print(f"     → Higher mock grades = lower self-ratings (or vice versa)")
        print(f"     → This suggests systematic bias or possible data quality issue")
    elif corr_pearson > 0.8:
        print(f"  ✓ Strong positive correlation: grades track well")
    else:
        print(f"  ? Weak correlation: self-rating diverges from actual performance")
    
    # Is discrepancy correlated with performance level?
    corr_disc_mock, p_disc_mock = stats.pearsonr(df_grades['mock'], df_grades['discrepancy'])
    print(f"\n--- Discrepancy vs {mock_attr} Performance ---")
    print(f"  Correlation: {corr_disc_mock:.6f} (p={p_disc_mock:.6f})")
    if corr_disc_mock > 0.3:
        print(f"  → Better students tend to underestimate themselves (or vice versa)")
    elif corr_disc_mock < -0.3:
        print(f"  → Better students tend to overestimate themselves (classic Dunning-Kruger?)")
    else:
        print(f"  → Bias is fairly uniform across performance levels")
    
    return df_grades, {
        'corr_pearson': corr_pearson,
        'p_pearson': p_pearson,
        'corr_spearman': corr_spearman,
        'p_spearman': p_spearman,
        'corr_disc_mock': corr_disc_mock,
        'p_disc_mock': p_disc_mock,
        'mean_discrepancy': df_grades['discrepancy'].mean(),
        'std_discrepancy': df_grades['discrepancy'].std(),
        'overestimate_pct': 100*overestimate/len(df_grades),
        'underestimate_pct': 100*underestimate/len(df_grades)
    }


def visualize_grade_discrepancy(df_grades, network_name='Aquaintance Network', mock_attr='Grade_Mock', self_attr='Grade_Received'):
    """
    Create comprehensive visualization of grade discrepancy.
    """
    
    fig, axes = plt.subplots(2, 2, figsize=(13, 11))
    
    # [0, 0] Scatter plot with diagonal
    ax = axes[0, 0]
    ax.scatter(df_grades['mock'], df_grades['self'], alpha=0.6, s=60, edgecolors='black', linewidth=0.5)
    
    # Add diagonal (perfect agreement)
    min_val = min(df_grades['mock'].min(), df_grades['self'].min())
    max_val = max(df_grades['mock'].max(), df_grades['self'].max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect agreement', alpha=0.7)
    
    ax.set_xlabel(mock_attr, fontsize=11)
    ax.set_ylabel(self_attr, fontsize=11)
    ax.set_title(f'{network_name}\n{mock_attr} vs {self_attr}', fontsize=12, fontweight='bold')
    ax.legend()
    ax.grid(alpha=0.3)
    
    # [0, 1] Discrepancy histogram
    ax = axes[0, 1]
    ax.hist(df_grades['discrepancy'], bins=20, alpha=0.7, color='steelblue', edgecolor='black')
    ax.axvline(0, color='red', linestyle='--', linewidth=2, label='No bias')
    ax.axvline(df_grades['discrepancy'].mean(), color='darkgreen', linestyle='-', linewidth=2, 
               label=f'Mean discrepancy: {df_grades["discrepancy"].mean():.3f}')
    
    ax.set_xlabel(f'Discrepancy ({self_attr} - {mock_attr})', fontsize=11)
    ax.set_ylabel('Count', fontsize=11)
    ax.set_title(f'Distribution of {self_attr} Bias', fontsize=12, fontweight='bold')
    ax.legend()
    ax.grid(alpha=0.3)
    
    # [1, 0] Bland-Altman plot (agreement plot)
    ax = axes[1, 0]
    mean_grades = (df_grades['mock'] + df_grades['self']) / 2
    
    ax.scatter(mean_grades, df_grades['discrepancy'], alpha=0.6, s=60, edgecolors='black', linewidth=0.5)
    
    # Mean difference line
    mean_diff = df_grades['discrepancy'].mean()
    ax.axhline(mean_diff, color='blue', linestyle='-', linewidth=2, label=f'Mean diff: {mean_diff:.3f}')
    
    # Limits of agreement (±1.96 SD)
    std_diff = df_grades['discrepancy'].std()
    ax.axhline(mean_diff + 1.96*std_diff, color='red', linestyle='--', linewidth=1.5, alpha=0.7)
    ax.axhline(mean_diff - 1.96*std_diff, color='red', linestyle='--', linewidth=1.5, alpha=0.7, 
               label=f'Limits of agreement')
    ax.axhline(0, color='gray', linestyle=':', linewidth=1)
    
    ax.set_xlabel(f'Mean Grade ({mock_attr} + {self_attr}) / 2', fontsize=11)
    ax.set_ylabel(f'Difference ({self_attr} - {mock_attr})', fontsize=11)
    ax.set_title('Bland-Altman Agreement Plot', fontsize=12, fontweight='bold')
    ax.legend()
    ax.grid(alpha=0.3)
    
    # [1, 1] Discrepancy vs Performance
    ax = axes[1, 1]
    
    # Color by discrepancy direction
    colors = ['green' if x > 0 else 'red' for x in df_grades['discrepancy']]
    ax.scatter(df_grades['mock'], df_grades['discrepancy'], alpha=0.6, s=60, c=colors, edgecolors='black', linewidth=0.5)
    
    ax.axhline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel(mock_attr, fontsize=11)
    ax.set_ylabel(f'Discrepancy ({self_attr} - {mock_attr})', fontsize=11)
    ax.set_title(f'Bias vs {mock_attr} Level\n(Green=overestimate, Red=underestimate)', fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    return fig


def check_data_quality_issues(df_grades, mock_attr='Grade_Mock', self_attr='Grade_Received'):
    """
    Check for potential data quality issues that might explain negative correlation.
    """
    
    print(f"\n{'='*70}")
    print("Data Quality Checks")
    print(f"{'='*70}")
    
    # 1. Constant values?
    if df_grades['mock'].nunique() == 1:
        print(f"⚠ WARNING: All mock grades are identical ({df_grades['mock'].iloc[0]})")
    if df_grades['self'].nunique() == 1:
        print(f"⚠ WARNING: All self grades are identical ({df_grades['self'].iloc[0]})")
    
    # 2. Outliers?
    Q1_mock = df_grades['mock'].quantile(0.25)
    Q3_mock = df_grades['mock'].quantile(0.75)
    IQR_mock = Q3_mock - Q1_mock
    outliers_mock = df_grades[(df_grades['mock'] < Q1_mock - 1.5*IQR_mock) | 
                               (df_grades['mock'] > Q3_mock + 1.5*IQR_mock)]
    
    if len(outliers_mock) > 0:
        print(f"⚠ {len(outliers_mock)} outliers in mock grades (>1.5 IQR)")
    
    Q1_self = df_grades['self'].quantile(0.25)
    Q3_self = df_grades['self'].quantile(0.75)
    IQR_self = Q3_self - Q1_self
    outliers_self = df_grades[(df_grades['self'] < Q1_self - 1.5*IQR_self) | 
                               (df_grades['self'] > Q3_self + 1.5*IQR_self)]
    
    if len(outliers_self) > 0:
        print(f"⚠ {len(outliers_self)} outliers in self grades (>1.5 IQR)")
    
    # 3. Scale mismatch?
    mock_range = df_grades['mock'].max() - df_grades['mock'].min()
    self_range = df_grades['self'].max() - df_grades['self'].min()
    range_ratio = self_range / mock_range if mock_range != 0 else np.nan
    
    print(f"\nRange (max - min):")
    print(f"  Mock: {mock_range:.2f}")
    print(f"  Self: {self_range:.2f}")
    print(f"  Ratio: {range_ratio:.2f}")
    
    if range_ratio > 2 or range_ratio < 0.5:
        print(f"  ⚠ Significant scale difference!")
    
    # 4. Reversed scale?
    if df_grades['discrepancy'].mean() > df_grades['discrepancy'].std():
        print(f"\n⚠ POSSIBLE SCALE REVERSAL: Mean discrepancy ({df_grades['discrepancy'].mean():.3f}) is large and positive")
        print(f"   Check: Are mock and self on opposite scales? (e.g., one is inverted?)")


# ============================================================================
# USAGE
# ============================================================================

if __name__ == "__main__":
    # df_grades, stats_dict = analyze_grade_discrepancy(G_acquaintance, 
    #                                                    mock_attr='Grade_Mock',
    #                                                    self_attr='Grade_Self',
    #                                                    network_name='Acquaintance Network')
    # 
    # check_data_quality_issues(df_grades)
    # 
    # fig = visualize_grade_discrepancy(df_grades, network_name='Acquaintance Network')
    # fig.savefig('grade_discrepancy_analysis.png', dpi=300, bbox_inches='tight')
    # plt.show()
    
    pass
