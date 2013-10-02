import re,json

raw_html = open("raw_courses.html", "r").read()

course_regex = "<td class=\"nttitle\".*>(CS.*)</a>"
raw_courses = re.findall(course_regex, raw_html)

courses = []

for raw_course in raw_courses:
	course = {}
	pieces = raw_course.split(" ")
	course["college"] = pieces[0]
	course["id"] = pieces[1] 
	course["title"] = " ".join(pieces[3:])
	courses.append(course)

courses_json_str = json.dumps(courses)
open("courses.json", "w").write(courses_json_str)

