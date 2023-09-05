import pandas as pd
dataset = pd.read_csv('matches.csv')

#DATA PREP pip install dataprep
from dataprep.eda import create_report
reports=create_report(dataset)
reports.show_browser()
report.save('report') 

#EDA using sweetviz pip install sweetviz
import sweetviz as sv
sweet_report = sv.analyze(dataset)
sweet_report.show_html('sweet_report.html')

#EDA using Autoviz pip install autoviz==0.0.6
from autoviz.AutoViz_Class import AutoViz_Class
autoviz = AutoViz_Class().AutoViz('matches.csv')

#EDA using dtale pip install dtale
import dtale
dtale.show(dataset,open_browser=True)



















#pandas_profiling pip install pandas-profiling
#from pandas_profiling import ProfileReport
#profile = ProfileReport(dataset, explorative=True)
#Saving results to a HTML file
#profile.to_file("output.html")
#reports.save('DataPrepRepot')