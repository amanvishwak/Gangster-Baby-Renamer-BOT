import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22182189")

API_HASH  = os.environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8182224498:AAG4leCVgBgVEYUmyBzS_N5cK_1OSeRD0mg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL  = os.environ.get("DB_URL","mongodb+srv://aman991932:aman@cluster0.18hv15a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")




    
    

    # database config
    DB_NAME =      
    
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/29a3acbbab9de5f45a5fe.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5977931010').split()]
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'AV_BOTz_UPDATE').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002110971750"))
    
