import requests

schoolname = input("학교 이름을 입력하세요: ")
class_name = input("반을 입력하세요 예(1-1 = 1학년 1반): ")
print("검색중 기다려주세요. 5초 정도 소요됩니다.\n")

url = f"https://api.hoo.gay/schedule/{schoolname}/{class_name}"
response = requests.get(url)
data = response.json()
timetable = data["timetable"]

days = ["월요일", "화요일", "수요일", "목요일", "금요일"]
for day_idx, day in enumerate(days):
    print(day + " 시간표")
    for i in range(1, 8):
        print(f"{i}교시: {timetable[day_idx+1][i*2-1]}({timetable[day_idx+1][i*2]})")
    print()