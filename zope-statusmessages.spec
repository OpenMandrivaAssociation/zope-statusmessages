%define product		statusmessages
%define realVersion     2.0.1
%define release         1

%define version %(echo %{realVersion} | sed -e 's/-/./g')

%define zope_minver	2.7
%define plone_minver	2.0

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Summary:	Provides an easy way of handling internationalized status messages
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		System/Servers
Source:		http://plone.org/products/statusmessages/releases/%{version}/statusmessages-%{version}.tar.bz2
URL:		http://plone.org/products/statusmessages/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}
Requires:	plone >= %{plone_minver}

Provides:	plone-Faq == %{version}
Obsoletes:	zope-Faq


%description
It is quite common to write status messages which should be shown to the user
after some action. These messages of course should be internationalized. As
these messages normally are definied in Python code, the common way to i18n-ize
these in Zope is to use Zope3 MessageID's. MessageID's are complex objects
consisting of a translation domain and a default unicode text and might have an
additional mapping dict and a distinct id.
The usual way to provide status messages in CMF/Plone has been to add a
"?portal_status_messages=some%20text" to the URL. While this has some usability
problems it also isn't possible to i18n-ize these in the common way, as the URL
is currently limited to the ASCII charset, but an encoding providing support for
the full unicode range is required.
The solution provided by this tool is to use session cookies to store the
messages.

%prep
%setup -c

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a %{product} %{buildroot}%{software_home}/Products/%{product}


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(0644, root, root, 0755)
%{software_home}/Products/*


