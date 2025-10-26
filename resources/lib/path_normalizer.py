# actual addon code
import xbmc
import urllib.parse
import os

def to_kodi_path(path):
    # Normalize slashes (works on all OS)
    normalized = os.path.abspath(path).replace("\\", "/")
    # Encode safely but keep ':' after drive letter
    encoded = "file:///" + urllib.parse.quote(normalized, safe=":/")
    # Add file:// prefix for Kodi
    return encoded
