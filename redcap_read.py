from redcap import Project, RedcapError
TOKEN = "8092328E3AA4D7901F5341ADA9DD1177"
URL = "https://redcap.tamhsc.edu/redcap/api/"
forms = ["Background Demos", "PROMIS Bank v1.0 Alcohol: Alcohol Use", 
		"Fagerstrom Test for Cigarette Dependence (formerly Fagerstrom Test for Nicotine Dependence",
		"PROMIS Bank v1.0 - E-Cigarette Nicotine Dependence",
		"PROMIS SF v1.0 - Severity of Sub Use (Past 3 mo) 7a",
		"BIS BAS"]
project = Project(URL, TOKEN)

rc.df = project.export_records(forms = forms, 
format='df', export_data_access_groups= True)