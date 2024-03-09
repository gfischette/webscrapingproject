from bs4 import BeautifulSoup
import requests
import csv
import time

link_list = ["/football/roster",
             "/baseball/roster"]

def get_baseball_football(url):
    page = requests.get("https://floridagators.com/sports" + url)
    soup = BeautifulSoup(page.text, 'html.parser')

    athletes = []
    
    
    name_list = soup.find_all("td", class_="sidearm-table-player-name")
    sport = soup.find_all("h2")[2].text
    if "2024 Spring Football Roster" in sport:
        sport = "2024 Football"
    else:
        sportnames = soup.find_all("h2")
        sport = sportnames[2].text.strip("Roster")

    hometown_list = soup.find_all("td", class_="hometownhighschool")
    for detail in range(len(name_list)):
        names = name_list[detail]
        hometown_detail = hometown_list[detail]

        name = names.find("a").text
        if hometown_detail:
            textstrip = hometown_detail.text
            split = textstrip.split("/")
            hometown = split[0]
            highschool = split[1]
        else:
            hometown = "not listed"
            highschool = "not listed"

        athlete_info = [sport, name, hometown, highschool]
        athletes.append(athlete_info)
    
    return athletes


link2_list = ["/mens-basketball/roster",
              "/womens-basketball/roster",
              "/mens-golf/roster",
              "/womens-golf/roster",
              "/womens-gymnastics/roster",
              "/womens-lacrosse/roster",
              "/womens-soccer/roster",
              "/softball/roster",
              "/mens-swimming-and-diving/roster",
              "/womens-swimming-and-diving/roster",
              "/mens-tennis/roster",
              "/womens-tennis/roster",
              "/womens-volleyball/roster"]

def get_other_sports(url_again):
    page = requests.get("https://floridagators.com/sports" + url_again)
    soup = BeautifulSoup(page.text, 'html.parser')

    athletes = []
    
    sportnames = soup.find_all("h2")
    sport = sportnames[2].text.strip("Roster")
    
    players = soup.find(class_="sidearm-roster-players")
    for detail in players.find_all(class_="sidearm-roster-player"):
        player_name = detail.find(class_="sidearm-roster-player-name")
        name = player_name.find("a").text
        hometownfind = detail.find(class_="sidearm-roster-player-hometown")
        if hometownfind:
            hometown = hometownfind.text
        else:
            hometown = "not listed"
        highschoolfind = detail.find("span", class_="sidearm-roster-player-highschool")
        if highschoolfind:
            highschool = highschoolfind.text
        else:
            highschool = "not listed"
        athlete_info = [sport, name, hometown, highschool]
        athletes.append(athlete_info)

    return athletes


link3_list = ["/track-and-field/roster",
              "/cross-country/roster"]

def get_running(url_again_again):
    page = requests.get("https://floridagators.com/sports" + url_again_again)
    soup = BeautifulSoup(page.text, 'html.parser')

    athletes = []

    sportnames = soup.find_all("h2")
    sport = sportnames[2].text.strip("Roster")

    players_overarching = soup.find_all(class_="sidearm-roster-players")
    for players in players_overarching:
        for detail in players.find_all(class_="sidearm-roster-player"):
            player_name = detail.find(class_="sidearm-roster-player-name")
            name = player_name.find("a").text
            hometownfind = detail.find(class_="sidearm-roster-player-hometown")
            if hometownfind:
                hometown = hometownfind.text
            else:
                hometown = "not listed"
            highschoolfind = detail.find("span", class_="sidearm-roster-player-highschool")
            if highschoolfind:
                highschool = highschoolfind.text
            else:
                highschool = "not listed"
            athlete_info = [sport, name, hometown, highschool]
            athletes.append(athlete_info)

    return athletes


def write_csv(link_list, link2_list, link3_list):
    csvfile = open('ufsports.csv', 'w', newline='', encoding='utf-8')
    c = csv.writer(csvfile)
    c.writerow(['sport', 'name', 'hometown', 'highschool'])
    for url in link_list:
        player_details = get_baseball_football(url)
        c.writerows(player_details)
    for url2 in link2_list:
        player_details2 = get_other_sports(url2)
        c.writerows(player_details2)
        time.sleep(1)
    for url3 in link3_list:
        player_details3 = get_running(url3)
        c.writerows(player_details3)
    csvfile.close()
    return None


write_csv(link_list, link2_list, link3_list)

