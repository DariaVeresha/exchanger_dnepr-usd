from exchanger_1.currency_pair import *


class ReadingRemains(Course):
    def __init__(self, name, available, available_uah):
        super().__init__(name, available, available_uah)
        self.name = name
        self.available = available
        self.available_uah = available_uah

    def operationUAH_USD(self):
        try:
            client = int(input('Amount in UAH: '))
            if client > 0:
                conversion = client / self.privat_course["usd"]["buy"]
                rate = 1 / self.privat_course["usd"]["buy"]
                remainder = self.available - conversion
                if self.available >= conversion:
                    balanceUAH_USD = self.available_uah + client
                    print(f'Available balance at the beginning of the operation: {self.available} USD\n'
                          f'UAH conversion: {round(conversion, 2)} USD| RATE: {round(rate, 2)} USD\n'
                          f'Balance update: {round(remainder, 2)} USD\n'
                          f'Balance update: {balanceUAH_USD} UAH')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {round(conversion, 2)} USD\n'
                          f'Available balance: {self.available} USD\n')
            else:
                print(f'Your exchange request:{client} is not correct')
        except ValueError:
            print('Your exchange request is not correct,value must be an integer')
        finally:
            print('Verification done')

    def operationUAH_UER(self):
        try:
            client = int(input('Amount in UAH: '))
            if client > 0:
                conversion = client / self.privat_course["eur"]["buy"]
                rate = 1 / self.privat_course["eur"]["buy"]
                remainder = self.available - conversion
                if self.available >= conversion:
                    balanceUAH_EUR = self.available_uah + client
                    print(f'Available balance at the beginning of the operation: {self.available} EUR\n'
                          f'UAH conversion: {round(conversion, 2)} EUR| RATE: {round(rate, 2)} EUR\n'
                          f'Balance update: {round(remainder, 2)} EUR\n'
                          f'Balance update: {balanceUAH_EUR} UAH')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {round(conversion, 2)} EUR\n'
                          f'Available balance: {self.available} EUR\n')
            else:
                print(f'Your exchange request:{client} is not correct')
        except ValueError:
            print('Your exchange request is not correct,value must be an integer')
        finally:
            print('Verification done')

    def operationUAH_BTC(self):
        try:
            client = int(input('Amount in UAH: '))
            if client > 0:
                conversion = client / self.privat_course["btc"]["buy"]
                rate = 1 / self.privat_course["btc"]["buy"]
                remainder = self.available - conversion
                if self.available >= conversion:
                    balanceUAH_BTC = self.available_uah + client
                    print(f'Available balance at the beginning of the operation: {self.available} BTC\n'
                          f'UAH conversion: {round(conversion, 2)} BTC| RATE: {round(rate, 2)} BTC\n'
                          f'Balance update: {round(remainder, 2)} BTC\n'
                          f'Balance update: {balanceUAH_BTC} UAH')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {round(conversion, 2)} BTC\n'
                          f'Available balance: {self.available} BTC\n')
            else:
                print(f'Your exchange request:{client} is not correct')
        except ValueError:
            print('Your exchange request is not correct,value must be an integer')
        except TypeError:
            print('Sorry: INVALID CURRENCY BTC')
        finally:
            print('Verification done')

    def operationUSD_UAH(self):
        try:
            client = int(input('Amount in USD: '))
            if client > 0:
                conversion = client * self.privat_course["usd"]["sale"]
                rate = 1 * self.privat_course["usd"]["sale"]
                remainder = self.available_uah - conversion
                if self.available >= conversion:
                    balanceUSD_UAH = self.available + client
                    print(f'Available balance at the beginning of the operation: {self.available_uah} UAH\n'
                          f'USD conversion: {round(conversion, 2)} UAH| RATE: {round(rate, 2)} UAH\n'
                          f'Balance update: {round(remainder, 2)} UAH\n'
                          f'Balance update: {balanceUSD_UAH} USD')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {conversion} USD\n'
                          f'Available balance: {self.available_uah} UAH\n')
            else:
                print(f'Your exchange request:{client} is not correct')
        except ValueError:
            print(f'Your exchange request is not correct,value must be an integer')
        finally:
            print('Verification done')

    def operationEUR_UAH(self):
        try:
            client = int(input('Amount in EUR: '))
            if client > 0:
                conversion = client * self.privat_course["eur"]["buy"]
                rate = 1 * self.privat_course["eur"]["buy"]
                remainder = self.available_uah - conversion
                if self.available >= conversion:
                    balanceEUR_UAH = self.available + client
                    print(f'Available balance at the beginning of the operation: {self.available_uah} UAH\n'
                          f'UAH conversion: {round(conversion, 2)} UAH| RATE: {round(rate, 2)} UAH\n'
                          f'Balance update: {round(remainder, 2)} UAH\n'
                          f'Balance update: {balanceEUR_UAH} EUR')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {round(conversion, 2)} UAH\n'
                          f'Available balance: {self.available_uah} UAH\n')
            else:
                print(f'Your exchange request:{client} is not correct')
        except ValueError:
            print('Your exchange request is not correct,value must be an integer')
        finally:
            print('Verification done')

    def operationBTC_UAH(self):
        try:
            client = int(input('Amount in BTC: '))
            if client > 0:
                conversion = client * self.privat_course["btc"]["buy"]
                rate = 1 * self.privat_course["btc"]["buy"]
                remainder = self.available - conversion
                if self.available >= conversion:
                    balanceBTC_UAH = self.available + client
                    print(f'Available balance at the beginning of the operation: {self.available_uah} UAH\n'
                          f'UAH conversion: {round(conversion, 2)} UAH| RATE: {round(rate, 2)} UAH\n'
                          f'Balance update: {round(remainder, 2)} UAH\n'
                          f'Balance update: {balanceBTC_UAH} BTC\n')
                else:
                    print(f'Sorry, error.The currency balance is not enough\n'
                          f'To complete the transaction, you must: {round(conversion, 2)} BTC\n'
                          f'Available balance: {self.available_uah} UAH\n')
            else:
                print(f'Your exchange request:{client} is not correct')
        except ValueError:
            print('Your exchange request is not correct,value must be an integer')
        except TypeError:
            print('Sorry: INVALID CURRENCY BTC')
        finally:
            print('Verification done')






