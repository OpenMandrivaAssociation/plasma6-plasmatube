%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200916
#define commit cc1ac2462e41873741c8b6f3fcafa29ae3ce6a30

Name:		plasma6-plasmatube
Version:	24.01.90
Release:	%{?git:0.%{git}.}1
Summary:	YouTube client for Plasma Mobile
%if 0%{?git}
Source0:	https://invent.kde.org/plasma-mobile/plasmatube/-/archive/v%{version}/plasmatube-v%{version}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/plasmatube-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(MpvQt)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	youtube-dl
Requires:	youtube-dl

%description
YouTube client for Plasma Mobile

%prep
%autosetup -p1 -n plasmatube-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang plasmatube

%files -f plasmatube.lang
%{_bindir}/plasmatube
%{_datadir}/applications/org.kde.plasmatube.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.plasmatube.svg
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/metainfo/org.kde.plasmatube.appdata.xml
