# YFX lilOutline

[![GitHub license](https://img.shields.io/github/license/yuufyu/YFX-lilOutline)](https://github.com/yuufyu/YFX-lilOutline/blob/main/LICENSE)
[![Blender Version](https://img.shields.io/badge/Blender-4.0.2-blue)](https://www.blender.org/)

## Overview

This Blender add-on enhances the appearance of outlines rendered using the [lilToon](https://github.com/lilxyzw/lilToon) shader by providing a smoother look.  
It achieves this by writing the direction of the outline into the vertex colors of the mesh.  

The lilToon shader utilizes the information stored in the vertex colors to control the direction of the outline.  
To leverage this feature, ensure that the lilToon shader's 'Outline > Vertex Color' setting is configured to 'RGBA -> Normal & Width'.  

This Blender add-on aims to bring functionality similar to [lilOutlineUtil](https://github.com/lilxyzw/lilOutlineUtil) in Unity to Blender.  

## Installation

1. Download the add-on ZIP file from the [Code > Download ZIP](https://github.com/yuufyu/YFX-lilOutline/archive/refs/heads/main.zip) page.
2. In Blender, go to `Edit > Preferences > Add-ons`.
3. Click the "Install" button and select the downloaded ZIP file.
4. Enable the "YFX lilOutline" add-on by checking the checkbox.


## Usage
1. Select the object(s) you want to apply the outline smoothing to.
2. Go to `View3D > Object > Smooth Outlines` in the Blender menu.

## Known Issues
- If custom normals are altered by modifiers (e.g., Data Transfer modifier), the add-on may not function as intended.  
Applying modifiers can avoid this issue.


## License
This add-on is licensed under the GNU General Public License (GPL) version 3. For details, see the [LICENSE](LICENSE) file.


## Author
- [yuufyu](https://github.com/yuufyu)


## Feedback and Contributions
Feedback and contributions are welcome! Feel free to open issues or submit pull requests.
