#
# TODO:
#	- don't package entire doc subdirectory as %doc, make install creates
#	  much more reasonable directory structure
#
Summary:	Editor for manipulating PDF documents
Summary(pl.UTF-8):	Edytor do manipulowania dokumentami PDF
Name:		pdfedit
Version:	0.3.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pdfedit/%{name}-%{version}.tar.bz2
# Source0-md5:	e4ed098f70a4c5675b16b22641f5a182
URL:		http://pdfedit.petricek.net/
BuildRequires:	autoconf
BuildRequires:	boost-devel
BuildRequires:	boost-call_traits-devel
BuildRequires:	libpaper-devel
BuildRequires:	motif-devel
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	t1lib-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Complete editing of PDF documents is made possible with PDFedit. You
can change either raw PDF objects (for advanced users) or use
predefined gui functions. Functions can be easily added as everything
is based on a scripts.

Scripting is used to a great extent in editor and almost anything can
be scripted, it is possible to create own scripts or plugins.

#description -l pl.UTF-8

%prep
%setup -q

%build
export QTDIR="%{_prefix}"
export QMAKESPEC="linux-g++"
%{__autoconf}
%configure
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	QTDIR="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README doc
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*.1*
