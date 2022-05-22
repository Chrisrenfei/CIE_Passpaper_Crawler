import urllib.request
import os
import time
import re
# import package


def delay():
    print('Robot is tired. It need a 30 secodn rest, sir.')
    print('---------line---------')
    time.sleep(30)   
# crawl delay requested by gceduide.com


def input_info():
    print('This program supports users to download:')
    print('9231, 9608, 9618, 9701, 9702, 9708, 9709, 9389, 9489, 9696, 9990')
    print('Tips: Entre wrong information may result program ERROR!')
    print('---------line---------')    
    subjNum = input('Subject you want to download (example:9618): ')
    years = input('Years you want to download: (example:2021)')
    print('---------line---------')
    return subjNum, years   
# input paper information


def create_folder(folderName):  
    os.chdir(path + '/'+ subjNum + '_' + years )
    os.mkdir(folderName)
    os.chdir(folderName)
# Create folder under main floder for program to store the paper pdf and entre the floder location

def check_year():
    pass

def check_paper():
    pass
# This is the function that havn't been developed

def find_papers():
    relink_time = 1
    linksus = False
    while relink_time <= 5 and not linksus:
        subjUrl = url + subjDic[subjNum] + years + '/'
        print('the programme is trying to bulid bridge with gceguide.com')
        try:
            req = urllib.request.Request(subjUrl, data, headers)
            web_info = urllib.request.urlopen(req)
            web_html = web_info.read().decode('utf_8')
            linksus = True            
        except:
            print('Web Link falled')
            if relink_time == 5:
                print('Please try again later')
                print('program end')
                time.sleep(10)
                exit()
                
            print('The program will retry to link the website in ' + str(relink_time*5) + ' second after')
            print('---------line---------')
            time.sleep(relink_time* 5)
# increment time delay for next rink 
        relink_time = relink_time + 1
# Set the maximum relink time allowed
    qplist = re.findall(subjNum + '_..._qp_..\.pdf',web_html)
    mslist = re.findall(subjNum + '_..._ms_..\.pdf',web_html)
    gtlist = re.findall(subjNum + '_..._gt\.pdf',web_html)
    print('get the paper list successfully')
    print('---------line---------')
    return qplist,mslist,gtlist      


def download_paper(list):
    
    folderName = subjNum + '_' + years + list[0][9:11]
    create_folder(folderName)
    listlen= len(list)
    print(subjNum + ' ' + list[0][9:11] + ' has started to download')
    print('---------line---------')
    for index in range(0,listlen,2):
        ThisPaper = list[index]
        thisUrl = url + subjDic[subjNum] + years + '/' + ThisPaper
        print('paper ' + ThisPaper + ' has started to download')
        try:
            req = urllib.request.Request(thisUrl, data, headers)
            tempFile = urllib.request.urlopen(req)
            paper = tempFile.read()
            # try to get the file from server
            
            with open(ThisPaper, 'wb') as f:
                f.write(paper)
            print('papper '+ ThisPaper + '.pdf' + ' download successfully')
            print('---------line---------')
            delay()
            # download the paper
                          
        except:
            print('Site access failed')
            print('paper download failed')
            print('---------line---------')
            delay()
    print('all ' + subjNum + ' ' + list[0][9:10] + 'has downloaded')
    print('---------line---------')



# This is the main program

print('CIE_Passpaper_Crawler version 2.0')
print('---------line---------')

url = 'https://papers.gceguide.com/A%20Levels/'
data = {}
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
subjDic = {
'9231':'Mathematics%20-%20Further%20(9231)/',
'9608':'Computer%20Science%20(for%20final%20examination%20in%202021)%20(9608)/',
'9618':'Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)/',
'9701':'Chemistry%20(9701)/',
'9702':'Physics%20(9702)/',
'9708':'Economics%20(9708)/',
'9709':'Mathematics%20(9709)/',
'9389':'History%20(for%20final%20examination%20in%202021)%20(9389)/',
'9489':'History%20(9489)/',
'9696':'Geography%20(9696)/',
'9990':'Psychology%20(9990)'}
# Subject support by the program, add new subject need to add element here
seaList1 = ['s', 'w']
papList = ['qp', 'ms']
path = os.getcwd()
print('Robot Initiallize successfully!')
# Initialize the variables

subjNum, years = input_info()
# Input download request information

folderName = subjNum + '_' + years
try:
    os.mkdir(folderName)
    os.chdir(folderName)
except:
    print(folderName + 'has existed, please first delete to folder and try again')
    print('program end')
    time.delay(10)
    exit()
# Try to create the main folder in the path

qplist,mslist,gtlist = find_papers()

download_paper(qplist)
download_paper(mslist)
download_paper(gtlist)

print('all paper has already been download, please check them in your computer')
print('Thanks for using')

time.sleep(10)
exit()
# end the program