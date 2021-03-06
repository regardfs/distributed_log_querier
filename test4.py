import sys
import unittest
from io import StringIO
import logging
import client
import os
import subprocess


class test_sample(unittest.TestCase):
    def setUp(self):
        
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_ngrep_vmlog(self):
        # Null return for grep on vm.log to test from client to 1 server
        logging.info("Test1: Null Return Grep - Client to 1 Server")
        unix_cmd = 'grep zzzzzzz /usr/local/mp1/vm.log'
        recv = client.main_sub("server-names.txt", unix_cmd)
        exp = 0
        self.assertEqual(recv,exp)
        logging.info("Test1 Complete: Test for Null Return on vm.log")
        
    def test_ngrep_m_vmlog(self):
        # Null return for grep on vm.log to test from client to 4 server
        logging.info("Test2: Null Return Grep - Client to 4 Servers")
        unix_cmd = 'grep zzzzzzz /usr/local/mp1/vm.log'
        recv = client.main_sub("server-names.txt", unix_cmd)
        exp = 0
        self.assertEqual(recv,exp)
        logging.info("Test2 Complete: Test for Null Return on vm.log")

    def test_ngrep_a_vmlog(self):
        # Null return for grep on vm.log to test from client to 7 servers
        logging.info("Test3: Null Return Grep  - Client to 7 Servers")
        unix_cmd = 'grep zzzzzzzz /usr/local/mp1/vm.log'
        recv = client.main_sub("server-names.txt", unix_cmd)        
        exp = 0
        self.assertEqual(recv,exp)  
        logging.info("Test3 Complete : Test for Null Return on vm.log")
    
    def tearDown(self):
        sys.stdout = self.held
        
        
if __name__ == "__main__":
    logging.basicConfig(filename = "unitest4.log", level = logging.INFO, filemode = "w")
    unittest.main()
