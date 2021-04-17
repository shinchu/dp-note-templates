# Note templates

Note templates made with [DrawBot](https://www.drawbot.com/).

Good for print, DIGITAL PAPER (DPT-RP1), and reMarkable 2.

## Install templates for reMarkable 2

[Customizing the Templates](https://remarkablewiki.com/tips/templates#specifications)

```bash
scp svg/*.svg root@remarkable:/usr/share/remarkable/templates/
scp png/*.png root@remarkable:/usr/share/remarkable/templates/
```

```json:templates.json

{
  "name": "Lettering",
  "filename": "lettering_grids_alt",
  "landscape": true,
  "iconCode": "\ue9fb",
  "categories": [
    "Creative"
  ]
},
{
  "name": "Lettering 2",
  "filename": "lettering_grids_plain",
  "landscape": true,
  "iconCode": "\ue9fa",
  "categories": [
    "Creative"
  ]
},
{
  "name": "Calligraphy",
  "filename": "calligraphy_lines",
  "landscape": true,
  "iconCode": "\ue990",
  "categories": [
    "Creative"
  ]
},
{
  "name": "Type sketch",
  "filename": "sketch_lines",
  "landscape": true,
  "iconCode": "\ue990",
  "categories": [
    "Creative"
  ]
},
{
  "name": "yPad",
  "filename": "planner",
  "landscape": true,
  "iconCode": "\ue9ca",
  "categories": [
    "Life/organize"
  ]
}

```

```bash
systemctl restart xochitl
```
