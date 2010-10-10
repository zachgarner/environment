Summary: Configuration of various linux development and environment tools
Name: zx-system
Version: %{date}
Release: %{time}
License: BSD
Group: Development/Tools
Requires: zx-system-yum
Requires: zx-system-env
Requires: zx-system-build
Requires: zx-system-server
BuildRoot: /var/tmp/%{name}-rpmroot
BuildArch: noarch

%define src ../../src

%description

%build

# Lighttpd
mkdir -p $RPM_BUILD_ROOT/etc/lighttpd/conf.d

%install
rm -rf $RPM_BUILD_ROOT

# Environment stuff
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cp %{src}/bash/profile.sh $RPM_BUILD_ROOT/etc/profile.d/zx.sh

mkdir -p $RPM_BUILD_ROOT/home/zx
cp %{src}/git/dot.gitconfig $RPM_BUILD_ROOT/home/zx/.gitconfig
cp %{src}/git/dot.gitignore $RPM_BUILD_ROOT/home/zx/.gitignore
cp %{src}/vi/dot.vimrc $RPM_BUILD_ROOT/home/zx/.vimrc

# Yum Client Configuration

mkdir -p $RPM_BUILD_ROOT/srv/yum

mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
cp %{src}/yum/zx.repo $RPM_BUILD_ROOT/etc/yum.repos.d

## Packages

%package yum
Summary: Yum client environment configuration
Group: Development/Tools
Requires: createrepo
%description yum

%package env
Summary: Various tool configurations
Group: Development/Tools
Requires: tree
%description env

%package build
Summary: Build Tools and Environment
Group: Development/Tools
Requires: subversion >= 1.6.12-0.1.el5.rf
Requires: git >= 1.7.1-2.el5.rf 
Requires: git-svn >= 1.7.1-2.el5.rf
Requires: rpm-build
%description build

%package server
Summary: Server services and tools
Group: Development/Tools
Requires: mysql
Requires: mysql-server
Requires: lighttpd
Requires: lighttpd-fastcgi
Requires: python-flup
%description server

## Pre

%pre yum
# rm -f /etc/yum.repos.d/*

## Post

%post yum
# createrepo /srv/yum
# Cannot do 'makecache' while yum installing
# yum makecache || true # ignore errors

%post server

# lighttpd
chkconfig lighttpd on
/etc/init.d/lighttpd start
/newservers/openPortInFirewall 80

# mysql
chkconfig mysqld on
/etc/init.d/mysqld start


## Files

%files

%files env
/etc/profile.d/zx.sh
/home/zx/.gitconfig
/home/zx/.gitignore
/home/zx/.vimrc

%files yum
/etc/yum.repos.d/*
/srv/yum

%files build

%files server
