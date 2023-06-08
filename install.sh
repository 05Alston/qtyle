#!/bin/bash
set -e

# Check if script is run as root
if [[ "$(id -u)" -eq 0 ]]; then
  echo "This script must not be run as root"
  exit 1
fi

# Update system 
sudo pacman -Syyu

# Install Git
if command -v git &>/dev/null; then
  echo "Git v$(git -v | cut -d' ' -f3) is already installed in your system"
else
  sudo pacman -S git --noconfirm
fi

# Find installed aur helper
pack_man=''

if command -v yay &>/dev/null; then
    echo "Yay $(yay -V | cut -d' ' -f2) is installed in your system"
    pack_man=yay
else
  if command -v paru &>/dev/null; then
    echo "Paru $(paru -V | cut -d' ' -f2) is already installed in your system"
    pack_man=paru
  else
    echo "Neither Paru nor Yay is present in your system."

    PS3='Please enter your choice:'
    options=("Yay" "Paru" "Quit")
    select opt in "${options[@]}"
    do
      case $opt in
        "Yay")
          sudo pacman -S --needed --noconfirm base-devel && rm -fr ~/yay && git clone https://aur.archlinux.org/yay.git ~/yay && cd yay && makepkg -si && cd ..
          pack_man=yay
          break
          ;;
        "Paru")
          sudo pacman -S --needed --noconfirm base-devel && rm -fr ~/paru && git clone https://aur.archlinux.org/paru.git ~/paru && cd paru && makepkg -si && cd ..
          pack_man=paru
          break
          ;;
        "Quit")
          exit
          ;;
        *) 
          echo "invalid option $REPLY" 
          exit
          ;;
      esac
    done
  fi
fi

# Install packages
$pack_man -Syu base-devel qtile python-psutil pywal-git viewnior feh picom-jonaburg-fix dunst zsh starship alacritty pfetch playerctl brightnessctl rofi ranger cava pulseaudio alsa-utils neovim networkmanager networkmanager-qt networkmanager-openvpn pavucontrol acpi btop blueman --noconfirm --needed

# Check and set Zsh as the default shell
[[ "$(awk -F: -v user="$USER" '$1 == user {print $NF}' /etc/passwd) " =~ "zsh " ]] || chsh -s $(which zsh)

# Install Oh My Zsh
if [ ! -d ~/.oh-my-zsh/ ]; then
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended 
else
  omz update
fi

# Install Zsh plugins
[[ "${plugins[*]} " =~ "zsh-autosuggestions " ]] || git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
[[ "${plugins[*]} " =~ "zsh-syntax-highlighting " ]] || git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Copy dots to location
mkdir ~/.config && cp -rf .config/* ~/.config
mkdir ~/.local && cp -rf .local/* ~/.local
cp .zshrc ~/




# Check if lightdm is installed and install if not
if pacman -Qs lightdm > /dev/null; then
 echo "lightdm is already installed"
else
 echo "lightdm is not installed. Installing..."
 sudo pacman -S lightdm lightdm-gtk-greeter --needed --noconfirm
fi

# Disable currently enabled display manager
if systemctl list-unit-files | grep enabled | grep -E 'gdm|lightdm|lxdm|lxdm-gtk3|sddm|slim|xdm'; then
 echo "Disabling currently enabled display manager"
 sudo systemctl disable --now $(systemctl list-unit-files | grep enabled | grep -E 'gdm|lightdm|lxdm|lxdm-gtk3|sddm|slim|xdm' | awk -F ' ' '{print $1}')
fi

# Enable and start SDDM
echo "Enabling and starting lightdm"
sudo systemctl enable lightdm.service
sudo systemctl start lightdm.service
echo "Installation Complete. Rebooting Now"
sleep 4
reboot
