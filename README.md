# track_length_plugin_kicad
This **Kicad PCB Editor python plugin** measures the selected track segments lengths and gives the **total length in mm**. It also **estimates resistance** for 1 Oz copper and T = 25C.

This guide was used: https://dev-docs.kicad.org/en/python/pcbnew/

This Youtube view was my inspiration: https://www.youtube.com/watch?v=WjDrvnIFPVY
\
\
\
**INSTALLATION**

**(1)** Copy the **track_length_plugin_kicad.py** script and icon file **track_length_plugin_icon.png** to your kicad scripts directory.

![picture](https://github.com/charkster/track_length_plugin_kicad/blob/main/docs/kicad_scripts_directory.png)



**(2) Tools -> External Plugins -> Refresh Plugins**

![picture](https://github.com/charkster/track_length_plugin_kicad/blob/main/docs/refresh_plugins_menu.png)
\
\
\
**USAGE**
\
\
**Select the track segments** using the **SHIFT** key and then **click** the new icon.

![picture](https://github.com/charkster/track_length_plugin_kicad/blob/main/docs/track_length_script.png)
