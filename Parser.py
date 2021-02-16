class Parser:
    analize_count = 4

    def __init__(self, target, save=None):
        self.save = save
        self.name = target
        self.find_nok = {}
        self.time = 17

    def run(self):
        self.read()
        self.write()

    def read(self):
        with open(self.name, mode='r', encoding='utf8') as file:
            for line in file:
                time = line[1:self.time]
                if 'NOK' in line:
                    if time in self.find_nok:
                        self.find_nok[time] += 1
                    else:
                        self.find_nok.update({time: 1})

    def write(self):
        with open('save-parse.txt', mode='w', encoding='utf8') as file:
            file.write(f'+{"+":-^30}+' + '\n')
            file.write(f'|{"Дата":^16} | {"NOK":^10} |' + '\n')
            file.write(f'+{"+":-^30}+' + '\n')
            for date, count in self.find_nok.items():
                file.write(f'|{date:^10} | {str(count):^10} |' + '\n')


class SortHours(Parser):

    def __init__(self, target, save=None):
        super().__init__(target, save)
        self.time = 14


class SortMonth(Parser):

    def __init__(self, target, save=None):
        super().__init__(target, save)
        self.time = 8


class SortYear(Parser):

    def __init__(self, target, save=None):
        super().__init__(target, save)
        self.time = 5


#  - по часам
#  - по месяцу
#  - по году


target_file = 'events.txt'
file_parser = SortMonth(target=target_file)
file_parser.run()