
html_template = """<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
</head>
<body>
<h1>Total: {total_value:.0f} </h1>

<h1>Last entries:</h1>
<p>
{last_lines}
</p>

<h1>Selected expenses weekly ({weekly_categories})</h1>
{selected_expenses_weekly}

<h1>Expenses monthly by categories</h1>
{monthly_by_categories}

<h1>Expenses by categories</h1>
{expenses_by_categories}
</body>
</html>"""


def represent_html(model):
    # copy model?
    model["last_lines"] = model["last_lines"].replace("\n", "</br>")
    result = html_template.format(**model)
    return result


def make_table(tt):
    result = ""
    result += '<table border="1">\n'
    for row in tt:
        result += '<tr>'
        result += (len(row)*'<td align="center">{}</td>').format(*row)
        result += '</tr>\n'
    result += '</table>'
    return result
