import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import engine
spec = json.load(open(sys.argv[1])); out = sys.argv[2]
os.makedirs(out, exist_ok=True)
only = sys.argv[3] if len(sys.argv) > 3 else None
for r in spec.get("reels", []):
    if not only or only == r["id"]: print(engine.render_reel(r, out))
for c in spec.get("carousels", []):
    if not only or only == c["id"]: print(engine.render_carousel(c, out))
