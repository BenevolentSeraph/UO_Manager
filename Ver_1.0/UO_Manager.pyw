# Need to do:
#   -   Auto-Update (keep track of versions)
#   -   Enhance the captcha solver to 100% accuracy

from pyperclip import copy
from threading import Thread
import cv2 as cv
import numpy as np
from os import getcwd, listdir, system, remove, mkdir
from os.path import isfile, isdir
import pyautogui
from time import sleep, time
from winsound import Beep
from datetime import datetime
from random import randint

import sys
sys.path.insert(0,"H:\Programming\Python\Modules")
from Pygame.GUIV4 import *

VERSION = 1.0

# Hidden imports: pygame, keyboard, playsound
# pyinstaller --hidden-import=pygame --hidden-import=keyboard --hidden-import=playsound --onefile -w UO_Manager.pyw

# Required Files

INSTRUCTIONS = """<html><head><meta content="text/html; charset=UTF-8" http-equiv="content-type"><style type="text/css">ol.lst-kix_sj0p28gentvp-7.start{counter-reset:lst-ctn-kix_sj0p28gentvp-7 0}ol.lst-kix_nimzqz9k5q9s-1{list-style-type:none}ol.lst-kix_68a5avympjv1-4.start{counter-reset:lst-ctn-kix_68a5avympjv1-4 0}ol.lst-kix_nimzqz9k5q9s-0{list-style-type:none}.lst-kix_68a5avympjv1-3>li:before{content:"" counter(lst-ctn-kix_68a5avympjv1-3,decimal) ". "}.lst-kix_68a5avympjv1-4>li:before{content:"" counter(lst-ctn-kix_68a5avympjv1-4,lower-latin) ". "}.lst-kix_sj0p28gentvp-0>li:before{content:"" counter(lst-ctn-kix_sj0p28gentvp-0,decimal) ". "}.lst-kix_sj0p28gentvp-2>li:before{content:"" counter(lst-ctn-kix_sj0p28gentvp-2,lower-roman) ". "}ol.lst-kix_nimzqz9k5q9s-5{list-style-type:none}ol.lst-kix_nimzqz9k5q9s-4{list-style-type:none}.lst-kix_68a5avympjv1-1>li:before{content:"" counter(lst-ctn-kix_68a5avympjv1-1,lower-latin) ". "}.lst-kix_68a5avympjv1-2>li:before{content:"" counter(lst-ctn-kix_68a5avympjv1-2,lower-roman) ". "}.lst-kix_68a5avympjv1-5>li:before{content:"" counter(lst-ctn-kix_68a5avympjv1-5,lower-roman) ". "}.lst-kix_68a5avympjv1-6>li:before{content:"" counter(lst-ctn-kix_68a5avympjv1-6,decimal) ". "}ol.lst-kix_nimzqz9k5q9s-3{list-style-type:none}.lst-kix_sj0p28gentvp-1>li:before{content:"" counter(lst-ctn-kix_sj0p28gentvp-1,lower-latin) ". "}.lst-kix_sj0p28gentvp-5>li:before{content:"" counter(lst-ctn-kix_sj0p28gentvp-5,lower-roman) ". "}ol.lst-kix_nimzqz9k5q9s-2{list-style-type:none}ol.lst-kix_axid0ojgfcq6-2.start{counter-reset:lst-ctn-kix_axid0ojgfcq6-2 0}.lst-kix_nimzqz9k5q9s-3>li{counter-increment:lst-ctn-kix_nimzqz9k5q9s-3}ol.lst-kix_nimzqz9k5q9s-8{list-style-type:none}.lst-kix_axid0ojgfcq6-6>li{counter-increment:lst-ctn-kix_axid0ojgfcq6-6}ol.lst-kix_nimzqz9k5q9s-7{list-style-type:none}.lst-kix_sj0p28gentvp-6>li:before{content:"" counter(lst-ctn-kix_sj0p28gentvp-6,decimal) ". "}ol.lst-kix_nimzqz9k5q9s-2.start{counter-reset:lst-ctn-kix_nimzqz9k5q9s-2 0}ol.lst-kix_nimzqz9k5q9s-6{list-style-type:none}.lst-kix_sj0p28gentvp-7>li:before{content:"" counter(lst-ctn-kix_sj0p28gentvp-7,lower-latin) ". "}ol.lst-kix_68a5avympjv1-1.start{counter-reset:lst-ctn-kix_68a5avympjv1-1 0}ol.lst-kix_sj0p28gentvp-4.start{counter-reset:lst-ctn-kix_sj0p28gentvp-4 0}.lst-kix_axid0ojgfcq6-5>li{counter-increment:lst-ctn-kix_axid0ojgfcq6-5}.lst-kix_nimzqz9k5q9s-4>li{counter-increment:lst-ctn-kix_nimzqz9k5q9s-4}.lst-kix_68a5avympjv1-7>li:before{content:"" counter(lst-ctn-kix_68a5avympjv1-7,lower-latin) ". "}.lst-kix_68a5avympjv1-8>li:before{content:"" counter(lst-ctn-kix_68a5avympjv1-8,lower-roman) ". "}.lst-kix_68a5avympjv1-4>li{counter-increment:lst-ctn-kix_68a5avympjv1-4}.lst-kix_sj0p28gentvp-4>li:before{content:"" counter(lst-ctn-kix_sj0p28gentvp-4,lower-latin) ". "}.lst-kix_sj0p28gentvp-3>li:before{content:"" counter(lst-ctn-kix_sj0p28gentvp-3,decimal) ". "}.lst-kix_nimzqz9k5q9s-2>li{counter-increment:lst-ctn-kix_nimzqz9k5q9s-2}ol.lst-kix_sj0p28gentvp-1.start{counter-reset:lst-ctn-kix_sj0p28gentvp-1 0}.lst-kix_nimzqz9k5q9s-5>li{counter-increment:lst-ctn-kix_nimzqz9k5q9s-5}.lst-kix_axid0ojgfcq6-4>li{counter-increment:lst-ctn-kix_axid0ojgfcq6-4}ol.lst-kix_nimzqz9k5q9s-8.start{counter-reset:lst-ctn-kix_nimzqz9k5q9s-8 0}ol.lst-kix_sj0p28gentvp-7{list-style-type:none}.lst-kix_68a5avympjv1-5>li{counter-increment:lst-ctn-kix_68a5avympjv1-5}ol.lst-kix_sj0p28gentvp-6{list-style-type:none}ol.lst-kix_sj0p28gentvp-5{list-style-type:none}.lst-kix_68a5avympjv1-2>li{counter-increment:lst-ctn-kix_68a5avympjv1-2}ol.lst-kix_sj0p28gentvp-4{list-style-type:none}ol.lst-kix_axid0ojgfcq6-7.start{counter-reset:lst-ctn-kix_axid0ojgfcq6-7 0}ol.lst-kix_sj0p28gentvp-8{list-style-type:none}.lst-kix_68a5avympjv1-0>li:before{content:"" counter(lst-ctn-kix_68a5avympjv1-0,decimal) ". "}ol.lst-kix_sj0p28gentvp-3{list-style-type:none}ol.lst-kix_sj0p28gentvp-2{list-style-type:none}.lst-kix_axid0ojgfcq6-7>li{counter-increment:lst-ctn-kix_axid0ojgfcq6-7}ol.lst-kix_sj0p28gentvp-1{list-style-type:none}ol.lst-kix_nimzqz9k5q9s-5.start{counter-reset:lst-ctn-kix_nimzqz9k5q9s-5 0}ol.lst-kix_sj0p28gentvp-0{list-style-type:none}ol.lst-kix_nimzqz9k5q9s-4.start{counter-reset:lst-ctn-kix_nimzqz9k5q9s-4 0}.lst-kix_nimzqz9k5q9s-6>li{counter-increment:lst-ctn-kix_nimzqz9k5q9s-6}.lst-kix_axid0ojgfcq6-3>li{counter-increment:lst-ctn-kix_axid0ojgfcq6-3}ol.lst-kix_sj0p28gentvp-5.start{counter-reset:lst-ctn-kix_sj0p28gentvp-5 0}.lst-kix_nimzqz9k5q9s-0>li{counter-increment:lst-ctn-kix_nimzqz9k5q9s-0}ol.lst-kix_axid0ojgfcq6-8.start{counter-reset:lst-ctn-kix_axid0ojgfcq6-8 0}ol.lst-kix_68a5avympjv1-3.start{counter-reset:lst-ctn-kix_68a5avympjv1-3 0}ol.lst-kix_nimzqz9k5q9s-3.start{counter-reset:lst-ctn-kix_nimzqz9k5q9s-3 0}.lst-kix_nimzqz9k5q9s-4>li:before{content:"" counter(lst-ctn-kix_nimzqz9k5q9s-4,lower-latin) ". "}.lst-kix_68a5avympjv1-3>li{counter-increment:lst-ctn-kix_68a5avympjv1-3}.lst-kix_nimzqz9k5q9s-3>li:before{content:"" counter(lst-ctn-kix_nimzqz9k5q9s-3,decimal) ". "}.lst-kix_nimzqz9k5q9s-7>li:before{content:"" counter(lst-ctn-kix_nimzqz9k5q9s-7,lower-latin) ". "}.lst-kix_sj0p28gentvp-5>li{counter-increment:lst-ctn-kix_sj0p28gentvp-5}ol.lst-kix_sj0p28gentvp-6.start{counter-reset:lst-ctn-kix_sj0p28gentvp-6 0}.lst-kix_nimzqz9k5q9s-0>li:before{content:"" counter(lst-ctn-kix_nimzqz9k5q9s-0,decimal) ". "}.lst-kix_nimzqz9k5q9s-8>li:before{content:"" counter(lst-ctn-kix_nimzqz9k5q9s-8,lower-roman) ". "}.lst-kix_sj0p28gentvp-8>li{counter-increment:lst-ctn-kix_sj0p28gentvp-8}.lst-kix_nimzqz9k5q9s-2>li:before{content:"" counter(lst-ctn-kix_nimzqz9k5q9s-2,lower-roman) ". "}.lst-kix_68a5avympjv1-0>li{counter-increment:lst-ctn-kix_68a5avympjv1-0}.lst-kix_nimzqz9k5q9s-1>li:before{content:"" counter(lst-ctn-kix_nimzqz9k5q9s-1,lower-latin) ". "}.lst-kix_sj0p28gentvp-8>li:before{content:"" counter(lst-ctn-kix_sj0p28gentvp-8,lower-roman) ". "}.lst-kix_68a5avympjv1-6>li{counter-increment:lst-ctn-kix_68a5avympjv1-6}.lst-kix_sj0p28gentvp-2>li{counter-increment:lst-ctn-kix_sj0p28gentvp-2}.lst-kix_nimzqz9k5q9s-6>li:before{content:"" counter(lst-ctn-kix_nimzqz9k5q9s-6,decimal) ". "}.lst-kix_nimzqz9k5q9s-5>li:before{content:"" counter(lst-ctn-kix_nimzqz9k5q9s-5,lower-roman) ". "}ol.lst-kix_axid0ojgfcq6-1{list-style-type:none}ol.lst-kix_axid0ojgfcq6-2{list-style-type:none}ol.lst-kix_axid0ojgfcq6-0{list-style-type:none}.lst-kix_axid0ojgfcq6-0>li{counter-increment:lst-ctn-kix_axid0ojgfcq6-0}ol.lst-kix_axid0ojgfcq6-5{list-style-type:none}ol.lst-kix_axid0ojgfcq6-6{list-style-type:none}ol.lst-kix_axid0ojgfcq6-3{list-style-type:none}ol.lst-kix_axid0ojgfcq6-4{list-style-type:none}ol.lst-kix_sj0p28gentvp-0.start{counter-reset:lst-ctn-kix_sj0p28gentvp-0 0}.lst-kix_sj0p28gentvp-3>li{counter-increment:lst-ctn-kix_sj0p28gentvp-3}.lst-kix_axid0ojgfcq6-0>li:before{content:"" counter(lst-ctn-kix_axid0ojgfcq6-0,decimal) ". "}ol.lst-kix_nimzqz9k5q9s-6.start{counter-reset:lst-ctn-kix_nimzqz9k5q9s-6 0}ol.lst-kix_axid0ojgfcq6-6.start{counter-reset:lst-ctn-kix_axid0ojgfcq6-6 0}.lst-kix_sj0p28gentvp-4>li{counter-increment:lst-ctn-kix_sj0p28gentvp-4}.lst-kix_axid0ojgfcq6-1>li:before{content:"" counter(lst-ctn-kix_axid0ojgfcq6-1,lower-latin) ". "}ol.lst-kix_68a5avympjv1-8.start{counter-reset:lst-ctn-kix_68a5avympjv1-8 0}.lst-kix_axid0ojgfcq6-2>li:before{content:"" counter(lst-ctn-kix_axid0ojgfcq6-2,lower-roman) ". "}ol.lst-kix_axid0ojgfcq6-7{list-style-type:none}.lst-kix_axid0ojgfcq6-3>li:before{content:"" counter(lst-ctn-kix_axid0ojgfcq6-3,decimal) ". "}.lst-kix_axid0ojgfcq6-5>li:before{content:"" counter(lst-ctn-kix_axid0ojgfcq6-5,lower-roman) ". "}ol.lst-kix_axid0ojgfcq6-8{list-style-type:none}ol.lst-kix_axid0ojgfcq6-3.start{counter-reset:lst-ctn-kix_axid0ojgfcq6-3 0}.lst-kix_axid0ojgfcq6-4>li:before{content:"" counter(lst-ctn-kix_axid0ojgfcq6-4,lower-latin) ". "}.lst-kix_nimzqz9k5q9s-8>li{counter-increment:lst-ctn-kix_nimzqz9k5q9s-8}ol.lst-kix_sj0p28gentvp-8.start{counter-reset:lst-ctn-kix_sj0p28gentvp-8 0}.lst-kix_axid0ojgfcq6-1>li{counter-increment:lst-ctn-kix_axid0ojgfcq6-1}ol.lst-kix_68a5avympjv1-5.start{counter-reset:lst-ctn-kix_68a5avympjv1-5 0}ol.lst-kix_axid0ojgfcq6-1.start{counter-reset:lst-ctn-kix_axid0ojgfcq6-1 0}ol.lst-kix_68a5avympjv1-2.start{counter-reset:lst-ctn-kix_68a5avympjv1-2 0}.lst-kix_68a5avympjv1-7>li{counter-increment:lst-ctn-kix_68a5avympjv1-7}ol.lst-kix_axid0ojgfcq6-4.start{counter-reset:lst-ctn-kix_axid0ojgfcq6-4 0}.lst-kix_sj0p28gentvp-0>li{counter-increment:lst-ctn-kix_sj0p28gentvp-0}.lst-kix_sj0p28gentvp-6>li{counter-increment:lst-ctn-kix_sj0p28gentvp-6}ol.lst-kix_nimzqz9k5q9s-7.start{counter-reset:lst-ctn-kix_nimzqz9k5q9s-7 0}.lst-kix_axid0ojgfcq6-2>li{counter-increment:lst-ctn-kix_axid0ojgfcq6-2}.lst-kix_68a5avympjv1-8>li{counter-increment:lst-ctn-kix_68a5avympjv1-8}.lst-kix_nimzqz9k5q9s-1>li{counter-increment:lst-ctn-kix_nimzqz9k5q9s-1}.lst-kix_axid0ojgfcq6-8>li{counter-increment:lst-ctn-kix_axid0ojgfcq6-8}.lst-kix_sj0p28gentvp-1>li{counter-increment:lst-ctn-kix_sj0p28gentvp-1}ol.lst-kix_axid0ojgfcq6-0.start{counter-reset:lst-ctn-kix_axid0ojgfcq6-0 0}ol.lst-kix_68a5avympjv1-6.start{counter-reset:lst-ctn-kix_68a5avympjv1-6 0}.lst-kix_68a5avympjv1-1>li{counter-increment:lst-ctn-kix_68a5avympjv1-1}ol.lst-kix_sj0p28gentvp-2.start{counter-reset:lst-ctn-kix_sj0p28gentvp-2 0}ol.lst-kix_nimzqz9k5q9s-1.start{counter-reset:lst-ctn-kix_nimzqz9k5q9s-1 0}.lst-kix_nimzqz9k5q9s-7>li{counter-increment:lst-ctn-kix_nimzqz9k5q9s-7}.lst-kix_sj0p28gentvp-7>li{counter-increment:lst-ctn-kix_sj0p28gentvp-7}.lst-kix_axid0ojgfcq6-7>li:before{content:"" counter(lst-ctn-kix_axid0ojgfcq6-7,lower-latin) ". "}.lst-kix_axid0ojgfcq6-6>li:before{content:"" counter(lst-ctn-kix_axid0ojgfcq6-6,decimal) ". "}ol.lst-kix_axid0ojgfcq6-5.start{counter-reset:lst-ctn-kix_axid0ojgfcq6-5 0}ol.lst-kix_68a5avympjv1-3{list-style-type:none}ol.lst-kix_68a5avympjv1-4{list-style-type:none}ol.lst-kix_68a5avympjv1-5{list-style-type:none}ol.lst-kix_68a5avympjv1-6{list-style-type:none}ol.lst-kix_68a5avympjv1-7{list-style-type:none}ol.lst-kix_68a5avympjv1-0.start{counter-reset:lst-ctn-kix_68a5avympjv1-0 0}ol.lst-kix_68a5avympjv1-8{list-style-type:none}li.li-bullet-0:before{margin-left:-18pt;white-space:nowrap;display:inline-block;min-width:18pt}.lst-kix_axid0ojgfcq6-8>li:before{content:"" counter(lst-ctn-kix_axid0ojgfcq6-8,lower-roman) ". "}ol.lst-kix_nimzqz9k5q9s-0.start{counter-reset:lst-ctn-kix_nimzqz9k5q9s-0 0}ol.lst-kix_68a5avympjv1-0{list-style-type:none}ol.lst-kix_68a5avympjv1-1{list-style-type:none}ol.lst-kix_68a5avympjv1-2{list-style-type:none}ol.lst-kix_sj0p28gentvp-3.start{counter-reset:lst-ctn-kix_sj0p28gentvp-3 0}ol.lst-kix_68a5avympjv1-7.start{counter-reset:lst-ctn-kix_68a5avympjv1-7 0}ol{margin:0;padding:0}table td,table th{padding:0}.c3{margin-left:72pt;padding-top:0pt;padding-left:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c0{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:12pt;font-family:"Arial";font-style:normal}.c4{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:14pt;font-family:"Arial";font-style:normal}.c2{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:10pt;font-family:"Arial";font-style:normal}.c5{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left;height:11pt}.c11{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:center}.c6{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c15{color:#000000;text-decoration:none;vertical-align:baseline;font-family:"Arial";font-style:normal}.c20{background-color:#ffffff;max-width:496.8pt;padding:57.6pt 57.6pt 57.6pt 57.6pt}.c14{margin-left:144pt;padding-left:0pt}.c16{font-weight:400;font-size:16pt}.c19{margin-left:108pt;padding-left:0pt}.c1{padding:0;margin:0}.c8{font-size:16pt;font-weight:700}.c10{margin-left:36pt;padding-left:0pt}.c18{font-style:italic}.c7{font-size:14pt}.c12{font-weight:700}.c13{margin-left:36pt}.c9{font-size:12pt}.c17{font-size:20pt}.title{padding-top:0pt;color:#000000;font-size:26pt;padding-bottom:3pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.subtitle{padding-top:0pt;color:#666666;font-size:15pt;padding-bottom:16pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}li{color:#000000;font-size:11pt;font-family:"Arial"}p{margin:0;color:#000000;font-size:11pt;font-family:"Arial"}h1{padding-top:20pt;color:#000000;font-size:20pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h2{padding-top:18pt;color:#000000;font-size:16pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h3{padding-top:16pt;color:#434343;font-size:14pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h4{padding-top:14pt;color:#666666;font-size:12pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h5{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h6{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;font-style:italic;orphans:2;widows:2;text-align:left}</style></head><body class="c20 doc-content"><p class="c11"><span class="c15 c12 c17">UO Manager Instructions</span></p><p class="c6"><span class="c15 c16">Features:</span></p><ol class="c1 lst-kix_68a5avympjv1-0 start" start="1"><li class="c6 c10 li-bullet-0"><span class="c7">Runebook Manager</span></li><li class="c6 c10 li-bullet-0"><span class="c4">Captcha Auto-Solver (&ldquo;Solve Captchas&rdquo; checkbox to enable/disable)</span></li><li class="c6 c10 li-bullet-0"><span class="c4">Auto-Installation</span></li></ol><p class="c5"><span class="c2"></span></p><p class="c6"><span class="c4">Auto-Installation:</span></p><p class="c6 c13"><span class="c0">The executable file (the main program named &ldquo;UO_Manager.exe&rdquo;) will create all the directories and files needed to keep the program alive. Upon running it for the first time, you&rsquo;ll notice a few things get created.</span></p><ol class="c1 lst-kix_nimzqz9k5q9s-0 start" start="1"><li class="c3 li-bullet-0"><span class="c0">The &ldquo;Books&rdquo; folder. This directory contains all the information regarding any rune books you create, stored easily in a text file.</span></li><li class="c3 li-bullet-0"><span class="c0">The second is the &ldquo;Temps&rdquo; folder. This is only for the captcha solver. It contains template images of the captcha message and buttons, in order to detect and solve them.</span></li><li class="c3 li-bullet-0"><span class="c0">You&rsquo;ll also notice the instructions page (this) be created just for practicality.</span></li></ol><p class="c6 c13"><span class="c9">It is important to know </span><span class="c9 c12">NOT</span><span class="c0">&nbsp;to manually mess with the directories or files that are created. Editing anything incorrectly could possibly corrupt your books and will certainly inhibit the main program.</span></p><p class="c5"><span class="c2"></span></p><p class="c6"><span class="c15 c16">Keeping track of runebooks:</span></p><ol class="c1 lst-kix_sj0p28gentvp-0 start" start="1"><li class="c6 c10 li-bullet-0"><span class="c4">Adding new books:</span></li></ol><ol class="c1 lst-kix_sj0p28gentvp-1 start" start="1"><li class="c3 li-bullet-0"><span class="c0">On the right-hand side of the UO Manager window, there are 4 things: An input field, 2 buttons, and a checkbox. The input field (for the runebook name) and top button (labeled &ldquo;Create Book&rdquo;) are for adding new books into the system.</span></li><li class="c3 li-bullet-0"><span class="c0">Once a book is created, you can exit or save/exit to see it in the main menu. Click it in the main menu to begin editing the book again.</span></li></ol><ol class="c1 lst-kix_sj0p28gentvp-0" start="2"><li class="c6 c10 li-bullet-0"><span class="c4">Editing books:</span></li></ol><ol class="c1 lst-kix_sj0p28gentvp-1 start" start="1"><li class="c3 li-bullet-0"><span class="c0">Upon clicking an existing book (on the left, if any are loaded) or upon creating a new book, you&rsquo;ll be taken to the editing page. The book name is listed right at the top center of the screen in big text, and there are 3 buttons for managing the book on the top right (save/exit, exit, delete).</span></li><li class="c3 li-bullet-0"><span class="c0">The book serial input field must be set to the serial of the runebook to be entered. To get this, you can click &ldquo;Object Inspector&rdquo; under the &ldquo;Macros&rdquo; tab in UOSteam.</span></li><li class="c3 li-bullet-0"><span class="c0">The book gump serial input field is where you enter the serial of the runebook&rsquo;s gump. To get it, record a macro and simply open the book. The gump&rsquo;s serial will be listed right between &ldquo;waitforgump&rdquo; and &ldquo;15000&rdquo; (separated by spaces).</span></li><li class="c3 li-bullet-0"><span class="c0">The target input fields correspond to the runes in the runebook. For example, the target #1 input field is for the tile coordinates (to be panned) in the first rune in the book. To get it, travel to the first rune and record a macro of you panning in the spot once. The tile&rsquo;s coordinates will be right after &ldquo;targettile&rdquo;.</span></li></ol><ol class="c1 lst-kix_sj0p28gentvp-0" start="3"><li class="c6 c10 li-bullet-0"><span class="c4">Generating macro:</span></li></ol><ol class="c1 lst-kix_sj0p28gentvp-1 start" start="1"><li class="c3 li-bullet-0"><span class="c0">Once you&rsquo;re satisfied with your collection of runebooks, you can automatically generate a UOSteam macro for them all using the &ldquo;Compile Books&rdquo; button in the main menu.</span></li><li class="c3 li-bullet-0"><span class="c0">There are a few requirements and stipulations for the macro:</span></li></ol><ol class="c1 lst-kix_sj0p28gentvp-2 start" start="1"><li class="c6 c19 li-bullet-0"><span class="c0">To keep track of all the MIBs (messages in a bottle) you&rsquo;ll obtain through the grind, you&rsquo;ll need a rune to your house, where you&rsquo;ll also afk between panning sessions. Your house should have a backpack right at the front door to store any MIBs. Consequently, the backpack will need to be emptied every 2-4 days.</span></li><li class="c6 c19 li-bullet-0"><span class="c0">For the rest of the items you&rsquo;ll obtain through panning, carrying a bank crystal is an absolute must. There will need to be 3 separate bags in your bank:</span></li></ol><ol class="c1 lst-kix_sj0p28gentvp-3 start" start="1"><li class="c6 c14 li-bullet-0"><span class="c0">A trash bag to get rid of shitty shoes that will be obtained occasionally.</span></li><li class="c6 c14 li-bullet-0"><span class="c0">A bag to store the gold nuggets.</span></li><li class="c6 c14 li-bullet-0"><span class="c0">A bag to store the large gems.</span></li></ol><ol class="c1 lst-kix_sj0p28gentvp-2" start="3"><li class="c6 c19 li-bullet-0"><span class="c0">On top of all of the bags, you&rsquo;ll also need a rune to your house (insured) in your inventory while you&rsquo;re panning.</span></li></ol><ol class="c1 lst-kix_sj0p28gentvp-1" start="3"><li class="c3 li-bullet-0"><span class="c0">After that&rsquo;s all said and done you can play the macro, follow the initial instructions to select the bags and house rune, then enjoy the wait.</span></li></ol><p class="c5"><span class="c0"></span></p><p class="c6"><span class="c7">Small side note</span><span class="c0">:</span></p><p class="c6 c13"><span class="c9">Once you run the captcha solver, you&rsquo;ll notice a file named &ldquo;Screenshot.png&rdquo; be created. It&rsquo;s a screenshot of your screen, used alongside the template images to detect if any captchas are active, and solve them if necessary. You </span><span class="c18 c9">may</span><span class="c0">&nbsp;delete this but only if the captcha solver isn&rsquo;t currently running.</span></p><p class="c5"><span class="c0"></span></p><p class="c6"><span class="c7">Expectations:</span></p><p class="c6 c13"><span class="c9">It is extremely tedious to set up the runebooks but once you do get it set up, you&rsquo;ll turn a profit like no other. If you maximize profits by using only large gold nugget spots in your runebooks and don&rsquo;t need to AFK at all (because panning through all of the books takes the entire gold depletion timer) you can expect to turn a profit well north of </span><span class="c12 c9">1,000,000</span><span class="c9">&nbsp;an hour. Regardless, taking the time to </span><span class="c9 c18">find</span><span class="c0">&nbsp;those large gold nugget spots to actually pan in is extraordinarily boring.</span></p><p class="c5"><span class="c0"></span></p><p class="c11"><span class="c8">Good Luck and Happy Panning!</span></p></body></html>"""

AFK_DATA = """137,80,78,71,13,10
26,10
0,0,0,13,73,72,68,82,0,0,0,82,0,0,0,18,8,6,0,0,0,200,116,137,247,0,0,0,1,115,82,71,66,0,174,206,28,233,0,0,0,4,103,65,77,65,0,0,177,143,11,252,97,5,0,0,0,9,112,72,89,115,0,0,18,116,0,0,18,116,1,222,102,31,120,0,0,12,86,73,68,65,84,88,71,109,152,63,139,227,88,22,197,175,171,101,120,2,11,244,160,4,37,24,195,42,152,160,38,88,214,19,109,45,116,82,208,193,20,116,82,65,5,27,76,184,159,163,63,75,111,214,11,149,52,84,210,80,201,4,149,173,179,113,48,129,22,106,65,6,27,36,176,64,175,65,69,207,239,200,114,219,61,204,157,158,178,45,61,189,123,239,185,231,254,121,154,44,126,90,124,241,149,55,243,157,85,245,218,114,127,97,206,188,213,23,181,249,38,182,80,117,220,51,235,234,198,98,62,37,85,23,236,210,82,11,141,179,186,104,184,80,152,185,202,154,16,44,205,115,179,186,178,120,29,216,163,176,220,42,43,227,218,210,58,183,144,59,11,181,161,35,54,11,236,217,149,195,158,78,123,241,108,215,57,118,231,127,182,240,220,175,170,134,103,82,43,194,154,61,47,44,184,96,46,14,86,118,233,176,192,97,119,158,87,44,172,121,30,77,121,131,158,212,98,246,232,92,142,217,232,43,214,214,241,120,108,181,117,40,141,217,222,97,68,197,179,141,75,45,117,13,91,165,86,179,119,46,179,28,79,177,166,98,141,108,168,141,251,210,199,103,199,58,99,95,107,240,143,189,186,34,128,79,42,120,236,149,159,253,248,174,207,55,102,187,214,124,246,189,89,31,108,214,121,75,62,183,214,238,122,235,250,198,182,130,54,9,86,161,44,235,123,11,109,97,113,139,117,249,204,154,168,177,168,143,216,172,183,56,201,172,143,74,179,201,204,18,208,72,34,153,30,44,154,78,184,159,90,59,137,45,75,90,172,5,112,0,157,102,115,139,88,89,130,69,130,161,61,96,196,209,212,146,36,49,219,196,60,15,0,19,76,179,214,214,255,219,96,199,139,245,201,185,205,219,18,27,50,115,197,212,194,51,246,132,23,203,0,60,113,145,197,219,96,187,8,128,147,210,90,108,79,63,199,182,237,112,188,237,109,187,118,214,70,216,217,123,158,153,153,99,31,199,247,36,75,108,218,199,246,140,79,253,52,183,190,222,88,75,192,146,190,53,56,0,6,53,122,231,214,248,200,242,38,216,164,223,2,226,185,197,65,6,54,54,133,75,175,230,127,137,222,89,211,91,214,214,246,204,197,190,195,104,34,33,32,118,113,107,57,223,219,136,13,123,174,77,34,219,184,115,11,219,169,197,41,208,37,83,145,7,3,91,235,243,200,90,226,145,108,123,155,182,173,237,102,185,77,26,216,192,130,124,118,110,237,11,108,128,201,53,32,54,44,36,108,214,78,215,56,144,0,96,194,254,189,181,40,107,48,212,79,182,86,225,88,210,108,109,211,162,103,110,150,69,47,230,60,193,168,182,22,0,219,114,217,220,163,35,216,148,128,86,221,214,182,3,209,83,155,99,87,89,73,67,102,191,97,127,148,41,200,51,128,109,205,101,248,30,111,44,144,21,46,74,248,228,249,170,183,138,207,28,186,122,215,218,100,18,240,37,64,141,11,243,144,36,56,236,219,62,227,39,160,147,124,29,251,122,48,123,198,190,208,59,3,99,155,44,254,118,249,197,147,114,29,14,6,82,68,180,190,254,4,219,70,121,188,187,129,201,21,209,111,236,230,61,108,251,19,89,222,93,219,226,195,227,240,253,225,231,5,127,73,41,254,222,190,127,26,174,173,222,22,164,125,138,1,80,79,169,33,48,61,233,78,24,98,216,239,2,229,3,182,47,62,46,135,245,167,178,124,123,216,143,228,100,93,238,214,86,83,134,226,10
212,96,161,145,254,138,102,197,110,228,43,43,127,0,112,82,29,71,20,100,149,18,254,177,61,165,137,43,157,199,6,9,65,109,130,242,28,43,96,95,165,138,66,106,212,216,231,184,222,240,112,10
89,252,234,191,124,97,15,149,57,71,121,33,143,11,214,214,37,30,166,202,55,244,176,231,25,159,252,131,234,212,39,87,248,175,32,62,220,93,14,159,215,31,30,208,69,180,194,197,240,91,114,127,87,216,253,155,11,123,120,115,105,247,56,90,86,39,0,99,4,152,88,161,186,59,202,42,22,80,40,146,30,252,143,89,163,202,18,119,128,128,167,193,55,223,128,248,240,243,94,183,68,215,133,125,199,127,5,245,204,5,202,138,64,117,170,233,141,81,122,71,125,141,21,5,32,228,251,160,184,85,105,43,106,62,106,244,143,5,170,227,232,234,248,76,169,215,254,18,88,115,75,61,89,195,231,237,251,165,93,253,178,182,34,199,46,106,109,94,3,146,202,127,90,16,64,118,80,96,88,155,19,149,10
125,34,74,44,42,112,171,162,71,156,9,209,160,72,114,231,250,253,74,42,237,17,6,1,135,61,190,185,26,126,223,124,92,241,75,241,221,139,171,157,93,82,153,189,26,139,204,76,143,32,123,26,72,83,199,182,248,244,48,94,225,54,191,201,89,243,164,166,232,209,1,136,12,171,26,26,27,214,58,195,185,81,30,94,23,128,226,108,249,243,237,120,5,67,87,107,180,172,217,66,76,41,213,203,8,136,16,146,85,10
16,219,229,23,86,138,97,242,82,20,92,120,251,231,199,210,174,200,138,82,205,173,172,1,4,202,52,212,87,50,79,30,118,100,98,30,4,232,200,82,4,78,90,13,91,43,130,155,211,64,139,120,77,224,213,164,40,75,10
130,76,117,106,53,172,196,4,49,51,224,207,153,56,236,4,200,192,152,189,120,82,70,89,131,157,95,165,169,142,140,145,237,161,188,32,30,29,236,38,8,216,249,85,194,15,118,251,105,159,230,146,213,155,197,208,21,149,122,37,81,110,80,26,216,88,221,49,69,7,109,147,136,30,29,201,249,93,202,181,106,31,84,73,40,96,25,25,81,145,83,149,186,36,41,94,224,172,114,186,26,2,204,222,48,50,85,154,43,176,124,52,229,209,120,158,194,77,244,194,33,117,115,71,211,41,9,160,38,5,96,181,0,67,15,18,211,240,60,172,47,208,163,53,43,17,124,0,227,66,79,91,85,2,176,18,16,166,58,50,66,159,10
202,228,230,239,215,95,42,106,10
157,220,46,63,236,193,90,190,189,130,214,112,21,244,23,80,94,242,240,246,114,96,230,31,101,5,115,26,54,188,250,120,4,239,32,79,164,126,141,17,184,182,175,193,148,15,53,175,161,188,72,33,255,60,142,169,1,93,143,53,118,73,201,168,113,196,96,96,76,154,118,53,169,204,248,83,23,232,127,127,100,185,228,158,140,185,253,180,175,195,7,121,32,112,36,46,25,241,39,182,98,207,10
194,220,158,148,145,39,101,29,217,117,245,254,91,251,239,223,92,99,31,97,42,106,238,29,123,134,228,241,13,125,67,197,151,136,57,1,26,86,118,86,7,70,0,82,73,179,225,65,22,31,159,168,23,203,175,32,14,34,52,70,81,253,124,188,91,240,121,13,136,21,5,124,188,241,7,185,194,25,146,145,56,178,183,34,203,84,80,107,254,131,194,30,198,16,63,64,229,15,41,116,16,129,28,96,143,135,133,170,61,196,115,96,237,1,196,211,250,153,187,99,109,150,45,146,155,79,75,216,94,80,26,142,235,20,208,229,29,229,7,226,29,64,92,141,101,235,138,64,164,154,149,71,57,148,51,101,149,106,238,1,196,135,215,199,253,232,64,100,78,73,61,229,43,78,52,148,136,51,37,131,186,232,48,48,141,242,8,35,239,223,94,219,227,169,209,213,145,254,129,161,87,192,120,106,13,136,64,249,163,67,143,128,124,143,225,7,25,234,174,134,121,213,47,58,100,67,125,165,218,88,153,174,173,4,64,71,0,189,246,27,197,1,130,70,152,193,107,214,56,186,244,73,140,209,125,252,209,145,134,95,165,254,117,252,66,157,139,135,220,219,255,64,84,17,131,253,56,28,24,14,178,58,9,66,117,242,61,86,55,28,165,58,1,56,31,234,208,94,84,213,75,74,98,77,61,30,136,136,77,103,169,10
158,58,149,42,231,40,170,28,5,117,40,86,75,28,69,206,31,68,140,138,41,246,142,72,232,132,112,188,195,58,192,114,212,196,229,48,6,141,18,43,85,97,25,251,57,21,24,0,84,147,200,169,167,57,77,168,210,201,101,20,117,70,167,110,78,224,110,105,22,55,159,8,148,59,65,50,62,58,164,147,203,65,130,63,218,159,210,157,135,177,104,20,53,13,69,163,171,79,136,225,11,123,186,187,178,199,215,215,240,72,246,237,37,29,10
224,94,134,94,58,74,141,157,7,201,57,233,168,165,104,196,114,208,136,47,118,230,49,210,139,25,39,70,57,28,212,192,164,230,122,144,78,125,126,20,14,134,195,167,198,15,185,21,116,116,26,37,39,162,142,61,5,240,65,134,99,89,129,114,49,69,251,106,156,208,109,141,35,24,171,57,246,32,139,15,180,26,152,243,77,215,63,97,215,237,88,199,37,149,114,107,148,125,243,25,133,41,161,60,101,164,244,193,156,70,0,143,82,3,244,213,135,39,187,254,229,113,176,225,32,129,33,252,32,67,25,28,229,250,151,99,205,173,99,6,31,64,244,66,147,78,46,242,156,73,135,138,125,197,12,121,144,152,27,129,34,91,95,30,169,141,134,175,66,133,227,33,64,224,187,54,249,38,247,200,249,253,78,199,186,215,97,145,128,45,233,212,40,131,33,156,109,185,205,188,75,72,8,11,215,150,111,143,14,44,96,225,65,150,212,98,117,241,123,70,50,201,195,235,147,81,139,89,241,32,11,216,43,185,127,125,53,164,158,186,218,211,184,246,154,122,119,197,158,41,71,182,229,191,246,153,114,51,54,163,39,106,103,206,19,7,169,148,13,163,136,133,247,52,89,201,18,246,30,196,169,164,209,209,83,152,28,56,119,27,25,53,185,250,105,241,69,229,177,226,161,156,104,116,41,51,18,39,7,6,21,46,194,83,161,194,120,224,52,162,48,182,112,8,96,158,130,206,92,247,80,90,239,25,124,93,50,119,49,222,214,29,205,132,180,215,92,74,180,74,168,88,0,67,125,241,15,50,91,96,43,196,123,67,115,186,177,202,96,131,81,58,70,134,18,184,52,159,237,163,195,190,4,147,148,208,112,161,227,27,165,216,234,244,87,244,163,152,58,74,149,29,114,232,122,156,36,116,2,210,238,1,3,61,181,171,82,77,99,238,76,85,22,180,41,135,10
13,208,10
220,16,105,157,140,232,202,195,201,134,75,144,152,203,26,134,126,64,15,171,134,210,80,112,13,77,106,144,37,99,145,14,1,122,179,49,96,177,127,78,175,47,116,34,58,227,172,1,73,48,152,69,117,202,195,205,175,168,66,49,93,85,39,30,53,21,91,177,28,160,27,214,13,47,104,140,194,142,17,53,27,122,91,97,103,24,142,77,238,80,168,49,174,4,184,20,166,150,24,28,214,204,113,0,53,204,104,212,169,152,110,28,226,106,48,91,186,5,178,195,64,53,153,78,77,73,35,19,170,229,74,80,57,80,208,233,220,195,27,30,233,71,31,190,241,49,24,51,136,138,211,48,163,131,166,230,102,201,254,188,160,153,149,15,200,161,55,71,158,180,204,41,73,42,39,195,158,248,37,27,26,26,78,13,154,122,3,37,156,99,72,37,119,6,251,148,125,116,105,53,37,7,104,41,250,245,210,69,11,114,26,146,130,254,106,118,62,127,231,122,186,169,125,54,215,207,44,68,47,214,79,157,205,179,198,56,251,91,203,119,107,91,172,234,169,25,59,115,73,108,201,228,5,203,123,75,136,122,223,204,184,23,89,217,198,54,37,122,9,86,236,50,98,9,115,120,10
247,34,203,56,220,251,98,102,187,40,182,245,228,55,235,49,176,119,173,245,155,200,242,172,176,201,108,98,61,135,255,109,136,0,179,177,222,111,108,186,155,96,39,172,228,119,4,170,89,179,225,155,183,89,210,90,18,247,182,241,122,123,147,88,249,111,103,235,255,204,113,188,183,122,2,0,241,204,146,77,111,190,237,109,199,158,58,149,240,195,214,191,37,128,25,44,82,225,143,35,123,6,136,180,105,45,204,209,193,117,213,246,105,232,109,154,244,214,17,173,105,194,115,210,142,63,41,224,187,112,78,99,244,150,224,209,58,237,129,195,217,115,243,127,139,230,122,33,82,217,171,252,187,252,93,159,113,123,10
245,49,46,238,35,254,119,214,227,212,115,210,216,247,128,59,153,155,109,85,242,219,207,134,54,75,48,34,100,23,214,111,245,170,11,131,183,189,129,23,6,101,54,221,52,54,253,140,83,91,69,25,198,246,137,109,178,220,166,220,207,4,82,4,176,51,0,219,228,128,14,128,68,187,126,201,112,190,181,172,197,134,140,193,125,151,0,76,1,184,156,109,1,164,33,152,13,97,113,216,105,122,99,67,64,18,156,153,102,60,215,78,9,102,9,147,33,0,132,208,91,157,164,223,50,9,204,248,141,210,25,182,109,177,237,60,181,120,186,177,77,255,87,174,11,91,108,153,65,89,72,146,225,163,109,169,213,172,245,24,58,137,209,131,198,4,139,49,216,252,142,245,16,169,79,18,91,197,91,155,97,79,75,48,34,233,175,216,124,218,219,43,255,93,241,46,106,48,70,239,201,136,100,22,49,210,64,231,128,195,17,197,185,105,103,86,204,217,172,132,97,78,239,242,10
219,36,145,222,16,14,198,236,100,236,37,27,183,107,155,19,209,141,10
67,15,219,232,144,240,205,60,251,77,167,80,123,55,29,198,156,225,157,32,142,18,14,130,69,206,146,90,9,207,166,243,57,44,227,185,93,106,224,73,144,90,216,170,215,91,128,254,76,96,53,106,96,167,39,138,129,26,152,189,36,86,111,112,48,62,183,26,96,197,42,143,243,42,19,147,108,110,13,37,33,202,98,107,39,4,6,128,29,65,137,27,130,208,123,236,132,186,48,184,65,175,83,38,96,75,50,83,254,232,93,107,139,126,79,233,104,41,23,91,139,240,101,66,109,16,177,35,254,36,122,73,186,211,39,231,167,154,245,192,22,44,179,223,1,66,130,67,187,200,213,123,201,0,0,0,0,73,69,78,68,174,66,96,130"""
# Converting to Bytes
AFK_DATA = AFK_DATA.replace("\n",",")
AFK_DATA = AFK_DATA.split(",")
for i in range(len(AFK_DATA)):
    AFK_DATA[i] = int(AFK_DATA[i])
AFK_DATA = bytes(AFK_DATA)


BUTTON_DATA = """137,80,78,71,13,10
26,10
0,0,0,13,73,72,68,82,0,0,0,30,0,0,0,22,8,6,0,0,0,215,99,44,207,0,0,0,1,115,82,71,66,0,174,206,28,233,0,0,0,4,103,65,77,65,0,0,177,143,11,252,97,5,0,0,0,9,112,72,89,115,0,0,18,116,0,0,18,116,1,222,102,31,120,0,0,0,66,105,84,88,116,77,105,99,114,111,115,111,102,116,46,71,97,109,101,68,86,82,46,73,100,0,0,0,101,110,45,117,115,0,0,97,53,97,50,49,101,51,101,45,53,55,54,102,45,52,101,50,102,45,56,50,98,51,45,55,99,100,97,98,50,99,53,54,55,101,53,96,157,197,216,0,0,0,73,105,84,88,116,77,105,99,114,111,115,111,102,116,46,71,97,109,101,68,86,82,46,84,105,116,108,101,0,0,0,101,110,45,117,115,0,0,85,108,116,105,109,97,32,79,110,108,105,110,101,32,45,32,75,97,114,97,116,104,101,111,110,32,40,85,79,32,69,118,111,108,117,116,105,111,110,41,67,23,77,5,0,0,0,52,105,84,88,116,77,105,99,114,111,115,111,102,116,46,71,97,109,101,68,86,82,46,65,117,116,104,111,114,0,0,0,101,110,45,117,115,0,0,77,105,99,114,111,115,111,102,116,32,71,97,109,101,32,68,86,82,138,46,159,123,0,0,0,52,105,84,88,116,77,105,99,114,111,115,111,102,116,46,71,97,109,101,68,86,82,46,66,97,115,105,99,0,0,0,101,110,45,117,115,0,0,48,33,33,33,33,33,33,48,33,33,48,33,33,49,51,51,55,33,33,127,205,20,3,0,0,0,101,105,84,88,116,77,105,99,114,111,115,111,102,116,46,71,97,109,101,68,86,82,46,66,97,115,105,99,72,97,115,104,0,0,0,101,110,45,117,115,0,0,51,55,48,54,57,48,50,97,97,97,49,48,97,54,49,50,52,102,51,99,52,102,51,56,55,54,100,98,101,49,54,101,50,100,55,48,98,99,51,102,98,56,54,57,49,98,57,50,99,97,52,99,102,102,48,51,51,98,99,51,50,57,56,51,208,16,175,239,0,0,0,188,105,84,88,116,77,105,99,114,111,115,111,102,116,46,71,97,109,101,68,86,82,46,69,120,116,101,110,100,101,100,0,1,0,101,110,45,117,115,0,0,120,156,125,204,177,14,194,32,20,133,225,119,185,115,49,244,34,109,195,236,210,197,197,78,26,135,91,184,77,72,90,48,128,198,196,248,238,162,15,224,252,127,231,188,96,141,150,214,209,129,1,210,132,45,43,22,186,239,22,177,103,92,196,128,179,18,189,117,52,163,213,93,207,26,26,184,165,104,57,231,35,109,92,71,118,245,28,202,142,159,92,211,131,83,246,49,128,105,27,200,133,82,153,252,15,161,68,37,164,22,216,78,136,6,149,193,225,92,57,7,247,31,108,236,60,29,238,137,74,125,29,195,137,109,12,46,131,145,223,84,200,81,33,48,151,235,251,3,154,190,58,170,141,59,122,164,0,0,0,96,105,84,88,116,77,105,99,114,111,115,111,102,116,46,71,97,109,101,68,86,82,46,72,97,115,104,0,0,0,101,110,45,117,115,0,0,100,53,51,56,51,100,49,99,49,52,55,102,49,98,57,51,54,51,101,99,101,50,48,56,55,97,102,50,50,100,51,54,55,97,57,101,49,50,102,97,55,54,102,101,56,55,102,55,48,53,48,48,98,52,53,52,101,54,52,102,56,52,102,49,8,178,70,9,0,0,3,194,73,68,65,84,72,75,173,86,61,76,219,64,20,126,208,32,217,82,34,229,6,36,223,232,74,69,50,82,135,100,171,7,134,172,221,202,152,49,99,199,118,35,3,67,198,176,177,50,50,54,35,99,70,87,42,18,72,12,120,96,240,0,146,189,217,18,145,236,129,138,190,239,157,47,152,20,65,85,248,164,139,239,255,123,239,187,123,239,178,54,153,236,221,151,101,69,85,101,75,73,104,91,160,143,200,33,165,28,233,71,211,113,48,226,112,189,224,254,46,183,93,202,243,92,250,154,208,90,81,81,228,188,174,238,96,184,46,81,183,171,105,109,111,239,219,61,58,138,162,160,52,77,27,228,50,143,97,140,112,93,179,169,233,55,198,24,84,50,214,220,220,194,101,22,24,137,253,234,30,38,117,216,32,223,16,195,139,162,72,153,56,227,146,139,39,22,226,48,195,120,9,60,16,154,122,83,133,85,56,53,177,29,55,202,249,62,19,91,169,147,159,71,4,195,106,158,55,71,90,249,108,64,197,30,119,153,152,165,22,226,100,198,26,26,82,182,255,205,217,173,106,81,130,243,245,12,241,225,225,244,222,41,230,228,178,22,95,39,115,177,10
8,130,128,226,56,150,250,107,49,30,133,236,87,73,179,121,198,231,235,145,231,105,90,7,145,31,244,184,244,101,18,164,64,9,195,190,144,59,108,208,75,101,50,25,255,213,215,132,199,103,170,245,54,215,30,46,225,58,194,64,251,125,30,236,201,2,28,188,214,90,228,25,14,119,107,114,51,249,57,132,97,88,215,12,154,228,218,15,72,121,62,215,16,1,166,111,29,97,36,242,218,131,96,96,209,229,229,153,144,142,70,67,26,12,6,98,144,82,74,198,237,113,192,192,193,32,148,249,189,94,64,253,126,95,198,236,184,69,179,9,143,17,126,45,196,88,154,156,81,190,226,214,249,121,76,243,249,156,118,119,191,8,97,28,95,114,146,168,141,100,128,12,201,3,231,101,99,188,215,51,99,81,20,201,215,34,79,99,42,150,177,12,242,138,90,88,152,38,177,92,174,85,204,102,39,226,41,100,196,185,27,117,176,1,8,112,150,152,133,36,129,186,73,22,0,190,81,116,102,26,140,44,185,164,70,50,20,188,219,217,9,247,139,155,83,90,44,22,244,43,94,44,229,204,178,76,250,174,175,83,218,220,212,180,181,245,94,60,83,10
4,138,218,237,141,154,172,69,173,22,86,180,104,99,195,229,254,182,40,209,237,110,46,163,226,131,94,99,163,23,116,149,81,61,222,161,117,12,20,124,193,32,227,83,192,226,131,131,3,58,62,254,33,109,144,194,56,215,237,46,139,245,30,233,16,49,26,4,219,148,36,28,180,53,242,162,164,188,202,101,142,185,92,142,241,88,253,190,33,213,105,83,180,226,177,5,60,63,61,61,165,139,139,115,238,135,129,119,108,121,135,58,157,77,186,189,197,67,129,7,3,51,91,252,93,208,254,254,148,174,174,174,232,238,238,14,157,20,126,84,180,193,71,2,143,149,106,243,90,151,90,144,15,113,166,216,90,78,108,108,145,203,135,95,178,117,216,236,241,193,224,194,161,172,34,138,56,1,177,39,200,245,227,241,68,188,197,122,11,205,251,151,124,55,156,36,91,222,106,145,26,9,4,177,12,82,207,243,36,44,172,231,255,10
67,58,126,36,177,133,199,175,17,94,36,72,108,28,131,54,12,173,251,228,176,199,184,185,136,89,27,143,171,97,241,28,166,211,67,254,53,9,8,107,161,154,85,76,233,128,31,32,212,207,185,148,162,142,120,44,15,3,3,242,224,50,33,126,97,57,22,34,179,189,84,134,195,145,204,183,237,38,105,19,80,31,222,34,4,215,166,211,201,125,207,47,197,210,239,147,19,33,182,132,79,45,254,31,28,77,135,114,179,103,115,156,189,18,101,13,177,78,40,252,52,32,14,75,227,169,49,235,213,128,221,56,251,36,227,127,54,121,69,113,225,49,177,73,214,203,63,2,159,251,252,103,32,78,88,10
246,84,134,222,8,188,25,148,139,43,251,250,153,215,107,73,108,243,45,44,132,20,22,88,228,56,104,63,54,7,183,222,134,156,228,123,94,135,182,13,35,179,238,33,164,154,109,215,117,232,15,91,159,24,243,132,124,240,194,0,0,0,0,73,69,78,68,174,66,96,130"""
# Converting to Bytes
BUTTON_DATA = BUTTON_DATA.replace("\n",",")
BUTTON_DATA = BUTTON_DATA.split(",")
for i in range(len(BUTTON_DATA)):
    BUTTON_DATA[i] = int(BUTTON_DATA[i])
BUTTON_DATA = bytes(BUTTON_DATA)

# Captcha Solver
PIC_PREFIX = "pic"
IMG_TYPE = "png"
TEMPLATE_DIR = "Temps"
AFK = cv.imread(f"{getcwd()}\{TEMPLATE_DIR}\AFK.{IMG_TYPE}",0)
BUTTON = cv.imread(f"{getcwd()}\{TEMPLATE_DIR}\Button.{IMG_TYPE}",0)

def rand_val(arr):
    return arr[randint(0,len(arr)-1)]

def detect_img(base, template, threshold):
    caught = []
    
    # match the template
    res = cv.matchTemplate(base, template, cv.TM_CCOEFF_NORMED)
    minv, maxv, minl, maxl = cv.minMaxLoc(base)
    loc = np.where(res >= threshold)
    h, w = template.shape

    # for each point detected, append it to the list
    for pt in zip(*loc[::-1]):
        caught.append((pt,(w,h)))

    # return the points where it found the image
    return caught

def solve(AFK, BUTTON):
    button_threshold = 0.9
    afk_threshold = 0.9

    base_dir = str(getcwd())
    
    pyautogui.screenshot(f"{base_dir}\Screenshot.{IMG_TYPE}")
    sleep(0.5)
    base = cv.imread(f"{base_dir}\Screenshot.{IMG_TYPE}",0)
    result = base.copy()

    # Check for the afk text
    captcha_present = len(detect_img(result, AFK, afk_threshold)) > 0 # returns whether it detected an afk img
    
    if captcha_present:
        caught = detect_img(result, BUTTON, button_threshold) # get the points where buttons were detected
        if len(caught) == 0: return False # it failed to detect any buttons, thus can't give an answer - return false
        pause = 0.2
        speed = 0.2
        answer = (rand_val(caught)[0][0]+12, rand_val(caught)[0][1]+8)
        pos = pyautogui.position()
        pyautogui.moveTo(answer[0], answer[1], speed)
        sleep(pause)
        pyautogui.click()
        sleep(pause)
        pyautogui.moveTo(pos[0], pos[1], speed)
        sleep(pause)
        #cv.imshow("Result",result)
        #cv.waitKey(0)
    return captcha_present

# Book Manager

class book:
    BOOK_DIR = "Books"
    FILE_TYPE = "txt"
    def __init__(self,filepath=""):
        self.filepath = filepath
        self.book = ["",""]
        self.targets = []
        for i in range(16):
            self.targets.append("")
        if filepath != "":
            self.load(filepath)
    def save(self,filepath=None):
        #print(filepath)
        if filepath == None: filepath = self.filepath
        f = open(f"{self.BOOK_DIR}\{filepath}.{self.FILE_TYPE}","w")
        lines = f"{self.book[0]},{self.book[1]}"
        for targ in self.targets:
            lines += f"\n{targ}"
        f.write(lines)
        f.close()
    def load(self,filepath):
        f = open(f"{self.BOOK_DIR}\{filepath}","r")
        lines = f.readlines()
        f.close()
        for x in range(len(lines)):
            if x == 0:
                lines[x] = lines[x].replace("\n","")
                l = lines[x].split(",")
                self.book = [l[0], l[1]]
            else:
                lines[x] = lines[x].replace("\n","")
                self.targets[x-1] = lines[x]
        #self.output()
    def output(self):
        print(f"Info\n{self.book[0]}\n{self.book[1]}")
        for y in range(len(self.targets)):
            print(y+1)
            print(self.targets[y])

def delete_book(b):
    global books, screens, active_screen
    screens[0] = screen()
    del books[b]
    remove(f"{book.BOOK_DIR}\{b}.{book.FILE_TYPE}")
    reload()
    active_screen = screens[0]

def create_book():
    global books, MAX_BOOKS, screens
    book_keys = tuple(books.keys())
    if len(book_keys) <= MAX_BOOKS:
        filepath = screens[0].get_object(1).text
        if not filepath in book_keys:
            if len(filepath) < 2 or filepath in book_keys: return False # name too short or already taken.
            books[filepath] = book()
            books[filepath].save(filepath)
            edit_book(filepath)
            return True
        else:
            message(5,'Name Taken.')
            return False
    else:
        message(5,'Books Full.')
        return False

def save_book():
    global screens, active_screen, books
    screens[0] = screen()
    filepath = screens[1].get_object(0).text
    serials = (screens[1].get_object(2).text, screens[1].get_object(4).text)
    targets = []
    for i in range(16):
        #print(6+i*2)
        targets.append(screens[1].get_object(6+i*2).text)
    books[filepath].book = serials
    books[filepath].targets = targets
    books[filepath].save(filepath)
    reload()
    active_screen = screens[0]
    #print(filepath)
    #print(serials)
    #print(targets)

def edit_book(filepath):
    global screens, active_screen, SCREEN_SIZE
    screens[1].remove_all()
    screens[1] = screen()
    s = screens[1]
    b = books[filepath]
        
    # Book serial and book gump serial
    s.add_objects((
        text([round(SCREEN_SIZE[0]/2),30], color=(200,200,200), border_width=0, text=f"{filepath}", font_size=24),
        text([55,80], color=(200,200,200), border_width=0, text=f"Book Serial:"),
        text_input([185,80], [150,40], color=(50,50,50), background_color=None, text_color=(200,200,200), valid_chars=ALPHANUMERIC, text=b.book[0]),
        text([355,80], color=(200,200,200), border_width=0, text=f"Book Gump Serial:"),
        text_input([510,80], [150,40], color=(50,50,50), background_color=None, text_color=(200,200,200), valid_chars=ALPHANUMERIC, text=b.book[1]),
    ))
    
    # all 16 targets
    column_size = 8
    for i in range(16):
        mult = (int(i/column_size), i%column_size)

        s.add_objects((
            text([45+mult[0]*280,130+mult[1]*40], color=(200,200,200), border_width=0, text=f"Target #{i+1}:", font_size=14),
            text_input([180+mult[0]*280,130+mult[1]*40], [180,25], color=(50,50,50), background_color=None, text_color=(200,200,200), valid_chars=ALPHANUMERIC, char_limit=15, font_size=14, text=b.targets[i]),
        ))

    # save/exit/delete
    size = [90, 40]
    s.add_objects((
        button([SCREEN_SIZE[0]-round(size[0]/2+5), round(size[1]/2)+5], size, color=(0,80,0), variables=globals(), function="save_book()"),
        text([SCREEN_SIZE[0]-round(size[0]/2+5), round(size[1]/2)+5], color=(200,200,200), border_width=0, text=f"Save/Exit"),
        button([SCREEN_SIZE[0]-round(size[0]/2+5), round(size[1]/2)+5 + size[1]+5], size, color=(0,0,80), variables=globals(), function="screens[0] = screen()\nactive_screen=screens[0]\nreload()"),
        text([SCREEN_SIZE[0]-round(size[0]/2+5), round(size[1]/2)+5 + size[1]+5], color=(200,200,200), border_width=0, text=f"Exit"),
        button([SCREEN_SIZE[0]-round(size[0]/2+5), round(size[1]/2)+5 + (size[1]+5)*2], size, color=(80,0,0), variables=globals(), function=f"delete_book('{filepath}')"),
        text([SCREEN_SIZE[0]-round(size[0]/2+5), round(size[1]/2)+5 + (size[1]+5)*2], color=(200,200,200), border_width=0, text=f"Delete"),
    ))
            
    active_screen = s

def compile():
    global books
    totallines = """usetype 0x1f1c
sysmsg 'Select your trash bag, must be in your bank!'
promptalias 'trash'
sysmsg 'Select your jewl bag, must be in your bank!'
promptalias 'jewl'
sysmsg 'Select your nugget bag, must be in your bank!'
promptalias 'nugget'
sysmsg 'Select your MIB bag, must be in your bank!'
promptalias 'mib'
sysmsg 'Select your home rune, must be in your backpack!'
promptalias 'home'
@settimer 'test' 0
while @timerexists 'test'\n"""

    _index = -1
    for y in books.keys():
        _index += 1
        #print(f"Generating a script for {y}.")
        script = ""
        lebook = books[y]
        for x in range(len(lebook.targets)):
            if lebook.targets[x] != "":
                script += f"""  @settimer 'peace' 11000
  if not @timerexists 'wither'
    @createtimer 'wither'
  endif
  @settimer 'wither' 4000
  while @timerexists 'test'
    clearjournal
    @useobject {lebook.book[0]}
    waitforgump {lebook.book[1]} 3000
    @replygump {lebook.book[1]} {7+6*x}
    @createtimer '3s'
    @settimer '3s' 0
    while @timer '3s' <= 3000
      pause 100
      if @injournal 'disturbed' 'system'
        break
      endif
      if @injournal 'This book' 'system'
        break
      endif
      if @injournal 'You have not yet recovered' 'system'
        break
      endif
      if @injournal 'blocked' 'system'
        break
      endif
    endwhile
    @removetimer '3s'
    if not @injournal 'disturbed' 'system'
      if not @injournal 'This book' 'system'
        if not @injournal 'You have not yet recovered' 'system'
          if not @injournal 'blocked' 'system'
            break
          endif
        endif
      endif
    endif
  endwhile
  clearjournal
  while @timerexists 'test'
    sysmsg 'Spot #{x+1}'
    @usetype 0x9d8
    pause 50
    @usetype 0x9d7
    waitfortarget 3000
    targettile {lebook.targets[x]}
    @createtimer '15s'
    @settimer '15s' 0
    while @timer '15s' <= 15000
      pause 100
      @getenemy 'enemy''murderer''gray''criminal''closest'
      if @inrange 'enemy' 10
        if @inrange 'enemy' 4
          if @timer 'wither' > 3000
            if mana > 30
              cast 'wither'
              @settimer 'wither' 0
            endif
          endif
        endif
        if @timer 'peace' >= 10000
          @useskill 'peacemaking'
          waitfortarget 1000
          @target 'enemy'
          pause 100
          if not @injournal 'You must wait' 'system'
            @settimer 'peace' 0
          endif
          if @injournal 'instrument' 'system'
            @settimer 'peace' 0
          endif
          if @injournal 'You must wait' 'system'
            @settimer 'peace' 9000
          endif
        endif
      endif
      if @injournal "pan for gold while riding!"
        @useobject 'self'
        pause 100
        break
      endif
      if @injournal 'You pan' 'system'
        break
      endif
      if @injournal 'There do' 'system'
        break
      endif
      if @injournal 'You need to be closer' 'system'
        break
      endif
      if @injournal 'Target cannot be seen' 'system'
        break
      endif
      if @injournal 'You are already' 'system'
        pause 3000
        break
      endif
    endwhile
    @removetimer '15s'
    if @injournal 'You need to be closer' 'system'
      @useobject {lebook.book[0]}
      waitforgump {lebook.book[1]} 3000
      @replygump {lebook.book[1]} {7+6*x}
      @createtimer '3s'
      @settimer '3s' 0
      while @timer '3s' <= 3000
        pause 100
        if @injournal 'disturbed' 'system'
          break
        endif
      endwhile
      @removetimer '3s'
    endif
    if @injournal 'Target cannot be seen' 'system'
      @useobject {lebook.book[0]}
      waitforgump {lebook.book[1]} 3000
      @replygump {lebook.book[1]} {7+6*x}
      @settimer '3s' 0
      while @timer '3s' <= 3000
        pause 100
        if @injournal 'disturbed' 'system'
          break
        endif
      endwhile
      @removetimer '3s'
    endif
    if @injournal 'There do' 'system'
      break
    endif
    if @injournal 'You pan'
      @usetype 0x9d8
      @createtimer '1s'
      @settimer '1s' 0
      while @timer '1s' <= 1000
        pause 100
        if @injournal 'You sift' 'system'
          break
        endif
      endwhile
      @removetimer '1s'
    endif
    clearjournal
  endwhile
  pause 50
  clearjournal\n"""
        script += f"""  @usetype 0x1f1c
  pause 600
  while @findtype 0x170f 'backpack'
    @movetype 0x170f 'backpack' 'trash'
    pause 600
  endwhile
  while @findtype 0x2307 'backpack'
    @movetype 0x2307 'backpack' 'trash'
    pause 600
  endwhile
  while @findtype 0x170b 'backpack'
    @movetype 0x170b 'backpack' 'trash'
    pause 600
  endwhile
  while @findtype 0x1711 'backpack'
    @movetype 0x1711 'backpack' 'trash'
    pause 600
  endwhile
  @movetype 0x172a 'backpack' 'nugget'
  pause 600
  @movetype 0xc74 'backpack' 'nugget'
  pause 600
  @movetype 0x1727 'backpack' 'nugget'
  pause 600
  @movetype 0x172a 'backpack' 'nugget'
  pause 600
  @movetype 0xc74 'backpack' 'nugget'
  pause 600
  @movetype 0x1727 'backpack' 'nugget'
  pause 600
  while @findtype 0x5732 'backpack'
    @movetype 0x5732 'backpack' 'jewl'
    pause 600
  endwhile
  while @findtype 0x3192 'backpack'
    @movetype 0x3192 'backpack' 'jewl'
    pause 600
  endwhile
  while @findtype 0x3193 'backpack'
    @movetype 0x3193 'backpack' 'jewl'
    pause 600
  endwhile
  while @findtype 0x3194 'backpack'
    @movetype 0x3194 'backpack' 'jewl'
    pause 600
  endwhile
  while @findtype 0x3195 'backpack'
    @movetype 0x3195 'backpack' 'jewl'
    pause 600
  endwhile
  while @findtype 0x3196 'backpack'
    @movetype 0x3196 'backpack' 'jewl'
    pause 600
  endwhile
  while @findtype 0x3197 'backpack'
    @movetype 0x3197 'backpack' 'jewl'
    pause 600
  endwhile
  while @findtype 0x3197 'backpack'
    @movetype 0x3199 'backpack' 'jewl'
    pause 600
  endwhile
  while @findtype 0x3198 'backpack'
    @movetype 0x3198 'backpack' 'jewl'
    pause 600
  endwhile
  while @findtype 0x3199 'backpack'
    @movetype 0x3199 'backpack' 'jewl'
    pause 600
  endwhile
  sysmsg 'Finished! (#{_index+1}: {y})'\n"""
        totallines += script
    totallines += """  sysmsg 'Finished All!'
  while not @findobject 'mib'
    cast 'sacred journey'
    @createtimer '5s'
    @settimer '5s' 0
    while @timer '5s' < 5000
      if @injournal 'blocked' 'system'
        break
      endif
      if @injournal 'disturbed' 'system'
        break
      endif
    endwhile
    @removetimer '5s'
    pause 100
    if not @injournal 'blocked' 'system'
      if not @injournal 'disturbed' 'system'
        @target 'home'
        pause 1000
      endif
    endif
    @clearjournal
  endwhile
  useskill 'hiding'
  while @findtype 0x99f 'backpack'
    @movetype 0x99f 'backpack' 'mib'
    pause 600
  endwhile
  @settimer '15m' 0
  while @timer '15m' <= 900000
    useskill 'hiding'
    pause 200
    walk 'east'
    pause 200
    walk 'east'
    pause 10000
    walk 'west'
    pause 200
    walk 'west'
    pause 10000
  endwhile
endwhile"""
    #print(totallines)
    #_count = len(totallines.split("\n"))
    #print(f"Total Lines: {_count}")
    #print(f"Total Characters: {len(totallines)}")
    #copy(totallines)
    #print("Copied.")
    return totallines

# Error/Popup Message
def message(duration, msg):
    global active_screen, SCREEN_SIZE, error_time, error_group
    c = [round(SCREEN_SIZE[0]/5)*4, round(SCREEN_SIZE[1]/5)*4]
    error_group.remove_all()
    error_group.hidden = False
    error_group.add_objects((
        panel(c, [200,75]),
        text(c, text=msg, color=(200,200,200), border_width=0, font_size=20),
    ))
    error_time = time() + duration

# Main Program
if __name__ == "__main__":
    # Handling Dependencies
    if not isdir("Temps"):
        mkdir("Temps")
    if not isdir("Books"):
        mkdir("Books")

    if not isfile("Temps\\AFK.png"):
        f = open("Temps\\AFK.png", "wb")
        f.write(AFK_DATA)
        f.close()

    if not isfile("Temps\\Button.png"):
        f = open("Temps\\Button.png", "wb")
        f.write(BUTTON_DATA)
        f.close()

    if not isfile("Instructions.html"):
        f = open("Instructions.html", "w")
        f.write(INSTRUCTIONS)
        f.close()
    
    # Game window
    title = "UO Manager"
    pygame.init()
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()
    running = True
    SCREEN_SIZE = (800,500)
    FPS = 60
    display = pygame.display.set_mode(SCREEN_SIZE)

    error_time = 0
    error_group = group()

    # Screen & objects
    BUTTON_SIZE = [100, 40]
    screens = [
        screen(), # Main screen with all the books and buttons.
        screen() # Spare screen for editing/creating books.
    ]
    active_screen = screens[0]

    MAX_BOOKS = 24
    def reload():
        global active_screen, screens, books, MAX_BOOKS, BUTTON_SIZE, error_group
        s = screens[0]
        
        s.add_objects((
            text([570,25], text="Runebook Name:", color=(200,200,200), border_width=0),
            text_input([720,25], [150,40], color=(50,50,50), background_color=None, text_color=(200,200,200), text="", valid_chars=ALPHANUMERIC),
            button([735,75], [120,40], variables=globals(), function="create_book()"),
            text([735,75], text="Create Book", color=(0,0,0), border_width=0),
            button([735,125], [120,40], variables=globals(), function="copy(compile())\nmessage(5,'Script Copied.')"),
            text([735,125], text="Compile Books", color=(0,0,0), border_width=0),
            text([690,180], text="Solve Captchas:", color=(200,200,200), border_width=0),
            checkbox([780,180], [30,30])
        ))

        s.add_object(error_group)

        # Handling runebook storage
        #print("Loading books.")
        books = {}
        for x in listdir("Books"):
            if len(tuple(books.keys())) >= MAX_BOOKS:
                break
            lebook = x.split(".")
            lebook.pop(len(lebook)-1)
            lebook = ".".join(lebook)
            #print(f"Loading book '{lebook}'.")
            books[lebook] = book(x)
        #print(f"Finished loading books.")

        # Adding the books in
        book_keys = tuple(books.keys())
        if len(book_keys) == MAX_BOOKS:
            b_col = (255,0,0)
        else:
            b_col = (0,255,0)
        s.add_objects((
            text([BUTTON_SIZE[0]/2+5+round(BUTTON_SIZE[0]/2)+2,25], text=f"Books: {len(tuple(books.keys()))}", color=b_col, border_width=0, font_size=20),
            text([BUTTON_SIZE[0]/2+5+round(BUTTON_SIZE[0]*1.5)+15,25], text=f"Max: {MAX_BOOKS}", color=(255,0,0), border_width=0, font_size=20),
        ))
        for b in range(len(book_keys)):
            column_size = 8
            size_changed = [BUTTON_SIZE[0]+10, BUTTON_SIZE[1]+10]
            c = [int(b/column_size)*size_changed[0]+round(size_changed[0]/2), b%column_size*size_changed[1]+round(size_changed[1]/2)+50]

            k = book_keys[b]
            s.add_objects((
                button(c, BUTTON_SIZE, variables=globals(), function=f"edit_book('{book_keys[b]}')"),
                text(c, text=book_keys[b], color=(0,0,0), border_width=0)
            ))
    reload()

    solve_time = time() - 1
    def solve_captcha():
        global AFK, BUTTON
        # check for & solve captcha
        solved = captcha_present = solve(AFK, BUTTON)
        if solved: message(5, "Solved Captcha.")
    
    # Game Loop
    while running:
        # check to solve any captchas every 5 seconds
        if solve_time < time() and screens[0].get_object(7).toggled:
            t = Thread(target=solve_captcha)
            t.start()
            solve_time = time() + 3
        
        if error_time != 0 and error_time < time():
            error_time = 0
            error_group.hidden = True
        # Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    message(5, f"Version: {VERSION}")
        
        # Draw Screen
        display.fill(active_screen.background_color)
        active_screen.draw(display)
        pygame.display.update()
        clock.tick(FPS)
    # Exit
    pygame.quit()
