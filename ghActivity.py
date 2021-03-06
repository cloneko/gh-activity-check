#!/usr/bin/python3
import xml.etree.ElementTree as et
import urllib.request

class ghActivity:

  request = urllib.request

  def wget(self,url):
    return self.request.urlopen(url).read()

  def getFeedById(self,id):

    update = []
    url = 'https://github.com/' + str(id) + '.atom'
    root = et.fromstring(self.wget(url)) 

    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
      updated = entry.find('{http://www.w3.org/2005/Atom}updated').text
      title   = entry.find('{http://www.w3.org/2005/Atom}title').text
      update.append({'updated':updated,'title':title}) 
      
    return (update) 
