base = 10


def multiply(number):
    return base * number


def add(number):
    return base + number


print(multiply(5))
print(add(7))

base = 13

print(multiply(5))
print(add(7))


class Calculator:
    def __init__(self, base):
        self.base = base

    def multiply_by(self, number):
        return self.base * number

    def add_to(self, number):
        return self.base + number


base_ten_calc = Calculator(base=10)
print(base_ten_calc.multiply_by(5))
print(base_ten_calc.add_to(7))


class Sftp2S3:
    def __init__(self, server_name, bucket_name):
        self.bucket = boto3.resource('s3').Bucket(bucket_name)
        self.sftp_server = self._init_sftp(server_name)

    def _init_sftp(self, server_name): pass

    def _needs_sync(self, file_name): pass

    def _copy_from_sftp(self, file_name): pass

    def sync_file(self, file_name):
        if (self._needs_sync(file_name)):
            self._copy_from_sftp(file_name)


s2s_sync = Sftp2S3(server_name='a.b.c', bucket_name='my-bucket')
s2s_sync.sync_file('foo.txt')
s2s_sync.sync_file('baz/bar.txt')
