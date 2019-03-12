# coding: utf-8

from horoscope import generate_prophecies
from horoscope import times,advices,promises

def generate_page(head, body):
	page = f"<html>{head}{body}</html>"
	return page


def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>
	"""
	return head

def generate_body(header):
	body = f"<h1>{header}</h1><img src='disk.png' width=100 hight=100><ol>"
	body = body + "<li>Времена: </li><ul></ol>"
	for t in times:
		body = body + "<li>" + t + "</li>"
	body = body + "<ol><li>Глаголы : </li></ol>"
	for a in advices:
		body = f"{body}<li>{a}</li>"
	body = f"{body}<ol></li>Предсказания:</li></ol>"
	for p in promises:
		body = f"{body}<li>{p}</li>"
	return f"<body>{body}</ul><hr /><a href='index.html'>Тутачки главная страничка</a></body>"

def save_page(title,header, output="about.html"):
	fp = open(output, "w", encoding="utf-8")
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header = header
			),
	)
	print(page, file=fp)
	fp.close()

#####################

save_page(
	title="Реализация",
	header = "О чем этоооу"
	)
