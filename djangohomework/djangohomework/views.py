from django.http import HttpResponse



# @get_math
def get_math(request):
    str1 = ''

    for i in range(1, 10):
        str1+='<tr>'
        for j in range(1, i + 1):
            # print("<td>{}*{}={}</td>".format(i, j, i * j), end=' ')
            str1 += "<td>{}*{}={}</td>".format(i, j, i * j)
        # str1 += '<tr>{}</tr>'.format(str1)
        str1+='</tr>'
    html = """
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <title>
                    九九乘法表
                    </title>
                    <style>
                        .content {
                           color: pink;
                           text-align: center;
                        }
                        table{
    	    border-collapse:collapse;
    	    border:1px solid red;
    	}
                   td{border:1px solid blue;width:100px;height:30px;background-color:green; }
                    </style>
                </head>
                <body>
                <table>
                    <h1 align='center'>显示一个九九乘法表</h1>
                    <p class='content'>%s</p>
                </table>
                </body>
            </html>
            """
    html1=html%(str1)
    string="获得一个九九乘法表：{}".format(html1)
    return HttpResponse(string)