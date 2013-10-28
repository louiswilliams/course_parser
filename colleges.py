import re,json

raw_html = open("coursesearch.html", "r").read()

#html_regex = "<OPTION VALUE=\"(.*)\">(.*)"
html_regex = "<option value=\"(.*)\">(.*)"

schools_raw = re.findall(html_regex,raw_html)

schools = []

for school_raw in schools_raw:
	school = {}
	school["name"] = school_raw[0]
	school["title"] = school_raw[1]
	schools.append(school)
	print school

open("schools.json", "w").write(json.dumps(schools))
