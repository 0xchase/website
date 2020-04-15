#!/usr/bin/python2

import os

def main():
    generateMalwareTable()

def generateMalwareTable():
    os.system("rm cybersecurity.html")
    os.system("ls malware-reports/* > temp.txt")

    files = ""
    with open("temp.txt", "r") as f:
        files = f.read().split("\n")
    os.system("rm temp.txt")

    html1 = ""
    html2 = ""

    with open("skeletons/cybersecurity.html", "r") as f:
        html1 = f.read()

    tabledata = ""
    for f in files:
        name = f.split("/")[-1]
        tabledata += """
                                <tr>
                                    <td>""" + name + """</td>
                                    <td><a href=" """ + f + """ " target="_blank">""" + name + """</a></td>
                            </tr>
    """


    table = """
    <h3>Malware Analysis</h3>
    <div class="table-wrapper">
            <table>
                    <thead>
                            <tr>
                                    <th>Sample</th>
                                    <th>Writeup</th>
                            </tr>
                    </thead>
                    <tbody>
                    """ + tabledata + """
                    </tbody>
            </table>
    </div>
    """
    for line in html1.split("\n"):
        if "Malware Table" in line:
            html2 += table
        else:
            html2 += line + "\n"

    with open("temp.html", "w") as f:
        f.write(html2)

    os.system("mv temp.html cybersecurity.html")

main()
