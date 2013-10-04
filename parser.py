import re,json

raw_html = open("raw_courses.html", "r").read()

courses_html = raw_html.split("<td class=\"nttitle\"")[1:]
course_regex = "<a href=\".*\">(CS.*)</a>"
# course_regex = "(.*?)"
credit_regex = "([\d]\.[\d]+) Credit hours"

courses = []

for course_html in courses_html:
	raw_course = re.findall(course_regex,course_html)[0]
	
	course = {}
	pieces = raw_course.split(" ")
	course["college"] = pieces[0]
	course["id"] = pieces[1] 
	course["title"] = " ".join(pieces[3:])
	course["credit"] = re.findall(credit_regex,course_html)[0]
	courses.append(course)

courses_json_str = json.dumps(courses)
# print courses
open("courses.json", "w").write(courses_json_str)

