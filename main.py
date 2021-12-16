import pandas as pd
from datetime import date, timedelta

#########################################################

# meta information
export_name = "milo_export.csv"
consultants = ["Cameron Turnbow", "Scott Varner", "Kjersten Moore", "Mike Crane",
               "Chase Pendleton", "Brock Stuart", "Lauren Beall", "Alex Hart",
               "Jacob Michael", "Jeffrey Ouzts", "David Krause"
               ]
week_ago = pd.to_datetime(date.today() - timedelta(weeks=1))
save_path = "../../Downloads/result.csv"

publishing_date = "publishing date"
clean_date = "clean_date"
interviewer = "interviewer"
interview_editor = "interview editor"
client_name = "client Name"
interviewee_company = "interviewee company"

#########################################################

# logic for automation
# read CSV file
miloCSV = pd.read_csv("../../Downloads/" + export_name)

# drop all interviews that haven't been published
miloCSV.dropna(subset=[publishing_date], inplace=True)

# sort dates descending
miloCSV.sort_values(by=publishing_date, ascending=False, inplace=True)

# needs the Excel sheet to have a clean_date column. Editing required.
miloCSV.dropna(subset=[clean_date], inplace=True)

# get a copyable output dataframe
miloOutFormat = miloCSV[[clean_date, interviewer, interview_editor, client_name, interviewee_company]]

# get the frame that will contain the values we pull from
miloOut = miloOutFormat.loc[
    (pd.to_datetime(miloOutFormat[clean_date]) >= week_ago),
    [interviewer, interview_editor, client_name, interviewee_company]]

result = pd.DataFrame
for consultant in consultants:
    result = miloOut.loc[
        miloOut[interviewer] == consultant, [interviewer, interview_editor, client_name, interviewee_company]].sample(3)
    result.to_csv(save_path, mode="a", header=None)
