from resources.lib.hot_reload import hotReload

hotReload()

import os
import xbmc, urllib.parse # type: ignore
import xbmcaddon # type: ignore
import xbmcgui # type: ignore
import xbmcplugin # type: ignore
import sys
from resources.lib.path_normalizer import to_kodi_path
import subprocess
import shutil
from threading import Timer

player = xbmc.Player()

accuracy = [
    { 'name': 'fine', 'description': 'Decent accuracy, Fastest and Recommended', 'accuracy': 'base', 'language': "English"}, 
    # { 'name': 'good', 'description': 'Great accuracy, Slower and Requires more resources', 'accuracy': 'medium'} 
]

addon = xbmcaddon.Addon()
video_path = xbmc.Player().getPlayingFile()
base_video_name = os.path.splitext(video_path)[0]
currentPlayingMedia = player.getVideoInfoTag().getTitle()

params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
action = params.get('action');

def generateSubtitle (): 
    handle = int(sys.argv[1])

    command = 'whisper'
    if shutil.which(command) is None:
        xbmcgui.Dialog().ok(
            "subgenX - Error",
            f"The '{command}' not found on your system, Please make sure Python 3.8 or later & OpenAI Whisper is installed and available in Systems PATH.\n" \
            "For whisper: https://github.com/openai/whisper/discussions/1463\n" \
            "For Python: https://www.python.org/downloads/release/python-380\n" \
            "PATH: Win + X  ->  select PowerShell (Admin) -> [Environment]::SetEnvironmentVariable('whisper', '<path to whisper.exe>', 'Machine')"
        )
        xbmc.log(f"[subgenX] '{command}' not found in PATH", xbmc.LOGERROR)
        return

    testFile = video_path
    # testOutputDir = r"D:\songs"
    # output_dir = xbmc.translatePath("special://temp/")

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    process = subprocess.Popen([
        "whisper",
        testFile,
        "--language", "en",
        "--output_format", "srt",
        "--model", "base",
        "--output_dir", os.path.dirname(video_path)
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, startupinfo=startupinfo)
    
    # Collect outputs
    stdout_lines = []
    stderr_lines = []

    for line in process.stdout:
        line = line.strip()
        stdout_lines.append(line)
        xbmc.log(f"[subgenX]:: {line}", xbmc.LOGINFO)

    for line in process.stderr:
        line = line.strip()
        stderr_lines.append(line)
        xbmc.log(f"[subgenX][ERROR]:: {line}", xbmc.LOGERROR)


    xbmc.log(f"[subgenX][ERROR]:: {process.returncode}")
    # xbmcplugin.setResolvedUrl(handle, True, xbmcgui.ListItem(path=base_video_name.join(".srt")))
    
    Timer(2.0, lambda: player.setSubtitles(base_video_name.join(".srt"))).start()

    # Handle result
    # if process.returncode != 0:
    #     # xbmc.log(f"[subgenX][ERROR]:: {line}", stderr_lines[-3:])
    #     xbmcgui.Dialog().ok("subgenX", "subgenX failed")
    # else:
        # xbmcplugin.setResolvedUrl(handle, True, xbmcgui.ListItem(path=r"D:\songs\Benson Boone - Beautiful Things (Official Music Video).srt"))
    icon_path = r"./resources/icon.png"
    if not os.path.exists(icon_path): ## checking if icon exists or not
        icon_path = xbmcgui.NOTIFICATION_INFO

    xbmcgui.Dialog().ok("subgenX", "Completed successfully!")
    xbmcgui.Dialog().notification(
        heading="subgenX",
        message="Subtitle generated successfully!",
        icon= icon_path,  # or a custom image path
        time=5000,  # duration in ms
        sound=True
    )
        # xbmcplugin.setResolvedUrl(handle, True, xbmcgui.ListItem(path=r"D:\songs\Benson Boone - Beautiful Things (Official Music Video).srt"))


# listing options for subtitle generation
def list_subtitles():
    handle = int(sys.argv[1])
    # video_path = sys.argv[2]  # Kodi passes the currently playing video path
    # subs = search_subtitles(video_path)

    path = to_kodi_path(base_video_name)
    xbmc.log(f'FILEPATH: {path}.en.srt')
    print(path)

    for ac in accuracy:
        li = xbmcgui.ListItem(label=f"{ac['name']} [{ac['language']}]", label2=ac['description'])
        # subtitle_file = 'D:\songs\Benson Boone - Beautiful Things (Official Music Video).srt'
        xbmcplugin.addDirectoryItem(handle=handle, url=f'plugin://service.subtitles.subgenx/?action=download&file={currentPlayingMedia}', listitem=li, isFolder=False)
    xbmcplugin.endOfDirectory(handle)

    # for sub in subs:
    #     li = xbmcgui.ListItem(label=f"{sub['language']} - {sub['score']}")
    #     li.setProperty("IsPlayable", "true")
    #     li.setSubtitles([sub['url']])
    #     xbmcplugin.addDirectoryItem(handle, sub['url'], li, isFolder=False)
    # xbmcplugin.endOfDirectory(handle)

if action == 'download': 
    file = params.get("file")
    if file: 
        xbmcgui.Dialog().ok("Download", f"Subtitle Generation Started for: {file}\n Depending on your system resources Process might take few minutes!\nand if you are running it for the first time then it might take some more time and may require internet connection for the first time setup only.")
        generateSubtitle()
elif action is None: 
    xbmcgui.Dialog().ok("SubGenX", "Main menu here")

# main entry point
if __name__ == "__main__":
    list_subtitles()

