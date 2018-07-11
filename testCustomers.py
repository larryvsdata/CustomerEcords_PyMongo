#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:42:03 2018

@author: ermanbekaroglu
"""

import unittest
from Customers import Customers
from datetime import datetime

class TestCustomers(unittest.TestCase):
    
    def setUp(self):
        self.testCustomers=Customers()
        self.testCustomers.saveRecords()
        self.recordLatest={"account_id" : 5421654, "event_date": str(datetime.now()).split()[0], "account_standing": "G", "account_information": {"first_name": "Mark", "last_name": "zabinsky", "date_of_birth": "1966-09-18", "address": {"street_number": "153", "street_name": "Fort Street", "city": "Emeraldville", "state": "CA", "zip_code": "91341"}, "email_address": "mark_zabinsky@gmail.com"} }
        self.recordWrong={"account_id" : 54165, "event_date": str(datetime.now()).split()[0], "account_standing": "G", "account_information": {"first_name": "Mark", "last_name": "zabinsky", "date_of_birth": "1966-09-18", "address": {"street_number": "153", "street_name": "Fort Street", "city": "Emeraldville", "state": "CA", "zip_code": "91341"}, "email_address": "mark_zabinsky@gmail.com"} }
    
    def testLatest(self):
        print("Testing the latest entry")
        self.testCustomers.insertARecord(self.recordLatest)
        self.assertEqual(self.testCustomers.findTheLatest(),self.recordLatest)
        
    def testDelete(self):
        print("Testing the delete function")
        self.testCustomers.insertARecord(self.recordLatest)
        self.testCustomers.deleteARecord(self.recordLatest["account_id"])
        self.assertEqual(self.testCustomers.exists(self.recordLatest["account_id"]),False)
        
    def testCheckRecord(self):
        print("Testing the check function")
        self.assertEqual(self.testCustomers.checkOneRecord(self.recordWrong),False)
    
    
if __name__ == "__main__":
    unittest.main()
