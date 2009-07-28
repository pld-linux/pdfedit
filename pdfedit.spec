#
# TODO:
#	- don't package entire doc subdirectory as %doc, make install creates
#	  much more reasonable directory structure
#	- fix default fontpath for ghostscript fonts as now it seeks
#		/usr/share/ghostscript/fonts/
#		/usr/local/share/ghostscript/fonts/
#		/usr/share/fonts/default/Type1/
#		/usr/share/fonts/default/ghostscript/
#		/usr/share/fonts/type1/gsfonts/
#	  instead of /usr/share/fonts/Type1/
#	  userspace solution: echo fontDir /usr/share/fonts/Type1 >> ~/.xpdfrc
#
Summary:	Editor for manipulating PDF documents
Summary(pl.UTF-8):	Edytor do manipulowania dokumentami PDF
Name:		pdfedit
Version:	0.4.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pdfedit/%{name}-%{version}.tar.bz2
# Source0-md5:	98eb8d8d42027241c10a5c9bedacc20e
URL:		http://pdfedit.petricek.net/
BuildRequires:	autoconf
BuildRequires:	boost-devel >= 1.35.0
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
predefined GUI functions. Functions can be easily added as everything
is based on a scripts.

Scripting is used to a great extent in editor and almost anything can
be scripted, it is possible to create own scripts or plugins.

%description -l pl.UTF-8
PDFedit umożliwia pełną edycję dokumentów PDF. Można modyfikować
surowe obiekty PDF (dla zaawansowanych użytkowników) lub używać
predefiniowanych funkcji interfejsu graficznego. Można łatwo dodawać
własne funkcje, jako że wszystko jest oparte na skryptach.

Skrypty pozwalają w znaczny sposób rozszerzać edytor i prawie wszystko
można osiągnąć z poziomu skryptów; można tworzyć własne skrypty i
wtyczki.

%prep
%setup -q
# remove bashizms
sed -e 's/function //g' -i getversion tools/generate_lang.sh

%build
export QTDIR="%{_prefix}"
export QMAKESPEC="linux-g++"
%{__autoconf}
%configure \
	CXX_EXTRA="%{rpmcflags}"
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	%{?debug:--disable-release}

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
