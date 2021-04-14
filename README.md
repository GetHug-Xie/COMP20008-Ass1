# COMP20008 2021 Semester 1 Assignment 1
Readme file

Student Name: Jie Xie
Student ID: 1174437

Brief description: 
This assignment contains two parts. 
In part A I built a dataframe based on the data about COVID-19, and plotted 2 graphs of case fatality rate vs confirmed new cases. 
Part B is about word processing. I saved all files in the local folder "cricket" and access each file in that.
In part B I listed all files with their documentID, and wrote some program about searching for keywords in a text.

A list of dependencies (the libraries, what you need to import):
import pandas;
import argparse;
import matplotlib.pyplot;
import math;
import re;
import os;
import sys;
import nltk;
from nltk.stem import PorterStemmer;
from nltk.tokenize import sent_tokenize, word_tokenize;
from IPython.display import display;
