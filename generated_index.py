# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

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

def generate_body(header, paragraphs,link):
	body = f"<h1>{header}</h1>"
	link = f"<a href='about.html'>О реализации</a>"
	for p in paragraphs:
		body = body + f"<p>{p}</p>"
	return f"<body>{body}<hr />{link}</body>"




def save_page(title, header, paragraphs,link, output="index.html"):
	fp = open(output, "w", encoding="utf-8")
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs,link=link
		 ),

	)
	print(page, file=fp)
	fp.close()


#####################

today = dt.now().date()

save_page(
	title="Фуфлоскоп",
	header="Ниже вы увидете генерацию шуток на " + str(today) + " которые ничего не изменят в вашей жизни",
	paragraphs=generate_prophecies(),
	link="Писька с ручкой"
)