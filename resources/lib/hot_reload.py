import sys
import importlib

ADDON_ID = "service.subtitles.subgenx"

def hotReload():
    # --- Development Reload Helper ---
    # Reload all your modules inside resources/lib/
    for name, module in list(sys.modules.items()):
        if name.startswith("resources.lib."):
            importlib.reload(module)
    print(f"[{ADDON_ID}] Modules reloaded for development mode.")
