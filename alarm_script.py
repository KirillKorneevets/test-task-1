import psutil
import requests


API_URL = ''
MEMORY_THRESHOLD_PERCENT = 90


def send_alarm():
    try:
        response = requests.post(API_URL)
        if response.status_code == 200:
            print('Alarm sent successfully!')
        else:
            print(f'Failed to send alarm. Status code: {response.status_code}')
    except Exception as e:
        print(f'Error sending alarm: {e}')



def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent # Возвращает текущий процент использования виртуальной памяти на системе
    print(f'Текущее потребление памяти: {memory_percent}%')

    if memory_percent > MEMORY_THRESHOLD_PERCENT:
        send_alarm()



if __name__ == "__main__": 
    """
    Бесконечный цикл мониторинга
    """
    while True:
        check_memory_usage()