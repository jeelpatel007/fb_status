# you can import it using pip install facebook-sdk
import facebook

def main():
  # Replace the values by your actual page id and access token values.
  cfg = {
    "page_id"      : "VALUE",  # Step 1
    "access_token" : "VALUE"   # Step 3
    }
  
  # Uploads a pre-defined "Hello, World" status.
  # You can import status value from user in sophisticated application.
  api = get_api(cfg)
  msg = "Hello, world!"
  status = api.put_wall_post(msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  
if __name__ == "__main__":
  main()
