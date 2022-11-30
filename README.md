# track_length_plugin_kicad
This **Kicad PCB Editor python plugin** measures the selected track segments lengths and gives the **total length in mm**. It also **estimates resistance** for 1 Oz copper and T = 25C.

This guide was used: https://dev-docs.kicad.org/en/python/pcbnew/

This Youtube view was my inspiration: https://www.youtube.com/watch?v=WjDrvnIFPVY

This on-line resistance calculation tool was used to ensure the plugin's results are accurate:\
https://www.allaboutcircuits.com/tools/trace-resistance-calculator/


## **INSTALLATION**

### **(1)** Find plugin directory... **Tools -> External Plugins -> Open Plugin Directory**

![picture](https://github.com/charkster/track_length_plugin_kicad/blob/main/docs/refresh_plugins_menu.png)

### **(2)** Copy **track_length_plugin_kicad.py** and **track_length_plugin_icon.png** to your plugin directory.

![picture](https://github.com/charkster/track_length_plugin_kicad/blob/main/docs/kicad_scripts_directory.png)

### **(3)** Refresh plugins... **Tools -> External Plugins -> Refresh Plugins**



## **USAGE**

### **Select the track segments** using the **SHIFT** key and then **click** the new icon.

![picture](https://github.com/charkster/track_length_plugin_kicad/blob/main/docs/track_length_script.png)
