import os
from supabase import create_client

# Credentials come from the environment (see .env.example)
url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]  # publishable key; still keep it out of git

# Create connection to database
supabase = create_client(url, key)

# Insert one test course into the courses table
result = supabase.table("courses").insert({
    "title": "Python for L&D Automation"
}).execute()

# Print what got inserted
print("Inserted record:", result.data)