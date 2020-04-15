#!/usr/bin/python2

import os

def main():
    generateMalwareTable()
    os.system("pwd")
    os.system("cp skeleton/index.html index.html")
    os.system("cp skeleton/physics.html physics.html")
    os.system("cp skeleton/gamedesign.html gamedesign.html")
    os.system("cp skeleton/synthesizers.html synthesizers.html")
    os.system("cp skeleton/vsts.html vsts.html")
    os.system("cp skeleton/piano.html piano.html")
    os.system("cp skeleton/blog.html blog.html")
    os.system("cp skeleton/filmscoring.html filmscoring.html")

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
