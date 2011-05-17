%define pkgname ubuntu-font-family
%define _fontdir %{_datadir}/fonts/TTF/ubuntu

Name: fonts-ttf-ubuntu
Summary: Ubuntu Font Family
Version: 0.70.1
Release: %mkrel 2
License: Ubuntu Font Licence 1.0
Group: System/Fonts/True type
URL: http://font.ubuntu.com/
Source: http://font.ubuntu.com/download/%{pkgname}-%{version}.zip
BuildRequires: freetype-tools
BuildArch: noarch
BuildRequires: fontconfig
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Ubuntu Font Family are a set of matching new libre/open fonts in
development during 2010--2011. The development is being funded by
Canonical Ltd on behalf the wider Free Software community and the
Ubuntu project.  The technical font design work and implementation is
being undertaken by Dalton Maag.

Both the final font Truetype/OpenType files and the design files used
to produce the font family are distributed under an open licence and
you are expressly encouraged to experiment, modify, share and improve.

%prep
%setup -q -n %{pkgname}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_fontdir}
install -m 644 *.ttf %{buildroot}%{_fontdir}
ttmkfdir %{buildroot}%{_fontdir} > %{buildroot}%{_fontdir}/fonts.dir
ln -s fonts.dir %{buildroot}%{_fontdir}/fonts.scale
mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_fontdir} \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-ubuntu:pri=50

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc *.txt
%dir %{_fontdir}
%{_fontdir}/*.ttf
%verify(not mtime) %{_fontdir}/fonts.dir
%{_fontdir}/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-ubuntu:pri=50
