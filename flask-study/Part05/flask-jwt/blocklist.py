#BLOCKLSIT 관리 파일
BLOCKLSIT = set()

def add_to_blocklist(jti):
    BLOCKLSIT.add(jti)

def remove_from_blocklist(jti):
    BLOCKLSIT.discard(jti)