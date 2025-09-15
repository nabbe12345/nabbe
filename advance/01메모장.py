class Study:

    study = ''
    book = ''


    def __init__(self,study,book):
        self.study = study
        self.book  = book



school =Study('파이썬','라이브러리')
print(f'{school.study},{school.book}')