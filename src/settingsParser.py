#! /usr/bin/env python

import xml.etree.ElementTree as et

class settings_parser():
    
    def initialize(self, filename):
        self.settings = {}
        xml_settings = et.parse("../chris_home.xml")
        
        doc_root = xml_settings.getroot()
        
        for child in doc_root.findall('dest_db_connection'):
            self.settings['type'] = child.get('server_type')
            self.settings['name'] = child.get('name')
            self.settings['connection'] = child.find('connection').text
            self.settings['port'] = child.find('port').text
            self.settings['db_name'] = child.find('db_name').text
            self.settings['user'] = child.find('username').text
            self.settings['password'] =child.find('password').text
            
            #print self.settings['name']
            #print self.settings['connection']
            #print self.settings['port']
            #print self.settings['db_name']
            #print self.settings['user']
            #print self.settings['password']
            
            return self.settings
    
    