import random,time
def getrandomdate(startdate,enddate):
    print(f"random date between {startdate} and {enddate}")
    randomgenerator =random.random()
    dateformat='%m/%d/%y'
    starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime=starttime+randomgenerator*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("random date=",getrandomdate("1/1/2016","2/12/2025"))
