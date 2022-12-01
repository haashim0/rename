import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "14505719")

API_HASH = os.environ.get("API_HASH", "620f0a2aa2cd1474a4953619b3e3643d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5945219564:AAHMjrNCDXTgfBT-HuBmxjDN_0RHOORYqbA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "TamilDub_Linkzz") 

DB_NAME = os.environ.get("DB_NAME","re")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Haashim:Haashim@mfile0.t9hxg.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/e6e4ed068ace5ca43f348.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5291606032').split()]

PORT = os.environ.get("PORT", "8080")
