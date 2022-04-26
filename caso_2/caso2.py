import pandas as pd
pd.set_option('display.max_rows',None, 'display.max_columns', None)


#punto 2
def regions():
  
  csv = pd.read_csv('vehicles.csv', usecols=["region"])

  df = pd.DataFrame(csv, columns=["region"])

  dups = df.pivot_table(columns=['region'], aggfunc='size')

  new_df = pd.DataFrame(dups, columns=['total regions']).count()

  total = new_df.to_json()

  all_regions = dups.reset_index().to_json(orient='records')

  print(all_regions, total)
  return "done"

#punto 1 y punto 3
def new_file():
  data = pd.read_csv('vehicles.csv', sep=',', index_col=0 )
  df = pd.DataFrame(data.dropna())
  df = df.astype({"year": int})

  df.to_csv("without_nan.csv")

  return "done"

#punto 4
def price_condition():
  data = pd.read_csv('vehicles.csv', sep=',')
  df = pd.DataFrame(data)
  new_df = df[(df["price"] >= 15000) & ((df["condition"] == "good") | (df["condition"] == "excellent"))]
  new_df.to_csv("new_csv.csv")

  return "done"

#punto 5
def blue_chevrolet_cars():
  data = pd.read_csv('vehicles.csv', sep=',')
  df = pd.DataFrame(data)
  new_df = df[(df["manufacturer"] >= "chevrolet") & (df["paint_color"] == "blue")]
  print(new_df["id"].count())

  return "done"

#punto 6
def regions_map():
  
  csv = pd.read_csv('vehicles.csv', usecols=["region"])

  df = pd.DataFrame(csv, columns=["region"])

  dups = df.pivot_table(columns=['region'], aggfunc='size')

  dups = dups.index.tolist()

  return dups

