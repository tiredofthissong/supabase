from supabase import create_client

# Your Supabase credentials
url = "https://gilvijxmudywgcaslfxz.supabase.co"
key = "sb_publishable_3QYyHIXrfZJb5s-DBjnrDg_qSDRVBRd"

# Create connection to database
supabase = create_client(url, key)

# Insert one test course into the courses table
result = supabase.table("courses").insert({
    "title": "Python for L&D Automation"
}).execute()

# Print what got inserted
print("Inserted record:", result.data)