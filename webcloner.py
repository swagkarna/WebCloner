
banner = """



░██╗░░░░░░░██╗███████╗██████╗░░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

                                AUTHOR : SWAGKARNA
                                CONTACT : github.com/swagkarna
"""



try :
    import subprocess
    import cloudscraper
    import sys
    from colorama import Fore, Style,init
except ModuleNotFoundError:
    subprocess.call("pip3 install cloudscraper", shell=True)
    subprocess.call("pip3 install colorama", shell=True)
     
print(Style.BRIGHT+Fore.RED+banner+Fore.RESET)

def main():
    scraper = cloudscraper.create_scraper(browser='chrome')
    x = scraper.get(target).text
    print(str(x))
    with open('index.html', mode='w') as file :
         file.write(x)

target = str((sys.argv[1]))
main()
