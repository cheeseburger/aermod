#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:20:50 2024

@author: roelofburger
"""

class AERMOD:
    def __init__(self):
        self.domain_details = {}
        self.output_files = []
        self.aermet = AERMET()
        self.aermap = AERMAP()

    def run(self):
        if not self.check():
            print("Configuration incomplete. Please check the setup.")
            return
        print("Running AERMOD...")
        # Code to run AERMOD
        print("AERMOD run complete.")

    def check(self):
        # Check if all necessary configurations are set
        return True

    def create_domain(self, domain_details):
        self.domain_details = domain_details
        print("Domain created with details:", self.domain_details)

    def plot_concentration(self):
        print("Plotting concentration...")
        # Code to plot concentration

    def plot_wind_rose(self):
        print("Plotting wind rose...")
        # Code to plot wind rose