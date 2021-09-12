import socket
import time


class ClientError(Exception):
    '''Client Error'''
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError

    def _read(self):
        try:
            data = self.connection.recv(4096)
        except:
            raise ClientError
        return data.decode('utf-8')

    def _send(self, message):
        try:
            self.connection.sendall(message.encode())
        except:
            raise ClientError

    def _dict_sorted(self, data_dictionary):
        for k, v in data_dictionary.items():
            data_dictionary[k] = sorted(v)
        return data_dictionary

    def put(self, name_metric, metric_value, timestamp=None):
        timestamp = timestamp or int(time.time())
        metric_value = metric_value
        message = ' '.join(['put', name_metric, str(metric_value), str(timestamp)]) + '\n'
        self._send(message)
        data = self._read()
        if data == 'ok\n\n':
            return None
        if data == 'error\nwrong command\n\n':
            raise ClientError

    def get(self, name_metric):
        message = f'get {name_metric}\n'
        self._send(message)
        data = self._read()
        if data == 'ok\n\n':
            return {}
        if name_metric != '*':
            if data == 'error\nwrong command\n\n' or not (data.startswith('ok') and data.endswith('\n\n')) or not (
                    name_metric in data):
                raise ClientError

        response = data.lstrip('ok\n').rstrip('\n\n')
        response = [i.split() for i in response.split('\n')]

        result_dict = {}
        for name, value, timestamp in response:
            if name not in result_dict:
                result_dict[name] = []
            result_dict[name].append((int(timestamp), float(value)))

        result_dict = self._dict_sorted(result_dict)
        return result_dict

    def close(self):
        try:
            self.connection.close()
        except:
            raise ClientError


if __name__ == "__main__":
    client = Client("127.0.0.1", 8888, timeout=5)
    client.put("test", 0.5, timestamp=1)
    client.put("test", 2.0, timestamp=2)
    client.put("test", 0.5, timestamp=3)
    client.put("load", 3, timestamp=4)
    client.put("load", 4, timestamp=5)
    print(client.get("*"))

    client.close()
