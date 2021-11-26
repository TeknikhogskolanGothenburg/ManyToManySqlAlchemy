import datetime


def main():
    with open('c:\\cron_logs\\log.txt', 'a', encoding='utf-8') as logfile:
        logfile.write(f'{datetime.datetime.now()}, logging\n')


if __name__ == '__main__':
    main()
