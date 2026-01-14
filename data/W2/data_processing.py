import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re

# ============================================================================
# PART 1: DATA CLEANING AND FILTERING
# ============================================================================

df_codebook = pd.read_csv('/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/documentation/Student_Survey_Codebook_WS2526.csv', delimiter=";")
df_data = pd.read_csv('all_apps_wide_2025-11-26.csv', delimiter=",")

# filter out missing values
df_data = df_data[df_data['participant.label'].notna()]

# Original sets
set_variablenames_raw = set(df_codebook["variable_name"])
set_columnnames = set(df_data.columns)

# Expand patterns like {1-50} in the variable names of codebook
set_variablenames = set()
for var in set_variablenames_raw:
    # Skip if var is not a string (e.g., NaN)
    if not isinstance(var, str):
        continue
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

# Always include specific relation columns even if not in codebook
columns_to_keep = set(common_variablenames)
for col in df_data.columns:
    # Force-include grade, migration_eco, migration_culture columns
    if 'grade_' in col or 'migration_eco_' in col or 'migration_culture_' in col:
        columns_to_keep.add(col)
    # Force-include person columns from app_studium and app_migration
    elif 'app_studium.1.player.person_' in col or 'app_migration.1.player.person_' in col:
        columns_to_keep.add(col)

print(f"\nAfter adding forced columns: {len(columns_to_keep)} total columns")
df_data_filtered = df_data[list(columns_to_keep)]

# sort columns alphabetically
df_data_filtered = df_data_filtered.reindex(sorted(df_data_filtered.columns), axis=1)

# save filtered data
df_data_filtered.to_csv('data_filtered.csv', index=False)
print("Data filtered by Codebook variables and missing participant labels saved to 'data_filtered.csv'")

# ============================================================================
# PART 2: NETWORK RELATION CREATION
# ============================================================================

df_data = pd.read_csv('data_filtered.csv')

# Print column overview for debugging
print(f"\nTotal columns in filtered data: {len(df_data.columns)}")
app_network_cols = [c for c in df_data.columns if 'app_network' in c.lower()]
app_studium_cols = [c for c in df_data.columns if 'app_studium' in c.lower()]
app_migration_cols = [c for c in df_data.columns if 'app_migration' in c.lower()]
print(f"app_network columns: {len(app_network_cols)}")
print(f"app_studium columns: {len(app_studium_cols)}")
print(f"app_migration columns: {len(app_migration_cols)}")

# Create df_temp with ALL columns for edge extraction
df_temp = df_data.copy()

# Remove linksrechts_self from df_temp for edge processing
if "app_network.1.player.linksrechts_self" in df_temp.columns:
    df_temp = df_temp.drop("app_network.1.player.linksrechts_self", axis=1)

# Remove ONLY actual edge columns (person_, friend_, study_, etc. with numbers 1-50)
# Keep all other columns including survey questions
edge_patterns = ['person_', 'friend_', 'study_', 'support_', 'politics_', 'old_',
                 'grade_', 'linksrechts_', 'group_', 'migration_culture_', 'migration_eco_']

cols_to_keep = []
for col in df_data.columns:
    # Check if this is an edge column (has edge prefix + number)
    is_edge_col = False
    for pattern in edge_patterns:
        # Check if column has this pattern followed by a number
        if pattern in col and any(f'{pattern}{i}' in col for i in range(1, 51)):
            is_edge_col = True
            break

    # Exception: keep linksrechts_self
    if col == 'app_network.1.player.linksrechts_self':
        cols_to_keep.append(col)
    elif not is_edge_col:
        cols_to_keep.append(col)

df_data = df_data[cols_to_keep]
df_data.to_csv('data_filtered.csv', index=False)
print(f"Saved cleaned data with {len(df_data.columns)} columns")
grade_cols = [c for c in df_data.columns if 'grade_' in c]
mig_eco_cols = [c for c in df_data.columns if 'migration_eco_' in c]
mig_cul_cols = [c for c in df_data.columns if 'migration_culture_' in c]
print(f"  - grade_ columns: {len(grade_cols)}")
print(f"  - migration_eco_ columns: {len(mig_eco_cols)}")
print(f"  - migration_culture_ columns: {len(mig_cul_cols)}")

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
    "Group": "group_",
    "Migration Culture": "migration_culture_",
    "Migration Economy": "migration_eco_",
}

# Debug: Check what columns we have for each relation type
print("\n" + "="*70)
print("RELATION COLUMNS FOUND:")
print("="*70)
for relation, col_prefix in dict_relation_identification.items():
    found_cols = [col for col in df_temp.columns if col_prefix in col]
    print(f"{relation} ({col_prefix}): {len(found_cols)} columns")
    if len(found_cols) > 0 and len(found_cols) <= 3:
        print(f"  Examples: {found_cols[:3]}")
    elif len(found_cols) > 3:
        print(f"  Examples: {found_cols[:2]} ... {found_cols[-1]}")
print("="*70 + "\n")

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

        elif col_prefix in ["grade_", "linksrechts_", "group_", "migration_culture_", "migration_eco_"]:
            # Categorical relations: extract all unique non-missing values
            debug_once = False  # Only debug first participant
            for col in relation_cols:
                value = source_data[col].values[0]
                if pd.notna(value) and value != "x":
                    # Extract target id from column name
                    match = re.search(r'_(\d+)$', col)
                    if match:
                        target_num = match.group(1)

                        # Determine which app this column belongs to
                        if 'app_network' in col:
                            match_key = f"app_network.1.player.person_{target_num}"
                        elif 'app_studium' in col:
                            match_key = f"app_network.1.player.person_{target_num}"
                        elif 'app_migration' in col:
                            match_key = f"app_network.1.player.person_{target_num}"
                        else:
                            match_key = None

                        # Debug for migration/grade only on first participant
                        if not debug_once and col_prefix in ["grade_", "migration_culture_", "migration_eco_"]:
                            print(f"\nDEBUG {relation}:")
                            print(f"  Column: {col}")
                            print(f"  Value: {value}")
                            print(f"  Target num: {target_num}")
                            print(f"  Looking for: {match_key}")
                            print(f"  Found in columns: {match_key in source_data.columns}")
                            if match_key and match_key in source_data.columns:
                                print(f"  Person ID: {source_data[match_key].values[0]}")
                            debug_once = True

                        if match_key and match_key in source_data.columns:
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
