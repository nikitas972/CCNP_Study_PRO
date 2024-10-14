
import tkinter as tk
from gui import  show_content
from file_handler import read_file_content
from keywords import keyword_colors, title_color

# Define the files dictionary
files = {
    '1': 'VLANS.txt',
    '2': 'TRUNK.txt',
    '3': 'MAC-TABLES.txt',
    '4': 'Switching-CEF-TCAM.txt',
    '5': 'spanning-tree.txt',
    '6': 'port-types.txt',
    '7': 'STP Terminology.txt',
    '8': 'Root-bridge.txt',
    '9': 'root-ports.txt',
    '10': 'stp-topology-changes.txt',
    '11': 'rootguard-portfast-bpdug.txt',
    '12': 'mst.txt',
    '13': 'VTP.txt',
    '14': 'EIGRP.txt',
    '15': 'OSPF.txt',
    '16': 'path-vector.txt',
}

def main():
    window = (files, show_content)

if __name__ == "__main__":
    main()
