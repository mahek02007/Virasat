from database import engine
from sqlalchemy import text

tables_with_serial = ['places', 'media', 'sources', 'content_items', 'chat_messages']
with engine.connect() as conn:
    for t in tables_with_serial:
        query = text(f"SELECT setval(pg_get_serial_sequence('{t}', 'id'), COALESCE(MAX(id), 1)) FROM {t}")
        conn.execute(query)
        conn.commit()
        print(f"Reset sequence for {t} successfully")
