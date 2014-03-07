sudo apt-get update
sudo apt-get install git

# Set up Environment
git clone https://github.com/ZachGarner/environment.git


# Install Java 
    # Note: I found this wget command on stackoverflow. Seems to work.
wget --no-cookies --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com" "http://download.oracle.com/otn-pub/java/jdk/7/jdk-7u51-linux-x64.tar.gz"

sudo mkdir -p /usr/lib/jvm
sudo mv jdk1.7.0/ /usr/lib/jvm
sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.7.0/bin/java" 1
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.7.0/bin/javac" 1
sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/jvm/jdk1.7.0/bin/javaws" 1
    # Note: assumes PATH & JAVA_HOMEalready set up in .profile
