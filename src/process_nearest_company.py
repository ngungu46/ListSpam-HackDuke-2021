import numpy as np
from annoy import AnnoyIndex

def update_company(company_data, metric = 'euclidean'):
  t = AnnoyIndex(len(company_data[0]), metric)
  for i,v in enumerate(company_data):
    t.add_item(i,v)
  t.build(8)
  t.save('data/search_tool.txt')

def processing(user_data, nums_preference, metric = 'euclidean'):
  u = AnnoyIndex(len(user_data[0]), metric)
  u.load('data/search_tool.txt')
  return np.array(u.get_nns_by_vector(a, nums_preference))

def overwrite_nearest_data(user_data, company_data, nums_preference, metric = 'euclidean'):
  update_company(company_data, metric)
  result_list = []
  for i in user_data:
    nearest = processing(i, nums_preference, metric)
    result_list.append(nearest)
  result_list = np.array(result_list)
  np.savetxt('data/nearest.txt', result_list)

def add_user_nearest_data(user_data, user_id, nums_preference, metric = 'euclidean'):
  f = open('data/nearest.txt', 'w')
  data = f.read()
  user_nearest_data = process(user_data, nums_preference, metric)
  if(user_id < len(data)):
    for i in range(nums_preference):
      data[user_id][i] = user_nearest_data[user_id][i]
  else:
    data.append(user_nearest_data)
  np.savetxt('data/nearest.txt', data)
