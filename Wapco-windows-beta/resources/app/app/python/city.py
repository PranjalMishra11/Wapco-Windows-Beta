
import sys
import requests
import json
import re
url  = "https://codeforces.com/api/user.ratedList?activeOnly=true"
req  = requests.get(url = url)
data = req.json()

city         = dict()

lgm = {}
igm = {}
gm  = {}
im  = {}
mas = {}
cam = {}
exp = {}
spe = {}
pup = {}
newb= {}
top3= {}
flag= {}

city_rank         = []

for x in data['result']:
    if 'city' in x:
        if x['city'] != " " and x['city'] != "":
            city[x['city']] = city.get(x['city'], 0) + 1
  
    if 'rank' in x:
        if 'city' in x:
            if top3.get(x['city'], 0) == 0 :
                top3[x['city']] = []
            if x['city'] != " " and x['city'] != "" :
                if(len(top3[x['city']]) < 3):
                    top3[x['city']].append([x['handle'], x['rank'], x['avatar']])
                if(x['rank'] == 'legendary grandmaster'):
                        lgm[x['city']] = lgm.get(x['city'], 0) + 1
                elif(x['rank'] == 'international grandmaster'):
                    igm[x['city']] = igm.get(x['city'], 0) + 1
                elif(x['rank'] == 'grandmaster'):
                    gm[x['city']] = gm.get(x['city'], 0) + 1
                elif(x['rank'] == 'master'):
                    mas[x['city']] = mas.get(x['city'], 0) + 1
                elif(x['rank'] == 'candidate master'):
                    cam[x['city']] = cam.get(x['city'], 0) + 1
                elif(x['rank'] == 'expert'):
                    exp[x['city']] = exp.get(x['city'], 0) + 1
                elif(x['rank'] == 'specialist'):
                    spe[x['city']] = spe.get(x['city'], 0) + 1
                elif(x['rank'] == 'pupil'):
                    pup[x['city']] = pup.get(x['city'], 0) + 1
                elif(x['rank'] == 'newbie'):
                    newb[x['city']] = newb.get(x['city'], 0) + 1
                elif(x['rank'] == "international master"):
                    im[x['city']] = im.get(x['city'], 0) + 1

lgm  = dict(sorted(lgm.items(), key=lambda x: x[1], reverse = True))
igm  = dict(sorted(igm.items(), key=lambda x: x[1], reverse = True))
im   = dict(sorted(im.items(), key=lambda x: x[1], reverse = True))
gm   = dict(sorted(gm.items(), key=lambda x: x[1], reverse = True))
cam  = dict(sorted(cam.items(), key=lambda x: x[1], reverse = True))
mas  = dict(sorted(mas.items(), key=lambda x: x[1], reverse = True))
exp  = dict(sorted(exp.items(), key=lambda x: x[1], reverse = True))
spe  = dict(sorted(spe.items(), key=lambda x: x[1], reverse = True))
pup  = dict(sorted(pup.items(), key=lambda x: x[1], reverse = True))
newb = dict(sorted(newb.items(), key=lambda x: x[1], reverse = True))

color = {}
color["legendary grandmaster"] = """<i><font color="black">L</font><font color="red">egendary Grandmaster </font> </i>"""
color["grandmaster"] = """<i><font color="red">Grandmaster </font> </i>"""
color["international grandmaster"] = """<i><font color="red">International Grandmaster</font></i>"""
color["master"] = """<i><font color="#FFFF00"> Master </font></i>"""
color["international master"] = """<i><font color="#FFD700"> International Master </font></i>"""
color["candidate master"] = """<i><font color=" #FF1493"> Candidate Master </font></i>"""
color["expert"] = """<i><font color="blue"> Expert </font></i>"""
color["pupil"] = """<i><font color="#00FF00"> Pupil </font></i>"""
color["newbie"] = """<i><font color="#A9A9A9"> Newbie </font></i>"""
color["specialist"] = """<i><font color="#00CED1"> Specialist </font></i>"""

for x in lgm:
    if x in city_rank:
        continue
    else:
        city_rank.append(x)

for x in igm:
    if x in city_rank:
        continue
    else:
        city_rank.append(x)

for x in gm:
    if x in city_rank:
        continue
    else:
        city_rank.append(x)

for x in mas:
    if x in city_rank:
        continue
    else:
        city_rank.append(x)

for x in cam:
    if x in city_rank:
        continue
    else:
        city_rank.append(x)

for x in exp:
    if x in city_rank:
        continue
    else:
        city_rank.append(x)

for x in spe:
    if x in city_rank:
        continue
    else:
        city_rank.append(x)

for x in pup:
    if x in city_rank:
        continue
    else:
        city_rank.append(x)

                
for x in newb:
    if x in city_rank:
        continue
    else:
        city_rank.append(x)

cnt = 1

for x in city_rank:
    if cnt == 1:
        print("""<div class="container">
                    <img src="../images/back.jpg" alt="" style="width:100%;height: 600px;float: left;">
                    <div class="content">
                        <div style = "width:13%;float:left;margin-right:4%;">
                            <img src = "https://assets.billboard.com/assets/1536864895/images/charts/number-one.svg?2ee93f4eb55e153255fa onerror = this.src="../images/default.webp" style="width:35%;height:140px;float:right;">
                        </div>
                        <div style = "width:45%;float:left;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#FFFFFF;">
                            <strong style = "color:#FFFFFF;font-size:55px;">""" + x + """ </strong> <br>
                            <i style = "color:#E0E0E0;font-size:24px;"> Number of User &nbsp;: &nbsp;"""+ str(city[x]) + """ </i> <br>
                        </div>
                        <div style = "float:left;width:30%;">
                            <div class = "w3-container" onclick="myFunction2('Demo""" + str(829) + """')">
                                <center><r class="down1"></r></center>
                            </div>
                            <div id="Demo""" + str(829) + """\" class="w3-hide w3-right-align">
                                <ul class="w3-ul w3-card-4"> """)
        for y in top3[x]:
            print("""
                                    <li class="w3-bar" style = "background-color:white;">
                                        <img src="https:""" + y[2] + """" class="w3-bar-item w3-rectangle w3-hide-medium" style="width:85px">
                                        <div class="w3-bar-item">
                                            <span class="w3-large" style="float:left;">""" + y[0] + """</span><br>
                                            <span style = "float:left;"> """ + color[y[1]] + """</span>
                                        </div>
                                    </li>""")
        print("""               </ul>
                            </div>
                        </div>
                    </div>
                </div><div class = "row"> </div>""")
    else:
        s1 = str(cnt) 
        while len(s1) < 2:
            s1 = "&nbsp;&nbsp;" + s1
        print("""
                <div class="w3-container row" style="background-color:transparent;" onclick="myFunction2('Demo""" + str(cnt + 101) + """')">
                    <div style = "width:14%;float:left;">
                       <p class = "xyz"> <font size = "5"> <b>&nbsp;""" + s1 + """.</b>&nbsp;&nbsp;&nbsp;</font></p>
                    </div> 
                    <div class = ""w3-bar-item" style="width:68%;float:left;">
                        <span> <font size = "5"> <strong> """ + x + """ </strong> </font> </span>
                        <br> <span> <i style="color:grey;font-size: 18px;">  Number of Active User &nbsp;: &nbsp;""" + str(city[x]) + """</i></span>
                    </div>
                    <div style = "float:left;width:18%;margin-top:4.5%;height:15px;">
                        <center><g class="down"></g></center>
                    </div>
                    <div id="Demo""" + str(cnt + 101) + """\" class="w3-hide w3-right-align">
                        <ul class="w3-ul w3-card-4"> """)
        for y in top3[x]:
            print("""
                            <li class="w3-bar" style = "background-color:transparent">
                                <img src="https:""" + y[2] + """" class="w3-bar-item w3-rectangle w3-hide-medium" style="width:85px">
                                <div class="w3-bar-item">
                                    <span class="w3-large" style="float:left;">""" + y[0] + """</span><br>
                                    <span style = "float:left;"> """ + color[y[1]] + """</span>
                                </div>
                            </li>""")
        print("""       </ul>
                    </div>
                </div>
                <br>""")
    cnt += 1
    if cnt == 51:
        break