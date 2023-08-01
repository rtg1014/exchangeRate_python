import requests

def get_exchange_rate(base_currency, target_currency):
    api_key = "YOUR_API_KEY"  # ExchangeRate-API에서 발급받은 API 키 입력
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        rate = data.get("conversion_rate")
        return rate
    else:
        print(f"Failed to fetch data: {data.get('error')}")

# 사용 예시
base_currency = "USD"  # 기준 통화
target_currency = "KRW"  # 대상 통화

exchange_rate = get_exchange_rate(base_currency, target_currency)
if exchange_rate:
    print(f"1 {base_currency} = {exchange_rate} {target_currency}")




def get_exchange_rate_all(base_currency, target_currency):
    api_key = "YOUR_API_KEY"  # ExchangeRate-API에서 발급받은 API 키 입력
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        rate = data.get("conversion_rate")
        return rate
    else:
        print(f"Failed to fetch data: {data.get('error')}")

# 사용 예시
base_currency = "USD"  # 기준 통화
target_currency = "KRW"  # 대상 통화

exchange_rate = get_exchange_rate_all(base_currency, target_currency)
if exchange_rate:
    print(f"1 {base_currency} = {exchange_rate} {target_currency}")