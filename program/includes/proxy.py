from random import choice


class ProxySender(object):

    def __init__(self, proxy_list, proxy_type):

        self.vpn_list = proxy_list
        self.vpn_type = proxy_type

    def request(self):

        random_proxy = choice(self.vpn_list)
        if self.vpn_type == 'http':

            return {
                'http': random_proxy,
                'https': random_proxy,
            }

        elif self.vpn_type == 'sock4':

            return {
                'http': f'socks4://{random_proxy}',
                'https': f'socks4://{random_proxy}',
            }

        elif self.vpn_type == 'sock5':

            return {
                'http': f'socks5://{random_proxy}',
                'https': f'socks5://{random_proxy}',
            }