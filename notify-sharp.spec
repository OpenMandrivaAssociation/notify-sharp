Summary:	C# desktop notification client
Name:		notify-sharp
Version:	0.4.0
Release:	7
Source0:	%{name}-%version.tar.gz
License:	MIT
Group:		System/Libraries
Url:		http://www.ndesk.org/NotifySharp

BuildRequires:	mono-devel
BuildRequires:	monodoc
BuildRequires:	gtk-sharp2
BuildRequires:	ndesk-dbus-glib-devel
BuildArch:	noarch

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus).

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%package doc
Summary:	Development documentation for %{name}
Group:		Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
This package contains the API documentation for the %{name} in
Monodoc format.


%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%post doc
%{_bindir}/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %{_bindir}/monodoc ]; then %{_bindir}/monodoc --make-index > /dev/null
fi

%files
%doc AUTHORS NEWS README
%{_prefix}/lib/mono/gac/notify-sharp
%{_prefix}/lib/mono/notify-sharp

%files devel
%doc ChangeLog
%{_datadir}/pkgconfig/notify-sharp.pc

%files doc
%{_prefix}/lib/monodoc/sources/notify-sharp-docs.*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-5mdv2011.0
+ Revision: 666622
- mass rebuild

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.4.0-4mdv2011.0
+ Revision: 567952
- split out devel package
- update build deps

* Fri Dec 11 2009 Götz Waschk <waschk@mandriva.org> 0.4.0-3mdv2010.1
+ Revision: 476300
- rebuild for new webkit-sharp

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.0-2mdv2010.0
+ Revision: 426254
- rebuild

* Thu Sep 11 2008 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2009.0
+ Revision: 283772
- use tarball from Suse that contains the same code
- fix license

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0-2mdv2009.0
+ Revision: 219564
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Götz Waschk <waschk@mandriva.org>
    - fix requires exception for new mono
    - remove new automatic mono deps

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 08 2007 Götz Waschk <waschk@mandriva.org> 0-1mdv2008.0
+ Revision: 60146
- Import notify-sharp



* Wed Aug  8 2007 Götz Waschk <waschk@mandriva.org> 0-1mdv2008.0
- initial package
