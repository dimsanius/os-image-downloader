from classes.crawler import Crawler


class Home:
    OS_LINKS = {
        "Ubuntu": "https://releases.ubuntu.com/",
        "Fedora": "",
        "Debian": ""
    }

    def __init__(self):
        os_list = list(self.OS_LINKS.keys())
        print(os_list)

        for idx, item in enumerate(os_list):
            print(f"{idx}. {item}")
        selection = input("Selection: ")

        Crawler(name=os_list[int(selection)], link=self.OS_LINKS[os_list[int(selection)]])
