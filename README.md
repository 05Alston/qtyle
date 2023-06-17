
# Hey there!! This is my first Qtile rice

## INSTALLATION  (Arch Linux)

#### Note: This installation script is specifically designed for Arch Linux. It will work for a freshly installed system. If you've been using a different window manager, no worries - just be sure to take a complete backup of your current dots before running the script. And if you're already using Oh My Zsh, don't forget to remove that folder from your home directory

<details>
<summary><h3>Automated Installation</h3></summary>

- Clone the repo and cd into the cloned folder.

```sh
git clone https://github.com/05Alston/qtyle
cd qtyle
```

#### Now that you're in the cloned folder, it's time to run the script

- Make the script executable

```sh
chmod +x install.sh
```

- Run the script

```sh
./install.sh
```

#### Once the script finishes its work and launches lightdm, it's time to choose Qtile from the WM selector and dive right into the Amazing world of Qtile!
</details>

<details>
<summary><h3>MANUAL INSTALLATION (Universal)</h3></summary>

#### Note: While this guide is primarily intended for Arch Linux users, If you're running a different OS like Fedora, NixOS, or Debian. You'll still be able to follow along and get a clear idea of how to set things up. (using your OS's package manager and other tools)

#### Keep in mind that this configuration is tailored to assume that the main files, like ".config", will be located in the home folder (~/). However, if that's not the case for you, don't worry - you'll just need to make a few manual adjustments to the dotfiles.

<details>
<summary><h3>Dependencies</h3></summary>

#### To get started, let's make sure we have all the necessary prerequisites. In this case, I'm using Paru as the AUR helper, but keep in mind that your system may require a different approach.

- Installation using paru

```sh
paru -Syu base-devel qtile python-psutil pywal-git viewnior feh picom-jonaburg-fix dunst zsh starship alacritty pfetch neovim brightnessctl rofi ranger cava pulseaudio alsa-utils pavucontrol pamixer mpv  pulseaudio-alsa pulseaudio-bluetooth playerctl acpi btop noto-fonts noto-fonts-extra papirus-icon-theme xarchiver unzip networkmanager nm-connection-editor maim flameshot xrandr arandr blueman bluez bluez-utils i3lock-color eww tlp redshift nodejs-lts-hydrogen npm --noconfirm --needed
```

- Fonts required for the bar and other utils

 ➺ Any nerd font

 ➺ [JetBrains Mono](https://www.jetbrains.com/lp/mono/)

#### You could either download the zip files for these fonts and put them into ``~/.local/share/fonts/`` or ``/usr/share/fonts/``

#### You could also copy them from the ``.local/share/fonts/required`` directory. The fonts directory contains a lot of fonts that I use on my system so you'd be bloating your system if you don't require other fonts.

</details>

<details>
<summary><h3>Shell</h3></summary>

#### Next step is to install and setup the shell.

- Change the default shell to Zsh

```sh
chsh -s $(which zsh)
```

- Setting up Oh-my-zsh & plugins
  
```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended 
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

</details>

<details>
<summary><h3>Dotfiles</h3></summary>

#### With all the necessary prerequisites now installed, the next step is to replicate my setup by copying the dotfiles

- Clone the repo and cd into the cloned folder.

```sh
git clone https://github.com/05Alston/qtyle 
cd Cozytile
```

#### Now that you're in the cloned folder, it's time to copy those files over to your home directory.

- Copy the files using cp

```sh
cp -R ./. ~/
```

</details>

<details>
<summary><h3>Final step</h3></summary>

#### Now that you're done with copying the dotfiles, it's time to hop into Qtile. This requires installing a display manager like lightdm. Here are the steps to install lightdm:

- Install it using paru

```sh
paru -Sy lightdm
```

- Enable and start lightdm

```sh
sudo systemctl enable lightdm && sudo systemctl start lightdm
```

#### Now that you're in the login screen of lightdm, just select Qtile from wm selector, then login with your root password! viola ✨

- Enjoy!

#### Congratulations! You have successfully replicated my setup! Feel free to experiment with the configurations and enjoy!!!

</details>

</details>

<details>
<summary><h2>Screenshots</h2></summary>
</details>

<details>
<summary><h3>KEYBINDS</h3></summary>

| Key                                                                                                                                                         | Bind                                              |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------|
|                                                                                                                                                             |                                                   |
| Qtile Defaults                                                                                                                                              |                                                   |
|                                                                                                                                                             |                                                   |
| <kbd>super</kbd> + <kbd>h</kbd>                                                                                                                             | Move focus to left                                |
| <kbd>super</kbd> + <kbd>l</kbd>                                                                                                                             | Move focus to right                               |
| <kbd>super</kbd> + <kbd>j</kbd>                                                                                                                             | Move focus to down                                |
| <kbd>super</kbd> + <kbd>k</kbd>                                                                                                                             | Move focus to up                                  |
| <kbd>super</kbd> + <kbd>space</kbd>                                                                                                                         | Move window focus to other window                 |
| <kbd>super</kbd> + <kbd>control</kbd> + <kbd>h</kbd>                                                                                                        | Move window to the left                           |
| <kbd>super</kbd> + <kbd>control</kbd> + <kbd>l</kbd>                                                                                                        | Move window to the right                          |   
| <kbd>super</kbd> + <kbd>control</kbd> + <kbd>j</kbd>                                                                                                        | Move window to the down                           |
| <kbd>super</kbd> + <kbd>control</kbd> + <kbd>k</kbd>                                                                                                        | Move window to the up                             |
| <kbd>super</kbd> + <kbd>shift</kbd> + <kbd>h</kbd>                                                                                                          | Grow windows to the left                          |
| <kbd>super</kbd> + <kbd>shift</kbd> + <kbd>l</kbd>                                                                                                          | Grow windows to the right                         |
| <kbd>super</kbd> + <kbd>shift</kbd> + <kbd>j</kbd>                                                                                                          | Grow windows to the down                          |
| <kbd>super</kbd> + <kbd>shift</kbd> + <kbd>k</kbd>                                                                                                          | Grow windows to the up                            |
| <kbd>super</kbd> + <kbd>n</kbd>                                                                                                                             | Reset all window sizes                            |
| <kbd>super</kbd> + <kbd>f</kbd>                                                                                                                             | Toggle fullscreen                                 |
| <kbd>super</kbd> + <kbd>shift</kbd> + <kbd>Return</kbd>                                                                                                     | Toggle between split and unsplit sides of stack   |
| <kbd>super</kbd> + <kbd>Tab</kbd>                                                                                                                           | Toggle between layouts                            |
| <kbd>super</kbd> + <kbd>Control</kbd> + <kbd>r</kbd>                                                                                                        | Restart Qtile                                     |
| <kbd>super</kbd> + <kbd>Control</kbd> + <kbd>q</kbd>                                                                                                        | Shutdown Qtile                                    |
|                                                                                                                                                             |                                                   |
| Custom                                                                                                                                                      |                                                   |
|                                                                                                                                                             |                                                   |
| <kbd>super</kbd> + <kbd>Return</kbd>                                                                                                                        | Launch Terminal                                   |
| <kbd>super</kbd> + <kbd>c</kbd>                                                                                                                             | Close/Kill focused window                         |
| <kbd>super</kbd> + <kbd>r</kbd>                                                                                                                             | App launcher/ Rofi Drun                           |
| <kbd>super</kbd> + <kbd>p</kbd>                                                                                                                             | Rofi Powermenu                                    |
| <kbd>super</kbd> + <kbd>t</kbd>                                                                                                                             | **Rofi Theme_switcher**                             |
| <kbd>super</kbd> + <kbd>e</kbd>                                                                                                                             | Thunar File manager                               |
| <kbd>super</kbd> + <kbd>s</kbd>                                                                                                                             | Flameshot (Screenshot)                            |
| <kbd>super</kbd> + <kbd>h</kbd>                                                                                                                             | Roficlip                                          |

</details>

## CREDITS

I've yoinked stuff from various places.

- The [Cozytile](https://github.com/darkkal44/Cozytile/) setup from [darkkal44](https://github.com/darkkal44/) was a huge inspiration.
- [rofi](github.com/adi1090x/rofi) scripts from [adi1090x](github.com/adi1090x)
- [Paledark](https://github.com/Myagko/dotfiles) GTK theme from [Myagko](https://github.com/Myagko)

---

<div align="center">

#### Have a nice day!

</div>
