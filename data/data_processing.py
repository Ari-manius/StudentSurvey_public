import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re

# ============================================================================
# PART 1: DATA CLEANING AND FILTERING
# ============================================================================

df_codebook = pd.read_csv('Student_Survey_Codebook_WS2526.csv', delimiter=";")
df_data = pd.read_csv('all_apps_wide_2025-10-29.csv', delimiter=",")

# filter out missing values
df_data = df_data[df_data['participant.label'].notna()]

# Original sets
set_variablenames_raw = set(df_codebook["Variablename"])
set_columnnames = set(df_data.columns)

# Expand patterns like {1-50} in the variable names of codebook
set_variablenames = set()
for var in set_variablenames_raw:
    # Check if it has a pattern like {1-50}
    match = re.search(r'\{(\d+)-(\d+)\}', var)
    if match:
        start = int(match.group(1))
        end = int(match.group(2))
        # Expand the range
        base_pattern = var[:match.start()]  # Everything before {1-50}
        suffix = var[match.end():]           # Everything after {1-50}
        for i in range(start, end + 1):
            set_variablenames.add(f"{base_pattern}{i}{suffix}")
    else:
        # No pattern, keep as is
        set_variablenames.add(var)

print(f"Expanded placeholders from {len(set_variablenames_raw)} to {len(set_variablenames)} variables")

# Now do your comparisons
common_variablenames = set_variablenames.intersection(set_columnnames)
print(f"Common variablenames Coodebook / Dataset: {len(common_variablenames)}")

missing_variablenames = set_variablenames - set_columnnames
print(f"Missing variablenames in data: {len(missing_variablenames)}")
print("Examples:", list(missing_variablenames)[:5])

tost_variablenames = set_columnnames - set_variablenames
print(f"Extra variablenames in data: {len(tost_variablenames)}")
print("Examples:", list(tost_variablenames))

df_data_filtered = df_data[list(common_variablenames)]

# sort columns alphabetically
df_data_filtered = df_data_filtered.reindex(sorted(df_data_filtered.columns), axis=1)

# save filtered data
df_data_filtered.to_csv('data_filtered.csv', index=False)
print("Data filtered by Codebook variables and missing participant labels saved to 'data_filtered.csv'")

# ============================================================================
# PART 2: NETWORK RELATION CREATION
# ============================================================================

df_data = pd.read_csv('data_filtered.csv')

# Select all columns that contain 'app_network' for temp processing
temp_cols = [col for col in df_data.columns if 'app_network' in col.lower()]
df_temp = df_data[temp_cols].copy()  # ADD .copy() here
df_temp['participant.label'] = df_data['participant.label']
df_temp.drop("app_network.1.player.linksrechts_self", axis=1, inplace=True)

# Remove all app_network columns EXCEPT 'app_network.1.player.linksrechts_self'
cols_to_keep = [col for col in df_data.columns if 'app_network' not in col.lower()]
df_data = df_data[cols_to_keep + ['app_network.1.player.linksrechts_self']]

# Save cleaned data
df_data.to_csv('data_filtered.csv', index=False)

# relations dict
dict_relation_identification = {
    "Aquaintance": "person_",
    "Friend": "friend_",
    "Study": "study_",
    "Support": "support_",
    "Politics": "politics_",
    "OldFriend": "old_",
    "Grade": "grade_",
    "LeftRight": "linksrechts_",
    "Group": "group_"
}

# Initialize list to store results
relation_data = []

# Transform data into wide format with lists
for source_id in df_temp['participant.label'].unique():
    # Select rows for participant
    source_data = df_temp[df_temp['participant.label'] == source_id]

    # Dictionary to store this participant's relations
    participant_relations = {'Label': source_id}

    for relation, col_prefix in dict_relation_identification.items():
        # Select columns for relation
        relation_cols = [col for col in source_data.columns if col_prefix in col]
        targets = []
        seen_targets = set()  # Track target_ids to avoid duplicates

        if col_prefix == "person_":
            # Direct person IDs stored in columns
            for col in relation_cols:
                value = source_data[col].values[0]
                if value != "x" and pd.notna(value) and value not in seen_targets:
                    targets.append(value)
                    seen_targets.add(value)

        elif col_prefix in ["grade_", "linksrechts_", "group_"]:
            # Categorical relations: extract all unique non-missing values
            for col in relation_cols:
                value = source_data[col].values[0]
                if pd.notna(value) and value != "x":
                    # Extract target id from column name
                    match = re.search(r'_(\d+)$', col)
                    if match:
                        target_num = match.group(1)
                        # Build the person column name to lookup
                        match_key = f"app_network.1.player.person_{target_num}"

                        if match_key in source_data.columns:
                            target_id = source_data[match_key].values[0]
                            if target_id != "x" and pd.notna(target_id) and target_id not in seen_targets:
                                targets.append((target_id, value))
                                seen_targets.add(target_id)

        else:
            # Binary indicators: 1 means connection exists
            for col in relation_cols:
                value = source_data[col].values[0]
                if value == 1:
                    # Extract target id from column name
                    match = re.search(r'_(\d+)$', col)
                    if match:
                        target_num = match.group(1)
                        # Build the person column name to lookup
                        match_key = f"app_network.1.player.person_{target_num}"

                        if match_key in source_data.columns:
                            target_id = source_data[match_key].values[0]
                            if target_id != "x" and pd.notna(target_id) and target_id not in seen_targets:
                                targets.append(target_id)
                                seen_targets.add(target_id)

        # Store the list of targets for this relation
        participant_relations[relation] = targets

    # Add this participant's data to our list
    relation_data.append(participant_relations)

# Create the final dataframe
df_relation = pd.DataFrame(relation_data)
print(df_relation.head())
print(f"\nShape: {df_relation.shape}")

# Save to CSV
df_relation.to_csv('data_edges.csv', index=False)
