import os
os.system(“pip install telethon”)
from telethon.sync import TelegramClient
from telethon import TelegramClient, events, sync, functions, types

session = "1BVtsOMgBu4BJG9llWLJKS468eEES7sD2prj2nB0yAS8_yBNPBi2_UO4GW8FL9Igcoq1KT7_SYAOE5d4-BwhbePVP3UfHO86FkCNr5OlKYf5dcCN0DEiqh3CA_o9hcTMWoN1CC6kDWmD9dRoPnpeqKlQG2Eh3RJPMp89-3p-dxbvYRX9Cqd3F2jhPahOro6sUMdQe2AA3BvrcYN7QshSkZNiOUYAl-kd8SLJbhCiLtWMNF-rdFF29Odt6r9a4c3Bn-SEltIzcsRvwfLSa2hhF7No29zVItdBcMYFlq-URofPr42AFIq28L407R1yDysG2cBMoWLJ46rQx_pg_uKf9jMU3igPyqZ0="
api_id = 2991021
api_hash = "3a8d7a7a8b11da9f656fb1ae09e1c9d9"
client = TelegramClient(session, api_id, api_hash)
client.start()
@client.on(events.NewMessage)
async def my_event_handler(event):
  if event.raw_text == ".ping":
    await event.edit("Pong Pappa!!!")
    
    
client.run_until_disconnected()
