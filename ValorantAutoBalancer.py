import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
print('※このアプリは、直近1試合の試合結果からチームを決定します。')
print('※アプリを使用するためには https://blitz.gg への登録が必要です。')
print('Riot IDを入力し，ENTERを押してください')
str = input()
print('TAGLINEを入力し，ENTERを押してください')
str1= input()
print('オートバランスの種類を選択します。1から3のいずれかを入力し、ENTERを押してください。')
print('以下オートバランスの種類')
print('1:平均スコアのみ')
print('2:ファーストブラッド数+平均スコア')
print('3:ファーストブラッド数のみ')
print('※オートバランスの種類を選択後Chromeが開きます。Chromeが自動的に終了するまで、マウスから手を離してお待ちください。')
auto = int(input())
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

CHROMEDRIVER = "..\driver\chromedriver"
chrome_service = fs.Service(executable_path=CHROMEDRIVER)

driver1 = webdriver.Chrome(service=chrome_service,options=ChromeOptions)
str3 = "https://blitz.gg/valorant/profile/"
str4 = str3+str+'-'+str1
driver1.get(str4)
time.sleep(5)
driver1.maximize_window()
time.sleep(5)
element = driver1.find_element(By.XPATH,'//*[@id="main-content"]/div[1]/div[1]/div/div[2]/div/div[2]/div/div[1]/div/a')
driver1.execute_script("arguments[0].scrollIntoView();", element)

element.send_keys(Keys.ENTER)
time.sleep(5)

element = driver1.find_element(By.XPATH,'//*[@id="main-content"]/div[1]/div[1]/div/div/div/div[2]/div[2]/section[4]/div')
driver1.execute_script("arguments[0].scrollIntoView();", element)

elem = element.text.split('\n')
time.sleep(5)

playerlist = [[0 for i in range(9)] for j in range(10)]
for p in range(10):
    if p < 5:
        name = elem[7+7*p]
        score = float(elem[8+7*p])
        kill = float(elem[9+7*p].split()[0])
        death = float(elem[9+7*p].split()[2])
        assist = float(elem[9+7*p].split()[4])
        econ = float(elem[10+7*p])
        fb = float(elem[11+7*p])
        plants = float(elem[12+7*p])
        defuses = float(elem[13+7*p])
    else:
        name = elem[7+7*p+7]
        score = float(elem[8+7*p+7])
        kill = float(elem[9+7*p+7].split()[0])
        death = float(elem[9+7*p+7].split()[2])
        assist = float(elem[9+7*p+7].split()[4])
        econ = float(elem[10+7*p+7])
        fb = float(elem[11+7*p+7])
        plants = float(elem[12+7*p+7])
        defuses = float(elem[13+7*p+7])

    playerlist[p][0] = name
    playerlist[p][1] = score
    playerlist[p][2] = kill
    playerlist[p][3] = death
    playerlist[p][4] = assist
    playerlist[p][5] = econ
    playerlist[p][6] = fb
    playerlist[p][7] = plants
    playerlist[p][8] = defuses


if auto == 1:
    rank = sorted(playerlist, reverse=True, key=lambda x:(x[1]))
elif auto == 2:
    rank = sorted(playerlist, reverse=True, key=lambda x:(x[6],x[1]))
elif auto == 3:
    rank = sorted(playerlist, reverse=True, key=lambda x:(x[6]))

newteam =  [[0 for i in range(5)] for j in range(2)]
newteam[0][0] = rank[0][0]
newteam[0][1] = rank[9][0]
newteam[1][0] = rank[1][0]
newteam[1][1] = rank[8][0]

newteam[0][2] = rank[3][0]
newteam[0][3] = rank[6][0]
newteam[1][2] = rank[2][0]
newteam[1][3] = rank[7][0]

newteam[0][4] = rank[4][0]
newteam[1][4] = rank[5][0]

print("アタッカー")
print(newteam[0])
print(" ")
print("ディフェンダー")
print(newteam[1])

time.sleep(100)
driver1.quit()