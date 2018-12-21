import slackweb
import trainInfo
import configparser

# read ini
inifile = configparser.ConfigParser()
inifile.read('conf/config.ini', 'UTF-8')

# webhook url
url=inifile.get('settings','webhookurl')
print(url)
# 確認したい路線(list)
train=inifile.get('train','lines').split(',')
print(train)

slack = slackweb.Slack(url=url)
slack.notify(text=trainInfo.request(train))