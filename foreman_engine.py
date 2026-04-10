import os

def save_to_vault(query, answer, node_type="nonfiction/gardening"):
    filename = "".join(x for x in query if x.isalnum() or x in "._- ").strip()[:30] + ".txt"
    path = f"./vault/{node_type}/{filename}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(answer)
    print(f"\n[FOREMAN]: Saved to vault/{node_type}/{filename}")

def foreman_engine(query):
    # 1. LOCAL SCAN (The Librarian)
    for root, dirs, files in os.walk("./vault"):
        for file in files:
            if query.lower() in file.lower():
                with open(os.path.join(root, file), 'r') as f:
                    return f"\n--- [DIRECT HIT: {file}] ---\n{f.read()}"

    # 2. THE HANDSHAKE (Bridge Mode)
    print("\n[LIBRARIAN]: Nothing in Vault. Switching to Bridge Mode...")
    print("[EYES]: Waiting for Gemini response via Accessibility Service...")
    return "\n[SYSTEM]: Handshake Active. Standing by..."

print("\n=== FOREMAN ENGINE v2.0 (OFFLINE-FIRST) ACTIVE ===")
user_query = input("Search or Ask: ")
print(foreman_engine(user_query))
