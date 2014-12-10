
import time
import urllib.request
import re
from array import array
import random

gfdg

class GetAHref:
  def get(self,data):
    for i in range(len(data)):                                               #and data[i-2]=="a"
      if(data[i]=="h" and data[i+1]=="r" and data[i+2]=="e" and data[i+3]=="f" ):
        pomoc=data[i+6:len(data)]
                 
    konec=pomoc.find('"')
    fin=pomoc[0:konec]
    if("http" in fin):
      return(fin)
            
rep=GetAHref()
default="http://example.com"
navstivene=[]


while True:
  
  f=""
  headers = { 'User-Agent' : 'Mozilla/5.0 (compatible; DrojdBot/1.0; +http://bot.drojd.cz)' }
  request = urllib.request.Request(default,None, headers)
  
  
  try:
    filehandle  = urllib.request.urlopen(request )
  except:
    print("bad request")
  
  set_pole=[]
  end_pole=[]
  
  for lines in filehandle.readlines():
    try:  
      lines=lines.decode("utf-8")
    except:
      try:
        lines=lines.decode("windows-1250")
      except:
        break
    
    l1=re.sub('\n','',lines)
    l2=re.sub('\t','',l1)
    set_pole.append(l2)
  
  
  
  filehandle.close()
  #print("_______________")
  #print(set_pole)
  
  for i in range(len(set_pole)):
    if("a href" in set_pole[i]):
      
      if((rep.get(set_pole[i]))):
        end_pole.append(rep.get(set_pole[i]))
      
  
  
  for f in range(len(end_pole)):
    None
    #print(end_pole[f])
    #print(f)


  try:
    default=end_pole[random.randint(1,f)]
  except:
    break
  
  
 ##### print("######################")
  print(default+"#")
 
  
  
  
  navstivene.append(default)
  end_pole=""
