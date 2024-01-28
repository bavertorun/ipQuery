import requests
import colorama

banner = colorama.Fore.LIGHTBLACK_EX+"""

██╗██████╗      ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗
██║██╔══██╗    ██╔═══██╗██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝
██║██████╔╝    ██║   ██║██║   ██║█████╗  ██████╔╝ ╚████╔╝ 
██║██╔═══╝     ██║▄▄ ██║██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝  
██║██║         ╚██████╔╝╚██████╔╝███████╗██║  ██║   ██║   
╚═╝╚═╝          ╚══▀▀═╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   
                            Coded by: Baver Torun
                            Github: github.com/bavertorun 

"""
print(banner)

ip = input(colorama.Fore.LIGHTBLUE_EX+'Enter ip adress -> ')
rq = requests.get(f'http://ip-api.com/json/{ip}')
data = rq.json()


res = colorama.Fore.LIGHTGREEN_EX+f"""
Country: {data['country']}
CountryCode: {data['countryCode']}
Region": {data['region']}
RegionName": {data['regionName']}
City": {data['city']}
Zip": {data['zip']}
Timezone": {data['timezone']}
Isp": {data['isp']}
Org": {data['org']}
As": {data['as']}
Google Map Link : https://google.com/maps/place/{data['lat']}+{data['lon']}
"""
print(res)
