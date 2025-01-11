import aiohttp
import asyncio
import json


ssl_check = False  # Вимикаємо перевірку SSL
airdrop_name = "Soonchain"  # Назва аірдропу

eligible = 0  # Кількість гаманців, які отримали аірдроп
not_eligible = 0  # Кількість гаманців, які не отримали аірдроп
summary = 0  # Загальна кількість гаманців
# Функція для зчитування даних з файлів і видалення зайвих символів (наприклад, перенесення рядка)
def read_file(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]


# Зчитуємо адреси гаманців і проксі з файлів
wallet_addresses = read_file("wallet_addresses.txt")
proxies_list = read_file("proxies.txt")

# Перевірка, чи кількість гаманців і проксі співпадає
if len(wallet_addresses) != len(proxies_list):
    print("The number of wallets and proxies must be the same!")
else:
    print(f"\n      -- {airdrop_name} Airdrop checker --\n")
    async def fetch_data(wallet_address, proxy):
        # Формуємо проксі у форматі URL, перевіряючи префікс
        if not proxy.startswith("http://") and not proxy.startswith("https://"):
            proxy = f"http://{proxy}"

        # Встановлюємо проксі для aiohttp
        connector = aiohttp.TCPConnector(ssl=ssl_check)  # Вимикаємо перевірку SSL
        timeout = aiohttp.ClientTimeout(total=10)  # Таймаут для запиту

        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            try:
                async with session.get(
                    "https://soonchain.ai/api/airdrop",
                    params={"addr": wallet_address},
                    proxy=proxy  # Передаємо проксі
                ) as response:
                    if response.status == 200:
                        # Спробуємо отримати баланс з JSON відповіді
                        data = await response.json()
                        balance = json.loads(data.get("data", "{}")).get("balance", 0)
                        if balance:
                            global eligible
                            global summary
                            eligible += 1
                            summary += int(balance)
                            balance = '💎 ' + balance
                        else:
                            global not_eligible
                            not_eligible += 1
                            balance = '🚫'
                        print(f"{wallet_address} | Airdrop: {balance}")
                    else:
                        print(f"Error | {wallet_address}: {response.status}")
            except Exception as e:
                print(f"Error | {wallet_address}: {e}")

    async def main():
        tasks = []
        for wallet_address, proxy in zip(wallet_addresses, proxies_list):
            tasks.append(fetch_data(wallet_address, proxy))
        await asyncio.gather(*tasks)

    asyncio.run(main())

print(f"\nElegible: {eligible} | Not elegible: {not_eligible}", end=" ")
print(f"| Summary: {summary} tokens")
