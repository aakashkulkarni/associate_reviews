import pandas as pd

# meta information
export_name = "milo_export_clozd.csv"
consultants = ["Cameron Turnbow", "Scott Varner", "Kjersten Moore", "Mike Crane",
               "Chase Pendleton", "Brock Stuart", "Lauren Beall", "Alex Hart",
               "Jacob Michael", "Jeffrey Ouzts", "David Krause"
               ]
from_date = "2021/12/07"

# logic for automation
# read CSV file
miloCSV = pd.read_csv("../../Downloads/" + export_name)

# drop all interviews that haven't been published
miloCSV.dropna(subset=["publishing_date"], inplace=True)

# sort dates descending
miloCSV.sort_values(by="publishing_date", ascending=False, inplace=True)

# needs the Excel sheet to have a clean_date column. Editing required.
miloCSV.dropna(subset=["clean_date"], inplace=True)

# get a copyable output dataframe
miloOutFormat = miloCSV[["clean_date", "interviewer", "interview_editor", "client_name", "interviewee_company"]]

# convert clean_date column format to datetime format
miloOutFormat.loc["clean_date"] = pd.to_datetime(miloOutFormat["clean_date"])

# get the frame that will contain the values we pull from
miloOut = miloOutFormat.loc[
    (miloOutFormat["clean_date"] >= from_date), ["interviewer", "interview_editor", "client_name", "interviewee_company"]]

result = pd.DataFrame
for consultant in consultants:
    result = miloOut.loc[
        miloOut["interviewer"] == consultant, ["interviewer", "interview_editor", "client_name", "interviewee_company"]].head(3)
    result.to_csv("../../Downloads/result.csv", mode="a", header=None)
