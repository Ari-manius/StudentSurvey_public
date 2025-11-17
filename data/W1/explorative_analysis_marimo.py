import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    title: "Student Survey Explorative Analysis"
    author: "Marius"
    date: today
    ---
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import re
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy.cluster.hierarchy import linkage, dendrogram, fcluster, leaves_list
    from scipy.spatial.distance import pdist
    from sklearn.decomposition import FactorAnalysis
    return (
        dendrogram,
        fcluster,
        leaves_list,
        linkage,
        np,
        pd,
        pdist,
        plt,
        re,
        sns,
    )


@app.cell
def _(pd):
    # Load data
    df_code = pd.read_csv(
        '/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/documentation/Student_Survey_Codebook_WS2526.csv',
        delimiter=";"
    )
    df_data = pd.read_csv('data_filtered.csv')
    return df_code, df_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Missing Values
    """)
    return


@app.cell
def _(df_data, plt, sns):
    # Compact heatmap with column sorting by missingness
    sorted_cols = df_data.isnull().sum().sort_values(ascending=False).index
    df_sorted = df_data[sorted_cols]

    plt.figure(figsize=(14, 8))
    sns.heatmap(
        df_sorted.isnull(),
        yticklabels=False,
        cmap=['#2ecc71', '#e74c3c'],
        vmin=0,
        vmax=1
    )
    plt.title(
        'Missing Values Pattern (Red = Missing, Green = Present)',
        fontsize=14, fontweight='bold', pad=20
    )
    plt.xlabel('Columns (sorted by missingness)', fontsize=12)
    plt.ylabel(f'Rows (n={len(df_data)})', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df_data, pd, plt):
    # Calculate missing and "don't know" percentages
    missing_percentage = df_data.isnull().mean() * 100
    dont_know_percentage = (df_data == 0).mean() * 100

    combined_data = pd.DataFrame({
        'Missing (NaN)': missing_percentage,
        "Don't Know (0)": dont_know_percentage
    })

    # Filter to only show columns with at least one issue
    combined_data = combined_data[
        (combined_data['Missing (NaN)'] > 0) | (combined_data["Don't Know (0)"] > 0)
    ]
    combined_data['Total'] = combined_data.sum(axis=1)
    combined_data = combined_data.sort_values('Total', ascending=False).drop('Total', axis=1)

    # Visualize
    fig, ax = plt.subplots(figsize=(28, 12))
    combined_data.plot(
        kind='bar', stacked=True, ax=ax,
        color=['#440154', '#FDE724'], alpha=0.85
    )
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.title(
        'Missing Values and "Don\'t Know" Responses per Variable',
        fontsize=14, fontweight='bold', pad=20
    )
    plt.legend(title='Type', loc='upper right')
    plt.tight_layout()
    plt.show()

    print('\nColumns with highest data quality issues:')
    print(combined_data.sum(axis=1).sort_values(ascending=False).head(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ***
    ## Correlation Heatmap
    """)
    return


@app.cell
def _(dendrogram, df_data, fcluster, linkage, np, pd, pdist, plt, sns):
    # Select numeric columns and clean
    numeric_df = df_data.select_dtypes(include='number')
    numeric_df = numeric_df.dropna(axis=1, how='all')
    numeric_df = numeric_df.loc[:, numeric_df.nunique() > 1]

    # Compute correlation matrix
    correlation_matrix = numeric_df.corr()

    # Hierarchical clustering
    def correlation_distance(u, v):
        r = np.corrcoef(u, v)[0, 1]
        if np.isnan(r):
            return 1.0
        return 1 - abs(r)

    distance_vector = pdist(numeric_df.T, metric=correlation_distance)
    linkage_matrix = linkage(distance_vector, method='average', optimal_ordering=True)

    # Plot dendrogram
    plt.figure(figsize=(15, 7))
    dendro = dendrogram(linkage_matrix, labels=correlation_matrix.columns, leaf_rotation=90)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.show()

    # Reorder correlation matrix
    dendro_order = dendro['leaves']
    ordered_corr = correlation_matrix.iloc[dendro_order, dendro_order]

    plt.figure(figsize=(20, 16))
    sns.heatmap(ordered_corr, annot=False, cmap='coolwarm', fmt='.2f')
    plt.title('Clustered Correlation Matrix Heatmap')
    plt.show()

    # Extract clusters
    clusters = fcluster(linkage_matrix, t=0.5, criterion='distance')
    cluster_df = pd.DataFrame({
        'Variable': correlation_matrix.columns,
        'Cluster': clusters
    })
    cluster_df = cluster_df.sort_values('Cluster').reset_index(drop=True)

    print('Variable clusters (blocks):')
    print(cluster_df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ***
    ## Descriptive 1V Analysis

    ### Demography
    - Academic Family Background
    - Gender
    - Age / Secondary Education / Study Start
    - Financial Situation
    - Map with Place of Origin
    """)
    return


@app.cell
def _(df_data, plt, sns):
    # Gender distribution
    label_dict = {0: 'Unknown', 1: 'Male', 2: 'Female'}

    plt.figure(figsize=(8, 6))
    sns.countplot(data=df_data, x='app_demographic.1.player.gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.xticks(ticks=[0, 1, 2], labels=[label_dict[i] for i in range(3)])
    plt.title('Distribution of Gender')
    plt.show()
    return


@app.cell
def _(df_data, plt):
    # Financial situation comparison
    plt.figure(figsize=(14, 8))

    colors = {
        'personal_current': '#87CEEB',
        'personal_future': '#0000CD',
        'general_current': '#90EE90',
        'general_future': '#006400'
    }

    personal_current = df_data['app_demographic.1.player.financial_situation_personal_current'].value_counts().sort_index()
    personal_future = df_data['app_demographic.1.player.financial_situation_personal_future'].value_counts().sort_index()
    general_current = df_data['app_demographic.1.player.financial_situation_general_current'].value_counts().sort_index()
    general_future = df_data['app_demographic.1.player.financial_situation_general_future'].value_counts().sort_index()

    plt.plot(personal_current.index, personal_current.values, marker='o', linewidth=2.5,
             color=colors['personal_current'], label='Personal (Current)', markersize=8)
    plt.plot(personal_future.index, personal_future.values, marker='s', linewidth=2.5,
             color=colors['personal_future'], label='Personal (Future)', markersize=8)
    plt.plot(general_current.index, general_current.values, marker='o', linewidth=2.5,
             color=colors['general_current'], label='General (Current)', markersize=8)
    plt.plot(general_future.index, general_future.values, marker='D', linewidth=2.5,
             color=colors['general_future'], label='General (Future)', markersize=8)

    plt.xlabel('Financial Situation', fontsize=12, fontweight='bold')
    plt.ylabel('Count', fontsize=12, fontweight='bold')
    plt.title(
        'Financial Situation Distributions: Personal vs General, Current vs Future',
        fontsize=14, fontweight='bold'
    )
    plt.legend(fontsize=11, loc='best')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Study
    - Time Work next to time for studies
    - Psychological Variables in Study Context
    - Grade Expectation Self vs. Others
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Politics
    - LeftRight Self vs. Others
    - Popularity Contest: Beliebtheit Politiker*innen
    - Sonntagsfrage vs. Bundes Polit Barometer
    - Political Efficacy
    - Participation in Demonstrations and Petitions
    """)
    return


@app.cell
def _(df_data, plt):
    from upsetplot import UpSet, from_indicators

    # Define columns with their actual platform names
    platform_mapping = {
        'app_political.1.player.social_networks_1': 'Facebook',
        'app_political.1.player.social_networks_2': 'Twitter',
        'app_political.1.player.social_networks_3': 'LinkedIn',
        'app_political.1.player.social_networks_4': 'Instagram',
        'app_political.1.player.social_networks_5': 'Signal',
        'app_political.1.player.social_networks_6': 'YouTube',
        'app_political.1.player.social_networks_7': 'Snapchat',
        'app_political.1.player.social_networks_8': 'WhatsApp',
        'app_political.1.player.social_networks_9': 'TikTok',
        'app_political.1.player.social_networks_10': 'Telegram',
        'app_political.1.player.social_networks_11': 'Discord',
        'app_political.1.player.social_networks_12': 'Reddit',
        'app_political.1.player.social_networks_13': 'Other'
    }

    # Filter to existing columns
    existing_cols = [col for col in platform_mapping.keys() if col in df_data.columns]
    print(f"Found {len(existing_cols)} platform columns")

    # Create renamed subset with readable names
    df_platforms = df_data[existing_cols].rename(columns=platform_mapping)
    df_platforms = df_platforms.fillna(0).astype(bool)

    # Quick stats
    print("\nPlatform usage counts:")
    for platform in df_platforms.columns:
        count = df_platforms[platform].sum()
        pct = (count / len(df_platforms)) * 100
        print(f"{platform:12s}: {count:4d} ({pct:5.1f}%)")

    # Convert to UpSet format
    upset_data = from_indicators(df_platforms.columns.tolist(), data=df_platforms)

    # Create UpSet plot
    plt.figure(figsize=(15, 8))
    upset = UpSet(upset_data, 
                  sort_by='cardinality',
                  show_counts=True,
                  element_size=50,
                  intersection_plot_elements=8)  # Show top 8 intersections
    upset.plot()
    plt.suptitle('Social Media Platform Usage Overlaps', 
                 fontsize=18, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.show()

    # Summary statistics
    print(f"\n=== Summary ===")
    print(f"Total respondents: {len(df_platforms)}")
    print(f"Using at least 1 platform: {df_platforms.any(axis=1).sum()} ({df_platforms.any(axis=1).sum()/len(df_platforms)*100:.1f}%)")
    print(f"Using no platforms: {(~df_platforms.any(axis=1)).sum()} ({(~df_platforms.any(axis=1)).sum()/len(df_platforms)*100:.1f}%)")
    print(f"Mean platforms per person: {df_platforms.sum(axis=1).mean():.2f}")
    print(f"Max platforms used: {df_platforms.sum(axis=1).max()}")
    return (df_platforms,)


@app.cell
def _(df_platforms, pd, plt, sns):
    def create_conditional_probability_matrix(df_bool):
        """Create P(has Y | has X) matrix"""

        platforms = df_bool.columns.tolist()
        n = len(platforms)

        # P(Y | X) = P(X and Y) / P(X)
        conditional_prob = pd.DataFrame(0.0, index=platforms, columns=platforms)

        for x in platforms:
            x_users = df_bool[x].sum()
            if x_users == 0:
                continue

            for y in platforms:
                if x == y:
                    conditional_prob.loc[x, y] = 100.0  # P(X|X) = 1
                else:
                    both = ((df_bool[x]) & (df_bool[y])).sum()
                    conditional_prob.loc[x, y] = (both / x_users) * 100

        return conditional_prob

    # Create and visualize
    cond_prob = create_conditional_probability_matrix(df_platforms)

    plt.figure(figsize=(14, 12))
    sns.heatmap(cond_prob, 
                annot=True, 
                fmt='.1f',
                cmap='YlOrRd',
                cbar_kws={'label': 'Probability (%)'},
                square=True,
                vmin=0,
                vmax=100)
    plt.title('P(Column | Row): If user has Row platform, % who also have Column platform', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('Then they probably have...', fontsize=12)
    plt.ylabel('If user has...', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Meta
    - Time taken for survey
    - Wordclouds of feedback and network narrative
    """)
    return


@app.cell
def _(df_data, plt, re):
    from wordcloud import WordCloud, STOPWORDS

    # Feedback wordcloud
    feedback_text = ' '.join(df_data['app_end.1.player.feedback'].dropna().astype(str).tolist())
    feedback_text = feedback_text.lower()
    feedback_text = re.sub(r'[^\w\s]', '', feedback_text)

    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update(['app', 'player', 'game', 'really', 'just', 'like', 'die', 'ich'])

    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color='black',
        colormap='plasma',
        max_words=150,
        stopwords=custom_stopwords,
        relative_scaling=0.5,
        collocations=False
    ).generate(feedback_text)

    plt.figure(figsize=(15, 7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Feedback Wordcloud', fontsize=18, fontweight='bold', color='Black', pad=20)
    plt.tight_layout(pad=0)
    plt.show()
    return STOPWORDS, WordCloud


@app.cell
def _(STOPWORDS, WordCloud, df_data, plt, re):
    # Network narrative wordcloud
    narrative_text = ' '.join(df_data['app_end.1.player.network_narrative'].dropna().astype(str).tolist())
    narrative_text = narrative_text.lower()
    narrative_text = re.sub(r'[^\w\s]', '', narrative_text)

    custom_stopwords_narrative = set(STOPWORDS)
    custom_stopwords_narrative.update([
        'den', 'app', 'player', 'game', 'really', 'just', 'like',
        'die', 'der', 'ich', 'und', 'habe'
    ])

    wordcloud_narrative = WordCloud(
        width=1200,
        height=600,
        background_color='black',
        colormap='plasma',
        max_words=150,
        stopwords=custom_stopwords_narrative,
        relative_scaling=0.5,
        collocations=False
    ).generate(narrative_text)

    plt.figure(figsize=(15, 7))
    plt.imshow(wordcloud_narrative, interpolation='bilinear')
    plt.axis('off')
    plt.title('Network Narrative Analysis', fontsize=18, fontweight='bold', color='Black', pad=20)
    plt.tight_layout(pad=0)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ***
    ## Motivated Strategies
    """)
    return


@app.cell
def _(df_code, df_data, pd, plt, sns):
    # Filter for Motivated Strategies questions
    df_MS = df_code[df_code['page'] == 'MotivatedStrategies']
    variables_MS = list(df_MS.variable_name)
    questions_MS = df_MS['question_german'].tolist()

    # Combine variable names with questions
    labels_MS = [f'{var.split(".")[-1]} \n {q}' for var, q in zip(variables_MS, questions_MS)]
    df_MS_data = df_data[variables_MS]

    # Melt to long format
    df_melted_MS = df_MS_data.melt(var_name='Variable', value_name='Response')
    label_map_MS = dict(zip(variables_MS, labels_MS))
    df_melted_MS['Variable'] = df_melted_MS['Variable'].map(label_map_MS)

    # Sort and categorize
    sorted_labels_MS = sorted(labels_MS, key=lambda x: x.split(' – ')[0])
    df_melted_MS['Variable'] = pd.Categorical(
        df_melted_MS['Variable'],
        categories=sorted_labels_MS,
        ordered=True
    )

    # Plot
    plt.figure(figsize=(10, len(labels_MS) * 0.5))
    sns.boxplot(
        data=df_melted_MS,
        x='Response',
        y='Variable',
        palette='coolwarm',
        orient='h',
        order=sorted_labels_MS
    )
    plt.title('Motivation for Studying', fontsize=16)
    plt.xlabel('Antwort (1–7)')
    plt.xlim(-0.5, 7.5)
    sns.despine()
    plt.tight_layout()
    plt.show()
    return (df_MS_data,)


@app.cell
def _(df_MS_data, leaves_list, linkage, plt, sns):

    # df_MS_data columns example: ["motivation.Q1", "cogstrategy.Q2", "selfefficacy.Q1"]
    df_MS_data_renamed = df_MS_data.copy()

    # Take only the part after the last "."
    df_MS_data_renamed.columns = [col.split('.')[-1] for col in df_MS_data_renamed.columns]

    print(df_MS_data_renamed.head())


    # df_MS_data contains only the survey variables
    corr_matrix = df_MS_data_renamed.corr()

    # Convert correlations to distances: distance = 1 - correlation
    distance = 1 - corr_matrix
    # Hierarchical clustering using 'average' linkage
    Z = linkage(distance, method='average')

    # Get the order of variables after clustering
    cluster_order = leaves_list(Z)
    ordered_vars = corr_matrix.columns[cluster_order]

    corr_matrix_clustered = corr_matrix.loc[ordered_vars, ordered_vars]


    plt.figure(figsize=(10,8))
    sns.heatmap(
        corr_matrix_clustered,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1, vmax=1,
        linewidths=0.5
    )
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.title("Correlations of Study Motivations", fontsize=16)
    plt.tight_layout()
    plt.show()
    return (df_MS_data_renamed,)


@app.cell
def _(df_MS_data_renamed, pd):
    from factor_analyzer import FactorAnalyzer

    # Perform Factor Analysis with Varimax
    fa = FactorAnalyzer(n_factors=5, rotation='varimax')  # adjust n_factors as needed
    fa.fit(df_MS_data_renamed)

    # Get loadings
    loadings = fa.loadings_

    # Create loadings table
    loadings_df = pd.DataFrame(
        loadings,
        columns=[f'Factor{i+1}' for i in range(loadings.shape[1])],
        index=df_MS_data_renamed.columns
    )

    print("Varimax Rotated Factor Loadings:")
    print(loadings_df.round(3))

    # Get communalities and variance explained
    communalities = fa.get_communalities()
    variance = fa.get_factor_variance()

    # Create variance table
    variance_df = pd.DataFrame(
        variance,
        columns=[f'Factor{i+1}' for i in range(loadings.shape[1])],
        index=['SS Loadings', 'Proportion Var', 'Cumulative Var']
    )

    print("\nVariance Explained:")
    print(variance_df.round(3))

    # Add communalities
    loadings_df['Communality'] = communalities
    print("\nWith Communalities:")
    print(loadings_df.round(3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ***
    ## Popularity of Politicians
    """)
    return


@app.cell
def _(df_code, df_data, pd, plt, sns):
    # Filter for politician popularity questions
    df_popularity = df_code[df_code['page'] == 'ScaloPerson']
    variables_pop = list(df_popularity.variable_name)
    questions_pop = df_popularity['question_german'].tolist()

    # Combine variable names with questions
    labels_pop = [f'{var.split(".")[-1]} \n {q}' for var, q in zip(variables_pop, questions_pop)]
    df_pop_data = df_data[variables_pop]

    # Melt to long format
    df_melted_pop = df_pop_data.melt(var_name='Variable', value_name='Response')
    label_map_pop = dict(zip(variables_pop, labels_pop))
    df_melted_pop['Variable'] = df_melted_pop['Variable'].map(label_map_pop)

    # Remove "don't know" responses (0)
    df_melted_pop = df_melted_pop[df_melted_pop['Response'] != 0]

    # Transform scale 1–11 → -5 to +5
    df_melted_pop['Response'] = df_melted_pop['Response'].apply(lambda x: x - 6)

    # Compute median per variable for sorting
    medians_pop = df_melted_pop.groupby('Variable')['Response'].median()
    sorted_labels_pop = medians_pop.sort_values(ascending=False).index.tolist()
    df_melted_pop['Variable'] = pd.Categorical(
        df_melted_pop['Variable'],
        categories=sorted_labels_pop,
        ordered=True
    )

    # Plot
    plt.figure(figsize=(10, len(labels_pop) * 0.5))
    sns.boxplot(
        data=df_melted_pop,
        x='Response',
        y='Variable',
        palette='coolwarm',
        orient='h',
        order=sorted_labels_pop
    )
    plt.title('Popularity of Politicians', fontsize=16)
    plt.xlabel('Beliebtheit (-5 bis +5)')
    plt.xlim(-5.5, 5.5)
    sns.despine()
    plt.tight_layout()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
