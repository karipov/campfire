# NatureNet
![Made with love in Hack@Brown 2023](https://madewithlove.now.sh/af?heart=true&text=Hack%40Brown+2023)
> Upgrade your Camping Experience

Check out the Devpost for more: https://devpost.com/software/naturenet

## In action!
![parts](https://raw.githubusercontent.com/karipov/campfire/main/docs/parts.JPG)
![in action](https://raw.githubusercontent.com/karipov/campfire/main/docs/action.JPG)

## What are these files?
- All the source code is within the [`src`](https://github.com/karipov/campfire/tree/main/src) directory.
- The [`main`](https://github.com/karipov/campfire/blob/main/src/main.py) file contains the GPIO-checking loop and other files work on different aspects of the plant recognition, detection and narration pipeline.
- The [`campfire.service`](https://github.com/karipov/campfire/blob/main/campfire.service) helps setup everything as a `systemd` service such that the device works on-boot.
