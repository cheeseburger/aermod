#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:24:21 2024

@author: roelofburger
"""

class AERMET:
    def clean(self):
        print("Cleaning AERMET output files...")
        # Code to clean AERMET output files

    def create(self, config):
        self.config = config
        print("AERMET configuration created:", self.config)

    def show_config(self):
        print("AERMET configuration:", self.config)

    def run(self):
        print("Running AERMET...")
        # Code to run AERMET
        print("AERMET run complete.")

    def check_messages(self):
        print("Checking AERMET messages...")
        # Code to check AERMET messages