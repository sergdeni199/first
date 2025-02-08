from eth_account import Account
from mnemonic import Mnemonic

# Включаем HD Wallet функции
Account.enable_unaudited_hdwallet_features()


def create_wallets_evm(count: int):
    #from eth_account import Account
    # from mnemonic import Mnemonic
    # Включаем HD Wallet функции:
    # Account.enable_unaudited_hdwallet_features()

    wallets = {}
    mnemo = Mnemonic("english")  # Инициализация генератора мнемонических фраз

    for i in range(count):
        # Генерация новой сид-фразы и создание аккаунта
        seed_phrase = mnemo.generate(strength=128)
        account = Account.from_mnemonic(seed_phrase)

        address = account.address  # Получаем адрес аккаунта
        private_key = account.key.hex()  # Приватный ключ в формате hex
        wallets[address] = {"private_key": private_key, "seed_phrase": seed_phrase}

    # Сохранение адресов, приватных ключей и сид-фраз в файл
    with open("wallets_data.txt", "w") as file:
        for address, data in wallets.items():
            file.write(f"Address: {address}\n")
            file.write(f"Private Key: {data['private_key']}\n")
            file.write(f"Seed Phrase: {data['seed_phrase']}\n\n")


# Создаем 5 кошельков
create_wallets_evm(5)
