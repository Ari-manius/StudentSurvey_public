import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    Matching Codes from exams to codelist
    """)
    return


@app.cell
def _():
    import pandas as pd
    from thefuzz import fuzz
    from thefuzz import process
    import ast
    return ast, fuzz, pd, process


@app.cell
def _(ast, pd):
    def fix_perceived_grades(path):
        df_edges = pd.read_csv(path)

        df_edges["Grade"] = df_edges["Grade"].apply(ast.literal_eval)

        grade_map = {
            0: 0, 1: 1.0, 2: 1.3, 3: 1.7, 4: 2.0, 5: 2.3,
            6: 2.7, 7: 3.0, 8: 3.3, 9: 3.7, 10: 4.0, 11: 5.0
        }

        def map_grades_in_list(grade_list):
            return [(node_id, grade_map[int(grade)]) for node_id, grade in grade_list]

        df_edges["Grade"] = df_edges["Grade"].apply(map_grades_in_list)

        df_edges.to_csv(path, index=False)

    fix_perceived_grades('/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/data/W1/data_edges.csv')
    fix_perceived_grades('/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/data/W2/data_edges.csv')
    return


@app.cell
def _(mo):
    mo.md(r"""
    ***
    """)
    return


@app.cell
def _(pd):
    # Load Data 
    df_w1 = pd.read_csv("/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/data/W1/data_filtered.csv")
    df_w2 = pd.read_csv("/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/data/W2/data_filtered.csv")

    df_exam = pd.read_csv("/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/data/Tutorial_Exam/mockexam_og.csv", delimiter=";")
    df_exam["Code"] = df_exam["Code"].str.replace(r"\(\?\)", "", regex=True)

    df_code = pd.read_csv('/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/_rooms/code_list.txt', sep=" ", header=None)
    return df_code, df_exam, df_w1, df_w2


@app.cell
def _(mo):
    mo.md(r"""
    ***
    Cleaning Codes
    """)
    return


@app.cell
def _(df_code, df_exam):
    participant_exam = df_exam["Code"]
    # remove the (?)
    for code in participant_exam: 
        code.replace("(?)", "")

    code_errors = set(participant_exam) - set(df_code[0])
    return code_errors, participant_exam


@app.cell
def _(code_errors, df_code, fuzz, process):
    best_matches = []
    for code in code_errors:
        match, score, idx = process.extractOne(code, df_code[0], scorer=fuzz.ratio)
        best_matches.append((code, match, score))

    for original, matched_code, score in best_matches:
        print(f"{original} → {matched_code} ({score}%)")
    return


@app.cell
def _(participant_exam):
    # Your ground truth corrections
    corrections = {
        '0m3': 'om3',
        '4wo': '4w0',
        'g04': 'go4',
        '6uf': 'tuf',
        '19e': '199',
        'cau': 'cav',
        '1ru ': '1ru',      # keep as-is (uncertain)
        '351  361': '3s1',      # uncertain but mapping provided
        '15q ': '15f',      # uncertain
        'suv': 'snv',
        'swx ': 'swx',      # keep as-is (uncertain)
        'efu': 'efu',      # or 'efn'? pick one
        'twq': 'twg',
        '260': '26o',
        'tas': 'ras',
        'oov': 'oev',
        'efu/ efn' : 'efu',
        # 'mehendiran': None  # remove from list
    }

    corrected = participant_exam.map(lambda x: corrections.get(x, x))
    return (corrected,)


@app.cell
def _(corrected, df_code):
    remaining_errors = set(corrected) - set(df_code[0])
    print(remaining_errors)
    return


@app.cell
def _(corrected):
    df_exam["Code"] = corrected
    df_exam = df_exam.drop(df_exam.index[-1])
    return (df_exam,)


@app.cell
def _(df_code, df_exam, df_w1, df_w2):
    ## Fully participating 
    w1 = set(df_w1["participant.label"]) 
    w2 = set(df_w2["participant.label"])
    mock = set(df_exam["Code"])
    truth = set(df_code[0])

    in_all_list = truth & w1 & w2 & mock 
    len(in_all_list)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ***
    Transforming the Points to Grades
    """)
    return


@app.cell
def _(df_exam, pd):
    ## Transforming the pointts to grade
    df_exam["points (x-answersheet missing)"] = pd.to_numeric(
        df_exam["points (x-answersheet missing)"], 
        errors='coerce'
    )

    df_exam["PercentageMock"] = ((50 - df_exam["points (x-answersheet missing)"]) / 50) * 100
    df_exam["GradeMock"] = 4.0 + ((50 - df_exam["PercentageMock"]) / 50) * 3.0
    return


@app.cell
def _(df_exam):
    def grade_mapper(percentage):
        if percentage >= 95:
            return 1.0
        elif percentage >= 90:
            return 1.3
        elif percentage >= 85:
            return 1.7
        elif percentage >= 80:
            return 2.0
        elif percentage >= 75:
            return 2.3
        elif percentage >= 70:
            return 2.7
        elif percentage >= 65:
            return 3.0
        elif percentage >= 60:
            return 3.3
        elif percentage >= 55:
            return 3.7
        elif percentage >= 50:
            return 4.0
        else:
            return 5.0

    df_exam["GradeMock"] = df_exam["PercentageMock"].apply(grade_mapper)
    return


@app.cell
def _(df_exam):
    df_exam.to_csv('/Users/ramius/Desktop/CodeVault/01_Project/Work/Susumu/Student_Survey/StudentSurvey_WS2526/data/Tutorial_Exam/mockexam_fix.csv', index=False)
    return


if __name__ == "__main__":
    app.run()
