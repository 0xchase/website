#!/usr/bin/python2

import os

def main():
    os.system("rm -r reports")
    os.system("mkdir reports")

    generateMalwareTable()

def generateMalwareTable():
    text = []
    with open("reverseengineering.html") as f:
        text = f.read().split("\n")

    os.system("ls ~/github/malware-reports/ | grep -v README | grep -v scripts > temp")

    output = []
    tables = []
    with open("temp", "r") as f:
        tables = f.read().split("\n")
    tables = tables[:-1]

    for title in tables:
        output.append("""<h3>""" + title.replace("-", " ") + """</h3><div class="table-wrapper"><table><thead><tr><th>Sample Name</th><th>Writeup</th></tr></thead><tbody>""")

        os.system("ls ~/github/malware-reports/" + title + " > temp")

        reports = []
        with open("temp", "r") as f:
            reports = f.read().split("\n")
        reports = reports[:-1]

        for report in reports:
            os.system("cp ~/github/malware-reports/" + title + "/" + report + " reports/" + report)
            output.append("""<tr><td>""" + report.replace(".html", "") + """</td><td><a href=" """ + "reports/" + report + """" target="_blank">""" + report.replace(".html", "") + " Writeup" + """</a></td></tr>""")

        output.append("""</tbody></table></div>\n\n""")

    final = ""
    shouldAdd = True
    for line in text:
        if "Malware Table Start" in line:
            shouldAdd = False
            final += line + "\n"
            final += "\n".join(output)

        elif "Malware Table End" in line:
            shouldAdd = True
            final += line + "\n"
        else:
            if shouldAdd == True:
                final += line + "\n"

    with open("temp.html", "w") as f:
        f.write(final)
    
    os.system("mv temp.html reverseengineering.html")

    os.system("rm temp")

main()
