seconds=int(input())
seconds2 = seconds % 60
minute=seconds//60
hour=minute//60
minute2=minute % 60
hour3=str(hour)
if hour < 10:
    hour3="0"+hour3
minute3=str (minute2)
if minute2 < 10:
    minute3="0"+minute3
seconds3=str (seconds2)
if seconds2 <10:
    seconds3 = "0"+seconds3



print(" %s : %s : %s" % (hour3, minute3, seconds3))

