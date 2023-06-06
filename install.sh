#!/bin/bash

# Check if script is run as root
#if [[ "$(id -u)" -eq 0 ]]; then
#  echo "This script must not be run as root"
#  exit 1
#fi

# Update system 
sudo pacman -Syu

# Install Git
if command -v git &>/dev/null; then
  echo "Git v$(git -v | cut -d' ' -f3) is already installed in your system"
else
  sudo pacman -S git --noconfirm
fi

pack_man=''
# Find installed aur helper
if command -v yay &>/dev/null; then
    echo "Yay $(yay -V | cut -d' ' -f2) is installed in your system"
    pack_man=yay	
else
  if command -v paru &>/dev/null; then
    echo "Paru $(paru -V | cut -d' ' -f2) is already installed in your system"
    pack_man=paru
  else
    echo "Neither Paru nor Yay is present in your system."    

    PS3='Please enter your choice: '
    options=("Yay" "Paru" "Quit")
    select opt in "${options[@]}"
    do
        case $opt in
            "Yay")
                sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git ~/yay && cd yay && makepkg -si && cd ..
                pack_man=yay
		break
                ;;
            "Paru")
                sudo pacman -S --needed base-devel && git clone https://aur.archlinux.org/paru.git ~/paru && cd paru && makepkg -si && cd ..
		pack_man=paru
		break
	        ;;
            "Quit")
                exit
                ;;
            *) echo "invalid option $REPLY" 
		exit
		;;
        esac
    done
  fi
fi 


# Install packages
    $pack_man -Syu base-devel qtile python-psutil pywal-git viewnior picom-jonaburg-fix dunst zsh starship playerctl brightnessctl alacritty pfetch pcmanfm rofi ranger cava pulseaudio alsa-utils neovim networkmanager networkmanager-qt networkmanager-openvpn pavucontrol espanso font-manager bleachbit timeshift acpi btop blueman --noconfirm --needed

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

# Make Backup 


echo "Backing up the current configs. All the backup files will be available at ~/.qute.bak"
mkdir -p ~/.qute.bak

for folder in .* *; do
  if [[ -d "$folder" && ! "$folder" =~ ^(\.|\.\.)$ && "$folder" != ".git" ]]; then
    if [ -d "$HOME/$folder" ]; then
      echo "Backing up ~/$folder"
      cp -r "$HOME/$folder" ~/.qute.bak
      echo "Backed up ~/$folder successfully."
      echo "Removing old config for $folder"
      rm -rf "$HOME/$folder"
    fi
  fi
done

# Copy dots to location
mkdir ~/.config && cp -rf .config/* ~/.config
mkdir ~/.local && cp -rf .local/* ~/.local
cp .zshrc ~/




# Check if SDDM is installed and install if not
#if pacman -Qs sddm > /dev/null; then
#  echo "SDDM is already installed"
#else
#  echo "SDDM is not installed. Installing..."
#  sudo pacman -S sddm
#fi

# Disable currently enabled display manager
#if systemctl list-unit-files | grep enabled | grep -E 'gdm|lightdm|lxdm|lxdm-gtk3|sddm|slim|xdm'; then
#  echo "Disabling currently enabled display manager"
#  sudo systemctl disable --now $(systemctl list-unit-files | grep enabled | grep -E 'gdm|lightdm|lxdm|lxdm-gtk3|sddm|slim|xdm' | awk -F ' ' '{print $1}')
#fi

# Enable and start SDDM
#echo "Enabling and starting SDDM"
#sudo systemctl enable --now sddm

