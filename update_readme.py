from datetime import datetime

with open("README.md", "w") as f:
    f.write(f"# Mi Perfil\n\n")
    f.write(f"🕒 Última actualización: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC\n")
