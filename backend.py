import pandas as pd
import notion_df as nd
nd.pandas()

# Notion connection information
notion_token = "secret_omL8nzIdOZySUeAtSOCHm0bUNh2ydXdohuePKPBXkxm"

# Request db connection
request_db_url = "https://www.notion.so/b9ebcbea31694ab19309bb8bc1ef19d7?v=2438ec3776de46e4bebb25b20917e95e&pvs=4"
request_db_id = "b9ebcbea31694ab19309bb8bc1ef19d7"
requests_df = pd.DataFrame(nd.download(request_db_id, api_key=notion_token, resolve_relation_values=True))

# Work locations db connection
locations_db_url = "https://www.notion.so/7bc4a3417151424ca8707f5a1b1d5e03?v=4f28dc82c13f490da06f962384736ede&pvs=4"
locations_db_id = "7bc4a3417151424ca8707f5a1b1d5e03"
locations_df = pd.DataFrame(nd.download(locations_db_id, api_key=notion_token, resolve_relation_values=True))
locations_df = locations_df[locations_df['Status']=='Active']

# User Select Options
users_db_url = "https://www.notion.so/1de7448af925490caef5edc97cab9c4f?v=76c4b255da9f4ca789b1df1c4d051d78&pvs=4"
users_db_id = "1de7448af925490caef5edc97cab9c4f"
users_df = pd.DataFrame(nd.download(users_db_id, api_key=notion_token, resolve_relation_values=True))
users_df = users_df[users_df['Status']=='Active']

# Request type options
request_types = ["Documents/Forms",
                 "Cleaning Supplies",
                 "Office Supplies",
                 "Printer Ink"]