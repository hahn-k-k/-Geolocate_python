# Geolocate_python
from geoip import geolite2
import socket, subprocess 

cmd = r"C:\Program Files\Wireshark\tshark -i 4"

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
my_ip = socket.gethostbyname(socket.gethostname())


def get_ip_location(ip):
    location = reader.get(ip)
    
    try:
        country = location["country"]["names"]["en"]
    except:
        country = "Unknown"

    try:
        subdivision = location["subdivisions"][0]["names"]["en"]
    except:
        subdivision = "Unknown"    

    try:
        city = location["city"]["names"]["en"]
    except:
        city = "Unknown"
    
    return country, subdivision, city


for line in iter(process.stdout.readline, b""):
    columns = str(line).split(" ")

    if "SKYPE" in columns or "UDP" in columns:
        if "->" in columns:
            src_ip = columns[columns.index("->") - 1]
        elif "\\xe2\\x86\\x92" in columns:
            src_ip = columns[columns.index("\\xe2\\x86\\x92") - 1]
        else:
            continue
            
        if src_ip == my_ip:
            continue

        try:
            country, sub, city = get_ip_location(src_ip)
            print(">>> " + country + ", " + sub + ", " + city)
        except:
            try:
                real_ip = socket.gethostbyname(src_ip)
                country, sub, city = get_ip_location(real_ip)
                print(">>> " + country + ", " + sub + ", " + city)
            except:
                print("Not found")
