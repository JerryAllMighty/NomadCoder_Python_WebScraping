import csv

# 파일로 저장
def save_to_file(companies):
  file = open("jobs.csv", mode = "w") 
  writer = csv.writer(file)
  writer.writerow(["company_name"])
  for company in companies:
    writer.writerow([company])
  return 
