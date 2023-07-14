import configuration
import requests
import data


# Создал заказ и сохранил трек-номер
def post_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


response = post_order(data.order_body)
track_order = response.json()['track']


# print(track_order)


# Выполнил запрос на получение информации о заказе через трек-номер
def get_order_on_track(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + "?t=" + str(track_order),
                        headers=data.headers)


st_cod = get_order_on_track(track_order)
# print(st_cod.status_code)
