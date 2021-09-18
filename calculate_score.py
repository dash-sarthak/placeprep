import pickle
import pandas as pd
import random

FILE_NAME = "/home/sarthak/Desktop/Personal Projects/Placeprep/Website/finalized_model.sav"


def prob_percent(value_list):
    value_dict = {
        "Age": int(value_list[0]),
        "Internships": int(value_list[1]),
        "CGPA": int(float(value_list[2])),
        "HistoryOfBacklogs": int(value_list[3]),
        "Gender": int(value_list[4]),
        "Stream": int(value_list[5]),
    }

    val_df = pd.DataFrame(value_dict, index=[1])
    predictor = pickle.load(open(FILE_NAME, "rb"))
    prob_percent = round(predictor.predict_proba(val_df)[0][1] * 100, 2)

    if prob_percent == 100.0:
        return f"{10*value_dict['CGPA'] + random.randint(10-value_dict['CGPA'], value_dict['CGPA'])} %"

    return f"{prob_percent} %"

