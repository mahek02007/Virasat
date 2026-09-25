import os
import sys
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

endpoints = [
    ('/', 200),
    ('/health', 200),
    ('/docs', 200),
    ('/openapi.json', 200),
    ('/api/v1/regions', 200),
    ('/api/v1/regions/maharashtra', 200),
    ('/api/v1/regions/odisha', 200),
    ('/api/v1/regions/maharashtra/content', 200),
    ('/api/v1/content', 200),
    ('/api/v1/content/ajanta-caves', 200),
    ('/api/v1/places', 200),
    ('/api/v1/places/ajanta-caves-site', 200),
    ('/api/v1/facts', 200),
    ('/api/v1/facts/random', 200),
    ('/api/v1/search?q=caves', 200),
]

all_passed = True
print("=== VERIFYING ENDPOINTS AGAINST SUPABASE POSTGRESQL ===")
for ep, exp_status in endpoints:
    res = client.get(ep)
    status = res.status_code
    ok = (status == exp_status)
    if not ok:
        all_passed = False
    print(f"GET  {ep:<40} -> status: {status} [{'PASS' if ok else 'FAIL'}]")

chat_res = client.post('/api/v1/chat', json={'region_id': 'maharashtra', 'message': 'Tell me about Warli art'})
chat_ok = chat_res.status_code == 200
print(f"POST {'/api/v1/chat':<40} -> status: {chat_res.status_code} [{'PASS' if chat_ok else 'FAIL'}]")

if chat_ok:
    session_id = chat_res.json().get('session_id')
    hist_res = client.get(f'/api/v1/chat/{session_id}')
    hist_ok = hist_res.status_code == 200
    print(f"GET  {f'/api/v1/chat/{session_id}':<40} -> status: {hist_res.status_code} [{'PASS' if hist_ok else 'FAIL'}]")

print(f"\nALL SUITE STATUS: {'ALL PASSED' if all_passed and chat_ok else 'SOME FAILED'}")
