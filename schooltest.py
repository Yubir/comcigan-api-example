import requests

search = input("검색할 학교를 입력해주세요 : ")
print("검색중 기다려주세요. 5초 정도 소요됩니다.\n")

url = f"https://api.hoo.gay/school?search={search}"

try:
    response = requests.get(url)

    x = response.json()
    for i in range(len(x['results'])):
        print(x['results'][i])

except Exception as err:
    print(search+"라는 학교는 검색되지 않았습니다..")
