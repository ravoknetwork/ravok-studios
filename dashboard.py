# =========================================================
# SERVIDOR STANDALONE DO SITE & PAINEL - RAVOK STUDIOS
# (Opcional: o próprio BOT/bot.py já serve o Site e o Painel na porta 25611,
#  mas você também pode rodar este arquivo separado na porta 25584 se quiser!)
# =========================================================

import os
from quart import Quart, send_file, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Quart(__name__)

@app.route("/")
async def home():
    return await send_file(os.path.join(BASE_DIR, "index.html"))

@app.route("/painel")
@app.route("/painel.html")
@app.route("/admin")
async def painel():
    return await send_file(os.path.join(BASE_DIR, "painel.html"))

@app.route("/assets/<path:filename>")
async def assets(filename):
    return await send_from_directory(os.path.join(BASE_DIR, "assets"), filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=25584)
